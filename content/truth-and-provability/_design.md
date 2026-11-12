# Design log: Truth definitions and provability in fragments

## 1. Objectives

After the course, a student can:
- carry out recursive definitions inside IΣ₁ (provably total functions, course-of-values recursion);
- construct and use the partial truth definitions Sat_Σₙ: universal formulas, finite axiomatizability, diagonalization inside a model.

**Role in the track.** Second course of the track "Models of arithmetic", after `fragments-of-arithmetic`. Its results are used later in the track:
- the arithmetized completeness theorem (course end-extensions) needs Sat and the coding of syntax in IΣ₁;
- satisfaction for non-standard formulas is central in recursive-saturation;
- the provably total functions of IΣ₁ are the starting point of the indicator method in the course independence.

## 2. Prerequisites assumed

- fragments-of-arithmetic: PA⁻, IΔ₀, Parikh's theorem and exp, the hierarchy of induction and collection (`lem-fo-collection-closure`, `thm-fo-parsons`, `thm-fo-isigma-ipi`, `thm-fo-paris-kirby`, `ex-fo-bsigma-bpi`), coded sets and sequences (`def-coded-sequence`, `prop-seq-basic`, `thm-delta0-comprehension`, `thm-friedman-coded`).
- models-of-computation: primitive recursion, course-of-values recursion, Ackermann function.
- arithmetic-hierarchy: Tarski's theorem, Σ₁ = c.e.
- induction-conservation/separations: pointer only, for Rabin's theorem, which uses its models of definable elements.

## 3. Results, lesson by lesson

1. **provably-total.**
   - `def-provably-total`, and the dependence on the defining formula (example via Con(PA));
   - every PR function is provably total in IΣ₁, with its equations (`thm-pr-provably-total`), and the same for course-of-values recursion (`cor-course-of-values-provable`);
   - Parsons–Mints–Takeuti (`thm-pmt`, converse admitted), and IΣ₁ does not prove the Ackermann function total (`cor-ack-isigma1`);
   - exercises: functions with Δ₀ graphs provably total in IΔ₀ are polynomially bounded; cuts closed under PR functions; IΣ₂ proves the Ackermann function total.
2. **bounded-satisfaction.** Codes and assignments; arithmetization of syntax (`fact-syntax`, admitted in its details); Δ*₀ and Σ*ₙ (`def-delta0-star`); satisfaction tables (`def-sat-table`, `lem-sat-tables`); Sat₀, Δ₁ in IΣ₁, with Tarski's conditions (`def-sat0`, `thm-sat0`); exercise: Sat₀ is computable in ℕ.
3. **truth-definitions.** Sat_Σₙ and Sat_Πₙ (`def-sat-n`, `thm-sat-n`); Tarski's scheme for Σ*ₙ formulas from finitely many theorems of IΣ₁ (`cor-snowing`); term bounds reduced to bounds by variables over BΔ*₀ (`lem-variable-bounds`); general scheme and universal Σₙ formulas (`cor-snowing-general`); exercise on true Σ*₁ sentences.
4. **finite-axiomatizability.** IΣ*ₙ ≡ IΣₙ (`lem-isigma-star`); IΣₙ finitely axiomatizable for n ≥ 1 (`thm-isigma-finite`); Rabin: PA not axiomatized by Πₘ sentences (`thm-rabin`, proof with a pointer to induction-conservation/separations); the hierarchy is proper in every model of IΣ₁ (`thm-hierarchy-proper`); exercise: BΣₙ₊₁ finitely axiomatizable.

## 4. Proof techniques

- **Sequences of values and Σ₁ induction** for recursive definitions inside IΣ₁ (lesson 1).
- **Finite tables** for recursions in which the recursive calls change the assignment (lesson 2).
- **Quantification over assignments** for unbounded quantifiers (lesson 3).
- **One instance of a scheme represents all**, through a truth definition (lesson 4).
- **Diagonalization inside a model**, with the parameters folded into the diagonal element (lesson 4).

## 5. Choices

