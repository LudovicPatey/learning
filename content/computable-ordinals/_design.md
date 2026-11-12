# Design log: Computable ordinals

This file is the memory of the course (see "Designing tracks and courses" in
`AGENTS.md`). It is not rendered.

## 1. Objectives

After the course, a student can:

- manipulate well-orderings, ordinals, transfinite induction and recursion, and ordinal
  arithmetic at the level needed for computability;
- present computable ordinals by computable well-orderings, index them by the set `WO`,
  and say what an index does not reveal (successor versus limit);
- compute with Kleene's notations by **effective transfinite recursion** (recursion theorem
  plus induction on notations), and prove the Markwald–Kleene theorem;
- move between well-founded trees, their ranks and the Kleene–Brouwer ordering;
- prove Kleene's normal form for Π¹₁ sets, and the Π¹₁-completeness of WF, WO and O;
- prove that Π¹₁ is not Σ¹₁ and Spector's boundedness theorem, and apply boundedness and
  overspill arguments.

**Role in the track.** First course of the higher computability track
(`content/tracks-design.md`). It supplies two of the track's techniques (effective
transfinite recursion; well-founded trees and ranks) and the third (the boundedness
principle). The course on hyperarithmetic sets uses O, `+_O`, the uniform conversion
`prop-constructive-computable`, the normal form, the completeness of O and the boundedness
theorem; descriptive set theory and higher randomness use the normal form, the
Kleene–Brouwer ordering and `prop-pi11-not-sigma11`.

## 2. Prerequisites assumed

- Fundamentals: c.e. sets, ∅′ and its enumeration, SMN (`cor-smn-parameters`), the recursion
  theorem in the form `cor-self-reference`.
- Arithmetic hierarchy: Σ⁰ₙ/Π⁰ₙ classification, Post's theorem (`thm-post`, used in
  `prop-pseudo-wo`), relativized jumps.
- Set theory: ZFC; facts about von Neumann ordinals are admitted with references.

## 3. Results, lesson by lesson

1. **ordinals.** Rigidity (`lem-wo-rigid`), comparison (`thm-wo-comparison`), transfinite
   induction and recursion (`prop-transfinite`), ordinal arithmetic
   (`ex-ordinal-arithmetic`), ω₁ (`prop-omega1`).
2. **computable-well-orderings** (new, 2026-11-12). `def-computable-ordinal`, the index set
   WO and `L_e` (`def-wo`), closure properties and c.e. = computable for linear orders
   (`prop-computable-ordinals-basic`), ω₁ᶜᵏ (`def-omega1ck`), the order of type ω or ω+1
   depending on ∅′ (`prop-wo-not-transparent`). Exercises: ωⁿ and ω^ω computable; Σ⁰₂
   bounds.
3. **kleene-o.** Definition of O (`def-kleene-o`), examples (`ex-notations`), inversion
   (`lem-o-inversion`, new), c.e. initial segments (`prop-kleene-o-basic`), constructive ⇒
   computable uniformly (`prop-constructive-computable`), addition of notations
   (`lem-notation-sum`). Exercise: ε₀ is computable.
4. **markwald** (new, split from kleene-o). Supremum of a c.e. set of notations
   (`lem-notation-sup`), Markwald–Kleene (`thm-markwald`, `cor-constructive-computable`),
   relativization and ω₁ˣ. Exercise: no exact uniform conversion.
5. **well-founded-trees** (new, split from trees-and-pi11). Ranks (`def-tree-rank`), the
   tree of descending sequences (`prop-descending-tree`, new), Kleene–Brouwer
   (`thm-kleene-brouwer`), ranks of computable trees (`prop-rank-computable`, new).
   Exercises: rank ω and KB type ω+1; a computable tree with no computable path.
