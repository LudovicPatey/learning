# Design log: Effective descriptive set theory

This file is the memory of the course (see "Designing tracks and courses" in
`AGENTS.md`). It is not rendered.

## 1. Objectives

After the course, a student can:

- compare the ranks of well-founded trees by strictly monotone maps, and turn this into
  complexity computations (Σ¹₁ for "rank at most", Π¹₁ for its negation when one tree is
  well-founded);
- define the stages of a Π¹₁ set from a normal form, prove that stage comparison is Π¹₁
  (the Π¹₁ sets are normed), and use it as a substitute for "the first element
  enumerated";
- prove the reduction property for Π¹₁ sets, Kleene's separation theorem for Σ¹₁ sets,
  and the failure of the dual properties;
- uniformize Π¹₁ relations on numbers (Kreisel), select hyperarithmetic functions, and
  describe a Π¹₁ set as the increasing union of its hyperarithmetic stages along ω₁ᶜᵏ;
- prove Harrison's effective perfect set theorem and its consequences (countable Σ¹₁
  classes consist of hyperarithmetic sets; Suslin's theorem by relativization), and
  contrast Σ¹₁ with Π¹₁ singletons.

**Role in the track.** Third and last core course of the higher computability track
(`content/tracks-design.md`, since 2026-11-12). It supplies the technique "Π¹₁ norms and
stage comparison" and the analogy Π¹₁ ↔ c.e. in usable form. The higher randomness course
cites `lem-rank-comparison`, `thm-stage-comparison` (lesson `norms`), `cor-total-pi11` and
`thm-pi11-stages` (lesson `uniformization`).

## 2. Prerequisites assumed

- Computable ordinals: well-orderings and the comparison theorem (`thm-wo-comparison`,
  `lem-wo-rigid`), trees and ranks (`def-tree-rank`), the Kleene–Brouwer ordering
  (`thm-kleene-brouwer`), the normal form of Π¹₁ sets (`thm-pi11-normal-form`), WF and WO
  and their completeness (`cor-pi11-complete`), Π¹₁ ≠ Σ¹₁ with the universal set U
  (`prop-pi11-not-sigma11`), Spector's boundedness theorem (`thm-boundedness`), O
  (`def-kleene-o`).
- Hyperarithmetic sets: H-sequences (`lem-h-sequence-unique`), Kleene's theorem
  (`thm-kleene-delta11`), `lem-wf-rank-hyp` (admitted there), quantification over HYP
  (`cor-hyp-quantifier`), Σ¹₁ classes (`def-sigma11-class`), trees without hyperarithmetic
  paths (`thm-no-hyp-path`), the Kleene basis theorem (`thm-kleene-basis`), HYP countable
  (`prop-hyp-ideal`).
- Π⁰₁ classes: isolated members, perfect classes (`def-isolated`,
  `thm-perfect-continuum`, `cor-countable-computable`).

## 3. Results, lesson by lesson

1. **Π¹₁ norms and stage comparison** (`norms`): `lem-rank-comparison`; definition of
   stages `def-pi11-stage` (new); example of c.e. sets `ex-ce-stages` (new);
   `thm-stage-comparison`; `cor-initial-segments`; definition of Π¹₁ norms and the
   prewellordering property `def-pi11-norm` (new). Exercises: Δ¹₁ initial segments;
   the order-type norm on WO.
2. **The reduction and separation properties** (`reduction`, new on 2026-11-12, split
   from `norms`): `thm-pi11-reduction`, `cor-sigma11-separation`, inseparable Π¹₁ sets
   `prop-pi11-inseparable` (new; formerly an exercise of `norms`). Exercises: failure of
   reduction for Σ¹₁ (moved from `uniformization`); reduction of sequences.
3. **Uniformization and stages** (`uniformization`): `thm-kreisel-uniformization`, example
   for c.e. relations `ex-ce-uniformization` (new), `cor-total-pi11`, failure for Σ¹₁
   relations, uniform version for relations with a set parameter (remark),
   `thm-pi11-stages` with the example `ex-ce-stages-below` (new); Spector–Gandy and
   L_{ω₁ᶜᵏ} characterizations admitted. Exercises: Π¹₁ partial functions with Δ¹₁
   domain; unbounded stages.
