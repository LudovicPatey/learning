# Design log: Custom separations and forcing design

This file is the memory of the course (see "Designing tracks and courses" in
`AGENTS.md`). It is not rendered.

## 1. Objectives

After the course, a student can:

- explain why the classical avoidance properties (cone, PA, one hyperimmunity, lowness)
  do not separate the Ramsey-type problems below RT²₂, and split a separation into a
  preservation theorem and a separating instance;
- define hyperimmunity (of sets), k-immunity and constant-bound immunity, dependent
  hyperimmunity, and preservation of k hyperimmunities, and compare them;
- read the property preserved by a problem off the third case of the three-case argument
  (worked example: WKL preserves hyperimmunity but not immunity);
- design a notion of forcing for a Ramsey-type problem in three steps (extendibility,
  block extendibility, computational properties), separating optional from required
  structural properties;
- prove that EM avoids cones and preserves ω hyperimmunities, that RT²₂ does not preserve
  2, and deduce SRT²₂ ≰_ω EM and ADS ≰_ω EM, with RT²₂ ≡ EM + ADS on Turing ideals;
- prove that CAC preserves c.b.-immunity (split triples, constant-bound compactness) and
  that ADS preserves dependent hyperimmunity (split pairs, extremal question);
- build the separating instances by finite injury, and deduce DNC, RT²₂, EM ≰_ω CAC and
  SCAC ≰_ω ADS;
- design the notion of forcing for FS² and prove its cone avoidance; describe the
  extension to FS³ through the thin set theorems.

**Role in the track.** Fifth course of "Lowness and avoidance" (`tracks-design.md`),
after `effective-forcing`, `avoidance`, `lowness`, `compactness-avoidance`. It does not
depend on `lowness` (no lowness result is used), nor on `jump-cone-avoidance`, written
in parallel. It is where the two meta-skills of the track are taught explicitly: choosing
the weakness property, and designing the notion of forcing.

## 2. Prerequisites assumed

- `reducibilities/preservation`: `def-weakness`, `lem-preservation-ideal`,
  `thm-preservation-separation`.
- `effective-forcing`: `def-forcing-notion` (only to note that EM conditions lack
  refinement), the forcing question framework.
- `avoidance`: three-case argument and `thm-local-cone-avoidance`, Seetapun forcing and
  question (`def-seetapun-forcing`, `lem-seetapun-question`), `def-disjunctive-notion`,
  `lem-scott-preservation`, `def-preserve-hyperimmunity`, `thm-hyperimmunity-examples`,
  `thm-local-hyperimmunity`.
- `compactness-avoidance`: `def-preserve-immunity`, `def-countably-merging`,
  `cor-rt22-dnc`, `prop-rwkl-reductions`.
- `immunity-growth`: `def-hyperimmune-set`, `thm-hyperimmune-principal`,
  `ex-post-not-hypersimple`, `def-effectively-immune`, `thm-dnc-effectively-immune`.
- `pi01-classes`: `cor-bounded-pa`, `thm-pa-characterization`, `thm-dominated-basis`,
  `thm-cone-avoidance-basis`; `big-five`: Scott ideals.
- `ramsey-theorem`: `thm-seetapun`, `lem-scott-cone`, `prop-rt32-jump`,
  `thm-dj-cone-avoidance`.
- `turing-degrees`: `thm-limit-lemma`, `cor-complete-domination`.
- `lowness/stable-linear-orders`: ascending/descending sequences (definition only).

## 3. Results, lesson by lesson

1. **Custom properties and immunity** (`custom-properties`): the two halves of a
   separation; solutions closed under subsets are immune (`prop-sd-subset-immune`);
   k-arrays, k-immunity, c.b.-immunity (`def-sd-cb-immune`); co-c.e. immune ⇔
   c.b.-immune (`prop-sd-coce-cb`), so Post's co-simple set is c.b.-immune, not
   hyperimmune; WKL analysis: the question yields finite blocks, hence hyperimmunity;
   WKL does not preserve immunity (`prop-sd-wkl-immunity`); table of the course's
   separations. Exercise `exr-sd-min-arrays` (arrays with min F_n > n).
2. **Designing a notion of forcing** (`erdos-moser-design`): tournaments, EM
   (`def-sd-tournament`), EM ≤_sc RT²₂ (`prop-sd-em-rt22`); step 1, EM conditions
   (`def-sd-em-condition`, figure `em-condition`), one-point extension
   (`lem-sd-em-extension`); step 2, the failure of blocks (`ex-sd-em-block`), limit
   colors and over-approximation, the question over partitions (`lem-sd-em-question`).
   Exercise: L-compatible blocks.