6. **trees-and-pi11** (retitled "Π¹₁ sets and Kleene's O"). `def-pi11-set`, normal form
   (`thm-pi11-normal-form`), WF and WO complete (`cor-pi11-complete`), O is Π¹₁
   (`prop-o-pi11`, new, with proof), **O is Π¹₁-complete (`thm-o-complete`, new, with
   proof)**.
7. **boundedness** (new). Π¹₁ ≠ Σ¹₁ (`prop-pi11-not-sigma11`, moved here), Spector
   (`thm-boundedness`, moved), `cor-boundedness` (moved), ω₁ˣ for arithmetic X and for O
   (`prop-omega1-relative`, new), an ill-founded computable order without arithmetic
   descending sequence (`prop-pseudo-wo`, new). Exercises `ex-tree-boundedness` (moved,
   now labeled), `ex-o-bounded`.

## 4. Proof techniques

| Technique | Where |
| --- | --- |
| Transfinite induction and recursion | ordinals (`prop-transfinite`); throughout |
| Effective transfinite recursion (recursion theorem + induction on notations or along a well-ordering) | kleene-o (`lem-notation-sum`, named there, quiz on totality), markwald (`thm-markwald`), ε₀ exercise, trees-and-pi11 (`thm-o-complete`, recursion on a tree) |
| Inversion for inductive definitions | kleene-o (`lem-o-inversion`), trees-and-pi11 (`prop-o-pi11`, `thm-o-complete`) |
| Ranks of well-founded trees; linearization by Kleene–Brouwer | well-founded-trees |
| Coding a computation in an order (SMN) | computable-well-orderings (`prop-wo-not-transparent`) |
| Normal forms (collapsing quantifiers, finite-use) | trees-and-pi11 (`thm-pi11-normal-form`) |
| Diagonal argument | boundedness (`prop-pi11-not-sigma11`); exercise on a tree without computable path |
| Boundedness argument | boundedness (`thm-boundedness`, `prop-omega1-relative`, exercises) |
| Overspill | boundedness (`prop-pseudo-wo`) |

## 5. Choices

- **Π¹₁-completeness of O is proved** (it was admitted). Three later courses rely on it
  (hyperarithmetic, descriptive set theory via kleene-theorem, higher randomness). The
  textbook route (Kleene–Brouwer ordering followed by the Markwald–Kleene map, as in
  Monin–Patey) requires showing that an ill-founded order is sent outside O. With sums of
  notations this needs "a +_O b ∈ O ⇒ b ∈ O", whose natural proof needs the index function of the limit clause of
  `+_O` to be injective (two different indices of the same sequence break the step from
  `a + c <_O a + d` to `c <_O d`). The proof chosen builds the notation of each subtree on
  top of the previous element of the chain (`F(n, b, σ)`): increasingness is then
  automatic, and the ill-founded case needs only `lem-o-inversion`. No property of `+_O`
  beyond `lem-notation-sum` is used, so `+_O` was not changed.
- **Splitting into seven lessons.** The design pass added intuition, examples and figures;
  `kleene-o` (3100 words) and `trees-and-pi11` (2600 words, plus the completeness proof)
  exceeded the 45-minute limit. Splits were chosen so that every moved label stays in the
  transitive prerequisites of the lessons that cite it, except Spector's theorem
  (`boundedness`, see open points): computable well-orderings before `kleene-o`, trees
  before `trees-and-pi11`.
- **Π¹₁ ≠ Σ¹₁ placed with boundedness.** The two results are the qualitative and
  quantitative forms of the same fact, and the move keeps `trees-and-pi11` within 45 minutes.
- **`prop-wo-not-transparent`** (formerly an exercise of kleene-o) is promoted: it motivates
  notations and is a clean example of coding ∅′ into an order type.
- **`prop-pseudo-wo`** is added as the arithmetic version of Harrison's theorem: it shows
  the overspill technique with what the course has, and Harrison's theorem itself is proved
  in the hyperarithmetic course.
