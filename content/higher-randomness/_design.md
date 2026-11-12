# Design log: Higher randomness

This file is the memory of the course (see "Designing tracks and courses" in
`AGENTS.md`). It is not rendered.

## 1. Objectives

After the course, a student can:

- describe a Π¹₁ class as the increasing union of its stages along the countable
  ordinals, prove that a sequence Y enters at a stage below ω₁^Y, that the stages below
  ω₁ᶜᵏ are Δ¹₁, and that every Δ¹₁ class is such a stage (boundedness for classes);
- prove Lusin's theorem that Π¹₁ and Σ¹₁ classes are measurable;
- define Δ¹₁-randomness, Π¹₁-Martin-Löf randomness and Π¹₁-randomness, compare them,
  and characterize Δ¹₁-randomness as Martin-Löf randomness relative to every
  hyperarithmetic set;
- build a universal higher Martin-Löf test by trimming along ordinal stages;
- prove the Sacks–Tanaka theorem (the class of sequences collapsing ω₁ᶜᵏ is Π¹₁ and
  null) by selection and boundedness;
- prove the characterization of Π¹₁-randomness (Stern; Chong–Nies–Yu), the existence
  of a largest null Π¹₁ class, the coincidence of Σ¹₁- and Δ¹₁-randomness, and the null
  cone theorem for ≤_h.

**Role.** Specialized course (`content/tracks-design.md`, algorithmic randomness:
"Higher randomness, which needs the higher computability track"). It is the place where
the two tracks meet: the higher computability track supplies stages, norms, selection
and boundedness; the randomness track supplies tests, measure and the majority vote. It
is a test of the analogy Π¹₁ ↔ c.e. and shows where it fails (limit stages, stages
beyond ω₁ᶜᵏ).

## 2. Prerequisites assumed

- Computable ordinals: WO and L_e (`def-wo`), the comparison theorem (`thm-wo-comparison`),
  trees and ranks, D_L (`prop-descending-tree`), Kleene–Brouwer (`thm-kleene-brouwer`),
  normal form (`thm-pi11-normal-form`), Π¹₁ ≠ Σ¹₁ (`prop-pi11-not-sigma11`), boundedness
  (`thm-boundedness`, `ex-o-bounded`), notations (`prop-constructive-computable`,
  `cor-constructive-computable`), ω₁^O > ω₁ᶜᵏ (`prop-omega1-relative`).
- Hyperarithmetic sets: H-sets (`def-h-sets`), H-sequences and their uniqueness
  (`lem-h-sequence-unique`, `prop-h-delta11`), Kleene's theorem and its relativization
  (`thm-kleene-delta11`), Spector's uniqueness (`thm-spector-uniqueness`), Σ¹₁ classes and
  the Kleene basis theorem (`def-sigma11-class`, `thm-kleene-basis`).
- Effective descriptive set theory: rank comparison (`lem-rank-comparison`), stages
  (`def-pi11-stage`, `thm-stage-comparison`), Kreisel selection (`cor-total-pi11`), stages
  of Π¹₁ sets (`thm-pi11-stages`).
- Martin-Löf randomness: measure (`fact-lebesgue-measure`, `prop-measure-effective`),
  tests and the universal test (`def-ml-test`, `thm-universal-test`), the density lemma
  and Sacks's theorem (`lem-density`, `thm-sacks`), Ω (`cor-omega-random`), leftmost
  paths of Π⁰₁ classes (`prop-leftmost-path`, through `martin-lof-tests`).

## 3. Results, lesson by lesson

1. **Stages of Π¹₁ classes** (`pi11-classes`, new 2026-11-12): stages of a Π¹₁ class
   `def-class-stages`, examples `ex-class-stages` (open classes, well-founded relations);
   `fact-pi11-stages` (now a proposition with proof: Δ¹₁ stages below ω₁ᶜᵏ, uniformly;
   entry below ω₁^Y); `prop-class-boundedness`; `cor-delta11-stage` (Δ¹₁ = bounded stage);
   `ex-delta11-classes` (hyperarithmetic singletons, classes arithmetic in a
   hyperarithmetic set, the well-founded relations are not Σ¹₁).