- **Provably total functions before truth definitions.** Course-of-values recursion in IΣ₁ justifies the arithmetization of syntax, so the order avoids a forward dependency.
- **Bounds by variables for the coded formulas** (HP's convention), because evaluating a term bound in a table could leave the bound r. `lem-variable-bounds` and `lem-isigma-star` show that nothing is lost. The finite-axiomatizability proof needs this care, which HP's sketch (Theorem I.2.52) does not discuss, since their Σ₀ formulas have variable bounds from the start.
- **What is proved and what is admitted.** Sat₀ is proved through tables (HP I.1.71–I.1.73). The coding of terms and formulas is admitted (HP I.1.60–I.1.69); its existence follows from `cor-course-of-values-provable`.
- **Parsons–Mints–Takeuti: converse admitted**, with a pointer in prose to the planned course independence (HP IV.3.7).
- **Rabin's theorem** is proved from the models of definable elements of induction-conservation, as a pointer.
- **Excluded:**
  - truth definitions in IΔ₀ + exp, and the finite axiomatizability of IΔ₀ + exp (Gaifman–Dimitracopoulos);
  - IΣₙ₊₁ ⊢ Con(IΣₙ), which is stated (HP I.4.34);
  - the arithmetized completeness theorem and the low basis theorem in IΣ₁ (HP I.3–I.4), which belong to the course end-extensions.

## 6. Comparison with the literature

- **Hájek–Pudlák.**

  | Hájek–Pudlák | Content | Here |
  | --- | --- | --- |
  | I.1(c), I.1.51–I.1.56 | provably recursive functions | lesson 1 |
  | IV.3.7 | Takeuti–Mints | lesson 1 (stated) |
  | I.1(d) | syntax, partial satisfactions, Sat_Σₙ, "it's snowing" | lessons 2–3 |
  | I.2(c), Theorem I.2.52 | finite axiomatizability | lesson 4 |
- **Wong.** His lectures 3–4 and 14 use satisfaction without constructing it in detail.

## 7. Pedagogical plan

1. provably-total:
   - quizzes on where BΣ₁ is used and on why the theorem is stated for derivations;
   - exercises on Parikh for functions, on cuts closed under PR functions, and on the Ackermann function in IΣ₂.
2. bounded-satisfaction:
   - why tables are needed: the assignment changes in the recursion;
   - quizzes on the use of Σ₁ induction and on the bound r.
3. truth-definitions:
   - quiz on maximal blocks;
   - the reduction of term bounds.
4. finite-axiomatizability:
   - the idea that one instance represents all;
   - quizzes on why the variable-bounds lemma is needed, on why n = 0 fails, and on the diagonal argument.

Possible additions: figures of a satisfaction table and of the diagonal set.

## 8. Sources

| Lesson | Checked against the text of Hájek–Pudlák | Not checked |
| --- | --- | --- |
| 1 | I.1.51–I.1.56; Corollary IV.3.7 ("Takeuti–Minc"), with Parsons 1970 | Takeuti, *Proof Theory* (1975), from memory |
| 2 | I.1.60–I.1.73; remarks to Chapter V, item (5) | — |
| 3 | I.1.74–I.1.76; remarks to Chapter I (Montague 59, Kreisel–Lévy 68) | details of Montague 1961 and Kreisel–Lévy 1968, from memory |
| 4 | Theorem I.2.52 and its remark; Introduction (Ryll-Nardzewski 1952, Rabin 1961); Corollary I.4.34; remarks to Chapter V (Gaifman–Dimitracopoulos 1982) | details of Rabin's paper, from memory |

## 9. Recent literature

Checked on 2026-11-12. Adamowicz, Kołodziejczyk and Paris, JSL 77 (2012) 649–655, on truth definitions without exponentiation, is mentioned in lesson 2. No change resulted.

## 10. Open points

- Lesson 1 is at the 50-minute limit.
- There is no figure in this course.
- Rabin's theorem depends on induction-conservation/separations, through a pointer.

## 11. History

- **2026-11-12.** Course created by splitting the first version of `fragments-of-arithmetic`, on the coordinator's decision.
  - Lessons moved here: provably-total, truth-definitions (split into `bounded-satisfaction` and `truth-definitions`) and finite-axiomatizability.
  - Labels moved, unchanged:
    - to provably-total: `def-provably-total`, `thm-pr-provably-total`, `cor-course-of-values-provable`, `thm-pmt`, `cor-ack-isigma1`;
    - to bounded-satisfaction: `fact-syntax`, `def-delta0-star`, `def-sat-table`, `lem-sat-tables`, `def-sat0`, `thm-sat0`;
    - to truth-definitions: `def-sat-n`, `thm-sat-n`, `cor-snowing`, `lem-variable-bounds`, `cor-snowing-general` (the last two from finite-axiomatizability);
    - to finite-axiomatizability: `lem-isigma-star`, `thm-isigma-finite`, `thm-rabin`, `thm-hierarchy-proper`.
  - Citations of induction-conservation labels were replaced by labels of fragments-of-arithmetic, or by lesson links.