- **Excluded:** closure of ω₁ᶜᵏ under exponentiation in general (only ωⁿ, ω^ω and ε₀ as
  exercises); the uniqueness of H-sets and Kleene's theorem Δ¹₁ = HYP (next course);
  admissibility and L(ω₁ᶜᵏ) (track exclusion); Σ¹₁ boundedness for classes (hyperarithmetic).
- **Ordinal set theory** is admitted (von Neumann ordinals), as it belongs to set theory.

## 6. Comparison with the literature

- **Monin–Patey**, chapter *Transfinite numbers* (sections *Ordinals*, *Induction and
  transfinite recurrence*, *Effective ordinals*, *Representation of ordinals by trees*,
  *Relativization*) and chapter *Beyond hyperarithmetic* (sections *The Π¹₁ sets and the
  well-orders*, the Kleene–Suslin section with Spector's boundedness lemma, the section on
  pseudo-well-orders). Same order of topics. Differences: our proof of the completeness of
  O is complete (see Choices); our proof that O is Π¹₁ uses closed pairs (X, Y) rather than
  their conditions (1)–(2); boundedness comes here rather than with Kleene–Suslin.
- **Simpson** V.1 (Definition V.1.1 coding of orders, V.1.2 Kleene–Brouwer, Lemma V.1.3,
  normal form Lemma V.1.4, Lemma V.1.8, Theorems V.1.9–V.1.10 WO not Σ¹₁), V.4
  pseudohierarchies, V.6 (Lemma V.6.2 Σ¹₁ bounding), VIII.3 (Definitions VIII.3.1–3, a
  different system O⁺/O of notations; Lemma VIII.3.4 Oˣ not Σ¹₁(X)). Simpson works in
  subsystems; the course works in ZFC.
- **Nies** Section 9.1 (pp. 366–369): Π¹₁ relations, ω₁ᶜᵏ, c.e. indices of well-orders as
  complete set, Exercise 9.1.8 (ω₁^O > ω₁ᶜᵏ), Theorem 9.1.14 (Spector).
- **Dzhafarov–Mummert** Definition 5.8.7, Proposition 5.8.8 (KB), Section 12.1 (ranks,
  Lemma 12.1.6).
- **Sacks, Chong–Yu, Rogers** are not in `external-data`; their section numbers were
  removed (the earlier "Sacks I.5" for the completeness of O could not be checked; Nies
  cites it as "Sacks 2.1.I"). Sacks is kept as a general reference only; Rogers' chapter
  number was removed.

## 7. Pedagogical plan

- ordinals: motivating paragraph on iterating the jump; examples and non-examples of
  well-orderings (`ex-well-orderings`); counterexamples for rigidity (ℤ, ℚ); idea of the
  comparison proof; worked arithmetic examples; figure `order-types`; the downward-closure
  argument named as recurrent.
- computable-well-orderings: examples (ω+1, ω·2, ω², ℚ); why c.e. linear orders are
  computable (quiz); figure `special-last`; why notations are needed.
- kleene-o: examples of notations, two incomparable notations of ω; figure `o-tree`;
  inversion principle; effective transfinite recursion named before `+_O`; quiz on totality.
- markwald: intuition for the supremum lemma and for `g`; existing quizzes.
- well-founded-trees: examples of trees and ranks; figure `kb-order` (post-order); rank vs
  KB type (strict inequality); descending-sequence tree.
- trees-and-pi11: inductive definitions are Π¹₁; intuition for the reduction to O; figure
  `o-completeness`; two quizzes on the reduction.
- boundedness: diagonal argument compared with c.e./co-c.e.; boundedness as yardsticks;
  figure `spector`; why both hypotheses are needed; overspill.

## 8. Sources (checked)

- ordinals: Kunen 2011, Jech 2003 (general); Monin–Patey, *Transfinite numbers*.
- computable-well-orderings: Monin–Patey *Effective ordinals* (c.e. linear orders are
  computable, Lemmas before Theorem Kleene–Markwald); Simpson Def. V.1.1; Nies 9.1.
