# Design log: Compactness avoidance

This file is the memory of the course (see "Designing tracks and courses" in
`AGENTS.md`). It is not rendered.

## 1. Objectives

After the course, a student can:

- define PA avoidance and strong PA avoidance for problems (with the two parameters
  D ≤_T Z), relate them to weakness properties and ω-models, and separate a problem from
  WKL by PA avoidance;
- recognize the property of a forcing question that PA avoidance needs (merging), and
  prove the abstract theorem for questions whose answers are Σ⁰₁ relative to the
  condition;
- state and prove Liu's lemma on finite valuations, and use it with weakly merging
  questions, simple or disjunctive;
- define the Ramsey-type weak König lemma, relate it to WKL and RT²₂, and prove that it
  admits PA avoidance by forcing with partitions that split instead of choosing;
- prove Liu's theorem that RT²₂ admits PA avoidance (RT²₂ does not imply WKL₀);
- prove that WWKL admits strong PA avoidance, define constant-bound trace avoidance,
  relate it to PA avoidance, and prove the abstract theorem for finitely merging questions
  with Liu's lemma for blocks;
- characterize DNC degrees by homogeneous sets for Π⁰₁ classes of positive measure, prove
  DNC avoidance and preservation of immunity from countably merging questions, and
  compare the avoidance notions.

**Role in the track.** Fourth course of the track "Lowness and avoidance"
(`tracks-design.md`), after `effective-forcing`, `avoidance` and `lowness`. It does not
depend on `lowness`, which was written at the same time: it only uses first-jump control
through cone avoidance, and none of the lowness results. It is the place where the use of
compactness by a theorem is detected and avoided. The later courses
`separation-design`, `jump-cone-avoidance` and `jump-compactness-avoidance` reuse its
three-case arguments with valuations and blocks, and the splitting technique.

## 2. Prerequisites assumed

- `effective-forcing`: notions of forcing (`def-forcing-notion`, `lem-generic-set`),
  forcing questions (`def-forcing-question`), merging and PA (`def-question-merging`,
  `thm-question-pa`), ω-merging and Sacks forcing (`exr-sacks-dnc`), computable Mathias
  forcing (`prop-mathias-question`, `thm-mathias-coh-preservation`).
- `avoidance`: cone avoidance for problems (`def-cone-avoidance-problem`,
  `ex-cone-avoidance-problems`, `prop-cone-avoidance-product`), Σ⁰₁(ℳ)-preserving
  questions (`def-question-local`, `thm-local-cone-avoidance`), the forcing that makes a
  set Δ⁰₂ (`thm-delta2-cone-avoidance`), Wang's theorem (`thm-coh-strong-cone`),
  disjunctive questions and Lachlan's disjunction (`def-disjunctive-notion`,
  `lem-disjunctive-construction`).
- `ramsey-theorem`: Mathias conditions, Dzhafarov–Jockusch (`thm-dj-cone-avoidance`),
  Seetapun (`thm-seetapun`), stable colorings (`thm-rt22-decomposition`, `prop-srt-d22`),
  `prop-rt32-jump`, `cor-wkl-not-rt22`.
- `reducibilities`: problems, weakness properties and preservation (`def-problem`,
  `def-weakness`, `lem-preservation-ideal`, `thm-preservation-separation`).
- `pi01-classes`, `big-five`: König's and weak König's lemma, compactness, PA degrees
  (`def-pa-degree`, `ex-pa-relative`, `cor-pa-basis`), isolated members, Scott ideals
  (`prop-wkl-scott`).
- `cohen-genericity`: the Posner–Robinson theorem (`cor-posner-robinson`).
- `immunity-growth`: DNC functions and escaping functions (`def-dnc`,
  `thm-dnc-effectively-immune`), immune sets.
- `martin-lof-randomness`: measure facts (`fact-lebesgue-measure`, `prop-measure-effective`,
  `lem-density`, `thm-sacks`), Levin–Schnorr (`thm-levin-schnorr`), the Π⁰₁ class of
  randoms (`cor-mlr-structure`), random sequences compute DNC functions (`cor-random-dnc`).

