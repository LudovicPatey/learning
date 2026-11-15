# Design log: Jump cone avoidance and second-jump control

This file is the memory of the course (see "Designing tracks and courses" in
`AGENTS.md`). It is not rendered.

## 1. Objectives

After the course, a student can:

- define jump cone avoidance and strong jump cone avoidance for problems, relate them to
  non-high solutions, derive them from weakly low bases when possible, and reduce the
  strong version to Δ⁰₃ instances;
- explain why Π⁰₂ sentences are forced by density, lift a forcing question from Σ⁰₁ to
  Σ⁰₂ sentences, and read off its complexity from the complexity of the partial order;
- prove jump cone avoidance with a forcing question for Σ⁰₂ sentences whose answers are
  Σ⁰₁ relative to the condition (three-case argument one level up);
- restrict a notion of forcing to the conditions a construction uses, as for cohesive
  sets along a path of decisions;
- work with partition regular and large classes, the largest partition regular subclass,
  intersections of Σ⁰₁ classes over a coded Scott ideal, cohesive classes and their
  cores;
- follow and reproduce the proof that every set has an infinite subset, of itself or of
  its complement, whose jump avoids a given cone (Monin–Patey), in particular one that is
  not high.

**Role in the track.** Sixth course of the track "Lowness and avoidance"
(`tracks-design.md`), after `effective-forcing`, `avoidance`, `lowness`,
`compactness-avoidance` and `separation-design`; it does not depend on the last two. It is
the first course on second-jump control, and prepares `jump-compactness-avoidance`, which
can cite: `def-jump-cone-avoidance`, `def-lifted-question`, `lem-lifted-question`,
`def-jump-question-local`, `thm-local-jump-cone`, `def-path-forcing`,
`def-partition-regular`, `def-large`, `prop-largest-partition-regular`,
`lem-decreasing-large`, `lem-cover-class`, `prop-largeness-complexity`,
`def-cohesive-class`, `lem-cohesive-compatible`, `def-cohesive-core`,
`prop-cohesive-core`, `thm-cohesive-class`, `lem-pigeon-setting`, `def-pigeon-condition`,
`def-valid-part`, `def-pigeon-sigma1`, `def-pigeon-pi2` (promises),
`def-pigeon-disjunctive`, `def-pigeon-one-side`.

## 2. Prerequisites assumed

- `effective-forcing`: notions of forcing, filters, `lem-dense-below`,
  `lem-rasiowa-sikorski`; the forcing relation (`def-forcing-formula`,
  `def-forcing-relation`, `prop-forcing-basic`, `thm-forcing-truth`,
  `def-n-generic-notion`); forcing questions (`def-forcing-question`,
  `ex-cohen-question`, `thm-tree-question`, `cor-question-jump-cone`); tree forcings
  (`prop-js-complexity`, `prop-tree-sigma2`); computable Mathias forcing
  (`prop-mathias-question`, `thm-mathias-coh-preservation`, `prop-mathias-dominant`,
  `cor-mathias-no-sigma2`).
- `avoidance`: `def-cone-avoidance-problem`, `def-question-local`,
  `thm-local-cone-avoidance`, `thm-delta2-cone-avoidance`, `cor-strong-delta2`;
  disjunctive notions (`def-disjunctive-notion`, `lem-disjunctive-cone`,
  `lem-disjunctive-construction`); the Seetapun forcing (`lem-seetapun-question`,
  `thm-seetapun-direct`) as a model of construction by sequences of conditions.
- `lowness`: `def-weakly-low-basis`, `prop-weakly-low-properties`, `lem-pa-choice`,
  `thm-coh-weakly-low`, `thm-d22-weakly-low`, `thm-rt22-weakly-low`, `thm-dhls`; codes
  of ideals (`def-coded-family`, `cor-scott-codes`).
- `ramsey-theorem`: Mathias conditions, cohesiveness (`def-cohesive`,
  `prop-coh-no-low`), Dzhafarov–Jockusch (`thm-dj-cone-avoidance`, `lem-scott-cone`),
  stable colorings (`thm-rt22-decomposition`, `prop-srt-d22`).
- `big-five`: Scott ideals (`prop-wkl-scott`). `reducibilities`: problems, weakness
  properties (`def-weakness`, `lem-preservation-ideal`).
