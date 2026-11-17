# Design log: Admissible sets and constructibility

This file is the memory of the course (see "Designing tracks and courses" in
`AGENTS.md`). It is not rendered.

## 1. Objectives

After the course, a student can:

- work in Kripke–Platek set theory: Σ-reflection, Σ-collection, Δ-separation, Σ-recursion
  (also along well-founded relations that are elements of an admissible set);
- relate admissible ordinals and the constructible hierarchy, and show that no ordinal
  strictly between ω and ω₁ᶜᵏ is admissible;
- analyze ω-models of KP through their standard parts;
- prove that ω₁ᶜᵏ is the second admissible ordinal, that HYP = P(ℕ) ∩ L_{ω₁ᶜᵏ}, that HYP is
  the set of reals of every ω-model of KP, and the Spector–Gandy theorem;
- state the relativized results (ω₁ˣ admissible) and Sacks's converse.

**Role.** Fifth core course of the higher computability track (written 2026-11-17,
`tracks-design.md`): the set-theoretic side of higher computability, which Sacks (Part C)
and Chong–Yu (Chapter 3) put at the base of α-recursion and of the later chapters. It uses
the Gandy and Kreisel basis theorems of `sigma11-basis`.

## 2. Prerequisites assumed

- `computable-ordinals` (ordinals, computable well-orderings, notations, normal form,
  ranks of trees), `hyperarithmetic` (Kleene's theorem), `descriptive-set-theory`
  (stages of Π¹₁ sets, Kreisel uniformization), `sigma11-basis` (Gandy and Kreisel
  basis theorems, Spector's collapse theorem).
- `models-of-computation` for the c.e. relations.

## 3. Results, lesson by lesson

1. **kripke-platek** — Δ₀ and Σ formulas, KP (`def-kp`), Σ-reflection with proof
   (`thm-sigma-reflection`), Σ-collection and Δ-separation (`cor-sigma-collection`),
   Σ-recursion (`thm-sigma-recursion`), admissible sets, HF, c.e. = Σ₁ over HF
   (`thm-hf-ce`). Featured: images of sets under Σ functions.
2. **constructible-hierarchy** — L_α; the Δ₁ definability of L_β over admissible sets
   (`fact-l-absolute`, admitted); α admissible iff L_α admissible (`thm-l-admissible`);
   admissible α > ω implies α ≥ ω₁ᶜᵏ (`prop-admissible-above-ck`); recursion along
   well-founded relations (`prop-wf-recursion`); standard parts of models of KP
   (`lem-standard-rank`, `lem-standard-kp`, `cor-omega-model-contains-l`).
3. **hyp-in-l** — nice codes of ω-models (`prop-omega-model-codes`), ω₁ᶜᵏ second admissible
   (`thm-ck-second-admissible`), HYP = P(ℕ) ∩ L_{ω₁ᶜᵏ} (`thm-hyp-l`), Kreisel's
   characterization by ω-models (`cor-hyp-omega-models`).
4. **spector-gandy** — the Spector–Gandy theorem (`thm-spector-gandy`), stages of Π¹₁ sets
   (`cor-pi11-stages-l`), relativization (`thm-omega1x-admissible`), Sacks's theorem
   (`thm-sacks-admissible`, admitted).

## 4. Proof techniques

Reflection; Σ-recursion and collection in admissible sets; absoluteness; standard parts and
transitive collapse; basis theorems applied to codes of ω-models.

## 5. Choices

- **Σ-reflection is proved** (Chong–Yu leave it as an exercise); Σ-recursion is proved inside
  KP with foundation, instead of Chong–Yu's model-theoretic argument.
- **The fine structure of L is admitted**: the Δ₁ definability of x = L_β over admissible
  sets (Chong–Yu, Theorem 3.3.2 and Proposition 3.3.3, which refer to Devlin). Projecta,
  master codes, condensation and Skolem functions (Chong–Yu 3.3.2, 3.4) are excluded.
- **L_{ω₁ᶜᵏ} ⊆ every ω-model of KP** is proved with `prop-admissible-above-ck` and the fact
  above, instead of Chong–Yu's induction along the J-hierarchy.
- **HYP ⊆ L_{ω₁ᶜᵏ}** is proved by Δ-separation with rank maps of computable trees, instead
  of Chong–Yu's use of Π⁰₁ singletons (their Proposition 2.1.5 is not in the platform).
- **Recursion along well-founded relations in an admissible set** is stated with a proof
  sketch (minimal elements taken in the universe).
- **The second form of the Spector–Gandy theorem** (∃z ∈ HYP, arithmetic) and Sacks's
  theorem on admissible ordinals are stated, not proved; the forcing proofs are in
  `hyperarithmetic-forcing` for related results and in Sacks and Chong–Yu (Section 5.4)
  for this one.
- **Excluded:** Barwise compactness (Barwise's book; Friedman–Jensen proof of Sacks's
  theorem), α-recursion theory (Sacks, Parts C–D).

## 6. Comparison with the literature

- **Chong–Yu, Chapter 3** (Sections 3.1–3.3, 3.5–3.7), checked in the PDF: the course
  follows its order.
- **Sacks, Chapter VII** (Σ₁ admissibility for ordinals) and **Barwise**, *Admissible Sets
  and Structures*: cited.

## 7. Pedagogical plan

Each lesson starts from the analogy with classical computability (HF and c.e. relations;
Π¹₁ and c.e.; HYP and finite sets). No figure so far; a figure of the standard part of a
non-standard ω-model would help lesson 2 (open point).

## 8. Sources (checked 2026-11-17)

Chong–Yu PDF: Definitions 3.1.1–3.1.4, Theorems 3.1.5–3.1.8, 3.1.12, Proposition 3.1.17,
Theorems 3.2.4–3.2.5, Section 3.3 (Theorems 3.3.2, 3.3.4, 3.3.6, Proposition 3.3.12),
Section 3.5 (Lemmas 3.5.3–3.5.4, Proposition 3.5.5), Section 3.6 (Propositions 3.6.3–3.6.5,
Lemma 3.6.6, Corollary 3.6.7, Theorem 3.6.8, Corollary 3.6.9), Section 3.7 (Theorems 3.7.1
and 3.7.3, Exercise 3.7.1), Section 5.4 (Theorem 5.4.12, Remark 5.4.13). Sacks's
bibliography for Kripke 1964, Platek 1966, Spector 1959, Gandy 1960, Kreisel 1962,
Sacks 1976 (Advances in Mathematics 19). Steel 1978 from Chong–Yu's bibliography.

## 9. Recent literature

The fine structure of L and its recursion-theoretic applications (master codes, Boolos–
Putnam) are developed in Chong–Yu 3.4; not included.

## 10. Open points

- A figure for standard parts of ω-models.
- A lesson proving Sacks's theorem (Steel forcing, Chong–Yu 5.4) could follow
  `hyperarithmetic-forcing`; it needs the generalized ramified hierarchy A(α, x).

## 11. Exercises

Featured: `ex-sigma-image`, `ex-nonstandard-ordinals`, `ex-wf-sigma1`,
`ex-hyp-reducible-l`. Further: HF smallest admissible, Π₁ not upward absolute, computable
sets in L_{ω+1}, HYP as the Δ₁ sets over L_{ω₁ᶜᵏ}, stages of O.

## 12. History

- **2026-11-17: course written** (four lessons) from Chong–Yu Chapter 3, with Sacks for
  checking, when the higher computability track was enlarged.
