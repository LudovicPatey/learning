# Design log: Fragments of arithmetic

## 1. Objectives

After the course, a student can:
- work in non-standard models of PA⁻ and IΔ₀, using the standard part, end extensions and the absoluteness of bounded formulas;
- use cuts as models (Parikh's theorem) and as failures of induction (definable cuts, overspill);
- prove the implications between induction, least number and collection schemes, checking that auxiliary formulas keep the required complexity;
- code finite sets and sequences in IΔ₀ + exp;
- read IΣₙ and BΣₙ₊₁ as comprehension principles for bounded Σₙ and Δₙ₊₁ sets.

**Role in the track.** First course of the track "Models of arithmetic" (`content/tracks-design.md`). It fixes the base theories, the hierarchy of fragments and the coding apparatus. The second course, `truth-and-provability`, builds the truth definitions and provably total functions on it. The later courses use the cuts, overspill, coded sets and the hierarchy: cuts-and-extensions (coded subsets of cuts, standard systems), end-extensions, recursive-saturation, independence.

## 2. Prerequisites assumed

- First-order logic: completeness, compactness, Löwenheim–Skolem, Gödel's incompleteness theorems (stated in lesson 1 and `_course.yaml`).
- arithmetic-hierarchy/arithmetic-definability: language of arithmetic, bounded and Σ₁ formulas (`def-bounded-formula`, `lem-bounded-computable`), Σₙ-definable = Σ⁰ₙ (`thm-definable-arithmetic`).
- models-of-computation: Cantor pairing (`def-cantor-pairing`), β-function (`def-beta`).
- induction-conservation: optional pointers only (links to lessons, no label citations): the second-order versions of the hierarchy, and the strictness of the hierarchy by models of definable elements (lesson `separations`), used in one remark and one exercise of coded-sets.

## 3. Results, lesson by lesson

1. **pa-minus.** `def-pa-minus`; `lem-pam-basic`; standard part (`prop-standard-part`); formula classes (`def-formula-classes`, `ex-delta0-examples`); end extensions (`def-end-extension`), absoluteness of Δ₀ formulas (`lem-delta0-absolute`), Σ₁ up / Π₁ down (`cor-sigma1-upward`); Σ₁-completeness of PA⁻ (`thm-sigma1-complete`); ℤ[X]⁺ (`ex-zx-plus`); non-standard models by compactness and from ¬Con(PA).
2. **bounded-induction.** `def-induction-scheme`; LΔ₀, division, parity (`prop-idelta0-basic`); pairing (`fact-pairing`, admitted); order type ℕ + ℤ·ℚ (`thm-order-type`); cuts (`def-cut`); Π₁ axiomatization of IΔ₀ (`lem-idelta0-pi1`); cuts closed under +,· are models of IΔ₀ (`lem-cut-model`).
3. **parikh.** Parikh's theorem (`thm-parikh`); bounded graph of exponentiation (`fact-exp`, admitted); `def-exp`; IΔ₀ ⊬ exp (`cor-idelta0-exp`); a model of IΔ₀ + ¬exp (`ex-idelta0-not-exp`); IΣ₁ ⊢ exp (`prop-isigma1-exp`).
4. **induction-collection.** Schemes (`def-fo-schemes`); contraction of quantifiers; IΣₙ ⇔ IΠₙ (`thm-fo-isigma-ipi`); Parsons' closure lemma (`lem-fo-collection-closure`); IΣₙ ⊢ BΣₙ (`thm-fo-parsons`); least number principles (`prop-fo-least-number`); BΣₙ₊₁ ⊢ IΣₙ without exp (`thm-fo-paris-kirby`); BΣₙ₊₁ ⇔ BΠₙ (`ex-fo-bsigma-bpi`); order induction (exercise); strictness stated with a pointer.
5. **definable-cuts.** IΣₙ ⇔ no proper Σₙ- or Πₙ-definable cut (`prop-cuts-induction`); overspill (`cor-overspill`); underspill and overspill for ∀x ≤ c (exercises).
6. **coding.** Ackermann membership (`def-ack-membership`); splitting, insertion and removal, extensionality (`lem-ack-basic`); Δ₀ comprehension (`thm-delta0-comprehension`); coded sequences (`def-coded-sequence`, `prop-seq-basic`); finite pigeonhole principle (exercise).
7. **coded-sets.** Friedman: IΣₙ ⇔ Σₙ sets piecewise coded (`thm-friedman-coded`); BΣₙ₊₁ ⇔ Δₙ₊₁ sets piecewise coded (`thm-collection-coded`); BΣₙ₊₁ + exp ⊢ IΣₙ (`cor-bsigma-exp`); exercise: IΔ₀ + exp ⊬ BΣ₁ (with a pointer to induction-conservation/separations).

## 4. Proof techniques

- **Absoluteness for end extensions** (lesson 1), used for Σ₁-completeness, for cuts as models and in every later cut argument.
- **Cuts as models** (lessons 2–3): a cut closed under the relevant functions satisfies a Π₁-axiomatized theory; compactness to make all term bounds fail at once (Parikh). It prepares the indicator method of the last course of the track.
- **Complexity bookkeeping** (lessons 2, 4, 6): the auxiliary formula of an induction must stay in the class for which induction is available. Two devices keep it there: a large power passed as a parameter that bounds the codes, and collection, which absorbs bounded quantifiers (Parsons).
- **Reversing an induction** (IΣₙ ⇔ IΠₙ); **bounding witnesses by collection** (BΣₙ₊₁ ⇒ IΣₙ).
- **Definable cuts and overspill** (lesson 5), including the cut produced by a failure of collection.
- **Splitting of binary expansions** (lesson 6).
- **Least witness for a Πₙ property** (Friedman) and **records from the right** (collection from coded Δₙ₊₁ sets), lesson 7.

## 5. Choices

- **Base theory PA⁻ (Kaye, Wong) rather than Q (Hájek–Pudlák).** It has an algebraic meaning (non-negative parts of discretely ordered rings), which gives ℤ[X]⁺ at once, and the standard part is an initial segment by an elementary lemma. Language {0, 1, +, ·, <}.
- **Δ₀ with term bounds**, as in the other courses. Bounds by variables appear only in the truth definitions of `truth-and-provability`.
- **Exponentiation through Bennett's Δ₀ formula (admitted)**, which keeps the language L_A and makes Ackermann membership bounded, as in Wong.
- **The hierarchy of induction and collection is proved here in first-order form (coordinator decision, 2026-11-12).** The course thereby no longer depends on the Advanced second-order course induction-conservation; that course is linked only as a pointer. The strictness (models of definable elements) is stated with a pointer to induction-conservation/separations. It is not used in proofs, except in one exercise of coded-sets.
- **Both a direct and a coded-set proof of BΣₙ₊₁ ⇒ IΣₙ.** The direct proof (lesson 4) needs no exp; the proof through coded sets (lesson 7, Wong's Corollary 2.9) explains it.
- **Excluded or moved:** the proof of Bennett's Δ₀ definition of exponentiation (long, HP V.3(c)); IΔ₀ and bounded arithmetic (HP V; a possible specialized course); parameter-free schemes; Slaman's BΣₙ ⇔ IΔₙ (mentioned); the strictness proof (pointer). Provably total functions, truth definitions and finite axiomatizability moved to `truth-and-provability`.

## 6. Comparison with the literature

- **Wong, Lectures 1–3.** Lecture 1: lesson 1 and the closure lemma. Lecture 2: PA⁻, Parsons, Paris–Kirby, Bennett, Ackermann coding and Friedman's theorems as statements; it corresponds to lessons 1–4 and 6. Lecture 3: proofs of Theorems 2.7–2.8, cuts, overspill and Proposition 3.3; it corresponds to lessons 5 and 7. Wong sketches the Σₙ case of Proposition 3.3 without the role of collection; the course gives a complete proof.
- **Hájek–Pudlák.**

  | Hájek–Pudlák | Content | Here |
  | --- | --- | --- |
  | I.1(a) | Q, Σ₁-completeness, IOpen | lessons 1–2 |
  | I.1(b) | IΣ₀(exp), bits, comprehension, sequences | lesson 6, with exp defined instead of a function symbol |
  | I.2(a) | induction and collection | lesson 4 |
  | I.2.7, I.2.13 | piecewise coding | lesson 7 |
  | V.1.4 | Parikh's theorem, same proof by cuts | lesson 3 |
  | V.3(c) | exponentiation relation | lesson 3 |
- **Kaye.** Not available. It is cited only for the PA⁻ axiomatization and Σ₁-completeness (Chapter 2), as reported by Wong.
- **induction-conservation.** It treats the same schemes for second-order formulas.

## 7. Pedagogical plan

1. pa-minus: intuition for the two key facts; ℤ[X]⁺ as the counterexample; figure of an end extension; quiz on the initial-segment hypothesis; exercise on predecessors.
2. bounded-induction: auxiliary bounded formulas; blocks figure and order-type theorem with ℤ[X]⁺ as counterexample (quiz); cuts as models; exercise LΔ₀ ⇒ IΔ₀.
3. parikh: the method stated before the proof; figure of the cut; quiz on closure under multiplication; example of IΔ₀ + ¬exp; exercises on the smallest cut and exponential cuts.
4. induction-collection: the chain of the hierarchy; intuition before each proof; quizzes on BΣₙ₋₁ in Parsons' proof and on the disjunct in Paris–Kirby; exercises: BΣₙ₊₁ ⇔ BΠₙ, order induction.
5. definable-cuts: why collection comes first (quiz); overspill and underspill.
6. coding: binary digits figure; the code is built with 2^a as a parameter (quiz); sequences (quiz); pigeonhole exercise.
7. coded-sets: least-code intuition (quiz); records figure and quiz for collection.

## 8. Sources (checked 2026-11-12 against the text files of the books)

- Lesson 1: Wong Lecture 2 (PA⁻ axioms; Σ₁-completeness with the reference [Kaye, Chapter 2]); HP Theorem I.1.8; HP Preliminaries 0.29.
- Lesson 2: HP Theorems I.1.10, I.1.18, I.1.22; HP Theorem V.1.4 (Π₁ axiomatization).
- Lesson 3: HP Theorem V.1.4; HP V.3(c) and the remarks to Chapter V, item (3) (Bennett 1962; Paris; Dimitracopoulos); Wong Fact 2.4 (Gaifman–Dimitracopoulos 1982); Parikh 1971 (JSL 36, 494–508).
- Lesson 4: Wong Theorems 2.2, 2.3 and Exercise 2.10; HP I.2(a), Theorems I.2.4–I.2.5, Lemmas I.2.8–I.2.15 and the remarks to Chapter I (Paris–Kirby 1978, Parsons 1970).
- Lesson 5: Wong Proposition 3.3, overspill (A. Robinson).
- Lesson 6: HP I.1.31–I.1.43; Wong Lecture 2; Ackermann 1937 (Math. Ann. 114, 305–315); Jeřábek 2012 (MLQ 58, 244–248), from Wong's bibliography.
- Lesson 7: Wong Theorems 2.7 (H. Friedman), 2.8 (folklore), Corollary 2.9; HP Theorem I.2.7, Lemma I.2.13 and the remarks to Chapter I (Kossak, Clote 1985); Slaman 2004 (PAMS 132); Adamowicz–Kołodziejczyk–Paris 2012 (JSL 77, 649–655; checked online).

## 9. Recent literature

Web search, 2026-11-12:
- Adamowicz, Kołodziejczyk and Paris (JSL 77, 2012) relate the open problem "IΔ₀ + ¬exp ⊢ BΣ₁?" to truth definitions. It is mentioned in lesson 7.
- No resolution was found of Paris's question IΔ₁ ⊢ LΔ₁ (equivalently BΣ₁), or of the IΔ₀ + ¬exp question. Both are presented as open, with the dates of the sources.

## 10. Open points

- Durations, by word count at 55 words per minute: pa-minus 50, bounded-induction 40, parikh 30, induction-collection 50, definable-cuts 25, coding 50, coded-sets 40. pa-minus and coding are at the 50-minute limit.
- induction-conservation proves the same hierarchy for second-order formulas. It could now point here for the first-order statements and for partial truth definitions (in `truth-and-provability`).
- Bennett 1962 and Gaifman–Dimitracopoulos 1982 bibliographic details come from Wong's bibliography, not from the original papers.

## 11. History

- **2026-11-12.** Course created (first version: 7 lessons, including provably total functions, truth definitions and finite axiomatizability, citing the hierarchy from induction-conservation).
- **2026-11-12 (later, coordinator decision).** Split into two courses so that each lesson takes at most about 50 minutes.
  - This course keeps pa-minus, bounded-induction (split into `bounded-induction` and the new `parikh`), coding and coded-sets (split into the new `definable-cuts` and `coded-sets`).
  - New lesson `induction-collection` proves the hierarchy in first-order form. Its labels are `thm-fo-isigma-ipi`, `lem-fo-collection-closure`, `thm-fo-parsons`, `prop-fo-least-number`, `thm-fo-paris-kirby` and `ex-fo-bsigma-bpi`, and `def-fo-schemes` moved there from coded-sets.
  - Labels moved to `parikh`: `thm-parikh`, `fact-exp`, `def-exp`, `cor-idelta0-exp`, `ex-idelta0-not-exp`, `prop-isigma1-exp`.
  - Labels moved to `definable-cuts`: `prop-cuts-induction`, `cor-overspill`.
  - The lessons provably-total, truth-definitions and finite-axiomatizability moved to the new course `truth-and-provability`.
  - Citations of induction-conservation labels were replaced by the new first-order labels, or by lesson links.
  - Exercises removed to shorten lessons: Boolean operations on coded sets (coding), the ω-rule (pa-minus), and the third exercise of the former coded-sets.