4. **Countable Σ¹₁ classes** (`perfect-sets`): `prop-sigma11-singleton` (and the
   converse: Σ¹₁ singletons = HYP), WF is a Π¹₁ singleton `prop-wf-pi11-singleton` (new),
   `thm-effective-perfect-set`, `cor-countable-sigma11`, Suslin's perfect set theorem by
   relativization `cor-analytic-perfect-set` (new). Exercises: countability of Σ¹₁ classes
   is Π¹₁; the non-hyperarithmetic sets contain a perfect class.

## 4. Proof techniques

- **Rank comparison by strictly monotone maps** (`norms`): gives the Σ¹₁ side of rank
  comparison; with the recursion on subtrees, a Π¹₁ side once one tree is well-founded.
- **Stage comparison** (`norms`), used for reduction (`reduction`), selection
  (`uniformization`), and in higher randomness. Presented as the analogue of "first
  enumerated", with c.e. sets as a worked special case (`ex-ce-stages`).
- **Two-sided definability**: a Π¹₁ property becomes Δ¹₁ once the ordinals are bounded
  (`cor-initial-segments`, `thm-pi11-stages`), as in Kleene's theorem.
- **Boundedness** (from the computable ordinals course): `thm-pi11-stages` (3).
- **Diagonalization against pairs of indices** (`prop-pi11-inseparable`), as for
  recursively inseparable c.e. sets.
- **Least fixed points of arithmetic rules give Π¹₁ singletons**
  (`prop-wf-pi11-singleton`).
- **Splitting (perfect tree) constructions** (`thm-effective-perfect-set`), from the Π⁰₁
  course, with Σ¹₁ singletons in place of isolated points; it is a first instance of
  forcing with Σ¹₁ classes. Its O-computable version is the method of the Kleene basis
  theorem applied at every node.
- **Relativization** to obtain boldface results (`cor-analytic-perfect-set`).

## 5. Choices

- **Trees and ranks rather than O and H-sets** for stages. Monin–Patey use the
  decomposition A = ⋃ A_α with A_α ∈ Σ⁰_{α+1} via O; ranks are closer to the normal form
  already proved, make the comparison lemma elementary, and are what higher randomness
  uses. The O-based view is mentioned in the notes.
- **Norms defined abstractly** (`def-pi11-norm`), in the form of Moschovakis (with ∞
  outside A), so that students can read Moschovakis Chapter 4 and the higher randomness
  literature. The general theory of normed pointclasses is not developed.
- **Split of `norms` into `norms` + `reduction`** (2026-11-12). With intuitions, the norm
  definition, examples and figures, the first lesson was about 3700 words. Reduction,
  separation and inseparability form a coherent unit, with the c.e. pattern (reduction
  for Π¹₁, separation for Σ¹₁, the duals fail) made explicit. The moved labels
  (`thm-pi11-reduction`, `cor-sigma11-separation`) were not cited outside the course.
- **Inseparable Π¹₁ sets promoted from exercise to proposition**, since uniformization
  and an exercise depend on it.
- **Uniformization on numbers only.** The Novikov–Kondo–Addison theorem (Π¹₁
  uniformization on reals) needs scales or Guaspari/Sacks-style analysis; mentioned,
  excluded. The uniform version with a set parameter is stated as a remark with a proof
  sketch, since it is what applications use.
- **Spector–Gandy and Σ₁ over L_{ω₁ᶜᵏ}** admitted, as precise forms of the analogy; their
  proofs need the Gandy basis theorem or admissible sets.
- **O as a Π¹₁ singleton** is admitted; **WF as a Π¹₁ singleton** is proved instead
  (short, by the inductive definition), which removes an admitted fact from the course
  and shows that the Σ¹₁ hypothesis of Harrison's theorem is needed.
- **Suslin's classical theorem** added as a corollary by relativization: it shows how
  effective proofs yield boldface results, a theme of Moschovakis's book.
- **Excluded:** Π¹₁ uniformization on reals, the Gandy–Harrington topology, the
  Mansfield–Solovay theorem and the largest thin Π¹₁ class, Cantor–Bendixson analysis of
  Π⁰₁ classes (Kreisel), the Σ¹₂ theory. Reasons: each needs tools beyond the track
  (Gandy basis theorem, scales, set theory of L) and would double the course.
