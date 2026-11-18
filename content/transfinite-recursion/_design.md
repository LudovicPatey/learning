# Design log: Arithmetical transfinite recursion

This file is the memory of the course (see "Designing tracks and courses" in
`AGENTS.md`). It is not rendered.

## 1. Objectives

After the course, a student can:

- work with countable well-orderings in second-order arithmetic: the Kleene–Brouwer
  ordering, arithmetic transfinite induction, uniqueness of hierarchies and of comparison
  maps, the comparison of two well-orderings in $\mathsf{ATR}_0$;
- prove that well-foundedness is not $\Sigma^1_1$ in $\mathsf{ACA}_0$, and use the method
  of pseudohierarchies;
- prove the main equivalents of $\mathsf{ATR}_0$ with complete proofs: $\Sigma^1_1$
  separation, unique paths, the perfect set theorem for closed sets, comparability of
  well-orderings, open and clopen determinacy.

**Role in the track.** Last core course of the reverse mathematics track, added on
2026-11-18 (`content/tracks-design.md`). The Big Five course surveys $\mathsf{ATR}_0$ and
$\Pi^1_1\text{-}\mathsf{CA}_0$ in one lesson, with the equivalents admitted; Simpson gives
them two chapters (V and VI) and Dzhafarov–Mummert a section (12.1, 12.3). The higher
computability track gives the computability-theoretic side (hyperarithmetic sets,
pseudo-well-orderings, $\mathrm{HYP} \not\models \mathsf{ATR}_0$); this course gives the
proof-theoretic side.

## 2. Prerequisites assumed

- **big-five:** `def-atr0`, the Kleene normal form (`fact-kleene-normal-form`, admitted
  there), `thm-pi11-trees`, `ex-wo-descending`, `ex-wo-sum`, `ex-hierarchy-ill-founded`,
  `thm-aca-equivalents`, König's lemma in ACA₀ (`thm-konig-aca`), `thm-wkl-separation`.
- **computable-ordinals:** the Kleene–Brouwer ordering (`thm-kleene-brouwer`), the
  boundedness theorem (mentioned).
- **hyperarithmetic:** pseudo-well-orderings and `prop-hyp-not-atr0` (mentioned, not used
  in proofs).
- Admitted in the course: the uniform normal form (`fact-uniform-normal-form`, Simpson
  V.1.4 and V.1.7), Kleene's theorem that quantification over HYP is Π¹₁ (a remark), the
  results on Π¹₁-CA₀ and stronger determinacy (survey).

## 3. Results, lesson by lesson

1. **well-orderings** — `def-kb-order`, figure `kb-order`, `prop-kb-aca` (Simpson V.1.3),
   `lem-ati`, `prop-hierarchy-unique`, `def-comparison-maps`, `lem-comparison-unique`,
   `thm-atr-comparability` (proof by the least unused element). Featured:
   `ex-wo-not-initial` (no embedding below the identity; trichotomy). Further: KB order on
   small trees, ω + 1 versus 1 + ω, sums and comparisons.
2. **pseudohierarchies** — `fact-uniform-normal-form`, `thm-wo-not-sigma11` (diagonal
   argument), `lem-pseudohierarchies`, the Cantor–Bendixson derivative,
   `thm-perfect-set-atr` for trees in ℕ^{<ℕ} (two cases: listing the paths, or a perfect
   subtree along a descending sequence), figure `perfect-subtree`. Featured:
   `ex-derivative-example`. Further: a pseudohierarchy of jumps, perfect trees are
   uncountable, a tree of derivative length ω + 1.
3. **sigma11-separation** — `def-sigma11-separation`, `lem-sum-wo`, products of trees,
   `thm-atr-sigma11-separation`. Featured: Δ¹₁ comprehension (`ex-delta11-ca`). Further:
   Σ⁰₁ separation and WKL, products of trees, the rank hierarchy.
4. **unique-paths** — `lem-unique-normal-form` (minimal Skolem functions),
   `thm-unique-paths` (ATR₀ ⇔ perfect set theorem ⇔ unique paths ⇔ the arithmetic scheme).
   Featured: `ex-unique-paths-aca`. Further: two paths in a perfect tree, comparison with
   Π¹₁-CA₀.
5. **comparability** — `lem-cwo-aca`, `lem-cwo-embedding`, `lem-sigma11-bounding`,
   `lem-double-descent`, `thm-cwo-atr` (Friedman). Featured: Σ¹₁ bounding ⇔ ATR₀
   (`ex-bounding-atr`). Further: orders with finite initial segments, a double descent
   ordering.
