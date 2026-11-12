# Design log: The Big Five

This file is the memory of the course (see "Designing tracks and courses" in
`AGENTS.md`). It is not rendered.

## 1. Objectives

After the course, a student can:

- state the systems ACA₀, WKL₀, ATR₀ and Π¹₁-CA₀ and use their equivalent forms (Σ⁰₁
  comprehension, jumps, ranges of injections; Σ⁰₁ separation; Π¹₁ comprehension as the
  existence of the set of ill-founded trees of a sequence);
- carry out a reversal to ACA₀ by coding the range of an injection into a computable
  instance, and a reversal to WKL₀ by coding an arbitrary binary tree or two disjoint Σ⁰₁
  properties;
- characterize the ω-models of ACA₀ (jump ideals) and WKL₀ (Scott ideals), and separate
  the systems with ω-models (REC, a low Scott ideal, ARITH);
- know the main theorems of ordinary mathematics equivalent to each system, with
  references, and the four separations of the chain.

**Role in the track.** Second course of the reverse mathematics track
(`content/tracks-design.md`), after second-order-arithmetic. The track design says the
reverse mathematics of analysis, algebra and topology is represented by "examples given
in the Big Five course": these are monotone convergence, Bolzano–Weierstrass and least
upper bounds (analysis), torsion subgroups (algebra), König's lemma (combinatorics),
Heine–Borel (topology), with surveys for the rest. The later courses use: Scott ideals and
the low model (ramsey-theorem/jockusch, seetapun; reducibilities/omega-reducibility), the
ACA₀ equivalents and König's lemma (ramsey-theorem/jockusch), ACA₀ and WKL₀ themselves
(induction-conservation).

## 2. Prerequisites assumed

- second-order-arithmetic: L₂, ω-models and absoluteness (`prop-omega-absolute`),
  induction from comprehension (`prop-induction-comprehension`), RCA₀ and Π⁰₁ induction
  (`prop-pi01-induction`), Turing ideals (`thm-rca-turing-ideal`, `cor-rca-not-wkl`), reals
  in RCA₀ and Specker sequences (`prop-specker`, lesson real-numbers). Codes of continuous
  functions (`def-continuous-code`, with index field) appear only in statements of the
  survey tables, not in proofs.
- pi01-classes: low and cone avoidance basis theorems, PA degrees
  (`thm-pa-characterization`), DNC₂ (`thm-dnc2-no-computable`), König's lemma and its
  computability strength (`thm-finitely-branching-jump`, `thm-konig-strength`,
  `prop-finitely-branching-coding`).
- arithmetic-hierarchy: Post's theorem (`thm-post`). Turing degrees: the jump, low sets.

## 3. Results, lesson by lesson

1. **Arithmetic comprehension** (`aca0`): definition (`def-aca0`); four equivalent forms
   (`thm-aca-equivalents`); jump ideals (`def-jump-ideal`), ω-models of ACA₀ and minimality
   of ARITH (`cor-aca-jump-ideal`). Exercises: no ω-jump in ACA₀; ARITH(A) is the least
   ω-model containing A.
2. **Theorems equivalent to ACA₀** (`aca0-reversals`, new 2026-11-12): monotone
   convergence (`thm-monotone-aca`), torsion subgroups (`thm-torsion-aca`, new), König's
   lemma (`thm-konig-aca`). Exercises: least upper bounds, Bolzano–Weierstrass.
3. **Weak König's lemma** (`wkl0`): definition (`def-wkl0`), Scott ideals
   (`def-scott-ideal`, `prop-wkl-scott`), a Scott ideal of low sets (`thm-low-scott`),
   Harrington's conservation (stated). Exercises: REC is the intersection of the ω-models;
   Scott ideals are not principal; bounded König's lemma in WKL₀.
4. **Σ⁰₁ separation and the Heine–Borel theorem** (`separation-heine-borel`, new
   2026-11-12): `thm-wkl-separation`, `thm-wkl-heine-borel`, table of further equivalents.
   Exercise: separation for injections with disjoint ranges.
5. **Transfinite recursion and Π¹₁ comprehension** (`atr0-pi11ca0`): well-orderings,
   `def-atr0`, `def-pi11-ca0`, Kleene normal form (`fact-kleene-normal-form`, admitted),
   `thm-pi11-trees`, survey table, separation table. Exercises: ATR₀ proves the ω-jump;
   ACA₀ + Σ¹₁-CA proves the ω-jump.

## 4. Proof techniques

- **Coding the range of an injection** (reversals to ACA₀): `thm-aca-equivalents` (4 ⇒ 2,
  least witnesses), then every reversal of lesson 2. Named explicitly at the start of
  lesson 2 and compared with the computable constructions of Specker and of
  `thm-finitely-branching-jump`.
- **Coding trees and separating sets** (reversals to WKL₀): lesson 4 (choice by a
  separating set, Cantor-set cover), and the bounded-tree coding in lesson 3.
- **ω-models and absoluteness**: every separation of the course; the minimal-model method
  (REC, ARITH).
