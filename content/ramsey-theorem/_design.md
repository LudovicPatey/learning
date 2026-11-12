# Design log: Ramsey's theorem for pairs

This file is the memory of the course (see "Designing tracks and courses" in
`AGENTS.md`). It is not rendered.

## 1. Objectives

After the course, a student can:

- state Ramsey's theorem for n-tuples and k colors, and explain why the number of
  colors is irrelevant for provability while the exponent is not;
- build pre-homogeneous sets with the Erdős–Radó tree and prove Jockusch's upper bound
  (PA over the (n−1)-st jump) and lower bounds (no Δ⁰₂ solutions for pairs, coding of ∅′
  for triples);
- prove that RTⁿ₂ is equivalent to ACA₀ for n ≥ 3 and that WKL₀ does not prove RT²₂;
- describe the computational content of COH through the Π⁰₁(∅′) class of decisions,
  and prove that cohesive sets can be low₂ but not low;
- prove the Cholak–Jockusch–Slaman decomposition RT²₂ ↔ SRT²₂ + COH in both directions,
  including the counting argument that keeps RT²₂ → COH inside RCA₀;
- use Mathias forcing with restricted reservoirs, and the disjunctive forcing of
  Dzhafarov and Jockusch, to prove cone avoidance and strong cone avoidance;
- prove Seetapun's theorem and build the ω-model separating RT²₂ from ACA₀;
- know the state of the art on RT²₂: Liu's theorem, the SRT²₂ vs COH problem and its
  solution, and where to read further.

**Role in the track.** Third course of the reverse mathematics track
(`tracks-design.md`): the case study of a principle below ACA₀ that escapes the Big Five.
It introduces the techniques used by the last two courses of the track: Mathias
forcing and preservation of weakness properties (`reducibilities`), and first-order
consequences of combinatorial principles (`induction-conservation`, which cites
`prop-rt-basic`).

## 2. Prerequisites assumed

- Turing reducibility, the jump, the limit lemma, relativization; finite extension
  arguments and cone avoidance by finite extensions (`turing-degrees/finite-extensions`,
  `thm-cone-avoidance`); Friedberg's jump inversion (stated in
  `turing-degrees/low-and-high`).
- Π⁰₁ classes, the low basis theorem, the cone avoidance basis theorem, PA degrees and
  their relativization, finitely branching trees and `thm-konig-strength`
  (`pi01-classes`).
- RCA₀, ACA₀, WKL₀, ω-models as Turing ideals, Scott ideals, `thm-low-scott`,
  `thm-aca-equivalents`, `thm-konig-aca` (`second-order-arithmetic`, `big-five`).

## 3. Results, lesson by lesson

1. **jockusch** — Ramsey's theorem and examples (`ex-rt-colorings`), `prop-rt-basic`;
   pre-homogeneous sets; Erdős–Radó tree (`prop-erdos-rado-tree`); Jockusch's upper bound
   (`thm-jockusch-upper`); exercises: H′ ≤ ∅″ for pairs, the classical proof gives ∅″ for
   pairs and no arithmetic bound for triples.
2. **triples** — Jockusch's coloring without Δ⁰₂ solutions (`thm-jockusch-no-delta2`) and
   Specker's theorem; limits of colorings (`lem-limit-coloring`); a computable coloring of
   triples coding ∅′ (`prop-rt32-jump`); RTⁿ₂ ↔ ACA₀ (`thm-rt3-aca`); WKL₀ ⊬ RT²₂
   (`cor-wkl-not-rt22`); exercises: no Σ⁰ₙ solutions, coding ∅⁽ⁿ⁻²⁾ into n-tuples.
3. **cohesiveness** — COH (`def-cohesive`, `ex-cohesive`); cohesive sets below R″
   (`prop-cohesive-exists`); the decision class 𝒞(R) and `prop-coh-decisions`;
   `cor-coh-bounds` (jump PA over ∅′ suffices; low₂ cohesive sets); `prop-coh-no-low`
   (no low cohesive set for some computable sequence; WKL₀ ⊬ COH).
4. **stable-colorings** — stable colorings (`def-stable-coloring`, `ex-stable`), D²₂
   (`def-d22`, `prop-srt-d22`); `thm-rt22-decomposition`; RT²₂ → COH over RCA₀
   (`thm-rt22-coh`); `cor-rt22-equivalence`.
