# Design log: Hyperarithmetic sets

This file is the memory of the course (see "Designing tracks and courses" in
`AGENTS.md`). It is not rendered.

## 1. Objectives

After the course, a student can:

- define the H-sets along Kleene's notations and the hyperarithmetic sets, and compute
  with them by effective transfinite recursion, writing out the recursion-theorem
  argument and the induction along `<_O`;
- decide, with an H-set as oracle, comparisons of ordinals of notations and ranks of
  trees, and prove Spector's uniqueness theorem;
- prove Kleene's theorem Δ¹₁ = HYP in both directions, the easy direction by uniqueness of
  H-sequences, the hard one by Spector's boundedness theorem;
- quantify over HYP (a Π¹₁ operation) and use definability arguments to build computable
  trees without hyperarithmetic paths and pseudo-well-orderings;
- prove that descending sequences of jumps compute every hyperarithmetic set, and deduce
  that HYP is not an ω-model of ATR₀.

**Role in the track.** Second core course of the higher computability track
(`content/tracks-design.md`): after `computable-ordinals` (notations, ω₁ᶜᵏ, Π¹₁ normal form,
boundedness), before `descriptive-set-theory` (norms, stage comparison, uniformization,
effective perfect set theorem). It provides "hyperarithmetic sets and Kleene's theorem"
and the first part of "Σ¹₁ classes and their basis theorems". The techniques it owns in
the track are **effective transfinite recursion** and the **boundedness principle** in
use; it also introduces the definability arguments with hyperarithmetic quantifiers.
The higher randomness course and the reverse mathematics track (big-five, ATR₀) cite it.

## 2. Prerequisites assumed

- `computable-ordinals/kleene-o`: notations, `<_O`, the c.e. relation `R`
  (`prop-kleene-o-basic`), `+_O` by the recursion theorem (`lem-notation-sum`),
  Markwald–Kleene (`cor-constructive-computable`), relativization, ω₁^O > ω₁ᶜᵏ.
- `computable-ordinals/trees-and-pi11`: ranks (`def-tree-rank`), Kleene–Brouwer
  (`thm-kleene-brouwer`), normal form (`thm-pi11-normal-form`), `prop-pi11-not-sigma11`,
  boundedness (`thm-boundedness`, and its first exercise for c.e. trees); Π¹₁-completeness
  of O is admitted there.
- Turing degrees and the arithmetic hierarchy: the jump theorem (`thm-jump`), Post's
  theorem (`thm-post`), relativized; recursion theorem (`cor-self-reference`).
- Π⁰₁ classes: leftmost path (`prop-leftmost-path`), low basis theorem (by analogy only).

## 3. Results, lesson by lesson

1. **h-sets** (Iterating the jump along notations): `def-h-sets`, example
   `ex-h-sets-small` with figure `fig-h-chain`, `prop-h-sets-basic` (reductions, finite
   and ω levels, strictness), effective transfinite recursion as a method,
   `prop-h-sets-uniform` (uniform indices of the reductions H_b′ ≤_T H_a; ∅′ ≤_T H_a).
   Exercises: b <_O c ⇒ 2^b ≤_O c; two incomparable notations of ω.
2. **spector-uniqueness** (new 2026-11-12): `lem-notations-below` (O_{<x} ≤_T H_{2^x}
   uniformly), `thm-spector-uniqueness` now proved (figure `fig-spector-matching`), the
   degrees 0^(α), many-one remarks, `def-hyp`, `prop-hyp-ideal`. Exercises: O computes
   HYP and is not in HYP; H-sets along ω·2; {y : |y| = |x|} ≤_T H_{2^{2^x}}.
3. **kleene-theorem**: `def-h-sequence`, `lem-h-sequence-unique`, `prop-h-delta11`,
   `cor-hyp-quantifier`, `lem-rank-sets` (new: Rk_{<x} ≤_T H_{2^x} uniformly, figure
   `fig-tree-ranks`), `lem-wf-rank-hyp` (now proved from it), `thm-kleene-delta11`.
   Exercises: Σ¹₁ subsets of O are bounded; HYP is Π¹₁ in X (both cited by other courses
   by position: keep their order).