- **Not added:** a lesson proving Spector–Gandy. It would be the natural next addition
  if the higher randomness course or a Π¹₁ forcing course needs it.

## 6. Comparison with the literature

- **Moschovakis, *Descriptive Set Theory* (2009), Chapter 4.** 4A (representation of Π¹₁
  by trees, boundedness), 4B (prewellordering: 4B.2 Π¹₁ normed, 4B.4 Easy Uniformization
  (Kreisel), 4B.5 Δ-selection, 4B.10–4B.12 reduction and separation), 4E.4
  (Novikov–Kondo–Addison), 4F.1 (effective perfect set theorem, Harrison), 4F.3
  (Spector–Gandy). The course is the case X = ω of 4A–4B and part of 4F, with proofs
  specialized to trees and without pointclass generality. Checked against the author's
  PDF (math.ucla.edu/~ynm).
- **Monin–Patey, chapter *Beyond hyperarithmetic*,** sections *The Π¹₁ sets and the
  well-orders* and *Analogies between Π¹₁ sets and c.e. sets*: Kreisel uniformization and
  total Π¹₁ functions via O-stages; chapter *Σ¹₁ and Π¹₁ classes*, sections *The
  continuum hypothesis for Σ¹₁ classes* (the same splitting proof, done with O) and *Π¹₁
  singletons* (O is a Π¹₁ singleton), *Study of a very special Π¹₁ class* (Guaspari's
  class, uniformization of Π¹₁ classes, Mansfield–Solovay). The course differs by using
  ranks and norms, and by proving reduction/separation, which Monin–Patey do not treat.
- **Simpson, SOSOA,** V.3 (Lusin separation in ATR₀), V.4–V.5 (perfect set theorem
  V.4.3 proved with pseudo-hierarchies; equivalent to ATR₀ over ACA₀, Theorem V.5.5),
  VI.2 (Π¹₁ uniformization Lemma VI.2.1 in Π¹₁-CA₀; Kondo's theorem equivalent to
  Π¹₁-CA₀ over ATR₀, Theorem VI.2.6). Cited in the notes for the reverse-mathematics
  strength.
- **Kechris, *Classical Descriptive Set Theory*,** Sections 29 (regularity properties,
  perfect set property), 34–35 (co-analytic ranks, rank theory), 36 (scales and
  uniformization): classical counterparts (section titles checked from the table of
  contents only).
- **Sacks, *Higher Recursion Theory*:** not available locally. Only part-level
  references are kept (Parts B and C, metarecursion and α-recursion), checked against
  the publisher's table of contents (Part A: chapters I–IV; Part B: V–VI; Part C:
  VII–IX; Part D: X–XIII).

## 7. Pedagogical plan

- `norms`: intuition (descents imitated by a map); example of ranks of full trees; why
  "strictly" matters (non-strict maps always exist); counterexample to the strict
  comparison formula for ill-founded trees; figure `rank-map`; c.e. sets as a worked
  example of stages; non-canonicity of the stages; the reason for the hypothesis n ∈ A
  (quiz); norm definition; exercise on the WO norm.
- `reduction`: the c.e. pattern stated first; figure `reduction-stages` (ties, ∞); quiz on
  tie-breaking; separation as complement of reduction; diagonal intuition before
  `prop-pi11-inseparable`, quiz on why reduction is used there; the table of which
  properties hold on which side.
- `uniformization`: why "least m" fails (negative information); figure
  `uniformization-choice`; c.e. relations as a special case; Σ¹₁ counterexample; uniform
  version; stages from below with the c.e. example; uniform versus non-uniform bounds;
  Spector–Gandy as "Σ₁ over HYP".
- `perfect-sets`: the Π⁰₁ splitting construction recalled and what replaces isolated
  points; Σ¹₁ singletons = HYP; failure for Π¹₁ singletons explained from the proof, then
  WF; figure `sigma11-splitting` (nested cylinders of the σ_s); necessity of the Σ¹₁
  hypothesis; O-computability as Kleene basis at every node; relativization to Suslin.
- Figures are generated by `scripts/figures/descriptive-set-theory.py`.

## 8. Sources (checked 2026-11-12)

- `norms`: Moschovakis 4A.3, 4B.2 and 4G remarks 5–9, 12 (Lusin–Sierpiński 1923 ordering;
  Kleene 1955, Spector 1955 representations; prewellordering isolated by Moschovakis
  1964, definition due to Kechris). Kechris 34–35. Monin–Patey as above.