- `pi01-classes`: cone avoidance basis, computably dominated basis
  (`thm-cone-avoidance-basis`, `thm-dominated-basis`), `prop-pi01-emptiness`.
- `turing-degrees`, `arithmetic-hierarchy`, `immunity-growth`, `cohen-genericity`: high
  sets (`def-high`), the jump theorem (`thm-jump`), Post's theorem (`thm-post`), Martin's
  theorem (`thm-martin-domination`), jump inversion (`cor-jump-inversion`), 1-genericity
  relative to an oracle (`def-relative-genericity`).

## 3. Results, lesson by lesson

(Ten lessons since the polishing pass of 2026-11-13; labels unchanged.)

1. **Jump cone avoidance** (`jump-cones`): `def-jump-cone-avoidance`,
   `prop-jca-not-high`, `ex-jca-problems` (weakly low bases; J; DOM has cone avoidance
   but not jump cone avoidance; Mathias forcing); the limits of first-jump control (short);
   `thm-delta3-jump-cone`, `cor-strong-jca-delta3`; `ex-no-low2-subset`. Exercises:
   products; jump hyperimmunity from weakly low bases.
2. **Forcing questions for Σ⁰₂ sentences** (`sigma2-questions`): density;
   `def-lifted-question`, `lem-lifted-question`; `ex-lifted-questions`; figure
   `lifted-question`; `def-jump-question-local`, `thm-local-jump-cone`. Exercise: jump
   hyperimmunity for Cohen generic sets (compactness of the lifted question).
3. **Weak König's lemma and two cones** (`wkl-two-cones`, new): why the basis theorems of
   level 1 do not combine; `thm-wkl-two-cones` (Wang), Lawton. Exercises: primitive
   recursive trees (second proof); ω-models without high members (moved from lesson 1),
   with a Scott ideal variant.
4. **Cohesiveness and restricted reservoirs** (`cohesiveness-second-jump`): unchanged in
   content (`lem-decision-tree`, `def-path-forcing`, `lem-path-questions`,
   `thm-coh-two-cones`).
5. **Partition regularity and largeness** (`partition-regularity`, new slug): the first
   two sections of the former `largeness` (`def-partition-regular`, `ex-partition-regular`,
   `lem-partition-regular-basic`, `def-large`, `prop-largest-partition-regular`,
   `lem-decreasing-large`), new quiz on item 5 of the examples, the three exercises.
6. **Largeness over a Scott ideal** (`largeness`, retitled): effective classes
   (`lem-cover-class`, `U_S`, `prop-largeness-complexity`), then cohesive classes
   (`def-cohesive-class`, `lem-cohesive-compatible`). The slug `largeness` keeps the
   definition of `U_S`, which `jump-compactness-avoidance` cites by lesson.
7. **The core of a cohesive class** (`cohesive-classes`, retitled): `def-cohesive-core`,
   `prop-cohesive-core`, uniqueness; `lem-large-split`, `thm-cohesive-class`, figure.
   Exercises: ultrafilter; greedy construction.
8. **Forcing with a cohesive class** (`pigeonhole-forcing`): `thm-pigeons-non-high`
   (statement), `lem-pigeon-setting`, conditions, validity, `def-pigeon-sigma1`,
   `lem-pigeon-sigma1`. The slug keeps compatibility and the classes V_{σ,φ}, cited by
   `jump-compactness-avoidance`.
9. **Questions for Σ⁰₂ sentences on two sides** (`pigeon-questions`, new): promises,
   disjunctive question, witnesses of invalidity, question on one side.
10. **Pigeons do not jump high** (`pigeons-non-high`): `lem-pigeon-requirements`, proof
    (cases A and B, general case), figure, `cor-pigeons-non-high`. Exercises: finite A and
    A ∈ ℳ (moved from lesson 8, as examples of case A); RT²₂; jump hyperimmunity.

## 4. Proof techniques

(Lesson numbers of the seven-lesson version of 2026-11-12; section 3 gives the current lessons.)

- **The three-case argument one level up** (Σ⁰₂ questions with answers Σ⁰₁ relative to a
  set avoiding the cone): lessons 2, 3, 7.
- **Lifting a question by quantifying over extensions**; the cost is the complexity of
  the partial order: lesson 2, used in lesson 3.
