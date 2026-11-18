# Design log: Learning structures in the limit

Not rendered. See "Designing tracks and courses" in `AGENTS.md`.

## 1. Objectives
A specialized, research-level course (no track) on the learnability of isomorphism types,
a direction of computable structure theory active since 2019 (Fokina, San Mauro, Bazhenov,
Rossegger, Soskova, Vatev). Two characterizations, proved in full.

## 2. Results
- `learning-from-informant`: framework; locking sequences (proved); characterization by
  Σ^inf_2 sentences (proved, both directions); computable learners from uniformly
  computable Σ^c_2 sentences; Boolean algebras, linear orders, E_0 (stated).
- `learning-from-text`: positive formulas; characterization by Σ^p_2 sentences (proved);
  separation of text and informant on [ω:1], [ω:2] (proved); complete classes (stated).

## 3. Proof techniques
Locking sequences (Blum–Blum) as forcing conditions; learners that guess witnesses and
abandon refuted ones; monotonicity of positive information.

## 4. Choices
- The direction learnable ⇒ separating sentences is proved directly with locking sequences
  for both informant and text, instead of the published routes (Turing embedding into a
  complete class and the pull-back theorem of Knight–Miller–Vanden Boom for informant;
  Scott-continuous embeddings and a positive pull-back theorem for text). This avoids the
  pull-back theorems and gives the two cases the same proof. Realizations are injective;
  for text, the injectivity is expressed with the symbol ≠ (a disjunct ¬(u ≠ v)), which
  keeps the sentence positive.
- The hypothesis space is the index set of the family, as in the 2024 paper.
- The separation of text and informant is proved by a direct argument on Σ^p_2 sentences
  (a structure with two classes whose positive diagram is contained in that of the
  one-class structure), not by the paper's Scott-continuity argument.
- The first draft of an example (the learner for {ω, ω*}) contained an abandoned attempt;
  rewritten before verification.

## 5. Sources
Bazhenov–Fokina–San Mauro, arXiv:1905.01601 (v2, read in full through a reading agent,
Theorem 3.1, Corollary 4.1, Section 4); Bazhenov–Fokina–Rossegger–Soskova–Vatev,
arXiv:2402.05744 (read in full: Theorem 3, Proposition 3, Lemmas 1–6, Propositions 4–6);
Fokina–Kötzing–San Mauro (ALT 2019), known through the two papers above; Bazhenov–
Cipriani–San Mauro (TCS 951, 2023), known through the statement quoted in the 2024 paper;
Bazhenov–San Mauro (JLC 2021), bibliographic data from the 2024 paper, content not used.

## 6. Possible extensions
Turing complexity of learners (by the abstract of Bazhenov–San Mauro, 0′ suffices for finite learnable families; not checked in the paper);
learning with other criteria (finite learning, behaviourally correct learning); the E_0
characterization with proof.

## 7. History
- 2026-11-18: course written (two lessons) after the exploration of the literature recorded
  in `tracks-design.md`.
