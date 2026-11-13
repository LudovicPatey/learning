# Design log: Jump compactness avoidance

This file is the memory of the course (see "Designing tracks and courses" in
`AGENTS.md`). It is not rendered.

## 1. Objectives

After the course, a student can:

- define jump PA avoidance (with the parameters D ≤_T Z, as in `compactness-avoidance`) and
  use it to build ω-models without cohesive sets for the Jockusch–Stephan sequence;
- prove jump PA avoidance from a merging Σ⁰₂ question with answers Σ⁰₁ relative to the
  condition (three-case argument with J^{D'});
- explain why Mathias forcing with one reservoir in a partition regular class produces
  cohesive sets, and why one large class cannot merge two negative Σ⁰₂ answers;
- work with large classes of tuples (product largeness), their intersection and cover
  lemmas, and the complexity of their largeness over a low code;
- define product Mathias forcing, its promises and Σ⁰₂ question, and merge by duplication;
- follow and reproduce the full proof that every Δ⁰₂ set has an infinite subset of itself or
  of its complement whose jump is not PA relative to ∅′ (Monin–Patey), and its consequence
  SRT²₂ ⊬_ω COH, RT²₂.

**Role in the track.** Seventh and last course of "Lowness and avoidance"
(`tracks-design.md`). It combines `compactness-avoidance` (PA avoidance, Liu's lemma, weak
merging) with `jump-cone-avoidance` (Σ⁰₂ questions, largeness, promises). It does not
depend on `separation-design`.

## 2. Prerequisites assumed

- `compactness-avoidance`: J^D, `def-pa-avoidance`, `thm-local-pa-avoidance`,
  `def-valuation`, `lem-liu-valuations` (applied with W = Z′ and D′ in place of D),
  `def-weakly-merging`, `thm-weak-merging-pa`, `thm-coh-pa-avoidance`,
  `thm-rt12-strong-pa`, `thm-liu-rt22`.
- `jump-cone-avoidance`: `def-jump-question-local`, `thm-local-jump-cone`, the
  translation χ_{e,x,v}; `largeness` (`def-large`, `prop-largest-partition-regular`,
  `lem-cover-class`, `prop-largeness-complexity`, `lem-partition-regular-basic`);
  `pigeonhole-forcing` (compatibility of strings, the classes 𝒱_{σ,φ}, `def-valid-part`,
  `lem-valid-part`); `pigeons-non-high` (`def-pigeon-pi2`, construction by tasks).
- `effective-forcing`: `def-forcing-relation`, `prop-forcing-basic`, `thm-forcing-truth`,
  `def-n-generic-notion`, `ex-cohen-question`.
- `lowness`: `cor-scott-codes`, `thm-coh-weakly-low`, `thm-weakly-low-model`,
  `def-weakly-low-basis`, `thm-d22-weakly-low`, `thm-rt22-weakly-low`, `thm-dhls`.
- `ramsey-theorem`: `prop-coh-no-low`, `cor-coh-bounds`, `prop-srt-d22`,
  `thm-rt22-decomposition`, `thm-rt22-coh` (and its second exercise),
  `thm-dj-cone-avoidance`. `reducibilities`: `def-weakness`, `lem-preservation-ideal`.
  `big-five`: `prop-wkl-scott`. `immunity-growth`: `thm-dnc-effectively-immune`.

## 3. Results, lesson by lesson

1. `jump-pa-avoidance`: `def-jump-pa-avoidance`, `prop-jump-pa-model`,
   `ex-jump-pa-problems` (low bases yes; COH and RT²₂ no; D²₂ yes, forward pointer),
   `def-jump-merging`, `thm-jump-pa-merging`, `ex-cohen-jump-pa`,
   `prop-one-reservoir-cohesive`. Exercise: products of problems.
2. `product-largeness` (*Merging and product largeness*): failure of merging with evolving
   classes, `lem-no-two-sides`; index sets, `def-product-large`, `ex-product-large`,
   `lem-product-decreasing`, `lem-product-intersection` (with absorption: 𝒜 ∩ L_W large ⇒
   W ∈ 𝒜), `lem-product-cover`, `prop-product-complexity`. Figure `product-cover`.
3. `product-mathias`: slices, `def-product-condition`, `lem-product-basic`,
   `def-product-promise`, `lem-product-promise`, `def-product-question`,
   `lem-product-question`, `lem-product-merging` (figure `product-merging`),
   `thm-product-mathias`.
4. `meta-conditions`: `thm-d22-jump-pa` (statement), why a product condition may have no
   valid side, `def-meta-index`, `lem-branch-ramsey` (figure `meta-index`),
   `def-meta-condition`, `def-meta-extension`, `def-meta-valid`, `lem-meta-valid`.
5. `meta-questions`: `def-meta-promise`, `lem-meta-promise`, `def-meta-question`,
   `lem-meta-question`, `lem-meta-merging` (figure `weak-merging`).
6. `delta2-jump-pa`: `def-meta-requirement`, `lem-meta-requirement`, the construction by
   tasks, the tree of valid parts and König's lemma (figure `valid-tree`), proof of
   `thm-d22-jump-pa` including the relativization.
7. `srt22-coh`: `cor-srt22-jump-pa`, `thm-srt22-not-coh`, comparison table; jump DNC
   avoidance `def-jump-dnc-avoidance`, `prop-bi-immune-dnc` (HJKLS), `qu-d22-jump-dnc`.

## 4. Proof techniques

- Three-case argument one level up with J^{D'} (L1, L3) and with Liu's valuations
  relativized to ∅′ (L6).
- Merging by keeping both restrictions: duplication of reservoirs and product classes
  (L2–L3); weak merging by triplication with a Ramsey property of index sets (L4–L5).
- Compactness for covers (decreasing intersections, König's lemma on partial partitions,
  L2); refinement of covers to homogeneous parts (intersection and cover lemmas, L2).
- Scott property to take witnesses of non-largeness in the ideal (L3, L5).
- Promises (syntactic Π⁰₂ forcing) kept by descendants and made true on valid parts (L3, L5,
  L6).
- Progress measured by the number of unsettled branches (L6).
- Construction by sequences of conditions with tasks, and a path chosen afterwards by
  König's lemma on the finite sets of valid parts (L6).
- Preservation of a weakness property to build an ω-model (L1, L7).

## 5. Choices

- **Scope as in `tracks-design.md`** (jump PA avoidance; Mathias forcing and COH, product
  largeness; the Monin–Patey theorem), with the consequences for SRT²₂ and a short part on
  jump DNC avoidance. Complete proof of the main theorem in lessons 2–6.
- **Seven lessons at ≤ 2475 counted words** (wc -w, excluding the SVG lines): durations
  45, 45, 45, 45, 45, 40, 35. To fit, the Mathias/COH discussion is split between lesson 1
  (cohesive generics) and lesson 2 (failure of merging), and several exercises were cut
  (abstract weakly merging theorem, transitivity, WKL model, L(𝒜)).
- **No projections.** The monograph equips each branch with the projected class π_I(𝒰).
  Here extensions are defined with slices of tuples, promises and validity are stated on
  the whole class 𝒰^{𝕀_n}_S (the classes 𝒱^I depend only on the coordinates in I), and
  validity is defined as largeness of 𝒰_S ∩ L_{X^{I,i}} (the stronger form of a note of the
  monograph). This removes the projection lemmas and the commutative-diagram lemma; the
  facts needed (validity inherited by ancestors, invariance under finite changes, promises
  made true) are proved directly.
- **Construction by sequences of meta-conditions with tasks** instead of sufficiently
  generic filters, as in `jump-cone-avoidance/pigeons-non-high`; the path is obtained at
  the end by König's lemma on the sets of valid parts (the monograph defines paths through
  a generic filter).
- **Abstract theorem**: the merging version is proved (the monograph leaves it as an
  exercise); the weakly merging version is not stated separately, its argument appears in
  `lem-meta-requirement`.
- **WKL with cone avoidance and jump PA avoidance** (monograph, Theorem
  `wkl-cone-and-jump-pa-avoiding`): omitted; low bases already give jump PA avoidance for
  WKL, and the combined statement repeats `thm-wkl-two-cones`.
- **Thin-set and rainbow Ramsey exercises of the monograph**: omitted; the rainbow Ramsey
  connection is mentioned with Miller's theorem admitted.
- **Excluded**: strong jump PA avoidance of RT¹₂ (status not checked), countably merging
  questions at level 2 (only discussed through the open question).

## 6. Comparison with the literature

- Patey, *Lowness and avoidance*, chapter *Jump compactness avoidance* (main source):
  *Context and motivation*, *Jump PA avoidance* (L1); *Mathias forcing and COH* (L1–L2);
  *Product largeness* (L2); *Product Mathias forcing* (L3); *Pigeonhole principle* (L4–L6);
  *Jump DNC avoidance* (L7). Corrections and differences:
  - Definitions with Π⁰₁ formulas inside the Σ⁰₁ question ("?⊢ ψ" for "?⊢ ¬ψ") written
    explicitly with the classes 𝒱_{τ,¬ψ(m)}.
  - Product Mathias question, negative case: the extension must use the new index set
    S ∪ E (the monograph writes the old one).
  - Meta question, positive case: "D ⊆ C" for "D ⊇ C".
  - Validity: the monograph's definition (membership in the projected class) is not
    invariant under finite changes, which the step "make a promise true" needs; the course
    uses largeness of 𝒰_S ∩ L_{X^{I,i}}.
  - Strings compatible with (σ, X) instead of σ ∪ ρ, for the use principle (as in
    `jump-cone-avoidance`).
- Monin–Patey, *SRT²₂ does not imply RT²₂ in ω-models* (arXiv:1905.08427; first version
  *SRT22 does not imply COH in omega-models*; Advances in Mathematics, 2021). The course
  follows the monograph's presentation, not the paper line by line.
- Dzhafarov–Mummert §8.8 for the history; Chong–Slaman–Yang (JAMS 27 (2014) 863–892) for
  the non-standard model; HJKLS (2008) for `prop-bi-immune-dnc` and SRT²₂ ⊬_ω COH.

## 7. Pedagogical plan

1. Motivation by COH; table of examples; abstract theorem as L1 of compactness avoidance one
   jump up; Cohen as the extremal case; cohesive generics with one reservoir. Quizzes on
   the weakness class, on weakly low bases, on merging, on case 3.
2. The example "G ∩ R finite / G \ R finite" shows why one class cannot merge; products;
   figure of the four functions j for L_R × L_R̄; quizzes on refinement and non-triviality.
3. Conditions, promises, question, merging by duplication (figure); quiz on the Scott
   witness in 𝓜.
4. Why one tuple may have no valid side (explicit example); Ramsey property of branches
   (figure); meta-conditions; validity. Quizzes on 2u_n+1, on the cover lemma, on slices.
5. Promises on parts; the question about a set of branches (where Δ⁰₂ is used); weak
   merging (figure). Quizzes.
6. Forcing a requirement; counting branches; tasks; tree of valid parts (figure). Quizzes on
   positive answers, termination, why the path is chosen at the end, where "∅′ not PA
   relative to ∅′" is used.
7. Separation, comparison table, jump DNC avoidance and open question.

Figures: `scripts/figures/jump-compactness-avoidance.py` (deterministic), pasted by the
scratch script `paste_jca.py` (one figure block per lesson 2–6).

## 8. Sources, lesson by lesson

1. Monograph, *Context and motivation*, *Jump PA avoidance*, *Mathias forcing and COH*;
   Jockusch–Stephan MLQ 39 (1993) 515–530.
2. Monograph, *Mathias forcing and COH*, *Product largeness*; Monin–Patey (2021).
3. Monograph, *Product Mathias forcing*; Monin–Patey (2021).
4–6. Monograph, *Pigeonhole principle*; Monin–Patey (2021); Liu, JSL 77 (2012) 609–620;
   Dzhafarov–Jockusch, JSL 74 (2009) 557–578.
7. Monograph, *Pigeonhole principle*, *Jump DNC avoidance*; HJKLS, *Computational Prospects
   of Infinity II* (2008) 143–161; Chong–Slaman–Yang (2014); Dzhafarov–Mummert §8.8.

## 9. Recent literature

Checked 2026-11-12 (web search): the arXiv/HAL record of Monin–Patey 1905.08427 confirms
the two titles and publication in Advances in Mathematics; the volume and article number
were not confirmed online and are not given. No simpler proof of the theorem was found.

## 10. Open points

- Volume/article number of Monin–Patey (Adv. Math. 2021) to be added once checked.
- Miller's theorem on the rainbow Ramsey theorem is quoted from the monograph, not checked.
- Whether RT¹₂ admits strong jump PA avoidance is not discussed (not checked).
- `qu-d22-jump-dnc` is open according to the monograph; not checked against recent work.

## 11. History

- **2026-11-12.** Course created: seven lessons, five figures
  (`scripts/figures/jump-compactness-avoidance.py`), design log.