- **Absorbing the partial order into an oracle** (finite conditions read with a path P):
  lesson 3.
- **Restricting the partial order to the conditions the construction uses**: lesson 3
  (Boolean combinations along a path), lessons 6–7 (reservoirs in a core).
- **Choosing a parameter by a basis theorem one jump up** (path P avoiding the cone
  relative to ∅'; Scott ideal containing ∅' avoiding C): lessons 1, 3, 6.
- **Jump inversion** to move avoidance from a set to a jump: lesson 1.
- **Compactness for covers** (König's lemma on partial partitions; decreasing
  intersections of large classes): lessons 4, 5.
- **Choice of a large side by a PA set** relative to the jump of the code: lesson 5.
- **Scott property to replace a witness of non-largeness by one in the ideal**: lessons
  5, 6, 7.
- **Over-approximation by all partitions of the reservoir** (questions independent of
  the instance A): lesson 7.
- **Promises** (syntactic forcing of Π⁰₂ sentences kept along a sequence with a valid
  side): lesson 7.
- **Case distinction on validity and Lachlan's disjunction**: lesson 7.

## 5. Choices

- **Order and scope as in `tracks-design.md`**: use of first-jump control; WKL, COH and
  partition regularity; the pigeonhole principle. Two adjustments, justified by the
  existing courses:
  - The material of the monograph on Cohen forcing at level 2 (strong forcing, the Σ⁰₂
    question of Cohen forcing, the abstract theorem) is largely in `effective-forcing`
    (`cor-cohen-jump-cone`, `cor-question-jump-cone`, `thm-tree-question`,
    `prop-tree-sigma2`). Lesson 2 does not repeat it: it isolates the lifting of a
    question (`def-lifted-question`), which the monograph uses example by example and
    which `effective-forcing` uses only for k ≥ 2 inside `thm-tree-question`, and the
    local version of the abstract theorem (`thm-local-jump-cone`), needed for COH and
    RT¹₂ and absent elsewhere.
  - "Weakly low basis ⇒ jump cone avoidance" is item 3 of `prop-weakly-low-properties`
    (lowness); lesson 1 cites it and adds what is new: the definitions, non-high
    solutions, the reduction to Δ⁰₃ instances (new on the platform, from
    `thm-delta2-cone-avoidance` and jump inversion), and limits.
- **Wang's theorem as a corollary.** With `thm-tree-question`, the theorem is two
  applications of the abstract theorems to one generic set. The monograph's proof with
  primitive recursive trees is kept as an exercise, as an example of simplifying the
  partial order.