4. **sigma11-classes** (Σ¹₁ classes and their members): `def-sigma11-class`,
   `ex-sigma11-classes`, `thm-no-hyp-path`, `thm-kleene-basis`, Gandy basis theorem
   (admitted). Exercise: Π⁰₁ classes in Cantor space have hyperarithmetic members.
5. **pseudo-well-orderings** (new 2026-11-12, split from lesson 4): `thm-harrison`
   (figure `fig-harrison`), `thm-enderton-putnam` (new, proved), `prop-hyp-not-atr0`
   (new, proved). Exercises: the Σ¹₁ set of pseudo-well-orderings (second proof of
   Harrison); the well-founded part has type ω₁ᶜᵏ.

## 4. Proof techniques

- **Effective transfinite recursion** (introduced in lesson 1, used in
  `prop-h-sets-uniform`, `lem-notations-below`, `thm-spector-uniqueness`,
  `lem-rank-sets`): recursion theorem + induction along `<_O`. The course insists on the
  three steps (cases, fixed point, induction) and on what happens off O.
- **Counting jumps**: each lemma states exactly which H-set answers which question
  (Σ⁰₁(A) by A′, Π⁰₂(A) by A″); this is where the "+2" of `H_{2^x}` comes from.
- **Uniqueness gives Δ¹₁** (H-sequences, `prop-h-delta11`): "the unique Y such that" is
  both ∃Y and ∀Y.
- **Boundedness** (`thm-kleene-delta11`): a Σ¹₁ set of well-founded objects has ranks
  bounded below ω₁ᶜᵏ.
- **Definability arguments with hyperarithmetic quantifiers** (`thm-no-hyp-path`,
  second exercise of lesson 5): if HYP sufficed, a complete Π¹₁ set would be Σ¹₁.
- **Leftmost path** (`thm-kleene-basis`), as in the Π⁰₁ setting.
- **Non-uniform definability** (`thm-enderton-putnam`): uniqueness of H-sequences lets an
  arithmetic formula find an index, at the cost of a fixed number of jumps; contrasted
  explicitly with effective transfinite recursion.

## 5. Choices

- **Prove Spector's uniqueness theorem** (previously admitted). It is the result that
  makes 0^(α) and HYP well defined and closed under ⊕; admitting it left the central
  notion of the course on an unproved basis. The proof via `lem-notations-below` is short
  (two recursions of the same shape) and teaches the technique. Monin–Patey prove the
  comparison lemma and derive uniqueness through Σ⁰_α-completeness of H_{2^a}; we derive
  it directly, which avoids the effective Borel codes.
- **Prove the rank lemma** (`lem-wf-rank-hyp`, previously admitted with a sketch whose
  ordinal bound "|a|·2+2" was not justified). With c.e. trees T^i (prefix closure of W_i)
  the recursion is clean and gives a uniform version (`lem-rank-sets`). Since its
  revision of 2026-11-12, `higher-randomness` no longer uses it: it obtains the uniform
  Δ¹₁ definitions it needs from rank comparison. Kleene's theorem is now
  fully proved, modulo the Π¹₁-completeness of O, which is used only in exercises and in
  the Kleene basis theorem.
- **Enderton–Putnam instead of an admitted comparison.** The old proof that HYP is not
  a model of ATR₀ admitted "the comparison between jump hierarchies along computable
  well-orderings and the H-sets" (Simpson VIII.3). The Enderton–Putnam theorem, with
  Simpson's definability proof (Lemmas VIII.3.22–3.23), removes this and works for any
  ill-founded order, so the well-founded part argument became an exercise.
- **Split lesson 4** into Σ¹₁ classes (25 min) and pseudo-well-orderings (40 min): the
  added material made it 3300 words. Labels `def-sigma11-class`, `thm-no-hyp-path`,
  `thm-kleene-basis` stay in `sigma11-classes` (cited elsewhere); `thm-harrison`, which
  no other course cites, moved.