6. **open-determinacy** — games and strategies, `def-determinacy`,
   `thm-open-determinacy-atr` (ranks of winning positions; pseudohierarchy for player 1),
   descent games `lem-descent-games`, `thm-clopen-determinacy-atr` (Steel). Featured:
   clopen determinacy implies ACA₀ (`ex-clopen-aca`). Further: descent games and
   comparisons, the levels of a game won in two rounds.

## 4. Proof techniques

- **Arithmetic transfinite induction** (every lesson), and its limits: only for arithmetic
  formulas.
- **Ranking trees into well-orderings** by transfinite recursion: the rank hierarchy of
  lesson 3, the derivative of lesson 2, the winning positions of lesson 6.
- **Diagonalization** with codes (well-foundedness is not Σ¹₁).
- **Pseudohierarchies** (lessons 2 and 6): a recursion that never ends along a
  well-ordering is run along an ill-founded order, and a descending sequence gives the
  other alternative.
- **Unique witnesses** by minimal Skolem functions (lesson 4).
- **Uniformization by padding** (lesson 5): orders padded to a common type, so that one
  comparison map gives all comparisons.
- **Games that start with the choice of an instance** (lesson 6), which turn determinacy
  into comprehension.

## 5. Included, excluded, and why

- **Included:** the equivalents of ATR₀ that are proved in both Simpson and
  Dzhafarov–Mummert, and that use the main techniques: comparability, Σ¹₁ separation,
  perfect sets, determinacy; unique paths as the step to the perfect set theorem.
- **Excluded:** Borel sets and Lusin's theorem (Simpson V.3), the Ulm theory of abelian
  p-groups (V.7), the open Ramsey theorem (V.9), the Σ¹₁ axiom of choice (V.8.3 and
  Dzhafarov–Mummert 12.1, whose proof is long), β-models (VII). Each could be a specialized
  course; the course mentions them in the notes.
- **Π¹₁-CA₀** is treated only in surveys (perfect kernels, Σ⁰₁ ∧ Π⁰₁ determinacy): its
  main equivalent proof (Cantor–Bendixson) is a natural next exercise and a possible
  future lesson.

## 6. Comparison with the literature, and choices of proofs

- Simpson, Chapter V, is the main source; Dzhafarov–Mummert, Sections 5.8, 12.1, 12.3,
  the second.
- `thm-atr-comparability`: Simpson's proof of Lemma V.2.9 is two lines; the course gives a
  complete proof by the least unused element, with the three properties of the sets $R_j$.
- `thm-atr-sigma11-separation`, forward direction: Simpson goes through Lusin's theorem
  (Borel codes), Dzhafarov–Mummert through initial segments of $\mathcal O$ and double
  descent trees (their Lemma 12.1.7). The course uses products of trees and a single rank
  hierarchy along the sum of their Kleene–Brouwer orderings: shorter, and it uses only the
  tools of lesson 1.
- `thm-perfect-set-atr`: Simpson proves it for analytic codes (V.4.3); the course does the
  case of trees, in ℕ^{<ℕ} directly, which removes the need for the transfer from Baire
  space to Cantor space (Simpson V.5.6) in the reversal.
- `thm-unique-paths`: Simpson proves ATR₀ ⇒ statement 4 through the Borel domain theorem;
  the course goes through the perfect set theorem (as in Simpson's own reversal V.5.5,
  4 ⇒ 1), which avoids Borel sets entirely.
- `thm-cwo-atr`: Simpson V.6.8. Two points were made explicit: the class to which the
  bounding principle is applied for $U$ (orders $X * Y_n$ with $X_n$ ill-founded, so that
  they are well-orderings), and the induction on $n$ showing that the comparison map of the
  two sums matches the summands, which needs only one isomorphism $B_n \cong C$ at a time.
- `thm-clopen-determinacy-atr`: Simpson V.8.7, with his proof through Σ¹₁ separation.

## 7. Figures

Generated by `scripts/figures/transfinite-recursion.py`: `kb-order` (well-orderings),
`perfect-subtree` (pseudohierarchies).

## 8. Sources

- S. G. Simpson, *Subsystems of Second Order Arithmetic*, Chapters V and VI.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics*, Sections 5.8, 12.1, 12.3.
- Friedman (1975, 1976), Steel (1976), Friedman–Hirst (1990), Harrison (1968), Gale–Stewart
  (1953), Tanaka (1990), Friedman (1971).

## 9. History

- 2026-11-18: course created with six lessons. A first draft of an exercise on double
  descent orderings claimed that $n * \omega^*$ is finite; it is infinite, and the exercise
  was rewritten.