- **Closing a model under solutions while preserving a property** (low basis theorem
  iterated): `thm-low-scott`, and cone avoidance in an exercise; announced as the method of
  the Ramsey course.
- **Universal instances** (DNC₂ tree for WKL): `prop-wkl-scott` (2).
- **Normal forms** for computable presentations (torsion group): lesson 2.
- **Induction for Π⁰₁ formulas** in verifications: `thm-wkl-separation`.
- **Arithmetic transfinite induction** along a well-ordering: uniqueness of hierarchies,
  lesson 5.
- **Incompleteness** as a separation tool: ATR₀ vs Π¹₁-CA₀ (stated).

## 5. Choices

- **Split into five lessons (2026-11-12).** The former `aca0` (2300 words) and `wkl0` (2650
  words) could not receive intuitions, examples, figures and quizzes within the 25–45 minute
  bound. `aca0` keeps the system and its ω-models; the reversals move to `aca0-reversals`.
  `wkl0` keeps the system, the ω-models and conservation; the two equivalences move to
  `separation-heine-borel`. The slugs `aca0` and `wkl0` keep the labels cited by other
  courses (`def-aca0`, `thm-aca-equivalents`, `def-scott-ideal`, `prop-wkl-scott`,
  `thm-low-scott`). Moved labels: `thm-monotone-aca`, `thm-konig-aca` (to
  `aca0-reversals`); `thm-wkl-separation`, `thm-wkl-heine-borel` (to
  `separation-heine-borel`). External citations of the moved labels remain within
  transitive prerequisites (ramsey-theorem/jockusch requires big-five/wkl0, which requires
  aca0-reversals); analysis-in-rca0 cites `thm-monotone-aca` as a forward pointer.
- **Added torsion subgroups** (`thm-torsion-aca`): the track design promises algebra
  examples, and this is the shortest complete algebraic reversal (Simpson III.6.2). Bases of
  vector spaces and maximal ideals need quotient structures in RCA₀ and are only cited.
- **ACA₀ before WKL₀**, as in Simpson, Hirschfeldt and Dzhafarov–Mummert: WKL₀ is defined
  as a weakening of König's lemma, and the separation uses the jump ideals.
- **Low Scott ideal by a chain**, rather than Simpson's single path through a tree of codes
  of models: the chain uses only the low basis theorem relativized, and the same scheme
  is reused in the Ramsey course. Simpson's proof is mentioned.
- **ATR₀ and Π¹₁-CA₀ as a survey**: the track focuses on the world below ACA₀ and on
  first-order strength; the higher systems are needed for orientation and for the separation
  chain. Only `thm-pi11-trees` is proved; the normal form and all equivalents are admitted
  with exact references. Comparability of well-orderings (the central ATR₀ result) would
  require pseudohierarchies and was left out.
- **Excluded:** Σ¹₁-AC₀ and Δ¹₁-CA₀, β-models beyond a definition, the reverse mathematics
  of Ramsey's theorem (next course), conservation proofs (induction-conservation), weak weak
  König's lemma (randomness-related, not in the Big Five), well-ordering principles (one
  paragraph).

## 6. Comparison with the literature

- **Simpson, *Subsystems of Second Order Arithmetic*** (2009): Chapters III (ACA₀), IV
  (WKL₀), V (ATR₀), VI (Π¹₁-CA₀), VII–VIII (β- and ω-models), IX (conservation). The course
  follows his proofs for Lemma III.1.3, Theorems III.2.2, III.6.2, III.7.2, IV.1.2,
  Lemma IV.4.4, Lemma VI.1.1. Differences: monotone convergence reversal gives an explicit
  Δ⁰₁ definition; König's lemma reversal uses a simpler tree than Simpson's (7)–(8); the
  low Scott ideal is built as a chain.
- **Hirschfeldt, *Slicing the Truth*** (2014), Sections 4.3–4.5 and 10.3: the same
  equivalences, mostly as exercises (4.10–4.12), and the description of the reversal
  method, which lesson 2 makes explicit.
- **Dzhafarov–Mummert** (2022): Sections 5.6–5.8 (the systems, Kleene normal form
  Theorem 5.8.2), 10.5 (compactness), Chapter 11 (algebra), 12.1 (well-orderings). Close to
  the course in spirit; they treat ATR₀ in more detail.

## 7. Pedagogical plan

1. `aca0`: examples of arithmetic instances; intuition for the three forms of Σ⁰₁
   comprehension; remark on counting applications; examples and counterexamples of jump
   ideals; the minimal-model method named. Quizzes on the injection coding, on the join in
   (3 ⇒ 2), on ω-models.
2. `aca0-reversals`: the reversal pattern stated at the start; intuition before each
   theorem; figure `konig-tree` (the tree of the reversal with a dying wrong guess);
   remark on why the torsion group needs normal forms; remark on bounded trees. Quizzes on
   monotone convergence and König's lemma.
3. `wkl0`: examples of WKL instances (DNC₂, separating sets); why binary (counterexample:
   the König tree with two successors); universal instance; intuition for the low model.
   Quizzes on the low model (three questions). No figure: the chain construction is
   short.