## 3. Results, lesson by lesson

1. **PA avoidance** (`pa-avoidance`): notation J^D and the three facts on PA relative to D;
   PA avoidance and strong PA avoidance (`def-pa-avoidance`); equivalence with
   preservation of the weakness properties 𝒲_D, ω-models without PA sets, non-reductions
   (`prop-pa-avoidance-model`); abstract theorem for Σ⁰₁(ℳ)-preserving merging questions
   (`thm-local-pa-avoidance`); table of examples (`ex-pa-avoidance-problems`); COH
   (`thm-coh-pa-avoidance`); every set is Δ⁰₂ relative to a non-PA set
   (`thm-delta2-pa-avoidance`) and reduction of strong PA avoidance to Δ⁰₂ instances
   (`cor-strong-pa-delta2`); PA avoidance implies cone avoidance, also in the strong form
   (`thm-pa-implies-cone`). Exercise: products and ω-reducibility.
2. **Weak merging and Liu's lemma** (`weak-merging`): finite valuations, correctness,
   compatibility (`def-valuation`, `ex-valuations`); Liu's lemma (`lem-liu-valuations`,
   figure `liu-valuations`); weakly merging questions (`def-weakly-merging`) and the
   abstract theorem (`thm-weak-merging-pa`); weakly merging disjunctive questions
   (`def-disjunctive-weakly-merging`, `lem-disjunctive-pa`); the Dzhafarov–Jockusch
   question is weakly merging with k = 3 but its reservoirs are PA
   (`ex-dj-weakly-merging`). Exercises: an explicit U, ℓ colors.
3. **The Ramsey-type weak König lemma** (`ramsey-type-wkl`): homogeneous sets for trees and
   RWKL (`def-homogeneous-tree`); homogeneity through paths (`prop-homogeneous-member`);
   examples: singleton classes (RT¹₂), DNC₂ has a computable homogeneous set (`ex-rwkl`);
   RWKL ≤_c WKL and Flood's RWKL ≤_c RT²₂ (`prop-rwkl-reductions`). Exercises: one color
   suffices; Flood's coloring is stable with limit the leftmost path.
4. **Liu's theorem for RWKL** (`partition-forcing`): forcing with partitions
   (`def-partition-forcing`), part and splitting extensions (figure `splitting`); the
   progress lemma (`lem-partition-progress`); Liu's theorem (`thm-rwkl-pa-avoidance`).
   Exercises: homogeneous sets inside a given set (`exr-rwkl-subset`, used in lesson 5);
   cone avoidance for RWKL with the same forcing.
5. **Liu's theorem** (`liu-theorem`): Liu conditions and question (`def-liu-forcing`),
   preservation and weak merging with k = 3 through RWKL (`lem-liu-question`); strong PA
   avoidance of RT¹₂ (`thm-rt12-strong-pa`); RT²₂ admits PA avoidance (`thm-liu-rt22`);
   RT²₂ does not imply WKL₀ (`cor-rt22-not-wkl`); figure `liu-structure`. Exercises: strong
   PA avoidance of COH; RT¹_ℓ and RT²_ℓ.
6. **Randomness and the avoidance of closed classes** (`measure-and-closed-classes`): WWKL
   admits strong PA avoidance (`thm-wwkl-strong-pa`), PA sets are null (`cor-pa-null`,
   Kučera); c.b. traces and c.b. trace avoidance (`def-cb-trace`); k-traces of Π⁰₁(D)
   classes and DNC₂^D (`lem-trace-reduction`); c.b. trace avoidance implies PA avoidance
   (`prop-cb-trace-pa`); disperse sets (`def-disperse`) and Liu's lemma for blocks
   (`lem-liu-blocks`); finitely merging questions (`thm-finitely-merging-trace`); RT²₂
   admits c.b. trace avoidance (`thm-liu-closed-classes`, admitted); the class ℛ_c has no
   computable c.b. trace, so WWKL lacks c.b. trace avoidance (`prop-random-no-trace`);
   RT²₂ does not imply WWKL₀ (`cor-rt22-not-wwkl`). Exercises: singletons and cone
   avoidance; cone avoidance of WWKL from Sacks's theorem.
