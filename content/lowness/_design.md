# Design log: Lowness and first-jump control

This file is the memory of the course (see "Designing tracks and courses" in
`AGENTS.md`). It is not rendered.

## 1. Objectives

After the course, a student can:

- define low bases and weakly low bases for problems, explain why they are relativized,
  build ω-models of low or low₂ sets from them, and use them to separate problems;
- distinguish genericity properties (cone avoidance) from effectiveness properties
  (lowness), and say what each gives;
- represent conditions by codes and run a forcing construction with an oracle,
  deciding the jump of the generic set along the way ("forcing the jump");
- use lowness indices, and the uniform low basis theorem;
- build low sets with a forcing question that is decided by ∅′ but not Σ⁰₁
  ("weak preservation"), as for co-hyperimmune Σ⁰₂ sets and stable linear orders;
- use codes of Scott ideals, with computable indices for the closure operations, and
  answer questions about the members of a low code with ∅′;
- use a set PA relative to ∅′ to choose a true statement among two Π⁰₂ statements;
- prove that COH, D²₂ and RT²₂ admit weakly low bases (Jockusch–Stephan,
  Cholak–Jockusch–Slaman), hence low₂ solutions, and explain why no low basis exists.

**Role in the track.** Third course of the track "Lowness and avoidance"
(`tracks-design.md`), after `effective-forcing` and `avoidance`. It is the place where
effective first-jump control is taught as a method. The later courses
(`compactness-avoidance`, `separation-design`, `jump-cone-avoidance`,
`jump-compactness-avoidance`) can cite: `thm-jump-control` (effective generic sequences
deciding the jump), `thm-scott-class`/`cor-scott-codes`/`prop-low-code-questions`
(low codes of Scott ideals), `lem-pa-choice` and `lem-pa-between` (PA relative to ∅′),
`def-weakly-low-basis`, and the weakly low bases of COH, D²₂ and RT²₂.

## 2. Prerequisites assumed

- `effective-forcing`: notions of forcing, filters and `lem-generic-set`, the forcing
  relation at level 1 (`def-forcing-relation`), forcing questions
  (`def-forcing-question`), effective generic sequences (`thm-effective-generic`,
  `ex-low-basis-forcing`), computable Mathias forcing and its question
  (`prop-mathias-question`, `prop-mathias-dominant`).
- `avoidance`: cone avoidance for problems (`def-cone-avoidance-problem`), the local
  forcing question (`thm-local-cone-avoidance`), disjunctive notions
  (`def-disjunctive-notion`, `lem-disjunctive-construction`).
- `ramsey-theorem`: Mathias conditions, COH and its bounds (`prop-coh-no-low`,
  `cor-coh-bounds`), stable colorings and D²₂ (`def-d22`, `prop-srt-d22`), the
  decomposition (`thm-rt22-decomposition`), the Dzhafarov–Jockusch theorem, Jockusch's
  coloring without Δ⁰₂ solutions (`thm-jockusch-no-delta2`), Seetapun
  (`cor-rt22-not-aca`).
- `reducibilities`: problems, weakness properties, preservation, ω-models
  (`def-problem`, `def-weakness`, `lem-preservation-ideal`,
  `thm-preservation-separation`), Scott's theorem (`thm-scott-pa`).
- `big-five`: Scott ideals (`def-scott-ideal`, `prop-wkl-scott`, `thm-low-scott`).
- `pi01-classes`: low basis, cone avoidance basis, PA degrees and their characterization
  (`thm-low-basis`, `thm-cone-avoidance-basis`, `thm-pa-characterization`,
  `ex-pa-relative`, `cor-pa-basis`), emptiness of Π⁰₁ classes.
- `arithmetic-hierarchy`: Post's theorem; indices and lowness indices
  (`def-indices`, `prop-no-lowness-index`).
- `turing-degrees`: low sets (`def-low`, `prop-low-basic`, `thm-generic-low`,
  `cor-low-exists`), the jump theorem (`thm-jump`), the limit lemma.
- `immunity-growth`: immune and hyperimmune sets, disjoint strong arrays.

## 3. Results, lesson by lesson

