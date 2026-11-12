# Design log: Second-order arithmetic

## 1. Objectives

After the course, a student can:
- read, write and classify formulas of $\mathcal L_2$, and formalize statements about countable objects (functions, reals, continuous functions) through codings;
- use the completeness theorem with ω-models to prove unprovability, and absoluteness of arithmetic formulas to transfer statements between an ω-model and reality;
- characterize the ω-models of RCA₀ as Turing ideals and use REC as a counter-model;
- work in a non-standard model of RCA₀ with overspill, and keep apart "finite in the model" and "finite";
- formalize the reals and continuous functions on [0, 1] in RCA₀, prove the intermediate value theorem there, and refute monotone convergence in REC.

**Role in the track.** First course of the reverse mathematics track (`tracks.yaml`). It sets up the framework used by every later course: the language, Henkin models, ω-models and Turing ideals (Big Five, Ramsey's theorem, reducibilities), non-standard models (induction and conservation), and the coding of analysis (Big Five, Weihrauch reducibility).

## 2. Prerequisites assumed

- The arithmetic hierarchy and its relativization; Σ⁰₁ formulas define the c.e. sets (`arithmetic-hierarchy/arithmetic-definability`, `cor-sigma1-ce`, `def-relativized-hierarchy`).
- Turing reducibility, join, the jump, finite-oracle computations (`def-finite-oracle`).
- Π⁰₁ classes: an infinite computable binary tree without computable path (`pi01-classes/computable-members`, `thm-dnc2-no-computable`).
- First-order logic: completeness and compactness theorems (admitted, with references).

## 3. Results

1. **language-and-models.** `def-l2`, formula classes, `ex-formalization` (functions, infiniteness, the Π¹₂ shape of theorems as problems), `def-z2`, `prop-induction-comprehension`, `def-l2-structure`, `def-omega-model`, `prop-omega-absolute` (absoluteness, full induction in ω-models); the Big Five table.
2. **rca0.** `def-rca0`, `ex-rca-range`, `prop-pi01-induction`, `def-turing-ideal`, `ex-turing-ideals`, `thm-rca-turing-ideal`, REC is the least ω-model, `cor-rca-not-wkl`.
3. **nonstandard-models** (new). Existence by compactness, `fig-nonstandard-order`, `ex-definable-model` (definable sets over a model of true arithmetic give a model of ACA₀), `prop-full-standard` (Dedekind: full structures are standard), `prop-overspill`, `cor-standard-not-set`, finite versus bounded sets (admitted coding theorem), the role of induction (Hirst, Friedman, pointers).
4. **real-numbers** (new, split from analysis-in-rca0). `def-real-rca`, `ex-real-equality` (equality of reals not decidable), `prop-rca-complete`, `prop-specker`.
5. **analysis-in-rca0** (now "Continuous functions in RCA₀"). `def-continuous-code` (with an index field), evaluation, `fig-function-code`, `lem-value-sigma1`, `fig-bisection`, `thm-ivt-rca`.

## 4. Proof techniques

- **Absoluteness** of arithmetic formulas for ω-models (`prop-omega-absolute`); used in every ω-model argument (lessons 1, 2, 4).
- **Metatheoretic induction** on the true numbers (full induction in ω-models; Dedekind's theorem).
- **Separation by an ω-model**: REC as counter-model (`cor-rca-not-wkl`, `prop-specker`); completeness theorem.
- **Coding in RCA₀**: show that a construction is computable from given sets by giving Σ⁰₁ and Π⁰₁ definitions (`ex-rca-range`, `prop-rca-complete`, evaluation of codes, `thm-ivt-rca`); the index trick turning Σ⁰₁ descriptions into codes (`def-continuous-code`, Exercise 1 of lesson 5).
- **Compactness** to build non-standard models; **overspill** (`prop-overspill`), the basic technique for non-standard models, used again in the course on induction and conservation.
- **Non-uniform case distinction** in a classical proof (`thm-ivt-rca`), as the bridge to Weihrauch reducibility.

## 5. Choices

- **Henkin semantics first, full semantics as a contrast.** The completeness theorem is the reason for the choice; Dedekind's theorem (`prop-full-standard`) shows what full semantics would cost. Placed in the lesson on non-standard models, where it motivates why non-standard models must be allowed.
- **A lesson on non-standard models (new).** The track design gives "non-standard models and conservation" as a technique, and the course on induction and conservation (now in the track) starts with induction schemes in non-standard models. Before this revision the course mentioned non-standard models only in passing. The new lesson gives the minimum: existence, overspill, the standard part is not a set, finite versus bounded. Conservation and the Paris–Kirby hierarchy stay in the later course.
- **Splitting the analysis lesson.** With examples, figures and the evaluation lemma, the former lesson would have taken about 65 minutes. It is split into reals (with Specker sequences) and continuous functions (with the IVT). The slug `analysis-in-rca0` is kept for the second lesson, which has `real-numbers` as prerequisite, so every course that lists `analysis-in-rca0` as a prerequisite still reaches all moved labels transitively.
- **Index field in codes of continuous functions.** Adopted from Simpson (Definition II.6.1) and Dzhafarov–Mummert (Definition 10.3.3). It resolves the open point of the November 2026 review: without it, a code given by a Σ⁰₁ formula, such as the code of f − c, cannot be formed in RCA₀. The consistency condition is kept in the "overlapping intervals" form, which is equivalent to Simpson's condition with his two closure conditions (checked; see the remark in the lesson).
- **Lemma on Σ⁰₁ comparison of values (`lem-value-sigma1`).** It was used implicitly in the IVT proof and proved inside an exercise solution; it is now stated and proved before the IVT.
- **Formalization of arithmetic admitted.** Pairing, finite sequences, primitive recursion and the coding of finite sets in RCA₀ are admitted with precise references (Simpson II.2–II.3; Dzhafarov–Mummert 5.5). Proving them would add a long lesson of routine arithmetic and teach no technique used later.
- **Excluded.** Complete separable metric spaces, open and closed sets, and the reverse mathematics of analysis beyond the IVT and monotone convergence (Simpson II.5–II.7, Chapter IV; Dzhafarov–Mummert 10.5–10.8): the Big Five course gives the reversals that the track needs. RCA₀* and weaker bases (Dzhafarov–Mummert 6.6) are only mentioned.
- **Order of lessons.** Language → RCA₀ → non-standard models → reals → continuous functions. The non-standard lesson follows RCA₀ because overspill uses Σ⁰₁ and Π⁰₁ induction; the two analysis lessons end the course and lead to the Big Five.

## 6. Comparison with the literature

- **Simpson**, Sections I.2 (language, Z₂, models), II.1 (RCA₀, Theorem II.1.7 on ω-models), II.2–II.3 (finite sets, primitive recursion, bounded Σ⁰₁ comprehension, Π⁰₁ induction), II.4 (reals, Example II.4.7 Specker), II.6 (continuous functions, Theorem II.6.6 IVT), IX.1 (first-order part). The course follows Simpson's axioms and codings, but proves Π⁰₁ induction directly instead of through bounded Σ⁰₁ comprehension, and organizes RCA₀ around Turing ideals.
- **Dzhafarov–Mummert**, Chapter 5 (5.1–5.5 for lessons 1–2, 5.12 full semantics), Section 6.2 (cuts, overspill), Section 6.6 (why Σ⁰₁ induction), Chapter 10 (10.1–10.4: reals, continuous functions, IVT). The course shares their computability-theoretic emphasis and their view of theorems as problems (Chapter 3), announced in lesson 1 for the reducibilities course. Differences: DM use PA⁻ as basic axioms and define ω-models as Turing ideals; here ω-models are arbitrary and the characterization is a theorem.
- **Hirschfeldt**, *Slicing the Truth*, Sections 4.1–4.2: RCA₀, working in RCA₀, finite versus bounded. Similar level; the course adds the analysis.

## 7. Pedagogical plan

1. **language-and-models.** Intuition: Henkin semantics gives completeness; ω-models are where computability applies. Example of formalization (graphs of functions, infiniteness, the Π¹₂ shape, instances and solutions). Example of a comprehension instance (complement). Quizzes on absoluteness and full induction.
2. **rca0.** Intuition: the method of the track (computable proofs versus Turing-ideal counter-models); why Σ⁰₁ induction. Example: the range of an increasing function (Δ⁰₁ comprehension needs induction to justify a bounded definition). Examples and non-examples of Turing ideals, showing that both closure conditions are needed. Quizzes on the proof of the characterization and on completeness.
3. **nonstandard-models.** Figure of the order of a non-standard model. Example of a non-standard model of ACA₀ (definable sets). Dedekind's theorem with quiz (where fullness is used). Overspill with quiz; examples of the two failures of "finite = bounded". Exercises: underspill; sets of standard numbers are finite (and why non-standardness is needed).
4. **real-numbers.** Example of two representations of 0 (why the factor 2 in equality); example of an undecidable equality (`ex-real-equality`). Specker sequence with two quizzes (the tail argument, absoluteness of "limit").
5. **analysis-in-rca0.** Figure of a code (rectangles around the graph, shrinking around a point). Evaluation argument. Intuition for the IVT proof and figure of the bisection. Quizzes on the case distinction and on the existence of the bisection sequence. Exercise: code of f − c, using the index.

## 8. Sources

- **language-and-models:** Simpson, Definitions I.2.1–I.2.4 and the discussion after I.2.4 (ω-models satisfy full induction); Theorem II.2.2 (pairing); Dzhafarov–Mummert, Definitions 5.1.1–5.1.2, Theorem 5.1.5 (completeness), Definition 5.3.5, Exercise 5.13.1 (absoluteness for ω-submodels), Chapter 3 (problems). Friedman (ICM 1974, published 1975), Hilbert–Bernays (notes to Simpson I.2).
- **rca0:** Simpson, Definition II.1.5, Theorem II.1.7, Section II.3 (Theorems II.3.4, II.3.9, Corollary II.3.10), notes to II.1 and II.3 (Friedman's original axiomatization with primitive recursion); Dzhafarov–Mummert, Theorem 5.5.3, Theorem 6.6.1 (Hirschfeldt–Shore, JSL 72, 2007). Friedman, JSL 41 (1976), 557–559.
- **nonstandard-models:** Dedekind (1888); Dzhafarov–Mummert, Theorem 5.12.2, Proposition 6.2.2 (overspill, underspill), Sections 5.5.2 and 6.2, Section 6.5 (Hirst's theorem); Simpson, Theorem II.2.5 (bounded sets are coded), Corollary IX.1.11 (first-order part of RCA₀); Hirschfeldt, Section 4.2; Kaye, *Models of Peano Arithmetic* (general reference).
- **real-numbers:** Simpson, Definition II.4.4 and following remark, Theorem II.4.8, Example II.4.7, Theorem III.2.2; Dzhafarov–Mummert, Lemma 10.1.3, Exercise 10.9.2, Theorems 10.2.3–10.2.4; Specker, JSL 14 (1949), 145–158; Hirst (2007).
- **analysis-in-rca0:** Simpson, Definition II.6.1, Theorem II.6.6; Dzhafarov–Mummert, Definition 10.3.3, Proposition 10.3.4, Lemma 10.3.7, Theorem 10.4.1, Proposition 3.7.4, Theorem 10.4.3; Brattka–Gherardi, BSL 17 (2011), 73–117.

All section, theorem and page numbers above were checked against the text versions of Simpson (2nd ed.), Dzhafarov–Mummert (2022) and Hirschfeldt (2014).

## 9. Recent literature

- **Dzhafarov–Mummert (2022)** is the main recent presentation; the course now follows it for overspill, full semantics and the evaluation lemma, and cites it throughout.
- **Hirst, "Representations of reals in reverse mathematics"** (Bull. Pol. Acad. Sci. Math. 55, 2007, 303–316): single reals convert between representations in RCA₀; sequences may need WKL₀ or ACA₀. Cited in `real-numbers` as the justification-in-depth of the choice of fast Cauchy sequences.
- **Hirschfeldt–Shore (2007)**: Σ⁰₁ induction is needed for finite recursion (DM Theorem 6.6.1); used in `rca0` to justify the choice of Σ⁰₁ induction.
- **Brattka–Gherardi (2011)**: Weihrauch degree of the IVT; cited as the continuation of the non-uniformity remark.
- **Eastaugh, "Reverse Mathematics", Stanford Encyclopedia of Philosophy (2024)**: a survey of the foundational side; checked, not cited (the course does not treat philosophical aspects).
- No new proof or presentation found that would change the treatment of RCA₀, Turing ideals or the IVT.

## 10. Open points

- The coding of finite sets in RCA₀ (bounded sets have codes) is admitted. A future exercise could prove it with the Chinese remainder theorem (DM Theorem 5.5.8).
- `language-and-models` is about 2800 words (50 minutes), above the 45-minute target. Splitting it would move labels cited by other courses (`prop-omega-absolute`, `def-l2`, `def-z2`); not done.
- The claim that RCA₀ is the "first-order part IΣ₁" is stated with a pointer to `induction-conservation/first-order-parts`; that course should keep a label for it.

## 11. History

- **2026-11-12.** Design and pedagogy revision.
  - New lesson `nonstandard-models` (compactness, Dedekind's theorem, overspill, finite versus bounded, role of induction); the former section "The role of induction" of `rca0` is reduced to a pointer.
  - `analysis-in-rca0` split: reals and Specker sequences moved to the new lesson `real-numbers`; `analysis-in-rca0` now treats continuous functions and the IVT, with `real-numbers` as prerequisite. Moved labels: `def-real-rca`, `prop-rca-complete`, `prop-specker`.
  - `def-continuous-code` now has Simpson's index field (resolves the review point of `docs/REVIEW-2026-11.md`); new `lem-value-sigma1`; Exercise 1 rewritten to build a code for f − c.
  - New examples: `ex-formalization`, `ex-rca-range`, `ex-turing-ideals`, `ex-definable-model`, `ex-real-equality`. New quizzes on full structures, overspill and Specker sequences.
  - Three figures (`scripts/figures/second-order-arithmetic.py`): order of a non-standard model, code of a continuous function, bisection.
  - References checked against Simpson, Dzhafarov–Mummert and Hirschfeldt; notes rewritten with theorem numbers.