3. **The Erdős–Moser theorem, cone avoidance and hyperimmunities** (`erdos-moser-hyperimmunities`):
   step 3; EM admits cone avoidance (`thm-sd-em-cone`); preservation of k hyperimmunities
   (`def-sd-k-hyperimmunities`), compactness of the EM question (`lem-sd-em-compact`),
   EM preserves ω hyperimmunities (`thm-sd-em-hyperimmunities`, Patey). Exercises:
   WKL preserves ω hyperimmunities (`exr-wkl-hyperimmunities`); strong cone avoidance of
   EM (`exr-em-strong-cone`, restored 2026-11-13).
3b. **Separating EM from RT²₂** (`erdos-moser-separation`, new 2026-11-13): Δ⁰₂
   bi-hyperimmune set (`lem-sd-bihyperimmune`); SRT²₂ does not preserve 2
   (`prop-sd-rt22-two`); SRT²₂ ≰_ω EM (`cor-sd-em-not-srt22`, LST); RT²₂ ⇔ EM + ADS on
   Turing ideals (`prop-sd-rt22-em-ads`), ADS ≰_ω EM (`cor-sd-ads-not-em`). Exercise:
   RT²₂ preserves 2 among 3 hyperimmunities, RT²₃ not 3 among 3
   (`exr-rt22-two-among-three`, restored 2026-11-13).
4. **Partial orders and constant-bound immunity** (`chain-antichain`): CAC; CAC
   conditions with three stems and stem-based forcing (`def-sd-cac-condition`); (H) and
   extension (`lem-sd-cac-extension`); split triples (`def-sd-split-triple`, figure
   `split-triple`), the question (`lem-sd-cac-question`); constant-bound compactness;
   preservation of c.b.-immunity (`def-sd-preserve-cb`); CAC preserves it
   (`thm-sd-cac-cb`, Patey). Exercise: the case where (H) fails.
5. **Linear orders and dependent hyperimmunity** (`ascending-descending`): ADS conditions,
   split pairs (`def-sd-split-pair`), the extremal question (`lem-sd-ads-question`);
   essential formulas and dependent hyperimmunity (`def-sd-dependent`), consequences
   (`ex-sd-dependent`); ADS preserves it (`thm-sd-ads-dependent`, Patey). Exercise: a
   solution inside one part breaks the property.
6. **Building the separating instances** (`separating-instances`): Δ⁰₂ c.b.-immune set
   met by every DNC function (`thm-sd-dnc-cb`, Patey; figure `cb-columns`);
   DNC, RT²₂, EM ≰_ω CAC (`cor-sd-cac-not-dnc`); computable stable partial order with
   (I, B) dependently hyperimmune (`thm-sd-stable-order`, Patey); SCAC ≰_ω ADS
   (`cor-sd-ads-not-scac`, LST). Exercise: properties of the order.
7. **Forcing design for the free set theorem** (`free-set-design`): FS^n; FS¹ computably
   true (`lem-sd-fs1`); FS² conditions (`def-sd-fs-condition`); two candidates
   (`lem-sd-fs-extension`); limit patterns (`def-sd-fs-stabilize`), safe blocks
   (`lem-sd-fs-block`), the question (`lem-sd-fs-question`); FS² admits cone avoidance
   (`thm-sd-fs2-cone`); triples through the thin set theorems (described, admitted).
   Exercise: free sets give thin sets.

## 4. Proof techniques

- **Reading a property off a forcing question** (case 3 of the three-case argument):
  lessons 1, 3, 4, 5.
- **Design in three steps**: optional vs required structural properties (lessons 2, 7);
  safe blocks via limit behavior (homogeneity for limit colors, g-freeness for limit
  patterns); over-approximation by quantifying over a compact space of possible limits
  (partitions, patterns); closure properties of the reservoir class from the list of
  operations (lessons 3, 7).
- **Non-disjunctive vs disjunctive questions**: conjunctive requirements for EM, Lachlan's
  disjunction over 2 or 3 sides (lessons 3, 4, 5).
- **Constant-bound compactness** (lesson 4) and **extremality** (lesson 5).
- **Forcing through stems** instead of members when negative answers are not witnessed by
  restricting the reservoir (lessons 4, 5).