- **COH proof as in the monograph** (path P of decisions chosen by the cone avoidance
  basis theorem relative to ∅'), with the definability argument written out
  (monograph: exercise). The combined forcing of Patey (2017) is mentioned only: a first
  attempt at writing a solution showed that a Σ⁰₂ question needs care with the
  extendibility of nodes (Π⁰₁(∅')); not included rather than included with a doubtful
  solution.
- **Cohesive classes rather than the original construction.** The monograph's route
  (Monin–Patey hyperarithmetic paper; Le Houérou–Levy Patey–Mimouni) is followed: a
  cohesive class fixed in advance, computed by a set PA relative to ∅' and placed in a
  Scott ideal 𝒩 containing ∅' and avoiding C. It separates the combinatorics of
  largeness (lessons 4–5) from the forcing (lessons 6–7).
- **Partition regularity of the core proved directly** (item 4 of
  `prop-cohesive-core`) with the Σ⁰₁ classes L_k(V) of `lem-cover-class`, instead of the
  monograph's lemma that L(U_S) = U_{S'} with S' computable in S; shorter, and
  `lem-cover-class` is used twice (complexity of largeness, core).
- **ℳ-minimal classes not defined separately**: minimality is item 2 of
  `prop-cohesive-core`; the greedy algorithm (LLM, needs (S ⊕ M')') is an exercise, as
  motivation.
- **Construction by sequences of conditions with tasks**, as in
  `avoidance/seetapun-forcing`, rather than sufficiently generic filters: the notion of
  forcing has two sides, validity, and a syntactic relation for Π⁰₂ sentences, and the
  generic-filter framework of `effective-forcing` (one generic set) does not fit without
  extra definitions. The syntactic relation is called a **promise**, to avoid a third
  meaning of "forces".
- **Validity defined with the core** 𝒰 (the monograph's definition writes U_D^ℳ in one
  place and the core elsewhere; the core is what the proofs use).
- **Positive answer of the disjunctive question needs no validity**: in the monograph,
  the lemma is stated for conditions with both sides valid; the course observes that the
  positive case gives an extension whose members of side i satisfy the Σ⁰₂ sentence
  without any validity, and that validity matters only to turn promises into truth. The
  case distinction is made explicit (case A: some condition with an invalid side; case B:
  none).
- **Ten lessons** (since 2026-11-13). The lessons had 2500–3600 words for a stated 45
  minutes; they were split at natural points so that every lesson has at most 2475 words
  (45 minutes at 55 words per minute). The pigeonhole proof now has three lessons: the
  notion of forcing, the questions for Σ⁰₂ sentences, the construction. Slugs cited by
  other courses (`sigma2-questions`, `largeness`, `pigeonhole-forcing`,
  `pigeons-non-high`) keep the material cited from them.
- **Excluded, with reasons.**
  - Low₃ solutions for Δ⁰₃ sets (Monin–Patey 2019): mentioned only; needs effective
    second-jump control, a further layer.
  - The exercises of the monograph on jump DNC avoidance, Flood's packed sets, and the
    Π⁰₂ large classes containing co-hyperimmune sets: secondary.
  - Higher jump cone avoidance (hyperarithmetic reductions): `tracks-design.md` excludes
    it from the track.
  - Jump PA avoidance: belongs to `jump-compactness-avoidance`.
  - Strong jump cone avoidance for COH: not claimed (not checked in the literature).

## 6. Comparison with the literature

- **Patey, *Lowness and avoidance*, chapter *Jump cone avoidance*** (main source):
  *Context and motivation*, *Use first-jump control* (lesson 1); *Forcing and density*,
  *Weak König's lemma* (lesson 2); *Cohesiveness principle* (lesson 3); *Partition
  regularity*: *Largeness*, *Effective classes* (lesson 4), *ℳ-minimal classes*,
  *ℳ-cohesive classes* (lesson 5); *Pigeonhole principle* (lessons 6–7). Differences and
  corrections:
  - Definition of validity: uses U_D^ℳ where the core ⟨U_D^ℳ⟩ is meant (fixed).
  - Lemma `rt12-strong-jump-cone-avoiding-second-spec` is stated for "two Σ⁰₁ formulas"
    where Σ⁰₂ is meant, and with "q ⊩ ¬φ(G_i)" for the syntactic relation; the course
    states it for Σ⁰₂ sentences with promises, and drops the validity hypothesis in the
    positive case.
  - In the first-spec lemma, the cover class 𝒞_k is described with "Z_i ∉ ..." for
    "Z_j ∉ ..."; written correctly.
  - The forcing question for Σ⁰₁ formulas uses "ρ ⊆ Z, φ(σ ∪ ρ)"; the course uses strings
    compatible with (σ, Y), so that the use principle applies to members (a finite set
    ρ does not determine a prefix long enough to contain the use).
  - The construction of 𝒩: "M low so M' ∈ 𝒩" and "D ∈ 𝒩" are justified explicitly
    (`lem-pigeon-setting`): M' ≤_T ∅' ∈ 𝒩, and S is computed by a PA set relative to ∅'
    in 𝒩.
  - Exercise on COH (`coh-jump-cone-avoiding-second-req`) is done in the text
    (`lem-path-questions`).
- **Monin–Patey, *Pigeons do not jump high*** (Adv. Math. 352 (2019) 1066–1095,
  arXiv:1803.09771): the theorem, largeness and partition regularity; the abstract (read
  2026-11-12) lists: non-high subsets for every set, low₃ solutions for Δ⁰₃ sets, a
  simpler proof of Liu's non-PA theorem. The original proof was not followed line by
  line; the course follows the monograph's later presentation.
- **Hirschfeldt, *Slicing the Truth***: §2.1 (definitions, Theorem 2.2 Martin), §6.4
  (discussion before Theorem 6.49: whether some Δ⁰₂ set has only high Δ⁰₂ subsets), §6.5
  (cohesive sets). Used for context only.
- **Dzhafarov–Mummert** do not treat second-jump control of RT¹₂; not used.

## 7. Pedagogical plan

(Lesson numbers of the seven-lesson version of 2026-11-12; section 3 gives the current lessons.)

1. `jump-cones`: one jump up from cone avoidance; table of examples with DOM as the
   separating example; first-jump control first, and its two limits; the Δ⁰₃ reduction
   locates the difficulty; limits (DHLS, bi-immune relative to ∅''). Quizzes on the
   choice C = Z'' and on PA sets avoiding cones; on jump inversion.
2. `sigma2-questions`: density explained with "G is infinite"; the lifted question and
   figure `lifted-question`; table of three notions with the complexity of the order;
   quizzes on consistency and on why Mathias is Σ⁰₃; abstract theorem, quiz; Wang.
3. `cohesiveness-second-jump`: two diagnoses; tree of decisions with figure; quizzes on
   the oracle P and on sparsity; why P must avoid D (G' ≥ P).
4. `largeness`: positive/negative information; examples including strong cone avoidance
   as partition regularity; figure of a 2-cover; large vs partition regular with a
   counterexample; compactness lemmas; quizzes.
5. `cohesive-classes`: motivation from the failure of intersections and the order of a
   greedy construction; cohesive sets as example; compatibility (quizzes), core
   (quizzes), construction with figure `cohesive-choices`.
6. `pigeonhole-forcing`: roles of the two ideals; validity with figure; asymmetry of the
   Σ⁰₁ question; quizzes on validity and on each item of the lemma.
7. `pigeons-non-high`: promises; disjunctive question and question on one side; the
   requirements lemma as the three-case argument; the case split with figure; quizzes on
   validity, on case B, and on where C ≰ ∅' is used.

Figures are generated by `scripts/figures/jump-cone-avoidance.py` (deterministic).

## 8. Sources, lesson by lesson (checked 2026-11-12)

(Lesson numbers of the seven-lesson version of 2026-11-12; section 3 gives the current lessons.)

1. Monograph, *Context and motivation*, *Use first-jump control*; Hirschfeldt §2.1, §6.4;
   Cholak–Jockusch–Slaman JSL 66 (2001); Downey–Hirschfeldt–Lempp–Solomon JSL 66 (2001)
   1371–1381; Monin–Patey (2019).
2. Monograph, *Forcing and density*, *Weak König's lemma*; Wang JSL 81 (2016)
   1531–1554; Hirschfeldt–Jockusch–Kjos-Hanssen–Lempp–Slaman (2008) for Lawton's theorem
   (as cited by the monograph, not checked); Le Houérou–Levy Patey–Mimouni
   arXiv:2407.01236.
3. Monograph, *Cohesiveness principle*; Jockusch–Stephan MLQ 39 (1993) 515–530; Patey,
   Computability 6 (2017) 47–78; Hirschfeldt §6.5.
4. Monograph, *Partition regularity* (*Largeness*, *Effective classes*); Monin–Patey
   (2019, Adv. Math.); Monin–Patey arXiv:1905.08425; Monin–Patey JSL 89 (2024) 829–857.
5. Monograph, *ℳ-minimal classes*, *ℳ-cohesive classes*; Monin–Patey
   arXiv:1905.08425; Le Houérou–Levy Patey–Mimouni arXiv:2407.01236.
6. Monograph, *Pigeonhole principle*; Monin–Patey (2019); Dzhafarov–Jockusch JSL 74
   (2009) 557–578; Le Houérou–Levy Patey–Mimouni (2024).
7. Same; Liu JSL 77 (2012) 609–620 for the non-PA theorem mentioned.

## 9. Recent literature

Checked on 2026-11-12: the arXiv abstract of *Pigeons do not jump high* (web), to confirm
the three main results quoted; the bibliography of the monograph for Le Houérou, Levy
Patey and Mimouni (2024), whose cohesive classes are used. No simpler proof of the
Monin–Patey theorem was found. The 2024 paper of Monin and Patey (*Partition genericity
and pigeonhole basis theorems*) gives the structural facts on partition regular classes
quoted in lesson 4 (no non-trivial Σ⁰₂ partition regular class; measure and category).

## 10. Open points

- Lawton's theorem (low and cone-avoiding members of Π⁰₁ classes for Δ⁰₂ cones) is quoted
  from the monograph, which cites Hirschfeldt et al. (2008); not checked in that paper.
- Le Houérou–Levy Patey–Mimouni (arXiv:2407.01236) not read; attributions of
  `thm-cohesive-class` and of the greedy exercise follow the monograph.
- Ten lessons, one more than the guideline of about nine; merging would bring lessons
  above 45 minutes.
- `jump-compactness-avoidance/jump-pa-avoidance` and `product-mathias` list
  `sigma2-questions`, `pigeonhole-forcing` and `pigeons-non-high` as prerequisites; the
  promise (`def-pigeon-pi2`) is now in `pigeon-questions`, reached through
  `pigeons-non-high`.
- "The weakness of the pigeonhole principle under hyperarithmetical reductions" is cited
  as arXiv:1905.08425; a journal version was not confirmed.
- Strong jump cone avoidance of COH, and whether jump cone avoidance implies cone
  avoidance for natural problems, are not discussed.
- The combined notion of forcing of Patey (2017) for COH (choice of the path during the
  construction) could be added as an exercise with a checked solution.

## 11. Exercises

Every exercise has a label, an objective, a difficulty and a solution. Featured exercises
(in the text, section "Exercises" before the notes) are the ones every reader should do;
further exercises are in the collapsed block at the end of each lesson. Cross-lesson
associations (`lessons=`) are used only where every label cited is in the prerequisites of
the associated lesson; this left only `ex-pigeon-finite-instance` (also shown in
`pigeonhole-forcing`).

**Featured, and why.**
1. `jump-cones`: `ex-jca-products` (the reason for relativizing the definition, cited in
   the text), `ex-jca-jump-hyperimmunity` (first-jump control transfers domination).
2. `sigma2-questions`: `ex-cohen-jump-hyperimmunity` (compactness of the lifted question;
   template of three later exercises).
3. `wkl-two-cones`: `ex-wkl-primitive-trees` (restricting the order, the monograph's
   proof), `ex-wkl-no-high-ideal` (ω-models without high members).
4. `cohesiveness-second-jump`: `ex-path-jockusch-stephan` (cited in the text: paths are PA
   relative to ∅'). The hyperimmunity exercise moved to the further block.
5. `partition-regularity`: `ex-pr-large-trace`, `ex-pr-largest-subclass` (a pair; the
   second uses the first). The union/intersection exercise moved (its counterexample is
   already in the text).
6. `largeness`: `ex-large-finite-size` (new, short: cover classes computed by hand; the
   lesson is at the 45-minute limit).
7. `cohesive-classes`: `ex-cohesive-ultrafilter`, `ex-minimal-greedy` (cited in notes).
8. `pigeonhole-forcing`: `ex-pigeon-ideal-instance` (new, short: an instance in 𝒩 makes a
   side invalid at once).
9. `pigeon-questions`: `ex-pigeon-promise-infinite` (new: a promise is not truth on
   members, and needs validity).
10. `pigeons-non-high`: `ex-pigeon-instance-in-ideal`, `ex-pigeon-rt22`. The finite
    instance and jump hyperimmunity exercises moved to the further block.

**Further exercises, lesson by lesson.**
1. Single-solution problems fail JCA unless computable (Posner–Robinson); jump DNC
   avoidance separates low from weakly low bases (COH); strong JCA for 1-genericity
   relative to X' by finite extensions; transfer along ≤_c and ≤_sc.
2. Lifted question of Cohen forcing on "G finite" and on gaps [y, 2y); lifted question =
   "some extension forces" (independent of the level-1 question; JS case = the Σ⁰₂
   question of `prop-tree-sigma2`); preservation of non-Σ⁰₂ definitions (two cases);
   Π⁰₂-completeness of Mathias reservoir indices.
3. Two hyperimmunities for Π⁰₁ classes (LLM); PA sets / Scott ideals with no high member
   and no non-computable Δ⁰₂ member; two cones for Cohen generics and why 1-generics
   avoid Π⁰₁ classes without computable members; all cones at once at level 2 = lowness.
4. Hyperimmunity along a path (moved); binary-digit sequence (every set ≡_T a cohesive
   set); paths computable in ∅'; lifted question on "G ⊆* R_k" computes P; ω-model of
   WKL + COH without high members avoiding a cone.
5. Union/intersection (moved); L_Z ∩ L_X not partition regular; minimal partition
   regular classes = ultrafilters (motivates 𝓜-minimality); the Π⁰₂ class
   "many elements in [x, 2^x)"; density classes in detail; L(𝒜) for the lesson's
   counterexample.
6. Non-trivial large Π⁰₂ classes contain co-hyperimmune sets; largeness of a Σ⁰₁ class is
   Π⁰₂-complete; L_H cohesive iff H cohesive; S ⊕ M' PA over X' for X ∈ 𝓜 (LLM), so no
   Δ⁰₂ S with M low.
7. Splitting lemma fails with finite members; 𝓜-minimal ⇒ 𝓜-cohesive and equal to its
   core; members of 𝓜 in the core; a cohesive class inside the class of exercise 5.
8. Extension is a preorder; computing V_{σ,φ} and the role of validity; why U_S ∩ V and
   why cohesiveness (two counterexamples); why two ideals (S ∉ 𝓜, no Scott ideal contains
   the jump of its code).
9. Promises exclude counterexamples on valid extensions; the witness of invalidity
   (example where the question without witness fails); partitions may range over 𝒩;
   both questions on "G finite".
10. Finite instances and jump hyperimmunity (moved); neither high nor low₂; RT¹_k by
    induction; generic instances are in case B (both cases occur); preservation of
    non-Σ⁰₂ definitions for RT¹₂ (second proof of the theorem for Z = ∅).

**Sources.** Patey's monograph, chapter *Jump cone avoidance* (jump DNC avoidance; two
hyperimmunities for WKL, attributed to Le Houérou–Levy Patey–Mimouni; L_Z ∩ L_X, after
Monin–Patey 2024 and Mimouni; co-hyperimmune sets in large Π⁰₂ classes, after Monin–Patey
2024; S ⊕ M' PA, LLM 2024; RT¹₂ jump hyperimmunity, Monin–Patey 2019). The others were
written for the course; the non-Σ⁰₂ exercises follow `avoidance/non-sigma1-definitions`
one level up. The monograph's exercises on Flood's packed sets, on the combined COH
forcing of Patey (2017) and on the Π⁰₂ class whose cohesive subclass is not minimal were
not used (secondary, or no fully checked solution).

**Durations.** The further exercises are outside the reading time. `pigeons-non-high`
went from 45 to 35 minutes (1941 words); the featured exercises added to `largeness`
and `pigeonhole-forcing` keep them at 45 (2575 and 2587 words, below 47.5 minutes).

## 12. History

- **2026-11-12.** Course created: seven lessons, six figures
  (`scripts/figures/jump-cone-avoidance.py`), design log.
- **2026-11-13: polishing pass.** Split into ten lessons (new: `wkl-two-cones`,
  `partition-regularity`, `pigeon-questions`; `largeness` and `cohesive-classes`
  retitled); durations set from word counts. Corrections: primitive recursive tree of the
  WKL exercise (the stage-s test of the node of length s did not give [S] = [T]); the
  argument why first-jump control does not combine with cone avoidance (rewritten); the
  counterexample to compatibility without cohesiveness (L_Z is not Σ⁰₁; replaced by the
  classes "meets Z", "meets Z̄"); compactness of the lifted question in the hyperimmunity
  exercises (bounded sentences written so that a witness serves directly); the
  hyperimmunity exercise of the last lesson (construction of 𝒩 and compactness written
  out); the DNC case analysis of the Jockusch–Stephan exercise (values ≠ 0, 1); the
  uniformity needed in the complexity of the lifted question; a quiz justification
  ("G is far from low"); Hirschfeldt's remark of §6.4 concerns Δ⁰₂ subsets, which the
  theorem does not give; validity in the monograph is written with U_S, not the core.
  Figure `cohesive-choices`: subscripts L_Z instead of L(Z) (which denotes the largest
  partition regular subclass) and width within the view box.
- **2026-11-13: featured and further exercises.** Labels, objectives and difficulties
  for all existing exercises; featured exercises chosen (one or two per lesson, three new
  short ones for the lessons that had none); 41 new further exercises, at least four per
  lesson; positional references to exercises replaced by `:ref`; `pigeons-non-high` set
  to 35 minutes. See section 11.