- **Move** `thm-spector-uniqueness`, `def-hyp`, `prop-hyp-ideal` to the new lesson 2:
  `prop-hyp-ideal` needs uniqueness (closure under ⊕). All outside citers depend on
  `kleene-theorem`, which now has lesson 2 as prerequisite.
- **Gandy basis theorem stays admitted.** Its proof is forcing with Σ¹₁ classes with
  witnesses (Gandy–Harrington style); it belongs with the forcing material of
  `descriptive-set-theory` or a future course on Σ¹₁ forcing. Stated with an explanation
  of the difficulty (decreasing Σ¹₁ classes may have empty intersection) and a reference.
- **Harrison's order type** ω₁ᶜᵏ(1+η)+ρ stays admitted; the part used (well-founded part
  of type ω₁ᶜᵏ) is an exercise.
- **Excluded**: effective Borel codes and Σ⁰_α-completeness of H_{2^a} (mentioned as a
  remark), Π⁰₂-singleton characterization and moduli (Groszek–Slaman), hyperarithmetic
  reducibility and the hyperjump as a degree operator, Spector–Gandy theorem (stated in
  notes only). They belong to a later specialized course or to `descriptive-set-theory`.

## 6. Comparison with the literature

- **Monin–Patey**, chapters "Hyperarithmetic sets" (H-sets, Kleene's Σ⁰_α hierarchy,
  Spector's theorem O_{<α}, T_{<α} ≤_T H_{2^a}, completeness), "Beyond hyperarithmetic"
  (Π¹₁, Kleene–Suslin theorem with Spector boundedness), "Σ¹₁ and Π¹₁ classes" (Gandy,
  Kreisel bases), "The systems ATR₀ and Π¹₁-CA₀" (Harrison, Enderton–Putnam, HYP not a
  model of ATR₀). Our definition of H_a at limits (all columns below a) is theirs. We
  avoid the effective Borel codes, at the price of not proving Σ⁰_α-completeness.
- **Simpson**, Section VIII.3 (p. 322 ff.): H-sets along computable linear orders,
  uniqueness by definability (Lemma VIII.3.13), Kleene/Souslin in ACA₀ (Theorem VIII.3.19,
  p. 329), Lemmas VIII.3.22–3.23 (p. 331) on descending sequences, hyperarithmetic
  quantifiers (VIII.3.20, VIII.3.27); Remark I.11.4 for HYP and ω-models of ATR₀;
  Section V.4 for pseudo-hierarchies. Our H-sequences play the role of his H(a, X, Y).
- **Sacks** (Part A) and **Ash–Knight** are the standard monographs; no copy available,
  so they are cited without section numbers.

## 7. Pedagogical plan

1. h-sets: intuition (limit steps need fundamental sequences); example of ω and ω+2 with
   figure; quizzes on the definition and on strictness; ETR explained in three steps,
   with the uniform reduction as first worked example and a quiz on where induction is
   used.
2. spector-uniqueness: intuition (the obstacle: c and b_m on different branches);
   comparison lemma with the jump count made explicit; figure of the matching; quizzes
   on the Π⁰₂ count and on where |a| ≤ |b| is used; remark on why ⊕-closure needs the
   theorem.
3. kleene-theorem: intuition for both inclusions; figure of ranks; rank lemma; quizzes on
   the jump in the successor case, on hypotheses of Kleene's theorem, and on O.
4. sigma11-classes: examples (computing a path; non-hyperarithmetic sets), the
   definability argument named, leftmost path named, Gandy explained.
5. pseudo-well-orderings: intuition (HYP sees only part of the functions); figure of the
   Harrison order type; descending sequences of jumps motivated by hierarchies along
   ill-founded orders; quizzes on the non-uniformity and on the fixed number of jumps.

## 8. Sources

- Lesson 1: Kleene, BAMS 61 (1955) 193–213; Simpson VIII.3 notes (Davis, Mostowski,
  Kleene); Monin–Patey "Hyperarithmetic sets".
- Lesson 2: Spector, JSL 20 (1955) 151–163; Moschovakis, Pacific J. Math. 18 (1966)
  329–342 (data from Monin–Patey's bibliography; the content of the remark is
  Monin–Patey's summary); Monin–Patey for the lemma (their "Theorem (Spector)") and the
  Σ⁰_α-completeness; Simpson Lemma VIII.3.13.
- Lesson 3: Kleene 1955; Spector 1955 for the rank lemma (attribution as in Monin–Patey);
  Simpson Theorem VIII.3.19; Spector–Gandy for the converse of `cor-hyp-quantifier`
  (Simpson notes to VIII.3, Theorem VIII.3.27).
- Lesson 4: Kleene 1955; Gandy, BAMS 66 (1960) 501–502; Monin–Patey "Σ¹₁ and Π¹₁ classes".
- Lesson 5: Harrison, Trans. AMS 131 (1968) 526–543; Enderton–Putnam, JSL 35 (1970)
  429–430; Simpson Lemmas VIII.3.22–3.23, Section V.4 (Lemma V.4.12), Remark I.11.4,
  Sections VII.2, VIII.4, VIII.6.
- All bibliographic data checked against Monin–Patey's `bibliography.bib`; Simpson
  numbers checked in the text of the book.

## 9. Recent literature

A web search (2026-11-12) for new proofs of Spector's uniqueness theorem or new
presentations of pseudo-well-orderings found none relevant to this level: the material
is classical (1955–1970). Results found and not used: Montalbán's extension of Spector's
theorem on hyperarithmetically presented well-orderings to linear orders up to
bi-embeddability (computable structure theory, out of scope); recent uses of
pseudo-well-orderings in work on Martin's conjecture for hyperarithmetic degrees
(arXiv 2306.05746), not needed here. The Groszek–Slaman characterization of HYP by
moduli (cited by Monin–Patey as a 2007 talk) is not used, since no published reference
was checked.

## 10. Open points

- Π¹₁-completeness of O (admitted in `computable-ordinals`) is used in the Kleene basis
  theorem and in exercises; once it is proved there, nothing here changes.
- Gandy basis theorem admitted; a proof could go into `descriptive-set-theory` or a
  course on Σ¹₁ forcing, and the reference here would then point to it.
- Harrison's order type admitted.
- Relativization (H^X_a, Δ¹₁(X) = HYP(X)) is stated in one sentence after Kleene's
  theorem and used by `higher-randomness`; a relativized statement with a label might
  help citers.
- Sacks and Ash–Knight section numbers were removed because no copy was available; they
  could be restored after checking.

## 11. Exercises

Every exercise has a label, an objective, a difficulty and a full solution. Featured
exercises stay in the text, after the material they practice; the others are in the
collapsed block `:::::exercises` at the end of each lesson.

**Featured, and why.**

- h-sets: `ex-notation-successor-below` (2^b <_O a below a limit), placed where the fact
  is first used; the proofs of this lesson and of the next one rely on it.
- spector-uniqueness: `ex-same-ordinal-notations` (after the comparison lemma: one more
  jump decides equality of ordinals) and `ex-h-omega-two` (after the degrees 0^(α): the
  first computation of an H-set above ω, which uses Spector's theorem).
- kleene-theorem: `ex-sigma11-notations-bounded` and `ex-hyp-pi11-in-x`, after Kleene's
  theorem, in their old order: `descriptive-set-theory` (uniformization, perfect-sets)
  cites them as the "first" and "second exercise" of this lesson.
- sigma11-classes: `ex-unique-path-hyp` (new): isolated paths of computable trees are
  hyperarithmetic, so the tree of `thm-no-hyp-path` has a perfect set of paths. It uses
  Kleene's theorem in a new way and explains the shape of that tree; the old exercise on
  Π⁰₁ classes repeated the paragraph after the theorem and moved to the further block.
- pseudo-well-orderings: `ex-harrison-second-proof` and `ex-harrison-wf-part` (the text
  relies on the second for the type of the well-founded part).

**Further exercises, lesson by lesson.**

- h-sets: two incomparable notations of ω (moved); 1 <_O a and non-computability of H_a;
  H_a arithmetic iff |a| finite; H_a ≡_T ⊕ H_{a_n} at limits (the alternative definition);
  H_b ≤_1 H_a along <_O; H-sets from a base X ≤_T ∅′ (a full effective transfinite
  recursion, difficulty 3).
- spector-uniqueness: O computes HYP and is not in it (moved, associated with
  kleene-theorem); closure of HYP under the ω-jump; the relation of all H-sets is not
  hyperarithmetic and computes O with one jump; comparison of ordinals below |x| in
  H_{2^x}; a uniform join via +_O; every hyperarithmetic set is ≤_1 some H_a.
- kleene-theorem: ω₁^X = ω₁ᶜᵏ for hyperarithmetic X (announced in
  `computable-ordinals/boundedness`); WF is not hyperarithmetic; the relation of all H-sets
  is Π¹₁ and not Σ¹₁; a number a ∉ O with no H-sequence (recursion theorem); no Σ¹₁ set of
  notations indexes HYP.
- sigma11-classes: Π⁰₁ classes in Cantor space (moved); closure properties of Σ¹₁
  classes; the extendible nodes of the tree of `thm-no-hyp-path` are not hyperarithmetic;
  the index set of trees with paths but no hyperarithmetic path is Σ¹₁ and not Π¹₁.
- pseudo-well-orderings: paths versus Kleene–Brouwer descending sequences; descending
  sequences computable in O (Kleene basis); an ill-founded computable order with a jump
  hierarchy, hence descending sequences of jumps (removes the appeal to Harrison for
  their existence); HYP is not a Σ¹₁ class (difficulty 3).

**Sources.** The new exercises are standard consequences of the lessons, written for the
course. `ex-hyp-omega1-ck` follows the proof of `prop-omega1-relative`; the existence of
jump hierarchies along ill-founded orders and the failure of Σ¹₁ for HYP are the
definability arguments behind Harrison's pseudo-hierarchies (Simpson, Section V.4, for
the method; Monin–Patey, chapter "The systems ATR₀ and Π¹₁-CA₀"). `ex-unique-path-hyp`
is the effective counterpart of the fact that isolated points of a closed set are
definable from the tree; the perfect set theorem itself is in `descriptive-set-theory`.

**Not used.** Σ¹₁ singletons are hyperarithmetic, and countable Σ¹₁ classes have only
hyperarithmetic members: these are in `descriptive-set-theory/perfect-sets`. A function
with Π¹₁ graph and Δ¹₁ domain is hyperarithmetic: in
`descriptive-set-theory/uniformization`. Boundedness of Σ¹₁ sets of notations is also
`computable-ordinals` `ex-o-bounded`; the existing `ex-sigma11-notations-bounded` stays,
because other courses cite it.

## 12. History

- **2026-11-12.** Design and pedagogy revision. New lesson `spector-uniqueness` with the
  comparison lemma and a proof of Spector's theorem (previously admitted); `def-hyp` and
  `prop-hyp-ideal` moved there. Effective transfinite recursion made explicit in
  `h-sets`, with `prop-h-sets-uniform`. Rank lemma proved (`lem-rank-sets`, new), so
  Kleene's theorem is fully proved. Lesson `sigma11-classes` split; new lesson
  `pseudo-well-orderings` with the Enderton–Putnam theorem (proved) and a proof that
  HYP is not a model of ATR₀ without admitted comparison. Four figures
  (`scripts/figures/hyperarithmetic.py`). Unverifiable section numbers of Sacks and
  Ash–Knight removed; Simpson references checked and made precise.
- **2026-11-13: featured and further exercises.** Labels, objectives and difficulties for
  the 10 existing exercises; 2 featured per lesson except h-sets and sigma11-classes (1);
  23 new exercises, one of them featured (section 11). Text references to exercises by position inside
  the course replaced by `:ref`. Solution of `ex-harrison-wf-part` made precise (initial
  segment, type of W). Durations recomputed: h-sets 35, kleene-theorem 45 (cap; about
  2700 words), sigma11-classes 30.
