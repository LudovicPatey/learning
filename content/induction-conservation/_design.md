# Design log: Induction and conservation

## 1. Objectives

After the course, a student can:
- manipulate the schemes IΣₙ, BΣₙ, LΣₙ and their Π versions, and prove the implications between them;
- check the complexity of auxiliary formulas, using collection to absorb bounded quantifiers;
- separate fragments of arithmetic with models of definable elements;
- recognize the first-order content of a combinatorial principle (Hirst's theorem);
- prove conservation results by expanding a model of arithmetic with definable sets, and Π¹₁ conservation by adding generic solutions while preserving Σ⁰₁ induction.

**Role in the track.** Since 2026-11-12 the course is a core course of the reverse mathematics track (see `content/tracks-design.md`), after the Ramsey course and before reducibilities. It provides the "first-order strength" half of the track: the non-standard models that ω-models cannot see. Its last two lessons are the template for every Π¹₁-conservation proof in the literature on Ramsey-type principles.

## 2. Prerequisites assumed

- second-order-arithmetic: the language L₂, the basic axioms, RCA₀, Henkin semantics, completeness; non-standard models, overspill for Σ⁰₁ formulas, finite vs bounded sets (lesson `nonstandard-models`, added 2026-11-12).
- big-five: ACA₀, the jump, ARITH as the least ω-model of ACA₀; WKL₀, Scott ideals, the iteration of the low basis theorem (`thm-low-scott`).
- ramsey-theorem: RT^n_k, `prop-rt-basic` (RCA₀ proves RT¹ₖ for standard k).
- computability: the universal Σₙ sets, Post's theorem, the low basis theorem (forcing with Π⁰₁ classes).
- From logic: compactness, countable models, Gödel's first incompleteness theorem (admitted).

## 3. Results, lesson by lesson

1. **induction-collection.** Definitions of the schemes; Parsons' closure lemma (`lem-collection-closure`); IΣₙ ⇔ IΠₙ; IΣₙ ⇒ BΣₙ; IΣₙ ⇔ LΣₙ ⇔ LΠₙ.
2. **collection-induction.** Cuts; overspill for Σ⁰ₙ formulas (`prop-overspill-n`); BΣₙ₊₁ ⇒ IΣₙ; the hierarchy (figure); Slaman's BΣₙ ⇔ IΔₙ (admitted); BΣₙ₊₁ ⇔ BΠₙ (exercise `ex-bsigma-bpi`).
3. **separations.** Σₙ-elementary substructures; K_n(M) ≺_{Σn} M (`lem-kn-elementary`); K_{n+1}(M) ⊨ IΣₙ + ¬BΣₙ₊₁ (`thm-isigma-not-bsigma`, Parsons; Paris–Kirby); BΣₙ ⊬ IΣₙ (admitted, `thm-bsigma-not-isigma`); PA not finitely axiomatizable (Ryll-Nardzewski).
4. **pigeonhole.** Hirst: RT¹_{<∞} ⇔ BΣ⁰₂; RT²₂ ⇒ BΣ⁰₂ (Hirst); survey of the first-order part of RT²₂.
5. **first-order-parts.** Conservation via ω-extensions; ACA₀ conservative over PA, RCA₀ over IΣ₁ (Friedman); Jockusch–Solovay bound; ACA₀ ⊬ ACA₀′.
6. **forcing-subtrees.** Forcing with infinite subtrees; a single condition decides a Σ⁰₁ formula below a non-standard bound (`lem-harrington-decide`); one generic path preserves IΣ⁰₁ (`thm-path-induction`).
7. **harrington.** Π¹₁ conservation method; M[G] ⊨ RCA₀ when M ∪ {G} ⊨ IΣ⁰₁ (`lem-harrington-extension`, generalized); Harrington's theorem; Friedman's PRA conservation and Hilbert's program.

## 4. Proof techniques

- **Complexity bookkeeping for auxiliary inductions** (lessons 1–2): every proof applies induction to a formula built for the purpose, and the work is to show it stays in the class. Collection is the tool that absorbs bounded quantifiers.
- **Reversing an induction** (IΣ ⇔ IΠ), **bounding witnesses by collection** (BΣₙ₊₁ ⇒ IΣₙ).
- **Cuts and overspill** (lesson 2): the model-theoretic reading of induction.
- **Definable elements and the Tarski–Vaught test** (lesson 3): the basic separation technique of models of arithmetic.
- **Definable expansions** (lesson 5): add the definable sets to a model of arithmetic; statements about them translate back.
- **Compactness** (Jockusch–Solovay, lesson 5).
- **Forcing in non-standard models** (lesson 6): forcing with Π⁰₁ classes (low basis theorem) formalized; deciding non-standardly many questions with one condition through a lexicographically least guess, using LΠ⁰₁ in the ground model.
- **Iterated ω-extensions with bookkeeping** (lesson 7), the general Π¹₁-conservation method.

## 5. Choices

- **Split of the first lesson (2026-11-12).** The former lesson of about 3100 words covered all of the hierarchy. It is split: lesson 1 goes up from induction, lesson 2 contains the cut picture, collection ⇒ induction and the summary of the hierarchy. `thm-collection-induction` and `ex-bsigma-bpi` moved to lesson 2 (only cited inside the course).
- **New lesson on separations.** The course used IΣ₁ ⊬ BΣ₂ three times (RCA₀ ⊬ BΣ⁰₂, WKL₀ ⊬ RT¹_{<∞}, Hirst) while admitting it. The proof by definable elements is short, teaches a central technique of models of arithmetic, and needs only the course's own lemmas plus two admitted facts (partial truth definitions, finite pigeonhole principle in PA). The direct proof that K_{n+1}(M) ⊨ IΣₙ (via witnesses in K for the failure point) replaces Dzhafarov–Mummert's argument via least number principles. The other separation (BΣₙ ⊬ IΣₙ) is admitted: its construction is longer and teaches nothing new for the rest of the track.
- **Split of Harrington's lesson.** The former lesson (about 3200 words) is split into the one-step forcing construction (`forcing-subtrees`) and the iteration and consequences (`harrington`, slug kept since big-five/wkl0 links to it). `lem-harrington-extension` moved to `harrington` and was generalized to any G with M ∪ {G} ⊨ IΣ⁰₁, which isolates the general Π¹₁-conservation method.
- **Excluded:** PRA and the proof of Parsons' Π₂-conservation (Simpson IX.3; a course on proof theory would be needed); Π¹₁ conservation of COH (mentioned, Dzhafarov–Mummert 7.7.1; candidate exercise or specialized course); the proofs of the RT²₂ results (research level); Simpson's extension of Harrington's theorem to uncountable models; isomorphism theorems (Fiori-Carones et al.).
- **Order.** Pigeonhole comes after the separations (it uses them) and before first-order parts (it motivates them).

## 6. Comparison with the literature

- **Dzhafarov–Mummert, Chapter 6** (6.1 induction, bounding, least numbers; 6.3 Kirby–Paris hierarchy; 6.5 Hirst's theorem), **Sections 5.9–5.10** (conservation, first-order parts), **5.6** (ACA₀′, Theorem 5.6.7 = Jockusch–Solovay), **7.7** (Harrington). Closest to the course in scope. The course proves the separation with a different argument for IΣₙ in K_{n+1}(M), and uses Monin–Patey's lexicographic least guess for Harrington.
- **Hirschfeldt, *Slicing the Truth*:** 4.6 (first-order axioms), 6.8 (Hirst, Theorem 6.81; CJS Theorem 6.82), 7.1–7.2 (conservativity, Harrington, Theorem 7.8, framework Proposition 7.10). Hirschfeldt's proof of Hirst's theorem is close to ours.
- **Simpson, SOSOA, Chapter IX:** IX.1 first-order parts of RCA₀ and ACA₀ (Corollary IX.1.11), IX.2 Harrington (Theorem IX.2.1, credited to Harrington 1977 via Friedman, proof inspired by Jockusch–Soare), IX.3 PRA and Hilbert's program (Theorem IX.3.16, Remark IX.3.18). Simpson does not treat the hierarchy of collection.
- **Monin–Patey, chapter "Induction and conservation":** the source of the Harrington proof and the lemma ordering; also treats IOpen and bounded comprehension, excluded here.
- **Hájek–Pudlák** (Chapter I.2 induction and collection, Chapter IV models of fragments) and **Kaye** (chapters *Collection*, *Satisfaction*, *Subsystems of PA*): reference monographs for the first three lessons; chapter titles checked against the publisher's table of contents, not against the books.

## 7. Pedagogical plan

1. induction-collection: intuition paragraph (auxiliary formula pattern); example of instances (exponentiation and Parikh; collection with standard bound is trivial); intuition before IΣ ⇔ IΠ and before IΣ ⇒ BΣ; quizzes on the guard and on the use of BΣₙ₋₁.
2. collection-induction: figure of a cut; overspill and why its complexity hypothesis is needed (a model where the standard part is Σₙ-definable); intuition before BΣₙ₊₁ ⇒ IΣₙ; third quiz on the index shift; figure of the hierarchy with the position of RCA₀, WKL₀, RT²₂, ACA₀.
3. separations: intuition (names below b, values unbounded); example: the standard part is Σ₀- but not Σ₁-elementary; figure of codes and values; quiz on the three key steps.
4. pigeonhole: intuition before the proof of Hirst's theorem.
5. first-order-parts: intuition for the conservation method; standard examples (ARITH, REC) after each expansion theorem; intuition for Jockusch–Solovay.
6. forcing-subtrees: counterexample (the standard part as a path destroys induction); comparison with the low basis theorem; figure of the lexicographic choice; exercise on where BΣ⁰₁ is used.
7. harrington: figure of the tower of extensions; general method; consequences.

Possible additions: a figure for `lem-harrington-unique` (subtrees through strings of length n); an exercise on COH conservation.

## 8. Sources (checked 2026-11-12)

- Lessons 1–2: Paris–Kirby 1978 (Logic Colloquium '77, 199–209; checked in the bibliographies of Simpson, Hirschfeldt, D–M); Parsons 1970 (D–M bibliography); D–M Theorems 6.1.2 (Parsons, closure), 6.1.3; Slaman, PAMS 132 (2004) 2449–2456 (D–M, Hirschfeldt bibliographies); Parikh, JSL 36 (1971) 494–508 (checked online).
- Lesson 3: D–M Lemmas 6.3.2–6.3.3, Theorems 6.3.4 (Parsons, proof Paris–Kirby), 6.3.5 (Lessan; Paris–Kirby), Proposition 6.2.7 (finite pigeonhole). Ryll-Nardzewski, Fund. Math. 39 (1952) 239–263 (from memory; not checked against a book — open point).
- Lesson 4: Hirst thesis 1987 (D–M bibliography); Hirschfeldt Theorems 6.81, 6.82; CJS JSL 66 (2001) 1–55; Chong–Slaman–Yang Adv. Math. 308 (2017) 121–141; Patey–Yokoyama Adv. Math. 330 (2018) 1034–1070; arXiv:2404.18974 and 2402.11616 (checked online, v3 2026); Fiori-Carones–Kołodziejczyk–Wong–Yokoyama, JEMS (online 2024), arXiv:2112.10876.
- Lesson 5: Simpson IX.1, Corollary IX.1.11; Friedman JSL 41 (1976) 557–559 (Simpson bibliography [69]); D–M Theorem 5.6.7 and its history (Wang 1981, proofs by Jockusch and Solovay); D–M Definition 5.6.5, Proposition 5.6.6.
- Lessons 6–7: Simpson Theorem IX.2.1 and its notes; Jockusch–Soare TAMS 173 (1972) 33–56; Monin–Patey `maths-a-rebours.tex`, section "Π¹₁ conservation"; Hirschfeldt Theorem 7.8, Proposition 7.10; D–M Corollary 5.9.6, Theorem 7.7.1 (COH, CJS); Simpson Theorem IX.3.16 (Friedman) and Remark IX.3.18; Simpson IV.2, IV.3 (WKL₀ proves boundedness of continuous functions and the completeness theorem).

## 9. Recent literature

Checked (web search, arXiv abstract pages, 2026-11-12):
- Le Houérou, Levy Patey, Yokoyama, *Π⁰₄ conservation of Ramsey's theorem for pairs*, arXiv:2404.18974 (v1 2024, v3 May 2026): WKL₀ + RT²₂ is ∀Π⁰₄-conservative over RCA₀ + BΣ⁰₂. Improves Patey–Yokoyama's ∀Π⁰₃ result. Added to the pigeonhole lesson.
- Same authors, *Conservation of Ramsey's theorem for pairs and well-foundedness*, arXiv:2402.11616 (v3 June 2026): RT²₂ is Π¹₁-conservative over RCA₀ + BΣ⁰₂ + WF(ε₀), and over RCA₀ + BΣ⁰₂ + ⋃ₙ WF(ωₙ^ω); improves Chong–Slaman–Yang and Kołodziejczyk–Yokoyama. Added.
- These papers state (Theorem 1.2 of 2404.18974) that Π¹₁-conservation of RT²₂ over RCA₀ + BΣ⁰₂ is equivalent to ∀Π⁰₅-conservation, attributed to Fiori-Carones, Kołodziejczyk, Wong, Yokoyama (JEMS). Added, with the attribution "as recalled by".
- Le Houérou, Patey, *Largeness notions and polytime translation for ∀Σ⁰₃-consequences of RT²₂*, arXiv:2602.11906 (2026): polynomial proof-size bounds. Not added (proof complexity, beyond the course).
- The question "is RT²₂ Π¹₁-conservative over RCA₀ + BΣ⁰₂?" is still open according to these papers. The previous formulation in the course ("whether RT²₂ proves any arithmetic sentence not provable in RCA₀ + BΣ⁰₂") is replaced by the Π¹₁ formulation used in the literature, with the Π⁰₄ partial answer.

No newer, simpler proof of Hirst's or Harrington's theorems was found; the Monin–Patey presentation of Harrington's forcing (lexicographic least guess) is kept.

## 10. Open points

- Lessons `separations` (60 min), `first-order-parts` (55), `induction-collection` (50) and `forcing-subtrees` (50) exceed 45 minutes by the word-count rule (formulas inflate the count). Further splitting is possible: the Jockusch–Solovay section could become its own lesson with ACA₀′.
- Kaye and Hájek–Pudlák are cited by chapter title or chapter number from tables of contents only; sections not checked.
- Ryll-Nardzewski 1952 reference written from memory.
- The admitted facts (partial truth definitions, finite pigeonhole in PA, Parikh's theorem, BΣₙ ⊬ IΣₙ) could be proved in a specialized course on models of arithmetic.

## 11. History

- **2026-11-12.** Design revision (course moved into the reverse mathematics track).
  - Split of lesson 1 into `induction-collection` and `collection-induction`; new lesson `separations` with the proof of IΣₙ ⊬ BΣₙ₊₁ by definable elements; split of `harrington` into `forcing-subtrees` and `harrington`.
  - New labels: `ex-scheme-instances`, `prop-overspill-n`, `def-sigma-elementary`, `ex-standard-part-elementary`, `def-definable-elements`, `lem-nonstandard-definable`, `lem-kn-elementary`, `thm-isigma-not-bsigma`, `thm-bsigma-not-isigma`, `cor-pa-not-finite`, `thm-path-induction`. Moved: `thm-collection-induction`, `ex-bsigma-bpi` (to `collection-induction`), `lem-harrington-extension` (stays in `harrington`, generalized), the forcing lemmas (to `forcing-subtrees`).
  - Figures (generator `scripts/figures/induction-conservation.py`): cut, hierarchy, codes and values, lexicographic choice, tower of extensions.
  - References corrected: Jockusch–Solovay (Wang 1981, D–M 5.6.7; the "paper of Wang" was wrong); formalized Post theorem no longer cited to Simpson VIII.1; Simpson IX.1/IX.2/IX.3 section and theorem numbers; Kaye chapters; attribution of `prop-rt22-bsigma2` to Hirst.
  - RT²₂ literature updated (Le Houérou, Levy Patey, Yokoyama 2024).