1. **Low bases for problems** (`low-bases`): `def-low-basis-problem`;
   `ex-low-basis-problems` (WKL, RT¹₂ yes; J, COH, RT²₂, D²₂ no);
   `thm-low-basis-model` (ω-models of low sets); `cor-low-basis-separations`
   (J, COH, RT²₂ not ω-reducible); why lowness and not Δ⁰₂; `prop-low-second-jump`.
   Exercises: unrelativized low solutions without low basis; jump cone avoidance; J and
   Δ⁰₂ solutions.
2. **Forcing the jump effectively** (`forcing-the-jump`): `def-coded-forcing`,
   `def-jump-decision`, `thm-jump-control` (figure `jump-sequence`);
   `prop-jump-decision-examples` (Cohen, Jockusch–Soare, computable Mathias); the
   obstacle for cohesiveness located in the dense sets, not in the jump. Exercises: a
   low set with hyperimmune principal function; computable Sacks forcing.
3. **Weak preservation** (`weak-preservation`): `ex-no-low-subset` (prefix set of ∅′);
   `thm-cohyperimmune-low` (Jockusch) with `lem-cohyperimmune-dichotomy` (figure
   `hyperimmune-blocks`). Exercises: the Σ⁰₂ hypothesis is needed (Cohen generic);
   non-computable low subsets; consequence for the DHLS set.
4. **Stable linear orders** (`stable-linear-orders`, new 2026-11-13):
   `prop-stable-order-parts`, `thm-sads-low` (Hirschfeldt–Shore), sharpness.
   Exercises: solutions of SADS are the infinite subsets of A and A*; ω-model of
   WKL₀ + SADS of low sets.
5. **Coded Scott ideals** (`coded-ideals`): `def-coded-family`, `prop-no-self-code`;
   `thm-scott-class` (explicit Π⁰₁(X) class of codes, index functions join, red, pa;
   figure `scott-code`); `lem-scott-paths`; `cor-scott-codes` (PA sets compute codes; low
   codes). Exercises: cone-avoiding code; codes of jump ideals.
6. **Uniform lowness** (`uniform-lowness`, new 2026-11-13): lowness indices,
   `prop-uniform-low-basis`; `prop-low-code-questions`; comparison of lowness indices
   and low codes (joins). Exercises: `exr-lowness-index-reduction`; ∅′ names paths in a
   low code.
7. **Weakly low bases** (`weakly-low-bases`, new 2026-11-13): `lem-pa-choice`,
   `ex-pa-choice-infinite`, `lem-pa-between` (Simpson's density);
   `def-weakly-low-basis`, `ex-weakly-low-problems`, `prop-weakly-low-properties`
   (invariance, low₂, jump cone avoidance), `thm-weakly-low-model`. Exercises: converse
   of the choice lemma; products.
8. **Weakly low cohesive sets** (`beyond-zero-jump`): `thm-coh-weakly-low`
   (Jockusch–Stephan, forcing proof of CJS), `cor-coh-weakly-not-low`. Exercise:
   r-cohesive sets.
9. **The pigeonhole principle for Δ⁰₂ sets** (`cjs-theorem`): `thm-d22-weakly-low`
   (CJS), `lem-d22-infinity`, `lem-d22-decision`; Lachlan's disjunction (figure
   `side-grid`); relativization. Exercise: Hirschfeldt's low reservoirs.
10. **Low₂ solutions of RT²₂** (`ramsey-pairs-low2`): `thm-rt22-weakly-low`,
   `cor-rt22-low2`; `thm-dhls` (admitted). Exercises: WKL₀ + RT²₂ with low₂ sets;
   RT²_k.

## 4. Proof techniques

- **Codes of conditions** and **effective genericity** (oracle computes each code from
  the previous one): lessons 2–10.
- **Forcing the jump** (decision of Φ^G_e(e) with a recorded bit): lesson 2, used in
  lessons 3, 8, 9.
- **Decision on all members versus search for an extension** (Jockusch–Soare versus
  Cohen/Mathias): lesson 2.
- **Choice between two Σ⁰₂ alternatives, one of which is true** (∅′ searches for a
  witness of either): lesson 3 (hyperimmunity makes the alternatives exhaustive).