2. **Measure of Π¹₁ classes** (`pi11-measure`, new): `lem-stages-borel`, `thm-lusin`
   (with proof), figure `fig-stage-measure`, `fact-higher-borel` (admitted: measure of Δ¹₁
   classes uniformly Π¹₁; approximation by open classes c.e. in a hyperarithmetic set),
   `ex-measure-pi11`.
3. **Δ¹₁-randomness and higher Martin-Löf tests** (`higher-tests`): `def-delta11-random`,
   `ex-delta11-null`, `prop-delta11-arith`, `prop-pi11-open`, `def-higher-ml`,
   `ex-higher-ml-tests`, `prop-higher-ml-delta11`, separation admitted, `thm-higher-universal`
   with figure `fig-universal-trimming`, `cor-higher-mlr-class`. Exercise: Δ¹₁-random iff
   ML-random relative to every hyperarithmetic set.
4. **The Sacks–Tanaka theorem** (`sacks-tanaka`, new): `thm-sacks-tanaka` with a full
   proof (previously admitted). Exercise: λ(𝒜) = sup of the Δ¹₁ stages, hence the
   measure lemma for Π¹₁ classes from its Δ¹₁ case.
5. **Π¹₁-randomness** (`pi11-randomness`): `def-pi11-random`, `thm-chong-nies-yu`,
   `cor-pi11-random-class`, `thm-largest-null` (new label; previously a paragraph).
   Exercises: union of null Δ¹₁ classes is Π¹₁ and not Δ¹₁; finite changes and halves.
6. **Σ¹₁ null classes and hyperarithmetic reducibility** (`hyperdegrees`):
   `thm-sigma11-random` (moved here from `pi11-randomness`, new simpler proof),
   `def-hyp-reducible`, `fact-hyp-reducible` (now a proposition with proof),
   `thm-higher-null-cone` with figure `fig-majority-vote`, `cor-higher-null-cone`,
   hierarchy with figure `fig-randomness-hierarchy`, lowness results.

## 4. Proof techniques

- **Stage comparison by strictly monotone maps** (from `descriptive-set-theory/norms`):
  Δ¹₁-ness of the stages (`fact-pi11-stages`), trimming (`thm-higher-universal`).
- **Boundedness** (from `computable-ordinals/boundedness`): `prop-class-boundedness`,
  `cor-delta11-stage`.
- **Measure-theoretic stabilization** along ω₁: `thm-lusin`.
- **Trimming along stages** (classical: `thm-universal-test`): `thm-higher-universal`.
- **Selection and boundedness**: a total Π¹₁ relation on n is uniformized by a
  hyperarithmetic function (Kreisel), whose range of notations is bounded (Spector).
  Introduced for sets in `thm-pi11-stages`; here `thm-sacks-tanaka`, `thm-sigma11-random`.
- **Majority vote over a cylinder** (classical: `thm-sacks`): `thm-higher-null-cone`.
- **Decomposition of a null Π¹₁ class**: Δ¹₁ stages plus the null class 𝒞
  (`thm-chong-nies-yu`, `thm-largest-null`).
- **Relativization** of Kleene's and Spector's theorems: `fact-hyp-reducible`.

## 5. Choices

- **Two preliminary lessons on Π¹₁ classes.** The previous version admitted four
  "facts" (Δ¹₁ classes as classes D_{a,e} computed from H^Y_a, with uniform definitions;
  hyperarithmetic measures; approximation; Lusin) plus the stage facts. Most of this is
  provable with the tools of the prerequisite courses: the stage decomposition with
  `lem-rank-comparison`, the Δ¹₁ = bounded stage theorem with the boundedness argument,
  Lusin's theorem with a half-page stabilization argument (Nies 9.1.9). Proving them
  gives the students the picture the rest of the course uses. The D_{a,e} framework was
  dropped: every use is covered by the stages 𝒜^p_{|a|} (`cor-delta11-stage`) or, in the
  null cone theorem, by relativized H-sequences (`prop-h-delta11`).
