# Design log: Definability in the enumeration degrees

This file is the memory of the course (see "Designing tracks and courses" in `AGENTS.md`).
It is not rendered.

## 1. Objectives

Third course of the track "Enumeration degrees". After it, a student knows Kalimullin pairs
and can prove their robustness, knows the definability theorems for the jump, the total
degrees and the continuous degrees and their consequences for automorphisms, and knows the
open questions of the area.

## 2. Prerequisites assumed

`enumeration-jump`; `computable-analysis/computable-metric-spaces` for the last lesson;
Selman's theorem.

## 3. Results, lesson by lesson

1. **kalimullin-pairs** — `def-semi-computable`, `ex-left-cuts`, `def-k-pair`, `ex-k-pairs`,
   `thm-kalimullin-pairs` (the direction from K-pairs to robust minimal pairs proved; the
   converse admitted). Featured: `ex-k-pair-downward`.
2. **definability-and-automorphisms** — the formula RMP, `thm-jump-definable` and
   `thm-jump-definable-gs` (admitted), `thm-totality-definable` (admitted),
   `prop-maximal-pair-total` (proved from the admitted key lemma),
   `prop-automorphisms-restrict` (proved); the theory and open questions. Featured:
   `ex-rmp-formula`.
3. **continuous-degrees** — `def-continuous-reducibility`, `prop-continuous-embedding`
   (proved, with Selman's theorem for one direction), `thm-nontotal-continuous` and
   `thm-almost-total` (admitted), PA above (stated), represented spaces and
   `prop-sierpinski` (proved).

## 4. Proof techniques

Combinatorial characterization of a degree-theoretic property (guessing finite pieces and
excluding double errors); first-order formalization; transfer of automorphisms through a
definable automorphism base; conversion between names and enumerations.

## 5. Choices

- The research theorems (Kalimullin; Ganchev–Soskova; Cai–Ganchev–Lempp–Miller–Soskova;
  Andrews–Igusa–Miller–Soskova; Miller's nontotal continuous degree) are stated with their
  easy halves or consequences proved. Their proofs are research papers; the course aims at
  making the literature readable.
- First drafts of two exercises (on nontotal joins of K-pairs, and a garbled downward closure
  statement) were rewritten or removed on 2026-11-18; the claim that some nontrivial K-pairs
  have a nontotal join was replaced by the statement of Andrews et al. on joins of K-pairs,
  which is what the survey supports.

## 6. Sources

Soskova's survey (Sections 3–4); Jockusch (1968); Arslanov–Cooper–Kalimullin (2003);
Kalimullin (2003); Ganchev–Soskova (2015); Cai–Ganchev–Lempp–Miller–Soskova (2016);
Slaman–Woodin (1997); Slaman–Soskova (2017); Miller (2004); Andrews–Igusa–Miller–Soskova
(2019); Kihara–Ng–Pauly (arXiv:1904.04107).

## 7. History

- 2026-11-18: course written (three lessons).
- **2026-11-18 (polishing pass).** `continuous-degrees` had no featured exercise: `ex-cantor-total` moved into the text. Exercises moved between the text and the further exercises keep their text, hence their hash and endorsements.
- 2026-11-18: section on Martin's conjecture in the enumeration degrees (Nakid Cordero, arXiv 2025) added to `definability-and-automorphisms`.
- 2026-11-18 (polishing): further exercises added where lessons had at most one (checked like proofs); two solutions rewritten for clarity.