- **Disjoint strong arrays from a failed search** (pushing blocks to infinity): lesson 3.
- **Self-reference by diagonal on columns** (no ideal contains its code): lesson 5.
- **Π⁰₁ class of codes with clauses referring to earlier columns** (non-emptiness by
  recursion, membership by universal clauses): lesson 5.
- **Lowness of a code transfers questions about members to ∅′**: lessons 6 and 9.
- **Choice of a true Π⁰₂ statement by a PA set over ∅′** (separating ∅′-c.e. sets):
  lessons 7, 8, 9.
- **Density of PA degrees** to iterate weakly low bases: lessons 7, 10.
- **Disjunctive forcing over a Scott ideal, effectivized**, and **Lachlan's disjunction**
  with a non-uniform final side: lesson 9.
- **Preservation of a weakness property to build ω-models**: lessons 1, 4, 7, 10.

## 5. Choices

- **Overlaps handled by citation.**
  - Indices (canonical, Δ⁰₁, Σ⁰₁, lowness indices) and the non-uniformity results are
    in `arithmetic-hierarchy/codes`: cited, not redone. The monograph's section
    *Indices* is therefore replaced by the codes of conditions (lesson 2).
  - The low basis theorem and its forcing form are in `pi01-classes/basis-theorems` and
    `effective-forcing/generic-sets` (`ex-low-basis-forcing`): lesson 2 revisits it
    only through the uniform version with lowness indices (`prop-uniform-low-basis`, now in lesson 6),
    which is new to the platform.
  - Low and high sets, low generic sets: `turing-degrees/low-and-high`, cited.
  - COH: `ramsey-theorem/cohesiveness` proves the low₂ bound through the decision class
    and Friedberg jump inversion. Lesson 8 gives the direct forcing proof (Cholak,
    Jockusch, Slaman), under a new label (`thm-coh-weakly-low`) since it is stated in
    the relativized weakly low form that the course needs, and since it is the warm-up
    for lesson 9.
  - Spector's exact pairs (monograph, *Coding ideals*) are in `degree-structure`:
    mentioned in the notes of lesson 5 only.
  - Scott's theorem in the non-coded form (`thm-scott-pa`) and the low Scott ideal
    (`thm-low-scott`) are cited; lesson 5 gives the coded form.
- **The Scott class with explicit clauses.** The monograph uses an enumeration of
  primitive recursive tree functionals and the index ⟨a, b, c⟩, which can refer to
  itself (⟨0,0,0⟩ = 0 would require a column to be PA relative to itself). The course
  uses three explicit clauses (join, reduction, PA step), each referring to columns of
  smaller index, so that non-emptiness is a recursion and the index functions are
  explicit. Paths through trees of the ideal are obtained from the PA step through the
  uniformity of the PA characterization (`lem-scott-paths`).
- **The CJS theorem with a low code (monograph) rather than low reservoirs
  (Hirschfeldt, Dzhafarov–Mummert).** The low code fits the track's emphasis on coded
  Turing ideals, and it makes the proof the effective version of the Dzhafarov–Jockusch
  forcing of `avoidance`. The low reservoir version is an exercise of lesson 9.
- **Single-jump control only.** The double-jump control proof of CJS is mentioned, not
  given: the track has later courses on second-jump control, and the single-jump proof
  is the stronger statement.
- **Density of PA degrees proved** (`lem-pa-between`), in three lines, rather than
  admitted, since it is used twice (invariance of weakly low bases, RT²₂).
- **Choice lemma proved from separating sets** (`lem-pa-choice`), with the converse as
  an exercise.
- **Ten lessons.** The original plan had six; the final lesson on CJS exceeded 3700
  words and was split into the D²₂ theorem and its combination with COH and the limits.
  The polishing pass of 2026-11-13 measured the lessons (Markdown body without SVG, 55
  words per minute) and found five lessons above 45 minutes; it split them at natural
  points: SADS out of `weak-preservation`; lowness indices (out of `forcing-the-jump`)
  and questions about low codes (out of `coded-ideals`) into `uniform-lowness`, placed
  after `coded-ideals`, since both are ways of naming many low sets uniformly; the PA
  choice and weakly low bases (out of `beyond-zero-jump`) into `weakly-low-bases`,
  placed before it so that later courses citing `beyond-zero-jump` keep every label in
  their prerequisites. Labels were kept.
