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
   PA avoidance and strong PA avoidance (`def-pa-avoidance`), with RT¹₂ and WKL as first
   examples; equivalence with preservation of the weakness properties 𝒲_D, ω-models
   without PA sets, non-reductions (`prop-pa-avoidance-model`); abstract theorem for
   Σ⁰₁(ℳ)-preserving merging questions (`thm-local-pa-avoidance`). Exercise: products and
   ω-reducibility.
2. **First consequences of PA avoidance** (`pa-avoidance-examples`): table of examples
   (`ex-pa-avoidance-problems`); COH (`thm-coh-pa-avoidance`); every set is Δ⁰₂ relative
   to a non-PA set (`thm-delta2-pa-avoidance`) and reduction of strong PA avoidance to Δ⁰₂
   instances (`cor-strong-pa-delta2`); PA avoidance implies cone avoidance, also in the
   strong form (`thm-pa-implies-cone`).
3. **Weak merging and Liu's lemma** (`weak-merging`): finite valuations (`def-valuation`,
   `ex-valuations`); Liu's lemma (`lem-liu-valuations`, figure `liu-valuations`); weakly
   merging questions (`def-weakly-merging`) and the abstract theorem
   (`thm-weak-merging-pa`); weakly merging disjunctive questions
   (`def-disjunctive-weakly-merging`, `lem-disjunctive-pa`). Exercise: an explicit U.
4. **The Ramsey-type weak König lemma** (`ramsey-type-wkl`): the Dzhafarov–Jockusch
   question is weakly merging with k = 3 but its reservoirs are PA (`ex-dj-weakly-merging`);
   homogeneous sets for trees and RWKL (`def-homogeneous-tree`); homogeneity through paths
   (`prop-homogeneous-member`); examples (`ex-rwkl`); RWKL ≤_c WKL and Flood's
   RWKL ≤_c RT²₂ (`prop-rwkl-reductions`). Exercises: ℓ colors for the DJ question; one
   color suffices; Flood's coloring is stable with limit the leftmost path.
5. **Forcing with partitions** (`partition-forcing`): conditions, part and splitting
   extensions (`def-partition-forcing`, figure `splitting`); settling a requirement; the
   progress lemma (`lem-partition-progress`).
6. **Liu's theorem for RWKL** (`rwkl-pa-avoidance`): `thm-rwkl-pa-avoidance`. Exercises:
   homogeneous sets inside a given set (`exr-rwkl-subset`, used in lesson 7); cone
   avoidance for RWKL with the same forcing.
7. **Liu's theorem** (`liu-theorem`): Liu conditions and question (`def-liu-forcing`,
   `lem-liu-question`); strong PA avoidance of RT¹₂ (`thm-rt12-strong-pa`); RT²₂ admits
   PA avoidance (`thm-liu-rt22`, `cor-rt22-not-wkl`); figure `liu-structure`. Exercises:
   strong PA avoidance of COH; RT¹_ℓ and RT²_ℓ.
8. **Weak weak König's lemma** (`measure-and-closed-classes`): WWKL admits strong PA
   avoidance (`thm-wwkl-strong-pa`), PA sets are null (`cor-pa-null`, Kučera). Exercise:
   cone avoidance of WWKL from Sacks's theorem.
9. **Avoiding closed classes** (`closed-classes`): c.b. traces and c.b. trace avoidance
   (`def-cb-trace`); `lem-trace-reduction`, `prop-cb-trace-pa`; disperse sets
   (`def-disperse`) and Liu's lemma for blocks (`lem-liu-blocks`); finitely merging
   questions (`thm-finitely-merging-trace`); RT²₂ admits c.b. trace avoidance
   (`thm-liu-closed-classes`, admitted); `prop-random-no-trace`; `cor-rt22-not-wwkl`.
   Exercise: singletons and cone avoidance.
10. **DNC functions and homogeneous sets** (`rwwkl-dnc`): `prop-rwwkl-dnc`
    (Bienvenu–Patey–Shafer), `cor-rt22-dnc`, the chain of four levels of compactness.
    Exercise: admissible lengths of the tuples in (2 ⇒ 1).
11. **DNC avoidance and the comparison of avoidances** (`dnc-avoidance`):
    `def-dnc-avoidance`, `def-countably-merging`, `thm-countably-merging-dnc`,
    `prop-dnc-avoidance-cone`; preservation of immunity (`def-preserve-immunity`,
    `thm-countably-merging-immunity`); table and figure `avoidance-comparison`.
    Exercises: ω-models without RWWKL; a Δ⁰₂-inverting non-DNC set preserving an immune
    set.

## 4. Proof techniques