- **Only two admitted facts remain** (`fact-higher-borel`): the measure of Δ¹₁ classes
  is uniformly Π¹₁ (stated for pairs of Π¹₁ definitions, the form the proofs need), and
  the approximation of Δ¹₁ classes by open classes c.e. in a hyperarithmetic set. Both
  are effective transfinite recursions along Borel codes; their proofs would need effective
  Borel codes, which the hyperarithmetic course deliberately avoids. The general measure
  lemma for Π¹₁ classes is derived as an exercise of `sacks-tanaka`.
- **Sacks–Tanaka proved** (previously admitted with a sketch). The proof of Monin and
  Patey (selection and boundedness) uses only Kreisel selection, `ex-o-bounded`, the
  stages and the measure fact, and teaches the technique reused in `thm-sigma11-random`.
  Nies derives it instead from the hyperarithmetic null cone theorem and Spector's
  theorem; that order would make `thm-higher-null-cone` depend on an admitted cone result.
  In this course the null cone theorem uses Sacks–Tanaka, so Sacks–Tanaka must come first.
- **Σ¹₁ = Δ¹₁ moved to the last lesson.** It uses the same technique as Sacks–Tanaka and
  shortens the Π¹₁-randomness lesson; its new proof is shorter (measure ≥ 1 − 2⁻ⁿ at a
  selected stage, no auxiliary classes ℰ_α).
- **Largest null Π¹₁ class** promoted from a paragraph to a theorem (`thm-largest-null`),
  following Nies 9.3.6/9.3.8 with stages.
- **`fact-hyp-reducible` proved** from relativized Kleene and Spector theorems; the
  label is kept, the kind is now proposition (same for `fact-pi11-stages`).
- **Order.** Stages, measure, tests (to reach randomness early), Sacks–Tanaka, Π¹₁-
  randomness, Σ¹₁ and ≤_h. Sacks–Tanaka could precede the tests; it is placed just before
  its first use.
- **Excluded.** Higher prefix-free complexity and the higher Schnorr theorem (Hjorth–
  Nies; Nies 9.2) — a full course of its own, and the universal test is obtained directly
  by trimming. Higher K-triviality, lowness, hyp-dominated sets (Nies 9.2, 9.4),
  continuous higher reducibility (Bienvenu–Greenberg–Monin), Σ¹₁-genericity
  (Greenberg–Monin) — research topics, mentioned in the last lesson. The separations
  Δ¹₁ ≠ Π¹₁-ML and Π¹₁-ML ≠ Π¹₁ are admitted (constructions of Hjorth–Nies, Nies 9.2.9).

## 6. Comparison with the literature

- **Nies, Chapter 9** (Sections 9.1–9.4): preliminaries with Π¹₁ classes as functionals
  producing linear orders (9.1.3, 9.1.4), Lusin (9.1.9), Measure Lemma (9.1.10), Sacks's
  null cone (9.1.13), Spector (9.1.14), Sacks–Tanaka as a corollary (9.1.15); higher ML
  via Π¹₁ machines (9.2); Δ¹₁- and Π¹₁-randomness, largest null Π¹₁ class (9.3.6),
  characterization (9.3.9); lowness (9.4). The course uses trees instead of linear orders
  (so that the stage comparison of the descriptive-set-theory course applies verbatim),
  proves more of 9.1, and omits the L_{ω₁ᶜᵏ} (Spector–Gandy) viewpoint and Π¹₁ machines.
- **Monin–Patey, chapter "Higher randomness"**: overview of the three notions, the
  approximation lemma, Lusin, Sacks–Tanaka with the proof followed here, the
  characterization, Σ¹₁ = Δ¹₁, the null cone, then the separation Δ¹₁ ≠ Π¹₁-ML by a
  Π¹₁ construction, and higher Kolmogorov complexity. The course follows its order of
  results for lessons 4–6 and uses its proofs of Sacks–Tanaka and of the null cone.
- **Hjorth–Nies (2007)**: Π¹₁-ML-randomness, higher KC and Schnorr theorems, lowness,
  largest null Π¹₁ class ("strong randomness"). Their universal test comes from K; ours
  from trimming.
- **Chong–Yu (2015)**: monograph treatment, not checked locally.