4. `separation-heine-borel`: contrast with ACA₀ reversals; example of separation (DNC);
   intuition for both proofs; figures `separation-choice` and `cantor-cover`; quizzes on
   separation (three) and Heine–Borel (two); table of further equivalents.
5. `atr0-pi11ca0`: examples of coded orders (ω, ω+ω, ω*); intuition for ATR; figure
   `jump-hierarchy`; arithmetic transfinite induction named; tables of equivalents and of
   separations.

Figures are generated by `scripts/figures/big-five.py`.

## 8. Sources (checked against the books on 2026-11-12)

- `aca0`: Simpson Lemma III.1.3, Section VIII.1 (Corollary VIII.1.11), Section IX.1;
  Friedman, JSL 41 (1976) 557–559; Hirschfeldt 4.3; Dzhafarov–Mummert 5.6.
- `aca0-reversals`: Simpson Theorems III.2.2, III.2.9, III.4.3, III.5.5, III.6.2, III.7.2,
  Lemma IV.1.4; Friedman–Simpson–Smith, APAL 25 (1983) 141–181; Specker, JSL 14 (1949).
- `wkl0`: Simpson Sections VIII.2 (Theorem VIII.2.17, Corollaries VIII.2.18, VIII.2.27, notes
  on Scott), IX.2 (Harrington, 1977, unpublished), Theorem IX.3.16 and notes (Friedman,
  Parsons, Sieg 1985); Scott, Proc. Sympos. Pure Math. V (1962) 117–121; Jockusch–Soare,
  Trans. AMS 173 (1972) 33–56.
- `separation-heine-borel`: Simpson Lemma IV.4.4, Lemma IV.1.1, Theorem IV.1.2 and notes,
  Theorems IV.2.3, IV.3.3, IV.6.4, IV.7.7, IV.9.3–IV.9.4.
- `atr0-pi11ca0`: Simpson Section I.11 (Π¹₁-CA₀ ⊇ ATR₀), Lemma V.1.4, Lemma V.2.1,
  Proposition V.2.6, Theorems V.5.1, V.5.5, V.6.8, V.7.3, V.8.7, VI.1.3, VI.1.6, VI.4.1,
  Lemma VI.1.1, Theorems VII.2.7, VII.2.10, Corollary VII.2.11, Corollary VIII.6.6 and notes
  (Gandy–Kreisel–Tait 1960), Remark V.6.10 (Girard); Friedman ICM 1974 (1975) 235–242;
  Steel thesis 1976.

## 9. Recent literature

Checked (web search, 2026-11-12): well-ordering principles.
- Marcone–Montalbán, *The Veblen functions for computability theorists*, JSL 76 (2011)
  575–602: computability-theoretic proof of Friedman's equivalence of ATR₀ with
  "X WO ⇒ φ(X, 0) WO".
- Freund, *Π¹₁-comprehension as a well-ordering principle*, Adv. Math. 355 (2019) 106767:
  Π¹₁-CA₀ equivalent to a Bachmann–Howard fixed point principle for dilators.
- Girard (1987), see Hirst, APAL 66 (1994) 1–18, Theorem 2.6, and Simpson Remark V.6.10:
  ACA₀ ↔ "X WO ⇒ 2^X WO".
Effect: one paragraph in lesson 5, with references. No simpler proofs of the core
equivalences were found; Dzhafarov–Mummert (2022) is the recent textbook reference.

## 10. Open points

- Lessons 2, 4 and 5 have about 2750–2820 words (formulas inflate the count), slightly
  above the 2700 target; durations set to 50. A further split of lesson 5 (well-orderings
  and ATR₀ / Π¹₁-CA₀) could be considered if the survey grows.
- A proof of comparability of well-orderings in ATR₀, or of the normal form, would make
  lesson 5 less of a survey; both are long.
- Jockusch–Soare 1972 pages: Simpson's bibliography says 35–56, all other books 33–56;
  the course uses 33–56.

## 11. History

- **2026-11-12.** Design revision. Split into five lessons (new `aca0-reversals`,
  `separation-heine-borel`); new theorem `thm-torsion-aca`; intuitions, examples and
  counterexamples throughout; four figures (`scripts/figures/big-five.py`); six new quiz
  questions; new exercises (ARITH(A), least upper bounds, Scott ideals not principal,
  bounded König's lemma moved from a remark). References checked against Simpson:
  corrected "Π¹₁-CA₀ ⊢ ATR₀ (Simpson V.1)" to Section I.11 / Theorem V.5.1; the survey
  table now gives theorem numbers and base theories (perfect set and Cantor–Bendixson are
  over ACA₀ and for 2^ℕ, ℕ^ℕ, not ℝ); Lusin's separation removed from the table (its
  reversal in Simpson V.5 is through Σ¹₁ separation, which is listed); "Chapter VIII"
  references made precise; well-ordering principles added. The HYP/ATR₀ pointer now goes
  to hyperarithmetic/pseudo-well-orderings, where the fact is proved; aca0-reversals
  depends on second-order-arithmetic/real-numbers (new lesson of that course).