5. **cone-avoidance** — Mathias conditions (`def-mathias-condition`, `ex-mathias-coh`);
   cone avoidance for COH (`thm-coh-cone-avoidance`); Scott ideals avoiding a cone
   (`lem-scott-cone`); strong cone avoidance for RT¹₂ (`thm-dj-cone-avoidance`).
6. **seetapun** — Seetapun's theorem (`thm-seetapun`) and the ω-model (`cor-rt22-not-aca`);
   the place of RT²₂ (Liu, CJS low₂ and coding power, Monin–Patey, thin set theorems);
   COH versus SRT²₂ (table of bounds, separations); exercises: strong cone avoidance
   fails for stable colorings, coding power of RT³₂ is exactly ∅′, ω-model of
   WKL₀ + RT²₂ without ∅′.

## 4. Proof techniques

- **Pre-homogeneity / reducing the exponent** (lesson 1, reused in lessons 2 and 6):
  many applications of the pigeonhole principle organized in a finitely branching tree,
  then one application of the lower exponent.
- **Basis theorems and universality of PA degrees** (lesson 1, `cor-coh-bounds`,
  `lem-scott-cone`, exercise on RT³₂ cone avoidance).
- **Diagonalization against Δ⁰₂ approximations** (`thm-jockusch-no-delta2`).
- **Limits as an extra coordinate** (`lem-limit-coloring`): trading a jump for an
  exponent.
- **Coding by settling times / moduli** (`prop-rt32-jump`, `thm-rt3-aca`).
- **Limit lemma on the solution side** (`prop-coh-decisions`): guessing with the
  approximation evaluated at the element being added.
- **Counting instead of Σ⁰₂ induction** (`thm-rt22-coh`), with the contrast in an
  exercise.
- **Mathias forcing with restricted reservoirs** (lesson 5): Z-computable reservoirs for
  COH, a Scott ideal for RT¹₂; compared explicitly with finite extensions.
- **Lachlan's disjunction and the disjunctive (partition) question** (`thm-dj-cone-avoidance`).
- **ω-models by iterated preservation** (`cor-rt22-not-aca`, exercise WKL₀ + RT²₂).

## 5. Choices

- **Six lessons instead of three** (2026-11-12). The three original lessons were 50–65
  minutes after the pedagogical additions. The lower bound and triples form one lesson
  ("lower bounds"), cohesiveness and stability are separated, and the two forcing
  arguments form their own lesson, so that Seetapun's theorem is assembled in a short
  final lesson with the overview of the field.
- **Dzhafarov–Jockusch proof of Seetapun**, not Seetapun's original k-fold Mathias
  forcing (Dzhafarov–Mummert §8.3): it teaches the decomposition and isolates strong cone
  avoidance, which is the reusable statement (Liu's theorem and Monin–Patey follow the
  same pattern). The Scott ideal version follows Monin–Patey; Hirschfeldt's variant
  with cone-avoiding reservoirs is mentioned.
- **RT²₂ → COH proved** (new). The decomposition is an objective; proving only one
  direction left the equivalence admitted. The proof is short and teaches the
  lexicographic intuition and the counting trick.
- **Decision class 𝒞(R) proved** (new, after Monin–Patey, Brattka–Rakotoniaina, Patey):
  it gives the low₂ bound and the Jockusch–Stephan characterization (one direction) with
  little effort; the converse (every Π⁰₁(∅′) class is a decision class) is admitted.
- **Admitted:** Jockusch's Π⁰ₙ bound; CJS low₂ bounds for SRT²₂ and RT²₂; DHLS; CSY;
  Monin–Patey 2021; Liu; Chong–Lempp–Yang (D²₂ → BΣ⁰₂); McAloon (RT ↔ ACA₀′). Each is
  long or needs non-standard models.
- **Excluded:** first-order strength of RT²₂ (belongs to `induction-conservation`),
  Weihrauch/computable reducibility comparisons (belong to `reducibilities`), the
  Paris–Harrington theorem, other zoo principles (EM, ADS, CAC, thin sets) beyond a
  mention, Liu's proof (long; Hirschfeldt's appendix, DM §8.6).

## 6. Comparison with the literature

- **Hirschfeldt, Slicing the Truth, Chapter 6** (§§6.1–6.7): same sequence of topics
  (three proofs, arithmetic hierarchy, stability and cohesiveness, Mathias forcing,
  Seetapun). Hirschfeldt leaves many proofs as exercises; the course proves them.
  §6.8 (first-order axioms) is left to `induction-conservation`.