- **Candidates and Ramsey for pairs** to add one of several elements (lesson 7).
- **Finite injury with columns and thresholds** (DNC instance) and **movable markers with
  interval moves** (stable order) for separating instances (lesson 6).
- **Limit lemma colorings** for instances (lessons 3, 6).

## 5. Choices

- **Seven lessons, then eight; strict durations.** At 55 words per minute, 45 minutes is about 2475
  words (counted with `wc -w`, figures excluded). A first draft had lessons of 3000–4200
  words; the EM design was split into design (lesson 2) and step 3 + separations (lesson
  3), and the counterexample constructions were grouped in lesson 6, so that every lesson
  is 2150–2490 words (40–45 minutes). Several exercises were dropped to stay within the
  bound (strong cone avoidance of EM, RT¹₂ and two hyperimmunities, ADS ≤ CAC, COH
  preserves immunity).
- **Order: design before use.** The monograph treats custom properties (chapter *Custom
  properties*) before forcing design (chapter *Forcing design*), with the EM forcing "out of
  the blue" in the first. Here the EM forcing is designed first (lesson 2) and then used
  (lesson 3); FS comes last as a second design example.
- **One EM question.** The monograph has two EM questions (partitions in *Custom
  properties*, colorings with g-compatible blocks in *Forcing design*). The course uses the
  partition question with homogeneous blocks (mentioned as a valid variant in the
  monograph), for its similarity with the Seetapun question of `avoidance`; compatibility is
  an exercise.
- **EM conditions are not a notion of forcing in the sense of `def-forcing-notion`**
  (refinement fails), so constructions are decreasing sequences of conditions, as in
  `avoidance/seetapun-forcing`; the three-case argument is redone there.
- **Stem-based forcing for CAC and ADS.** The monograph's proof of the CAC question uses
  "p forces ¬φ" where the case analysis only gives conditions-level information; with forcing
  defined as truth on all members, Case 2 does not go through (members may be finite). The
  course defines forcing of Σ⁰₁ facts and their negations through stems of extensions, and
  checks that unions of stems satisfy what is forced.
- **Correction to the monograph's CAC question proof.** In property 2, Case 1 must require
  that the two stems satisfy φ₀ and φ₁ (otherwise the split triple obtained does not
  contradict the negative answer). Recorded in the lesson's notes.
- **Degenerate case (H) for CAC**, left to the reader in the monograph, is an exercise with
  solution (behaviors of missing sides cannot occur in the restricted reservoir).
- **Arrays.** k-arrays are disjoint strong arrays as in `immunity-growth`; the monograph's
  convention min F_n > n is shown equivalent (`exr-sd-min-arrays`) and used in proofs.
- **c.b.-immunity proof on co-c.e. sets** given directly by induction on the bound (the
  monograph leaves it as an exercise).
- **WKL fails immunity** (`prop-sd-wkl-immunity`) is added: it makes the "read the property"
  analysis two-sided, using the explicit intervals of Post's simple set.
- **Bi-hyperimmune Δ⁰₂ set** proved directly by a ∅′ finite extension argument, rather than
  through genericity.