- **Admitted.** The theorem of Downey, Hirschfeldt, Lempp and Solomon (`thm-dhls`):
  infinite injury priority construction, outside the scope; it is also mentioned in
  `ramsey-theorem/seetapun`. The results of Chong–Slaman–Yang and Monin–Patey are only
  mentioned.
- **Excluded.**
  - The exercise of the monograph adapting Seetapun's direct forcing to a weakly low
    basis for RT²₂ (it would duplicate lesson 9 with the Seetapun forcing of
    `avoidance/seetapun-forcing`).
  - Superlowness beyond the remark already in `pi01-classes` (`rem-superlow`).
  - Mileti's theorem (no universal instance of RT²₂/SRT²₂) and the jump-universal
    instance: mentioned in Hirschfeldt §6.6, not needed for the track.
  - Effective forcing over models with non-standard first-order part (conservation):
    belongs to `induction-conservation`.

## 6. Comparison with the literature

- **Patey, *Lowness and avoidance*, chapter *Lowness*** (main source): *Motivation*
  (lesson 1); *Indices* (cited from `arithmetic-hierarchy/codes`; replaced by codes of
  conditions); *Coding ideals* (lesson 4, with explicit clauses; exact pairs cited);
  *Basic constructions* (lesson 2); *Weak preservation* (lesson 3); *Beyond ∅′*
  (lesson 5); *Ramsey's theorem for pairs* (lessons 5–7). Differences and corrections:
  - Exercise "low over Y and Y low implies low": the monograph writes
    (X ⊕ Y)′ ≤_T Y instead of Y′; the course states the correct form in prose.
  - Theorem `scott-ideal-pi01`: the indexing ⟨a, b, c⟩ allows self-reference (see
    Choices), and the closure under reductions needs the compatibility clause to be
    restricted to {0,1} values; fixed by the explicit clauses.
  - Proof of `pi01-low`: the claim that the intersection is a singleton uses functionals
    Φ_e with Φ^G_e(e)↓ iff G(n) = 1; the course follows `thm-low-basis`, where every
    member of the intersection has the same jump, so no singleton is needed.
  - Lemma `d22-weakly-low-basis-genericity`, case P ≠ ∅: obtaining an M-code of a member
    of the class needs the uniform path function; made explicit in `lem-scott-paths`.
  - The final step of `d22-weakly-low-basis` (choice of the side by the pigeonhole
    principle) is written as Lachlan's disjunction with a figure.
  - Exercise `pa-degree-separation`: "if A(n) = 1" should read "if f(a, b) = 1"; the
    course proves the statement for Π⁰₂ sentences (`lem-pa-choice`).
- **Hirschfeldt, *Slicing the Truth***: §2.3 (Proposition 2.7, effective genericity);
  §3.1 (Exercises 3.11, 3.12, uniform low basis); §4.5 (Proposition 4.27, Theorem 4.26
  density of PA degrees); §6.4 (Theorem 6.37, DHLS); §6.5 (Theorem 6.44 and the
  discussion before it, Jockusch–Stephan with the CJS forcing proof); §6.6 (Theorems
  6.52, 6.53, 6.57, Corollary 6.58, with low reservoirs); §9.1 (Theorem 9.11
  Tennenbaum–Denisov, Exercise 9.6, Theorem 9.19 and Exercise 9.20 Hirschfeldt–Shore).
- **Dzhafarov–Mummert**: Definition 3.6.2 (admitting low solutions); Theorem 2.8.25 and
  Proposition 2.8.26 (PA choice, density); Theorem 7.5.6, Theorem 7.5.15, Corollary
  7.5.16 (COH); §8.5.2: Theorem 8.5.8, Corollary 8.5.9, Lemmas 8.5.11, 8.5.12 (with low
  reservoirs and induction on colors), Theorem 8.5.10 (Dzhafarov–Jockusch, low₂ with
  cone avoidance).