7. **DNC functions and the comparison of avoidances** (`dnc-avoidance`): RWWKL and DNC
   degrees (`prop-rwwkl-dnc`, Bienvenu–Patey–Shafer); a computable coloring all of whose
   homogeneous sets compute DNC functions (`cor-rt22-dnc`); DNC avoidance
   (`def-dnc-avoidance`), countably merging questions (`def-countably-merging`,
   `thm-countably-merging-dnc`); DNC avoidance implies cone avoidance
   (`prop-dnc-avoidance-cone`); preservation of immunity (`def-preserve-immunity`,
   `thm-countably-merging-immunity`); table and figure `avoidance-comparison`. Exercises:
   ω-models without RWWKL; a Δ⁰₂-inverting non-DNC set preserving an immune set.

## 4. Proof techniques

- **The three-case argument with a non-trivial third case**: the selection argument
  (lessons 1, 6, 7), Liu's lemma on valuations (lessons 2, 4, 5), Liu's lemma on blocks
  (lesson 6). Named "Liu's lemma" and referred to as such.
- **Merging, weak merging, finite and countable merging** of forcing questions: the
  property of the question that matches the avoided class (lessons 1, 2, 6, 7).
- **Splitting instead of choosing**: a notion of forcing that keeps all members of a Π⁰₁
  class and refines the partition, with König's lemma at the end to choose the branch of
  parts (lesson 4). This is the technique that avoids compactness while using it.
- **Compactness in the question** (universal quantifier over a Π⁰₁ class brought down to
  Σ⁰₁): lessons 2, 4, 5.
- **Reservoirs in the class being preserved**: Liu conditions (lesson 5), strong PA
  avoidance of COH (exercise).
- **Density points and measure questions**: forcing with closed classes of positive
  measure (lesson 6).
- **Posner–Robinson** to compare avoidance properties (lessons 1, 7).
- **Escaping c.e. sets of known size** with a DNC function (lesson 7).

## 5. Choices

- **Seven lessons.** The plan had six; the lesson on RWKL exceeded 4600 words and was
  split into the problem (lesson 3, 30 minutes) and Liu's proof (lesson 4). Lessons 1, 4,
  6 and 7 are about 3300–3900 words, a large part of which is mathematics; their
  duration is set to 45 minutes, the convention of `avoidance` and `effective-forcing`.
- **Parameters D ≤_T Z** as in the monograph. The course explains why: D = ∅ builds
  ω-models, D = Z is needed in the comparison with cone avoidance (Posner–Robinson). It
  proves that PA avoidance is equivalent to preserving the weakness properties
  𝒲_D = {Z : Z ⊕ D not PA relative to D}, which makes the definition fit the framework
  of `reducibilities` (this equivalence is not in the monograph).
- **The partial function J^D** with values in {0, 1} replaces Φ_x(x) throughout. With
  Φ_x(x) itself, the monograph's notion of correct valuation does not quite work: if
  Φ_x(x) converges to a value other than 0 and 1, a functional incompatible with a
  correct valuation at x may still be DNC₂. With J^D the case analyses are exact.
- **Selection instead of self-reference** in case 3 of the PA avoidance theorem
  (`thm-question-pa` of `effective-forcing` uses a self-referential index); the selection
  form is what generalizes to Liu's lemma.
- **Liu's lemma** is proved through "safe sets", a reorganization of the monograph's proof
  (two claims merged into one, the case "Φ_n(n) converges" removed from the search).