- **Dzhafarov–Mummert, Chapter 8**: §§8.1–8.2 bounds, §8.3 Seetapun's original proof,
  §8.4–8.5 stability, cohesiveness and the CJS decomposition with the DJ proof, §8.6 Liu,
  §8.7 first-order part, §8.8 SRT²₂ vs COH. The course follows its order for 8.4–8.5
  but puts the decomposition before Seetapun.
- **Monin–Patey, chapter "Ramsey's theorem"**: sections *Ramsey's theorem in the
  arithmetic hierarchy*, *Infinite pigeonhole principle* (DJ with Scott ideals, Liu),
  *Ramsey's theorem for pairs* (cohesiveness principle with decision classes, Mileti's
  proof of RT²₂ → COH, computational weakness via preservation). The course follows
  their treatment of COH and DJ.
- **Simpson §III.7**: RT(3) ↔ ACA₀ (Lemmas III.7.4–III.7.5, Theorem III.7.6).

## 7. Pedagogical plan

- jockusch: examples of colorings (parity: color not prescribed; min-coloring: infinitely
  many colors fail); comparison of the classical proof with the tree proof; figure of an
  Erdős–Radó tree computed by the generator (`erdos-rado`); an example of a coloring for
  which every set is pre-homogeneous.
- triples: intuition for the Δ⁰₂ diagonalization (one stage = one new element, requirements
  never conflict); complexity versus coding power; settling-time intuition for the
  triple coloring; quiz on each proof.
- cohesiveness: cohesive sets as countably many pigeonhole instances up to finite error;
  binary-digit example; decision strings R^σ and the class 𝒞(R); the "guess at the
  element being added" intuition.