## 7. Pedagogical plan

- `pi11-classes`: intuition "Π¹₁ classes are enumerated along the ordinals, like Σ⁰₁
  classes along ℕ"; examples: open classes (finite stages) and well-founded relations
  (all countable stages); the new phenomenon (stages beyond ω₁ᶜᵏ only for sequences
  collapsing ω₁ᶜᵏ); quizzes on the two comparisons and on a ∈ 𝒪; counterexample: the
  well-founded relations are not Σ¹₁.
- `pi11-measure`: intuition "the measures of the stages stop increasing"; figure
  `stage-measure`; example of a null non-Borel Π¹₁ class; the measure facts as higher
  counterparts of left-c.e. measures and outer regularity.
- `higher-tests`: why randomness restricts null classes ({X}); examples of null Δ¹₁
  classes; examples of higher tests and the counterexample showing uniformity is needed;
  figure `universal-trimming`; quizzes on the approximation and on trimming.
- `sacks-tanaka`: idea paragraph before the proof (cofinal ranks, selection,
  boundedness); quizzes on why the selection must be hyperarithmetic and where r < λ(ℬ)
  is used.
- `pi11-randomness`: O and the well-founded relations as examples; quizzes on the
  characterization; comparison of the largest null class with the other notions.
- `hyperdegrees`: Σ¹₁ as "Δ¹₁ stages carry almost all measure"; majority vote figure;
  hierarchy figure with separating examples; quizzes.

## 8. Sources (checked 2026-11-12)

- `pi11-classes`: Nies 9.1.3–9.1.4 (stages via linear orders); boundedness for classes
  is the class form of Spector's theorem (computable-ordinals course).