- `reduction`: Moschovakis 4B.10–4B.12 and 4G remark 13 (Lusin 1927 separation for Σ¹₁;
  Kuratowski 1936; Addison [1959a] lightface results; Kleene 1950 failure for Σ⁰₁).
  Kleene's Σ¹₁ separation by a HYP set: Kleene, *Hierarchies of number-theoretic
  predicates*, Bull. AMS 61 (1955), as cited in A. Miller, *Descriptive set theory and
  forcing* (arXiv math/9401202), Theorem 27.1. Addison, Fund. Math. 46, 123–135: dated
  1958 by the publisher (IMPAN) and Monin–Patey's bibliography, 1959 by Moschovakis and
  the JSL review; the course writes 1958.
- `uniformization`: Kreisel, Indag. Math. 24 (1962), 307–319 (Simpson bibliography [150];
  Moschovakis 4B.4–4B.5). Kondo, Japanese J. Math. 15 (1938), 197–230 (Simpson [146];
  Moschovakis 4G remark 21 for Novikov and Addison). Simpson VI.2.6. Spector–Gandy:
  Moschovakis 4F.3 (Spector 1960, Gandy 1960).
- `perfect-sets`: Harrison, PhD thesis, Stanford 1967 (Moschovakis bibliography, 4F.1);
  Harrison, TAMS 131 (1968), 526–543. Simpson V.4.3, V.5.5. Monin–Patey sections above.
  Kechris 29. Suslin 1917 (classical, not checked against a source; standard).

## 9. Recent literature

Checked: Monin–Patey's presentation (O-based stages); L. Bienvenu,
N. Greenberg and B. Monin, *Continuous higher randomness*, J. Math. Logic (2017)
(higher Turing reductions, built on the same view of Π¹₁ sets as c.e. along ω₁ᶜᵏ;
skimmed through Monin–Patey's account only); A. Marks's lecture
notes on effective descriptive set theory (Berkeley/UCLA) and recent papers citing the
effective perfect set theorem (e.g. arXiv 1906.04351, which cites Moschovakis 4F.1). No
simpler proof of the stage comparison theorem or of the effective perfect set theorem was
found; the present proofs are already the standard short ones. The Gandy–Harrington
forcing proof is an alternative, not simpler with the course's prerequisites. No question
presented as open in the course. Conclusion: no change of content from the recent
literature; references were corrected from the sources above.

## 10. Open points

- Should a Spector–Gandy lesson be added (needs the Gandy basis theorem, admitted in the
  hyperarithmetic course)?
- The hyperarithmetic course admits `lem-wf-rank-hyp`; `thm-pi11-stages` (2) depends on
  it.
- Exact section of Sacks for the Kreisel–Sacks metarecursion and the Σ₁(L_{ω₁ᶜᵏ})
  characterization not checked (book not available); only part-level references kept.
- Kechris references are checked at the level of section titles only.

## 11. History

- **2026-11-12.** Design revision.
  - New lesson `reduction`, split from `norms`; `prop-pi11-inseparable` promoted from an
    exercise; the Σ¹₁ reduction exercise moved there from `uniformization`.
  - New labels: `def-pi11-stage`, `def-pi11-norm`, `ex-ce-stages`,
    `ex-ce-uniformization`, `ex-ce-stages-below`, `prop-pi11-inseparable`,
    `prop-wf-pi11-singleton`, `cor-analytic-perfect-set`. No label removed.
  - Four figures (`rank-map`, `reduction-stages`, `uniformization-choice`,
    `sigma11-splitting`) and the generator `scripts/figures/descriptive-set-theory.py`.
  - Intuitions, examples and counterexamples added in every lesson; new quizzes
    (reduction, inseparability, Π¹₁ singleton); new exercises (WO norm, reduction of
    sequences, Π¹₁ functions with Δ¹₁ domain).
  - References checked against Moschovakis (2009), Simpson, Monin–Patey and the Sacks and
    Kechris tables of contents; unverifiable section numbers of Sacks removed;
    attributions of reduction/separation (Lusin, Kuratowski, Kleene, Addison) and of the
    Gandy–Harrington remark corrected (REVIEW-2026-11 items).