- stable-colorings: figure of a stable coloring as a table (`stable-coloring`); examples
  (parity not stable, h stable, Jockusch's coloring not stable); D²₂ as RT¹₂ for an
  approximated instance; lexicographic intuition and figure (`lex-monotone`) for RT²₂ → COH.
- cone-avoidance: why finite extensions cannot build cohesive sets; figure of a Mathias
  condition (`mathias-condition`); comparison with Cohen cone avoidance; Lachlan's
  disjunction and the partition question.
- seetapun: proof-structure figure (`seetapun-proof`); why the pigeonhole step uses the
  limit set and not the stable coloring (exercise with the coloring h); table comparing
  COH, SRT²₂, RT²₂.

## 8. Sources (checked against the books on 2026-11-12)

- jockusch: Jockusch 1972; Erdős–Radó 1956; Hirschfeldt §6.1 (Exercise 6.4), §6.2
  (Theorems 6.9, 6.20, 6.21); DM §8.1 (Lemma 8.1.2, Theorem 8.1.1); Monin–Patey.
- triples: Specker 1971; Jockusch 1972; Hirschfeldt Theorems 6.11, 6.13, 6.16, 6.17,
  Exercises 6.14, 6.15, Corollary 6.12 (Hirst), §6.3; DM Lemma 8.2.1, Theorems 8.2.2,
  8.2.4, Corollary 8.2.6, Theorem 8.1.6 (McAloon); Simpson III.7.4–III.7.6.
- cohesiveness: Jockusch–Stephan 1993; Hirschfeldt Theorems 6.34, 6.44, 6.45, Exercise
  6.42; DM Theorem 8.4.13; Monin–Patey section *Cohesiveness principle*
  (`prop_coh-sup`, `prop_coh-inf`, `cor-high-cohesif`); Brattka–Rakotoniaina 2017;
  Patey 2016.
- stable-colorings: CJS 2001; Hirschfeldt Definition 6.28, Exercises 6.29, 6.31, Theorem
  6.32 (Mileti; Jockusch–Lempp); DM §8.4.1, Theorem 8.4.9, Corollary 8.4.11, Theorem 8.5.1;
  Chong–Lempp–Yang 2010.
- cone-avoidance: Hirschfeldt Definition 6.40, Proposition 6.41, Exercise 6.62, Lemma
  6.63; DM Examples 7.2.5, 7.2.10, 7.3.9, Lemmas 8.3.7, 8.5.6, 8.5.7; DJ 2009;
  Monin–Patey section *Infinite pigeonhole principle and cone avoidance*.
- seetapun: Seetapun–Slaman 1995; DJ 2009; Hirschfeldt Theorems 6.37, 6.52, 6.53, 6.61,
  6.65, 6.71, Corollary 6.64; DM §§8.3, 8.5.1, 8.6, 8.8 (Theorems 8.8.2, 8.8.5, 8.8.7,
  Question 8.8.13), Proposition 8.5.5; Liu 2012; DHLS 2001; CSY 2014; Monin–Patey 2019,
  2021; Wang 2014; Cholak–Patey 2020 (bibliographic data checked in the bibliographies of
  DM and Monin–Patey).

## 9. Recent literature

Checked (web search and the DM/Monin–Patey books, 2026-11-12):

- **SRT²₂ vs COH**: solved — CSY 2014 (non-standard models), Monin–Patey 2021
  (ω-models). Already in the course; now presented with the table of bounds. Open at
  finer reducibilities: COH ≤_oc D²₂ (DM Question 8.8.13; Dzhafarov–Patey, "COH, SRT²₂,
  and multiple functionals", arXiv 1905.00321). Mentioned in the notes.
- **First-order part of RT²₂**: Patey–Yokoyama 2018 (Π⁰₃ conservation over RCA₀);
  Le Houérou, Levy Patey and Yokoyama, "Π⁰₄ conservation of Ramsey's theorem for pairs"
  (arXiv 2404.18974, v3 May 2026): WKL₀ + RT²₂ is ∀Π⁰₄-conservative over RCA₀ + BΣ⁰₂; and
  "Conservation of Ramsey's theorem for pairs and well-foundedness" (arXiv 2402.11616):
  Π¹₁-conservation over RCA₀ + BΣ⁰₂ + WF(ε₀). Whether RT²₂ is Π¹₁-conservative over
  RCA₀ + BΣ⁰₂ appears to remain open. Not in this course (belongs to
  `induction-conservation`); reported to the coordinator.
- **Ramsey-like theorems**: thin set theorems and Catalan numbers (Wang 2014,
  Cholak–Patey 2020); strong avoidance up the hierarchy (Monin–Patey 2019, "Pigeons do
  not jump high"). Added to the last lesson as an overview.
- **Presentations**: the decision-class characterization of COH (Brattka–Rakotoniaina;
  Patey; Monin–Patey book) gives a simpler route to Jockusch–Stephan's bounds; adopted.
  The Scott-ideal presentation of DJ (Monin–Patey) kept.

## 10. Open points

- Word counts of cone-avoidance and triples are slightly above 2700 (≈ 2800–2860 words
  including formulas); acceptable, could be trimmed.
- The pages and theorem number of Jockusch 1972 for the Π⁰ₙ bound were not checked.
- A figure for the Dzhafarov–Jockusch forcing (two sides and a partition) could help.
- Consider proving SRT²₂ cone avoidance for low₂-ness (CJS) or Liu's theorem in a future
  specialized course.

## 11. History

- **2026-11-12.** Design revision. Split into six lessons: `jockusch` (upper bound),
  `triples` (lower bounds, coding ∅′, RTⁿ₂ ↔ ACA₀; new), `cohesiveness` (COH and its
  bounds), `stable-colorings` (new; stability and the decomposition), `cone-avoidance`
  (new; Mathias forcing, COH cone avoidance, DJ), `seetapun`. Moved labels:
  `thm-jockusch-no-delta2` (jockusch → triples); `lem-limit-coloring`, `prop-rt32-jump`,
  `thm-rt3-aca`, `cor-wkl-not-rt22` (jockusch → triples); `def-stable-coloring`,
  `thm-rt22-decomposition`, `def-d22`, `prop-srt-d22` (cohesiveness → stable-colorings);
  `def-mathias-condition`, `thm-coh-cone-avoidance`, `lem-scott-cone`,
  `thm-dj-cone-avoidance` (seetapun → cone-avoidance). New labels: `ex-rt-colorings`,
  `ex-cohesive`, `prop-coh-decisions`, `cor-coh-bounds`, `prop-coh-no-low`, `ex-stable`,
  `thm-rt22-coh`, `cor-rt22-equivalence`, `ex-mathias-coh`. Five figures
  (`scripts/figures/ramsey-theorem.py`). Section numbers in Hirschfeldt restored;
  attributions corrected (see the review report).