- kleene-o: Kleene 1938 (JSL 3, 150–155); Monin–Patey (definition of O, example of `+_o`).
- markwald: Markwald, Math. Ann. 127 (1954), 135–149 (checked online); Spector, JSL 20
  (1955), 151–163 (Simpson bibliography); Monin–Patey; Nies Ex. 9.1.8.
- well-founded-trees: Simpson Def. V.1.2, Lemma V.1.3; Dzhafarov–Mummert Def. 5.8.7,
  Prop. 5.8.8, Lemma 12.1.6; Monin–Patey *Representation of ordinals by trees*; Kleene,
  Trans. AMS 79 (1955), 312–340 (Simpson bibliography).
- trees-and-pi11: Kleene 1955 (Trans. AMS 79); Kleene, Amer. J. Math. 77 (1955), 405–428
  (checked online) for the completeness of O; Simpson V.1.4, V.1.8; Monin–Patey
  *The Π¹₁ sets and the well-orders*; Nies 9.1.
- boundedness: Spector 1955; Simpson V.1.9–10, V.4, V.6.2, VIII.3.4; Harrison, Trans. AMS 131
  (1968), 526–543 (Simpson bibliography); Nies Ex. 9.1.8, Thm. 9.1.14; Monin–Patey.

## 9. Recent literature

- Checked Chong–Yu, *Recursion Theory: Computational Aspects of Definability* (de Gruyter,
  2015) by its table of contents only (Π¹₁ sets, hyperarithmetic theory); the text was not
  available, so nothing was taken from it.
- No simpler published proof of the completeness of O was found; the proof given here is a
  standard-style recursion-theorem argument written for this course, and is not attributed
  to a specific source beyond Kleene's theorem.
- Nothing presented as open in the course.

## 10. Open points

- `hyperarithmetic/kleene-theorem` cites `thm-boundedness`, now in `boundedness`; its
  lesson prerequisites should include `computable-ordinals/boundedness`, and its sentence
  "the first exercise of computable-ordinals/trees-and-pi11" should cite
  `:ref{#ex-tree-boundedness}`.
- Text in other courses still says the completeness of O is "admitted"
  (`hyperarithmetic/spector-uniqueness.md`, `hyperarithmetic/sigma11-classes.md`); it can
  cite `thm-o-complete`. `hyperarithmetic/sigma11-classes.md` cites "kleene-o, relativization"
  for ω₁^O > ω₁ᶜᵏ; it can cite `prop-omega1-relative`.
- `ordinals.md` keeps the prerequisite `arithmetic-hierarchy/sigma-pi-sets`, which it does
  not use (an entry point for the course).
- Within the course, forward pointers remain (kleene-o → `thm-o-complete`,
  computable-well-orderings → `cor-pi11-complete`, `thm-boundedness`, markwald →
  `prop-omega1-relative`, well-founded-trees → `ex-tree-boundedness`), all presented as such.
- A full proof that ω₁ᶜᵏ is closed under exponentiation could be an exercise.

## 11. History

- **2026-11-12.** Design and pedagogical revision. Seven lessons instead of three: new
  `computable-well-orderings`, `markwald`, `well-founded-trees`, `boundedness`; kleene-o and
  trees-and-pi11 retitled. The Π¹₁-completeness of O, previously admitted, is proved
  (`thm-o-complete`), with `prop-o-pi11` and the inversion lemma `lem-o-inversion`. New
  results `prop-descending-tree`, `prop-rank-computable`, `prop-omega1-relative` (replacing
  sketches in the relativization paragraph), `prop-pseudo-wo`; the former exercise on
  ω/ω+1 promoted to `prop-wo-not-transparent`. Six figures in
  `scripts/figures/computable-ordinals.py`. Unverifiable section numbers (Sacks I.5, Rogers
  Ch. 11) removed; references checked against Monin–Patey, Simpson, Nies and
  Dzhafarov–Mummert. All labels kept; moved labels listed in the open points.