- **Simpson**: Definition VII.2.1, Lemma VIII.2.9, Theorem VIII.2.17, Corollary
  VIII.2.18 (countable coded ω-models of WKL₀ as paths of one tree).

## 7. Pedagogical plan

1. `low-bases`: genericity versus effectiveness; table of examples with three kinds of
   failure (J, COH, RT²₂/D²₂); quiz on why lowness over Z; why Δ⁰₂ does not iterate;
   second jump for free.
2. `forcing-the-jump`: codes as a choice that determines what an oracle can compute;
   figure `jump-sequence`; quizzes on the recorded bit, on the role of S_n, on where
   ∅′ is needed for Mathias forcing; the obstacle for COH located in the dense sets.
3. `weak-preservation`: counterexample first (prefix set), then the dichotomy with
   figure `hyperimmune-blocks`; quiz on the zeros pushing blocks to infinity; both
   hypotheses needed.
4. `stable-linear-orders`: the case distinction that produces hyperimmunity; sharpness.
5. `coded-ideals`: diagonal argument; the class of codes with figure `scott-code`;
   quizzes on the restricted clause and on the order of columns.
6. `uniform-lowness`: lowness indices and their limits (uniform indices do not make the
   join low); low codes; comparison through joins.
7. `weakly-low-bases`: PA over ∅′ as "barely more than ∅′"; choice lemma with the DNC
   analogy; density; examples; consequences.
8. `beyond-zero-jump`: COH as the model proof, with quizzes on where P is used.
9. `cjs-theorem`: the Dzhafarov–Jockusch question effectivized; quizzes on all
   partitions, on the Scott property and on the role of P; Lachlan's disjunction with
   figure `side-grid`.
10. `ramsey-pairs-low2`: combination through the density of PA degrees; quizzes on Q
   and on relativization; limits.

Figures are generated by `scripts/figures/lowness.py` (deterministic).

## 8. Sources, lesson by lesson (checked 2026-11-12, again 2026-11-13)

1. Monograph, *Motivation*; Dzhafarov–Mummert Definition 3.6.2; Hirschfeldt
   Proposition 4.27, Theorem 6.37; Herrmann JSL 66 (2001) 923–934; Jockusch–Soare TAMS
   173 (1972); Downey–Hirschfeldt–Lempp–Solomon JSL 66 (2001) 1371–1381.
2. Monograph, *Indices*, *Basic constructions*; Hirschfeldt Proposition 2.7, proof of
   Theorem 6.44; Dzhafarov–Mummert Theorem 7.5.6, Lemma 8.5.11 (Claim 1).
3. Monograph, *Weak preservation*; Hirschfeldt–Jockusch–Kjos-Hanssen–Lempp–Slaman (2008),
   Computational Prospects of Infinity II, 143–161.
4. Hirschfeldt–Shore JSL 72 (2007) 171–206; Hirschfeldt Theorems 9.11, 9.19, Exercises
   9.6, 9.12, 9.20; Dzhafarov–Mummert Theorem 9.2.19; monograph exercise `sads-low`.
5. Monograph, *Coding ideals*; Scott (1962), Proc. Symp. Pure Math. 5, 117–121; Simpson
   VII.2, VIII.2.
6. Hirschfeldt Exercise 3.12, proof of Theorem 6.57; Dzhafarov–Mummert Lemma 8.5.12;
   Simpson VIII.2.9, VIII.2.17.
7. Monograph, *Beyond ∅′*; Hirschfeldt Theorem 4.26, Proposition 4.27, discussion before
   Theorem 6.44; Dzhafarov–Mummert Theorem 2.8.25, Proposition 2.8.26; Simpson, Handbook
   of Mathematical Logic (1977) 631–652 (pages as in Dzhafarov–Mummert; Hirschfeldt's
   bibliography gives other pages).
8. Jockusch–Stephan MLQ 39 (1993) 515–530; CJS JSL 66 (2001) 1–55; Hirschfeldt Theorem
   6.44; Dzhafarov–Mummert Theorem 7.5.15, Lemma 8.5.11.