- **DNC instance**: μ(i) is defined as the least s > i with ∅′_s↾i = ∅′↾i, so that |F_i| > i
  ≥ |W ∩ X_i| and A is infinite (the monograph's modulus may be too small for this), and so
  that μ is left-c.e. with an explicit proof. The c.b.-immunity induction starts at k = 0.
- **Stable order**: the sets are named B (small, "below almost everything") and I
  (isolated); the monograph's L* corresponds to B. Transitivity and limits are proved with
  the invariant "markers are non-decreasing in priority".
- **Free set theorem for pairs instead of triples.** The monograph designs the forcing for
  FS³, which needs cone avoidance of RT³_{<∞,ℓ} (Wang; Cholak–Patey), not proved in the
  platform. The course designs FS² completely, with RT²_k (from Seetapun) as the input,
  noting that FS² cone avoidance also follows from RT²₂ ⊢ FS² (Cholak–Giusto–Hirst–Jockusch),
  and describes FS³ in a section with the thin set theorems admitted. Patterns are bounded
  by 1 (ℓ₁ = ℓ₂ = 1).
- **Admitted results**: EM ⊢ RWKL (Bienvenu–Patey–Shafer; Flood–Towsner), used in
  `cor-sd-cac-not-dnc`; Wang's and Cholak–Patey's theorems on thin sets (lesson 7, prose).
- **Excluded.**
  - (Strong cone avoidance of EM and 2 among 3 hyperimmunities were restored as exercises
    on 2026-11-13, after the split of lesson 3.) ADS ≤ CAC is proved in the prose of
    `ascending-descending`; COH preserves immunity is covered by `compactness-avoidance`.
  - Abstract theorems (c.b.-compact questions preserve c.b.-immunity; extremal questions
    preserve dependent hyperimmunity): mentioned in notes of lesson 5 only.
  - Rainbow Ramsey theorem, trapped colorings, FS^n for all n (monograph exercises).
  - CAC ⊢ strong CAC, CAC ⇔ transitive colorings, Herrmann's order (Hirschfeldt–Shore).
  - ADS ⊢ COH (Hirschfeldt–Shore) and ADS ⊬ DNC.

## 6. Comparison with the literature

- **Patey, *Lowness and avoidance*, chapters *Custom properties* and *Forcing design***
  (main sources). Separation framework → lesson 1 (cited from `reducibilities`); Immunity
  and variants, Hyperimmunity and WKL → lesson 1; Erdős–Moser theorem (custom) → lesson 3;
  Partial orders → lessons 4 and 6; Linear orders → lessons 5 and 6; Forcing design: core
  concepts and EM → lessons 2–3; free set theorem → lesson 7 (pairs instead of triples).
  Differences: see Choices (stem-based forcing, Case 1 correction, degenerate case,
  modulus of the DNC instance, FS² instead of FS³).
- **Hirschfeldt, *Slicing the Truth*, Chapter 9**: ADS, CAC (Definitions 9.1–9.2,
  Exercise 9.3), Herrmann (Theorem 9.5), SCAC (Definition 9.24), LST (Theorems 9.29,
  9.31), RT²₂ = EM + ADS (Exercise 9.30), FS and TS (Definition 9.32, Theorem 9.35 CGHJ,
  Theorem 9.38 Wang). Checked in the text version.
- **Dzhafarov–Mummert, Section 9.8**: FS and TS, Theorem 9.8.3 (RT^n_2 → FS^n), Corollary
  9.8.8 (Wang: strong cone avoidance of FS). Checked.
- **Patey (2017), *Iterative forcing and hyperimmunity*** (EM preserves ω hyperimmunities;
  RT²₂ not 2) and **Patey (2018), *Partial orders and immunity*** (CAC, c.b.-immunity, DNC
  instance; ADS, dependent hyperimmunity, stable order): cited through the monograph.

## 7. Pedagogical plan

1. `custom-properties`: the two halves; immunity hierarchy with the Post example; the WKL
   analysis as the model of "reading the property"; table of the course.
2. `erdos-moser-design`: 3-cycles; the two cases of failure (optional/required); figure
   `em-condition`; the bad block example; homogeneity for limit colors; the question;
   quizzes on homogeneity and on the Scott ideal.
3. `erdos-moser-hyperimmunities`: closure properties; cone avoidance; why conjunctive
   requirements allow several hyperimmunities; quizzes on these points; the stable coloring
   from a bi-hyperimmune Δ⁰₂ set; RT²₂ as EM + ADS.
4. `chain-antichain`: why three stems; figure `split-triple`; the three cases of property 1;
   constant-bound compactness; quiz on transitivity.
5. `ascending-descending`: extremality as the design feature, contrasted with CAC; essential
   formulas as a game; quizzes on merging witnesses and on the role of extremality.
6. `separating-instances`: columns and cuts (figure `cb-columns`); left-c.e. cut; finite
   injury; movable markers and interval moves; quizzes.
7. `free-set-design`: the four cases; two candidates; patterns; quiz on the
   over-approximation.

Figures are generated by `scripts/figures/separation-design.py` (deterministic).

## 8. Sources, lesson by lesson

1. Monograph *Custom properties* §§ Separation framework, Immunity and variants,
   Hyperimmunity and WKL; Patey (2018); Jockusch–Soare (1972).
2. Monograph *Forcing design* §§ Core concepts, Erdős–Moser theorem; Patey (2017); LST
   (2013); Bovykin–Weiermann (2017).
3. Monograph *Custom properties* § Erdős–Moser theorem; Patey (2017); LST (2013);
   Hirschfeldt Ex. 9.30, Thm 9.31; Bienvenu–Patey–Shafer (2017); Flood–Towsner (2016).
4. Monograph *Custom properties* § Partial orders; Patey (2018); Hirschfeldt–Shore (2007).
5. Monograph *Custom properties* § Linear orders; Patey (2018); LST (2013);
   Hirschfeldt Ex. 9.3.
6. Monograph *Custom properties* §§ Partial orders, Linear orders; Patey (2018);
   Hirschfeldt–Shore (2007); LST (2013); Hirschfeldt Thm 9.29.
7. Monograph *Forcing design* § Free set theorem; Cholak–Giusto–Hirst–Jockusch (2005);
   Wang (2014); Cholak–Patey (2020); Hirschfeldt Thm 9.35; Dzhafarov–Mummert §9.8.

## 9. Recent literature

Checked on 2026-11-12 (web search): the implication EM → RWKL is confirmed by the abstract
of Flood and Towsner, *Separating principles below WKL₀* (MLQ 2016), which says it was
obtained independently by Bienvenu, Patey and Shafer. Not read: Liu and Patey,
*The reverse mathematics of the thin set and Erdős–Moser theorems* (Journal of Symbolic
Logic; listed in the bibliography of Dzhafarov–Mummert), which studies EM and the thin set
theorems together; a possible source for a future lesson on
thin sets. No change to the course.

## 10. Open points

- The exercise of the monograph "EM implies RWKL with the tournament built from leftmost
  strings" could not be verified as stated (a transitive subtournament of that tournament
  gives a stable linear order, whose ascending/descending sequences seem to need SADS); the
  course only cites the theorem as admitted. To check against Bienvenu–Patey–Shafer.