- **Forcing with partitions**: the extension relation is stated part by part ("for every
  Y and every part μ there is X"), since the monograph's definition with one X for all
  parts fails for splitting extensions (the part μ inherits from X_s with s depending on
  μ); transitivity and inheritance of compatible strings are proved. Settling a part is
  defined by explicit Σ⁰₁ and Π⁰₁ clauses, avoiding a forcing relation for parts; the
  set I of the monograph does not need acceptability; infinity is handled by a separate
  density step, and the final set is shown homogeneous through `prop-homogeneous-member`.
- **The DJ question as a counterexample** (`ex-dj-weakly-merging`): it is weakly merging,
  but its Scott-ideal reservoirs are PA, which motivates RWKL.
- **Measure forcing without the framework of `effective-forcing`**: closed classes of
  positive measure do not satisfy the refinement property of `def-forcing-notion`, so the
  proof of `thm-wwkl-strong-pa` is a decreasing sequence of classes with compactness.
- **c.b. traces**: the two exercises of the monograph (k-traces of Π⁰₁ classes give
  1-traces; 1-traces of homogeneous classes give members) are proved in
  `lem-trace-reduction`, by a non-uniform induction, for DNC₂^D only; this gives
  `prop-cb-trace-pa`. Liu's c.b. trace avoidance of RT²₂ is admitted.
- **Countable merging** is defined with an arbitrary set R of parameters of one formula,
  to avoid syntactic issues with "equivalent" sentences; finite merging likewise.
- **Excluded.**
  - The proof of c.b. trace avoidance for RWKL and RT²₂ (Liu 2015): the proof is the
    one of lessons 4–5 with blocks and kd-disperse sets; admitted with a description.
  - The simpler proof of PA avoidance of RWKL using that DNC₂ is Π⁰₁ (mentioned).
  - ADS (DNC avoidance without preservation of immunity, stated in the monograph without
    reference): ADS is not defined in the platform; mentioned in prose only.
  - Questions of jump PA avoidance: `jump-compactness-avoidance`.
  - The Shoenfield-type exercises on c.b. traces and DNC: included only for DNC
    (exercise of lesson 7).

## 6. Comparison with the literature

- **Patey, *Lowness and avoidance*, chapter *Compactness avoidance*** (main source):
  PA avoidance → lesson 1; Weak merging → lesson 2; Ramsey-type WKL → lessons 3–4; Liu's
  theorem → lesson 5; Randomness and Avoiding closed classes → lesson 6; DNC and
  compactness, DNC avoidance, Comparing avoidances → lessons 1 (PA ⇒ cone) and 7.
  Differences: J^D in place of Φ_x(x) (see Choices); the monograph's proof of
  `prop-rwwkl-dnc` (2 ⇒ 1) uses e + 2 elements while the measure bound needs e + 3
  distinct ones (corrected); in the measure proof, relative measure in [σ] replaces the
  shifted classes; the extension relation of the partition forcing is stated part by
  part; the comment that the PA avoidance proof of Cohen "Case 3: U is a Σ⁰₁ graph of a
  DNC₂ function" is replaced by the selection argument, since U need not be a graph.
- **Dzhafarov–Mummert**, Section 8.6 (Theorem 8.6.1, "RT²₂ admits PA avoidance"),
  Section 4.6 (Corollary 4.6.15, preservation of non-PA degrees).
- **Hirschfeldt, *Slicing the Truth***, Section 6.7: Theorem 6.71 (Liu, with a proof in the
  appendix), Theorem 6.72 (RT²₂ does not imply WWKL₀), Corollary 6.12 (Hirst).
- **Downey–Hirschfeldt**, Section 8.8: Kučera's theorem that the PA sets form a null class
  (stated before Theorem 8.8.4).
- **Liu (2012)**: the original proof combines compactness and disjunction in one forcing;
  the course follows the monograph in separating them through RWKL.

## 7. Pedagogical plan

1. `pa-avoidance`: compactness as what PA avoidance detects; why two negative answers must
   be merged; the table of examples; merging as "the condition itself witnesses the
   negative answer"; quizzes on case 2 and on totality of the selection; the role of D in
   the Posner–Robinson comparison.
2. `weak-merging`: the pigeonhole intuition (three answers, two on the same side); example
   of valuations; figure `liu-valuations`; quizzes on safety; the DJ question as the
   motivating failure.
3. `ramsey-type-wkl`: RWKL as RT¹₂ for an unknown member; examples at the two extremes;
   Flood's coloring; quizzes on compactness and leftmost strings.
4. `partition-forcing`: "split instead of choose"; figure `splitting`; quizzes on the
   number of parts, on the complexity of U, on the branch and the color.
5. `liu-theorem`: figure `liu-structure`; the nested applications of RWKL; quizzes on
   nesting and on the growing oracle; where strong avoidance is needed.
6. `measure-and-closed-classes`: density points; merging by additivity of measure;
   homogeneity of DNC₂; disperse sets; Kolmogorov complexity bound for traces.
7. `dnc-avoidance`: escaping c.e. sets; the counting fact; the chain of four levels of
   compactness; figure `avoidance-comparison` and the table.

Figures are generated by `scripts/figures/compactness-avoidance.py` (deterministic).

## 8. Sources, lesson by lesson (checked 2026-11-12)

1. Monograph §§ PA avoidance, Comparing avoidances; Liu, JSL 77 (2012) 609–620; Posner–
   Robinson, JSL 46 (1981) 714–722; Dzhafarov–Mummert §4.6.
2. Monograph § Weak merging (Liu's lemma attributed to Liu 2012); Liu 2012.
3. Flood, JSL 77 (2012) 1272–1280; Bienvenu–Patey–Shafer, Trans. London Math. Soc. 4 (2017)
   30–71 (arXiv:1411.5874); monograph § Ramsey-type WKL.
4. Liu 2012; Flood 2012; monograph § Ramsey-type WKL; Monin–Patey, Adv. Math. 352 (2019)
   (as cited by the monograph for the simpler proof; not checked).
5. Liu 2012; Hirschfeldt §6.7 (Theorems 6.71, 6.72, Corollary 6.12); Dzhafarov–Mummert
   §8.6 (Theorem 8.6.1); monograph § Liu's theorem.
6. Liu, Trans. AMS 367 (2015) 1609–1630 (arXiv:1602.03777); Kučera 1985; Downey–Hirschfeldt
   §8.8; monograph §§ Randomness, Avoiding closed classes.
7. Bienvenu–Patey–Shafer 2017; Flood 2012; Flood–Towsner, MLQ 62 (2016) 507–529
   (arXiv:1410.4068); monograph §§ DNC and compactness, DNC avoidance, Comparing
   avoidances.

## 9. Recent literature

Checked on 2026-11-12 (web search):

- **Bienvenu, Patey, Shafer (2017)**: RWWKL is equivalent to DNR over RCA₀, and RWKL is
  strictly stronger; used in lesson 7.
- **Flood–Towsner (2016)**: independent separation of RWKL from DNR; cited in lesson 7.
- **Liu (2015)**, *Cone avoiding closed sets*: RT²₂ does not imply WWKL₀ (Hirschfeldt,
  Theorem 6.72); admitted in lesson 6. Liu's term is "constant-bound enumeration".
- **Mimouni–Patey, *Ramsey-like theorems and immunities*** (arXiv:2508.15597, 2025):
  characterizes the Ramsey-like theorems preserving variants of immunity. Not read in
  full; it may bear on the monograph's question whether preservation of immunity implies
  DNC avoidance, which lesson 7 states as unanswered "as far as we know".
- No simpler proof of Liu's theorem than the RWKL decomposition was found.

## 10. Open points

- The monograph's simpler proof of PA avoidance of RWKL (Monin–Patey 2019) was not
  checked in the paper itself.
- Whether DNC avoidance implies PA avoidance is not settled in the course; the question
  of the monograph (immunity versus DNC avoidance) should be checked against
  Mimouni–Patey (2025).
- Lessons 1, 4, 6 and 7 exceed 3000 words (about 3300–3900); a later revision could move
  the Δ⁰₂ section of lesson 1 into exercises.
- Pointers to add in other courses (outside the allowed files): see the report.

## 11. History

- **2026-11-12.** Course created: seven lessons, four figures
  (`scripts/figures/compactness-avoidance.py`), design log.