- `pi11-measure`: Lusin — Nies Theorem 9.1.9 (checked), Monin–Patey "Higher randomness"
  (checked); measure fact — Nies Measure Lemma 9.1.10 (checked; refers to "Sacks
  1.11.IV"), Hjorth–Nies (cite "Exercise 1.11.IV"); approximation — Monin–Patey lemma
  (checked), Nies 9.3.3 refers to "Sacks 1.8.IV".
- `higher-tests`: Martin-Löf 1970; Hjorth–Nies 2007 (preprint text checked: definitions,
  universal test via K, largest null Π¹₁ set); Nies 9.2.8 (R_b test), 9.3.4–9.3.5
  (separation), Exercise 9.3.13 hint (Δ¹₁-random iff ML-random in every hyp set).
- `sacks-tanaka`: Sacks 1969, Tanaka 1967; Nies 9.1.11 (basis), 9.1.13–9.1.15; Monin–
  Patey proof (checked).
- `pi11-randomness`: Greenberg–Monin 2017 introduction (checked): Sacks [Sac90, IV.2.5]
  first defined Π¹₁-randomness; characterization first proved by Stern (1973, 1975),
  rediscovered by Chong–Nies–Yu; largest null Π¹₁ set by Stern and independently Kechris
  (1975), rediscovered by Hjorth–Nies. Nies 9.3.6, 9.3.8, 9.3.9, 9.3.11 (checked).
- `hyperdegrees`: Σ¹₁ = Δ¹₁ — Monin–Patey cite Sacks IV.2.5, Nies attributes to
  Chong–Nies–Yu 2008 (both recorded); null cone — Nies 9.1.13 (Sacks 2.4.IV), Monin–
  Patey proof; Spector — Nies 9.1.14; separations — Nies 9.2.9, 9.2.10, 9.3.5; lowness —
  Nies 9.2.16, Question 9.4.11; Greenberg–Monin Theorems 3.1 and 3.3 (checked).
- Sacks's book was not available; only chapter-level references are given, with the
  item numbers as quoted by Nies, Hjorth–Nies, Monin–Patey and Greenberg–Monin.

## 9. Recent literature

Checked (web, 2026-11-12):
- Greenberg and Monin, *Higher randomness and genericity*, Forum Math. Sigma 5 (2017):
  answer Nies's Question 9.4.11 — a set is low for Π¹₁-randomness iff it is
  hyperarithmetic (Theorem 3.1: if A is not hyperarithmetic, some Π¹₁-random is not
  Π¹₁(A)-ML-random); cupping (Theorem 3.3). The previous course mentioned Theorem 3.1 but
  not that it settles the open question; now said explicitly.
- Their introduction corrects attributions: the characterization of Π¹₁-randomness is
  due first to Stern (1973, 1975); the largest null Π¹₁ class to Stern and Kechris
  (1975). Theorem titles and notes updated.
- Monin, *Higher randomness and forcing with closed sets*, STACS 2014: the class of
  Π¹₁-randoms is Π⁰₃. Mentioned in the notes of `pi11-randomness`.
- Bienvenu, Greenberg and Monin, *Continuous higher randomness*, JML 2017: higher Turing
  reducibility; Π¹₁-randomness differs from higher weak 2-randomness. Cited only.
No simpler proof of the main theorems was found; the Monin–Patey proof of Sacks–Tanaka
is the simplest available with the course's tools.

## 10. Open points

- Attribution of Σ¹₁ = Δ¹₁: Sacks (Monin–Patey) or Chong–Nies–Yu (Nies). Both recorded in
  the notes; check Sacks IV.2.5 and Kechris/Stern 1975 when a copy is available.
- Original source of the measure lemma (Sacks 1969? Tanaka? Kechris 1973?) not checked;
  only Nies's and Hjorth–Nies's citations of Sacks's book are given.
- Sacks's section numbers (IV.1.8, IV.1.11, IV.2.2, IV.2.4, IV.2.5) come from secondary
  sources; kept at chapter level in the lessons.
- The separations Δ¹₁ ≠ Π¹₁-ML (Hjorth–Nies) and Π¹₁-ML ≠ Π¹₁ (higher Kučera–Gács) are
  admitted. A future lesson on higher prefix-free complexity could prove them.
- Monin's thesis, mentioned in the previous version, was removed from the references
  (no checked bibliographic data).

## 11. History

- **2026-11-12.** Design revision.
  - Course split into six lessons: new `pi11-classes` (stages), `pi11-measure` (Lusin and
    measure facts), `sacks-tanaka`; `hyperdegrees` renamed "Σ¹₁ null classes and
    hyperarithmetic reducibility".
  - Proved: the stage facts (`fact-pi11-stages`, now a proposition), Δ¹₁ = bounded stages
    (`prop-class-boundedness`, `cor-delta11-stage`, new), Lusin (`thm-lusin`, new),
    Sacks–Tanaka (`thm-sacks-tanaka`, previously admitted), `fact-hyp-reducible` (now a
    proposition), the largest null Π¹₁ class (`thm-largest-null`, new).
  - `fact-higher-borel` reduced to two admitted items (measure of Δ¹₁ classes;
    approximation); the D_{a,e} framework removed.
  - Moved labels: `fact-higher-borel` (higher-tests → pi11-measure), `fact-pi11-stages`
    (pi11-randomness → pi11-classes), `thm-sacks-tanaka` (pi11-randomness → sacks-tanaka),
    `thm-sigma11-random` (pi11-randomness → hyperdegrees). No external citers.
  - New labels: `def-class-stages`, `ex-class-stages`, `prop-class-boundedness`,
    `cor-delta11-stage`, `ex-delta11-classes`, `lem-stages-borel`, `thm-lusin`,
    `fig-stage-measure`, `ex-measure-pi11`, `ex-delta11-null`, `ex-higher-ml-tests`,
    `fig-universal-trimming`, `thm-largest-null`, `fig-majority-vote`,
    `fig-randomness-hierarchy`. No label removed.
  - Four figures, generator `scripts/figures/higher-randomness.py`.
  - Prerequisites updated after the restructuring of the prerequisite courses
    (`thm-sacks`, `lem-density` now in `martin-lof-randomness/upper-cones`;
    `ex-o-bounded` replaces "the first exercise of kleene-theorem"; `prop-omega1-relative`
    replaces the repeated argument that O collapses ω₁ᶜᵏ).
  - Attributions corrected after Greenberg–Monin 2017 (Stern; Kechris); the lowness
    question for Π¹₁-randomness reported as solved.