- **The three-case argument with a non-trivial third case**: the selection argument
  (lessons 1, 8, 11), Liu's lemma on valuations (lessons 3, 5, 7), Liu's lemma on blocks
  (lesson 9). Named "Liu's lemma" and referred to as such.
- **Merging, weak merging, finite and countable merging** of forcing questions: the
  property of the question that matches the avoided class (lessons 1, 2, 6, 7).
- **Splitting instead of choosing**: a notion of forcing that keeps all members of a Π⁰₁
  class and refines the partition, with König's lemma at the end to choose the branch of
  parts (lessons 5–6). This is the technique that avoids compactness while using it.
- **Compactness in the question** (universal quantifier over a Π⁰₁ class brought down to
  Σ⁰₁): lessons 4, 5, 7.
- **Reservoirs in the class being preserved**: Liu conditions (lesson 7), strong PA
  avoidance of COH (exercise).
- **Density points and measure questions**: forcing with closed classes of positive
  measure (lesson 8).
- **Posner–Robinson** to compare avoidance properties (lessons 1, 7).
- **Escaping c.e. sets of known size** with a DNC function (lesson 10).

## 5. Choices

- **Eleven lessons.** The plan had six; the first version had seven, of which six were
  3300–3900 words for a stated 45 minutes. The polishing pass (2026-11-13) measured every
  lesson at 55 words per minute and split them at natural points: PA avoidance (theory /
  consequences), forcing with partitions (forcing and progress lemma / the theorem),
  randomness (WWKL / closed classes), DNC (homogeneous sets / avoidance). Instead of
  splitting `weak-merging` and `liu-theorem` too, the Dzhafarov–Jockusch example moved to
  `ramsey-type-wkl`, which it motivates, and redundant prose was tightened. All lessons are
  now at most 2475 words (45 minutes). Eleven lessons exceed the usual nine; the course
  could be cut in two (PA avoidance and Liu's theorem; randomness and DNC) if needed.
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
    (exercise of lesson 11).

## 6. Comparison with the literature

- **Patey, *Lowness and avoidance*, chapter *Compactness avoidance*** (main source):
  PA avoidance → lessons 1–2; Weak merging → lessons 3–4; Ramsey-type WKL → lessons 4–6;
  Liu's theorem → lesson 7; Randomness → lesson 8; Avoiding closed classes → lesson 9; DNC and
  compactness, DNC avoidance, Comparing avoidances → lessons 2 (PA ⇒ cone), 10 and 11.
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

1. `pa-avoidance`: compactness as what PA avoidance detects; RT¹₂ and WKL right after the
   definition; why two negative answers must be merged; quizzes on case 2 and on the
   totality of the selection.
2. `pa-avoidance-examples`: the table; merging as "the condition itself witnesses the
   negative answer", against Jockusch–Soare forcing; the role of D in the
   Posner–Robinson comparison.
3. `weak-merging`: the pigeonhole intuition; examples of valuations; figure
   `liu-valuations`; quizzes on safety and on incompatibility.
4. `ramsey-type-wkl`: the DJ question as the motivating failure; RWKL as RT¹₂ for an
   unknown member; examples at the two extremes; Flood's coloring.
5. `partition-forcing`: "split instead of choose"; figure `splitting`; quizzes on the
   number of parts and on the complexity of U.
6. `rwkl-pa-avoidance`: the branch of parts chosen at the end; quizzes on the branch and
   the color.
7. `liu-theorem`: figure `liu-structure`; nested applications of RWKL; where strong
   avoidance is needed.
8. `measure-and-closed-classes`: density points; merging by additivity of measure;
   quizzes on the clopen subclass and on the constants.
9. `closed-classes`: homogeneity of DNC₂; disperse sets; Kolmogorov complexity bound for
   traces.
10. `rwwkl-dnc`: escaping c.e. sets; the counting fact; the chain of four levels.
11. `dnc-avoidance`: countable merging; figure `avoidance-comparison` and the table.

Figures are generated by `scripts/figures/compactness-avoidance.py` (deterministic).

## 8. Sources, lesson by lesson (checked 2026-11-12, rechecked 2026-11-13)

1. Monograph § PA avoidance; Liu, JSL 77 (2012) 609–620; Dzhafarov–Mummert §4.6
   (Corollary 4.6.15, checked).
2. Monograph §§ PA avoidance, Comparing avoidances; Posner–Robinson, JSL 46 (1981)
   714–722; Jockusch–Shore, JSL 49 (1984) 1205–1236 (monograph bibliography).
3. Monograph § Weak merging (Liu's lemma attributed to Liu 2012); Liu 2012.
4. Monograph § Weak merging (DJ exercise), § Ramsey-type WKL; Flood, JSL 77 (2012)
   1272–1280; Bienvenu–Patey–Shafer, Trans. London Math. Soc. 4 (2017) 30–71
   (arXiv:1411.5874).
5. Liu 2012; monograph § Ramsey-type WKL.
6. Liu 2012; Flood 2012; monograph § Ramsey-type WKL; Monin–Patey, Adv. Math. 352 (2019)
   1066–1095 (details from the monograph's bibliography; content of the simpler proof not
   checked).
7. Liu 2012; Hirschfeldt §6.7 (Theorems 6.71, 6.72, Corollary 6.12, checked);
   Dzhafarov–Mummert §8.6 (Theorem 8.6.1, checked); monograph § Liu's theorem.
8. Kučera 1985 (Downey–Hirschfeldt §8.8, checked); monograph § Randomness.
9. Liu, Trans. AMS 367 (2015) 1609–1630 (arXiv:1602.03777, checked); monograph § Avoiding
   closed classes; Hirschfeldt Theorem 6.72.
10. Bienvenu–Patey–Shafer 2017; Flood 2012; Flood–Towsner, MLQ 62 (2016) 507–529
    (arXiv:1410.4068); monograph § DNC and compactness.
11. Monograph §§ DNC avoidance, Comparing avoidances; Liu 2015.

## 9. Recent literature

Checked on 2026-11-12 (web search):

- **Bienvenu, Patey, Shafer (2017)**: RWWKL is equivalent to DNR over RCA₀, and RWKL is
  strictly stronger; used in lesson 10.
- **Flood–Towsner (2016)**: independent separation of RWKL from DNR; cited in lesson 10.
- **Liu (2015)**, *Cone avoiding closed sets*: RT²₂ does not imply WWKL₀ (Hirschfeldt,
  Theorem 6.72); admitted in lesson 9. Liu's term is "constant-bound enumeration".
- **Mimouni–Patey, *Ramsey-like theorems and immunities*** (arXiv:2508.15597, 2025):
  characterizes the Ramsey-like theorems preserving variants of immunity. Not read in
  full; it may bear on the monograph's question whether preservation of immunity implies
  DNC avoidance, which lesson 11 states as unanswered "as far as we know".
- No simpler proof of Liu's theorem than the RWKL decomposition was found.

## 10. Open points

- Whether DNC avoidance implies PA avoidance is not settled in the course; the question
  of the monograph (immunity versus DNC avoidance) should be checked against
  Mimouni–Patey (2025), not read.
- Eleven lessons: more than the usual nine (see Choices).
- No figure in lessons 8–10; a figure of the measure argument (density point, removed
  classes) or of disperse blocks could help.
- Forward references (not prerequisites): the table of `pa-avoidance-examples` cites
  `thm-rt12-strong-pa`, `thm-liu-rt22` and `ex-coh-strong-pa`; the prose of `ramsey-type-wkl` cites
  `thm-rwkl-pa-avoidance`.

## 11. Exercises

Each lesson has one or two featured exercises in the text, after the material they
practice, and a block of further exercises after the references (outside the reading
time). 67 exercises in all: 15 existing (all now labeled, with objectives) and 52 new.

**Featured (13).** `ex-pa-avoidance-product` (products and ω-reducibility, used as a
model for later closure arguments); `ex-strong-pa-stable` (new: the remark that Δ⁰₂
instances are the limit sets of stable colorings, proved); `ex-liu-explicit-u` (the two
alternatives of Liu's lemma on an example); `ex-homogeneous-one-color` and
`ex-flood-stable` (the definition of RWKL and Flood's coloring, both used later);
`ex-partition-transitive` (new: transitivity of the extension relation, the point where
the part-by-part definition matters); `exr-rwkl-subset` (used in `liu-theorem`);
`ex-coh-strong-pa` and `ex-rt-ell-pa` (the two extensions of Liu's theorem cited in the
tables); `ex-wwkl-cone-sacks`; `ex-singleton-trace` (c.b. traces and cones);
`ex-tuple-lengths` (why e + 3); `ex-dnc-avoid-rwwkl`. Moved to the further block:
`ex-dj-ell-colors`, `ex-rwkl-cone-direct`, `ex-delta2-immune-dnc`.

**Further, lesson by lesson.**
1. `pa-avoidance`: Cohen forcing relative to Z and the problem "non-computable in the
   instance"; countable products fail; changing the parameter D; why the oracle of the
   question must not be PA.
2. `pa-avoidance-examples`: two non-PA sets with PA join (1-generics, X △ P); the
   identity problem (PA but not strong PA avoidance); avoiding Z′ with D = Z without
   Posner–Robinson; a non-PA set with a jump PA over ∅′.
3. `weak-merging`: correct valuations and DNC₂; Liu's lemma fails for a PA oracle;
   safe sets found with W′; a weakly merging but not merging question (finite sets of
   strings); ℓ sides.
4. `ramsey-type-wkl`: ℓ colors (moved); two DJ answers cannot be merged; basic
   properties of homogeneous sets; homogeneity is Π⁰₁; homogeneous sets of DNC₂; Flood's
   coloring on an explicit tree.
5. `partition-forcing`: one witness for all parts fails (the choice of the log, now an
   exercise); a small splitting extension and why k + 1 partitions; the class of refined
   partitions; a class with one member (merging).
6. `rwkl-pa-avoidance`: cone avoidance (moved); the color cannot be prescribed; strong
   cone avoidance through RT¹₂; ℓ colors; acceptable parts may die.
7. `liu-theorem`: strong PA avoidance of RWKL; a stable coloring whose limit set a
   homogeneous set does not compute (the deduction removed from `ex-flood-stable`, which
   cited Liu's theorem before it is proved); only one side may avoid PA; property 2 of
   the Liu question.
8. `measure-and-closed-classes`: cone avoidance with measure questions (no merging);
   WWKL₀ does not imply WKL₀; countably many parameters D; the density threshold
   δ > 2/3; random sets that are not PA.
9. `closed-classes`: disperse sets and the empty block; k-traces and RT¹_k; a Π⁰₁ class
   with a computable 1-trace and no computable member (homogeneity needed); traces and
   the Δ⁰₂ forcing; c.b. trace avoidance as preservation of weakness properties; 1-traces
   of 𝓡_c compute DNC functions.
10. `rwwkl-dnc`: the other color; the relativized equivalence of RWWKL and DNC; the
    class of (2 ⇒ 1) has no computable member; its homogeneous sets are effectively
    immune (recursion theorem).
11. `dnc-avoidance`: Δ⁰₂ inversion with immunity (moved); preservation of immunity
    implies cone avoidance; countable, finite and binary merging; COH preserves
    immunity; RT¹₂ does not strongly avoid DNC degrees (random sets); strong DNC
    avoidance reduces to Δ⁰₂ instances.

**Sources.** Exercises of the monograph's chapter *Compactness avoidance*: the Δ⁰₂
variants (Shoenfield-type) for PA, traces and DNC; the k-trace/RT¹_k remark after the
c.b. trace section; the measure question for cone avoidance. The others are variants of
the proofs of the lessons. Duplicates avoided: Cohen generics are not PA or DNC
(`effective-forcing`), the codes of prefixes (`ex-coding-reservoir`, reused rather than
repeated), facts on PA relative to a set (`pi01-classes`), the one-sided negation of the
DJ question (`ex-disjunctive-one-negation`, cited).

## 12. History

- **2026-11-12.** Course created: seven lessons, four figures
  (`scripts/figures/compactness-avoidance.py`), design log.
- **2026-11-13: polishing pass.** Lengths measured at 55 words per minute (without SVG
  lines): four lessons split, the DJ example moved to `ramsey-type-wkl`, prose tightened;
  eleven lessons, all at most 45 minutes, labels unchanged. Corrections: the reference
  for the failure of strong PA avoidance of RT²₂ (the coloring of pairs in the proof of
  `prop-rt32-jump`, not the proposition itself, which is about triples); the quiz on the
  constants 9/10 and 1/5 of `thm-wwkl-strong-pa` (the constraint is 1/10 < t < 9/20, not
  t < 1/4); blocks coded with their length (the empty block); the c.b. trace avoidance of
  RWKL derived from that of RT²₂ by Flood's reduction instead of an unchecked claim about
  Liu's proof; an undefined "kd-disperse" explained; "the two cases" of the immunity
  proof; the forward reference "Liu's theorem of the next lesson" in an exercise of
  `ramsey-type-wkl`. Figures rendered and checked; `liu-valuations` (edge labels on the
  edges) and `avoidance-comparison` (overlapping arrows, floating labels, missing
  converse for DNC avoidance) regenerated. References checked against Downey–Hirschfeldt,
  Hirschfeldt, Dzhafarov–Mummert and the monograph's bibliography; an unchecked claim on
  Bienvenu–Patey–Shafer removed.
- **2026-11-13: featured and further exercises.** All exercises labeled, with objectives
  and difficulties; featured exercises placed in the text, the "Exercises" sections
  removed; 52 new further exercises (section 11). Positional references replaced by
  labels (`ex-dj-disjunctive`, `ex-preservation-downward`, `ex-flood-stable`,
  `ex-coh-strong-pa`, `ex-tuple-lengths`). `ex-flood-stable` no longer cites Liu's
  theorem (moved to `ex-limit-not-computable`). Durations recomputed: 35
  (`pa-avoidance-examples`), 40 (`ramsey-type-wkl`), 45 (`partition-forcing`), 25
  (`rwkl-pa-avoidance`).