9. Monograph, *Ramsey's theorem for pairs*; CJS (2001); Dzhafarov–Jockusch JSL 74 (2009);
   Hirschfeldt Theorems 6.52, 6.57; Dzhafarov–Mummert Lemma 8.5.12.
10. CJS (2001); Hirschfeldt Theorem 6.53, Corollary 6.58, Theorem 6.37;
   Dzhafarov–Mummert Theorem 8.5.8, Corollary 8.5.9, Theorem 8.5.10; Chong–Slaman–Yang
   JAMS 27 (2014); Monin–Patey Adv. Math. 389 (2021).

## 9. Recent literature

Checked on 2026-11-12 (web search):

- A 2026 arXiv paper, *Low-like basis theorems for Ramsey's theorem for pairs in
  first-order arithmetic* (arXiv:2601.07569), proves a low₂-type basis theorem for the
  Erdős–Moser principle over IΣ⁰₂ and presents it as a simpler proof of a conservation
  result. Not read in full; not cited in the lessons. A future revision of
  `induction-conservation` or of this course could use it.
- No simpler proof of the CJS theorem than the single-jump control proof was found.
- Monin–Patey (2021), already cited in `ramsey-theorem` and `reducibilities`, is
  mentioned in lesson 7 as the reason why D²₂ differs from COH.

## 10. Open points

- The attribution of `thm-cohyperimmune-low` to Jockusch follows the monograph, which
  cites Hirschfeldt–Jockusch–Kjos-Hanssen–Lempp–Slaman (2008); the bibliographic data of
  the paper were checked (2026-11-13), the attribution inside it was not.
- Ten lessons, slightly more than the nine suggested; merging any two of the new short
  lessons (`stable-linear-orders`, `beyond-zero-jump`) with a neighbor would exceed 45
  minutes.
- The co-hyperimmune lemma could be stated as an abstract theorem on "∅′-decidable
  forcing questions"; the course keeps it concrete.
- Hirschfeldt's Exercise 3.12 is stated for low trees; `prop-uniform-low-basis` is the
  equivalent version for trees computable in a low set.
- Outside the course: `reducibilities/wkl-reductions` says that a {0,1}-valued
  function DNC relative to Z need not compute Z; it always does (`ex-pa-relative`).
  `separation-design/erdos-moser-hyperimmunities` links to `lowness/weak-preservation`
  for ascending sequences, now in `lowness/stable-linear-orders`.

## 11. History

- **2026-11-12.** Course created: seven lessons, four figures
  (`scripts/figures/lowness.py`), design log.
- **2026-11-13: polishing pass.** Mathematics: the Mathias quiz of `forcing-the-jump`
  claimed that a Σ⁰₁ index of the reservoir would not make the question Σ⁰₁ (false:
  compatibility only needs positive membership), replaced; the quiz on `lem-pa-between`
  claimed that a {0,1}-valued DNC function relative to X need not compute X (false),
  replaced; strict inequality in the disjoint-array argument of
  `lem-cohyperimmune-dichotomy` (fails for σ empty) corrected to ≥; the case analysis of
  `thm-sads-low` made exhaustive (finite halves); "strictly weaker than RT²₂" in
  `low-bases` corrected to "does not imply"; the claim that the choice of reservoirs
  "requires" a PA oracle stated precisely; the description of codes of the ideal of
  computable sets corrected; Tennenbaum–Denisov reference completed (Exercise 9.12 for
  type ω + ω*). Figures: `jump-sequence` regenerated to follow the order of the proof
  (dense set, then decision); `side-grid` viewBox enlarged (last line was clipped).
  Structure: ten lessons (see Choices), durations set from word counts. Pedagogy:
  `ex-weakly-low-problems`, comparison of lowness indices and low codes, two SADS
  exercises.
  Track conventions applied after the polishing of `effective-forcing`: oracle order
  Z ⊕ G (base oracle first) throughout; Mathias "stem"; ⊩ and ?⊢ notation, with the
  Mathias question cited from `prop-mathias-question`; prerequisite
  `effective-forcing/generic-sets` for effective genericity.