- (Resolved 2026-11-13.) Flood–Towsner MLQ 62 (2016) 507–529 (web search); CGHJ LNL 21,
  104–119, and Cholak–Patey TAMS 373 (2020) 2743–2773, checked against the bibliography of
  Dzhafarov–Mummert; Dzhafarov–Jockusch JSL 74 (2009) 557–578 against the monograph's.
- Patey, *Partial orders and immunity*: the conference version is in LNCS 9709 (CiE 2016),
  353–363 (Dzhafarov–Mummert); the course cites the journal version, Computability 7 (2018),
  323–339 (monograph bibliography).
- Attribution of `prop-sd-rt22-two` to Patey (2017) is from the monograph's chapter context;
  the theorem environment carries no name.
- Durations (2026-11-13): eight lessons, at most 2476 words each (45 minutes); the
  shortest is `erdos-moser-separation` (about 1790 words, 35 minutes).

## 11. History

- **2026-11-12.** Course created: seven lessons, three figures
  (`scripts/figures/separation-design.py`), design log.
- **2026-11-13: polishing pass.**
  - Corrections: figure `em-condition` showed the pattern down/up/down/up on a transitive stem,
    which violates (b) (a₂, a₃ and any reservoir element form a 3-cycle); regenerated with
    down/down/up/up and the caption explains the constraint. `lem-sd-bihyperimmune`: the
    construction did not guarantee that A is infinite (requirements may only add zeros); each
    step now adds one element to each side. `prop-sd-coce-cb`: the union of the tail of the
    array is c.e., not computable. `thm-sd-dnc-cb`: base case k = 0 restated (Ψ_{e,0} is
    nowhere defined, since members are non-empty), and the use of R_{e,k} made explicit
    (no member is inside W). `lem-sd-em-question`: "at least two elements in σ". Ψ_{e,k}
    in `chain-antichain` now requires non-empty sets. Forward claim "ADS has no compactness,
    as ascending-descending shows" replaced by the correct pointer (ADS ≤ CAC, CAC ⊬ DNC).
  - Structure: lesson 3 split into `erdos-moser-hyperimmunities` (step 3, cone avoidance,
    ω hyperimmunities) and `erdos-moser-separation` (instance, SRT²₂ ≰ EM, RT²₂ = EM + ADS);
    two dropped exercises restored (`exr-em-strong-cone`, `exr-rt22-two-among-three`);
    `exr-em-l-compatible` labelled (used by the strong cone avoidance exercise). New labels
    carry no `sd-` prefix. Lessons 2, 6, 7 trimmed by a few words to stay at 45 minutes.
  - Consistency: linear orders written <_𝓛 in `ascending-descending`, as in
    `erdos-moser-separation` and `lowness/stable-linear-orders`; "satisfies" for strings defined in
    `erdos-moser-design` as in `avoidance/seetapun-forcing`.
  - References: Hirschfeldt sections corrected (EM 9.2.2, CAC 9.1 and 9.2.1); unused LST
    entry removed from lesson 2; Flood–Towsner pages added; Patey's thesis and
    Dzhafarov–Jockusch added where used.
