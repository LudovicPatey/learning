# Design log: Cuts and extensions

## 1. Objectives

After the course, a student can:
- read a formula with set parameters in a cut through codes in the ambient model, and prove closure properties of coded subsets of cuts by overspill;
- prove that the standard system of a non-standard model is a Scott set, that every countable Scott set is a standard system, and Tennenbaum's theorem;
- prove that semiregular cuts satisfy Σ⁰₁ induction, and characterize them by WKL₀ (Kirby–Paris);
- use the Tarski–Vaught test level by level; prove preservation theorems for cofinal extensions; prove that end extensions give collection; split an extension at the supremum of the small model; and deduce the Friedman–Paris conservation theorem.

**Role in the track.** Course 3 of the track "Models of arithmetic" (`content/tracks-design.md`), after `fragments-of-arithmetic` and `truth-and-provability`. It provides the cut techniques used by the later courses: coded sets and standard systems (recursive saturation, where countable recursively saturated models are determined by their theory and standard system), Scott sets and coded types (end-extensions), semiregular cuts (the indicator method of the course independence), and the splitting of extensions.

## 2. Prerequisites assumed

- First-order logic: completeness, compactness, the Tarski–Vaught test (stated in the course description and lesson 5).
- fragments-of-arithmetic: cuts (`def-cut`), absoluteness (`lem-delta0-absolute`, `cor-sigma1-upward`), `lem-cut-model`, `lem-idelta0-pi1`, the hierarchy (`thm-fo-parsons`, `lem-fo-collection-closure`, `thm-fo-isigma-ipi`, `thm-fo-paris-kirby`, `ex-fo-bsigma-bpi`), `prop-cuts-induction`, `cor-overspill` and underspill (unlabeled exercise, cited by lesson link), Ackermann coding (`def-ack-membership`, `lem-ack-basic`, `thm-delta0-comprehension`), sequences (`def-coded-sequence`, `prop-seq-basic`), `thm-friedman-coded`, `thm-collection-coded`, `fact-exp`, `prop-isigma1-exp`, `fact-pairing`.
- truth-and-provability: `thm-sat-n`, `cor-snowing`, `def-delta0-star`, `lem-variable-bounds` (one exercise of lesson 3).
- second-order-arithmetic: `def-l2`, `def-l2-structure`, `def-rca0`, `def-turing-ideal`; the relativization of `cor-sigma1-ce` (prose of the lesson language-and-models).
- pi01-classes: `thm-dnc2-no-computable`, `thm-pa-completions`, `thm-pa-characterization`.
- Pointers only (lesson links, no label citations): big-five/wkl0 (Scott ideals), induction-conservation/pigeonhole (Hirst's theorem), fragments-of-arithmetic/induction-collection (contraction of quantifiers, strictness of the hierarchy).

## 3. Results, lesson by lesson

1. **standard-system** (45 min). `def-coded-subsets`, `ex-coded-subsets`; absoluteness for bounded L₂ formulas evaluated through codes (`lem-delta00-absolute-cut`); separation lemma (`lem-cut-separation`); Δ⁰₁ comprehension in (I, Cod(M/I)) (`cor-cod-delta1-ca`); SSy(M) is a Turing ideal (`thm-ssy-turing-ideal`); exercise: SSy is preserved by end extensions (`ex-ssy-end-extension`).
2. **weak-konig-cuts** (40 min). Binary strings in IΔ₀ + exp (`def-strings-model`, `lem-strings-model`); trees in cuts (`def-tree-cut`); Scott's theorem on WKL in proper exponential cuts (`thm-scott-wkl-cut`); Scott sets (`def-scott-set`); SSy(M) is a Scott set (`cor-ssy-scott-set`); exercises: exponential cuts closed under the operations (`ex-exp-cut-closed`), sums of codes of disjoint sets (`ex-subset-sum`).
3. **scott-tennenbaum** (40 min). Every countable Scott set is SSy of a model of PA (`thm-scott-converse`); the Scott set problem (Knight–Nadel, Gitman); Tennenbaum's theorem for addition in models of IΔ₀ + exp (`thm-tennenbaum`); exercises: the Σ*ₙ theory of M is in SSy(M), and SSy of a non-standard model of true arithmetic contains every arithmetic set (`ex-ssy-truth`); second proof that SSy is a Scott set via the separation lemma and PA degrees (`ex-scott-separation`).
4. **semiregular-cuts** (50 min). `def-semiregular`, `ex-not-semiregular`; semiregular cuts are closed under the operations (`lem-semireg-closed`); (I, Cod(M/I)) ⊨ IΣ⁰₁ (`thm-semireg-isigma1`); Kirby–Paris characterization by WKL₀ (`thm-kirby-paris-wkl`); regular cuts (`def-regular-cut`), regular ⇒ semiregular (`prop-regular-semireg`); the characterization by BΣ⁰₂ admitted.
5. **cofinal-extensions** (50 min). `def-n-elementary`, `ex-n-elementary`; hierarchical Tarski–Vaught test (`lem-tarski-vaught-n`); cofinal extensions and suprema (`def-cofinal-ext`); BΣₙ₊₁ + Σₙ-elementary cofinal ⇒ Σₙ₊₂-elementary (`thm-cofinal-preservation`, `cor-cofinal-preservation`); Friedman's strong collection (`thm-strong-collection`).
6. **collection-end-extensions** (45 min). Paris–Kirby: end extensions give collection (`thm-end-ext-collection`); converse admitted (`fact-end-ext-converse`); splitting theorem (`thm-splitting`); cofinal Σₙ₊₁-elementary extension satisfying BΣₙ₊₁ (`thm-cofinal-bsigma`); Friedman–Paris conservation (`thm-friedman-paris-conservation`); exercises `ex-sup-elementary`, `ex-conservation-sharp`.

## 4. Proof techniques

- **Evaluating through codes** (lesson 1, `lem-delta00-absolute-cut`): a bounded property of a cut and its coded subsets is a bounded property of the ambient model. Used in every later cut argument.
- **Overspill to choose a bound just above the cut** (lessons 1–2): the separation lemma, Scott's theorem. The argument "go up to the model, use its induction, come back to the cut" is named the non-standard method in lesson 2.
- **Least witnesses below an element above the cut** (lesson 4): semiregularity bounds the witnesses that lie in the cut, which turns Σ⁰₁ formulas into bounded ones.
- **Chains of complete theories in a Scott set** (lesson 3), with definable Skolem functions in PA.
- **Coding witness functions to transfer statements logically** (lesson 5): in a cofinal extension, the transferred formula must have its complexity logically, since nothing is known in the big model.
- **Underspill** (lesson 6), **Tarski–Vaught test level by level** (lessons 5–6), **splitting at the supremum** (lesson 6).

## 5. Choices

- **Scope as in tracks-design, with three adjustments.** (1) The arithmetized completeness theorem and MacDowell–Specker are excluded (next course), so the converse of Scott's WKL theorem for models of WKL₀ (Wong 4.13) and the construction of end extensions from collection (HP IV.1.53) are stated with pointers. (2) Scott's converse for countable Scott sets is proved instead, with a direct construction that needs no arithmetized completeness. (3) The Paris–Kirby unprovability of the totality of fast-growing functions in IΣ₁ (Wong 5.6) is left to the course independence, where indicators are treated; lesson 4 points to it.
- **Separation lemma as the central tool of lesson 1.** It gives Δ⁰₁ comprehension in any multiplicative proper cut (used for the Kirby–Paris theorem), the Turing ideal property of SSy, Tennenbaum's theorem, and an alternative proof that SSy is a Scott set. It replaces HP's Rosser-device proof of Theorem IV.2.14.
- **Tennenbaum's theorem for addition in IΔ₀ + exp**, proved through the standard system; multiplication is mentioned with a reference (it needs prime coding).
- **Strings coded with a leading digit** (Wong's coding) rather than the sequences of `def-coded-sequence`, because their size is 2^length, which matches exponential cuts.
- **Semiregular cuts defined through coded sequences** (`def-coded-sequence`), with Wong's definition. The (⇐) direction of the Kirby–Paris theorem, not proved by Wong, is proved by a Σ⁰₁ induction on the codes d_y of initial pieces of the preimages, which avoids relativizing the whole hierarchy to set parameters.
- **Regular cuts** defined as HP's 1-Ramsey cuts (pigeonhole for coded colorings); only regular ⇒ semiregular is proved; the characterization by BΣ⁰₂ and the existence of semiregular non-regular cuts are admitted.
- **Cofinal preservation theorem** (`thm-cofinal-preservation`) assembled from Wong's Further exercises (b)–(d) to Lecture 6, with the observation that the transferred formulas must be logically Πₙ (the difficulty Wong flags); HP's Theorem IV.1.24 obtains Σ₀-elementarity from MRDP, which is avoided by assuming it.
- **Splitting theorem through strong collection** (Enayat–Mohsenipour proof, as in Wong), with Friedman's strong collection proved in lesson 5 by a direct induction instead of Wong's least-number argument.
- **Excluded:** arithmetized completeness, MacDowell–Specker, recursive saturation (later courses); the Gaifman splitting theorem (needs MRDP in IΔ₀ + exp, admitted in Wong); strong cuts and ACA₀; k-extendable cuts and arithmetic with a top (HP IV.2(c)); Wong's Theorem 6.8 (theories of k-elementary cuts); Tennenbaum's theorem for multiplication.

## 6. Comparison with the literature

| Source | Content | Here |
| --- | --- | --- |
| Wong 3 | cuts, Cod(M/I), coding of strings, Thm 3.5 stated | lessons 1–2 |
| Wong 4 | proof of Thm 3.5, WKL₀, ACT, Scott–Tanaka | lesson 2 (Thm 3.5); ACT excluded |
| Wong 5 | semiregular cuts, Lemma 5.8, Thm 5.9 (one direction proved), Thm 5.6 | lesson 4 (both directions of 5.9); 5.6 excluded |
| Wong 6 | Thms 6.1, 6.3, 6.4, 6.6, Tarski–Vaught, splitting, exercises on cofinal extensions | lessons 5–6 |
| HP IV.1(c) | overspill, k-elementarity (1.17–1.19), 1.22, 1.24 | lessons 5–6 |
| HP IV.1(e)–(f) | 1.53 (end extensions ⇔ BΣ), 1.59–1.67 (conservation by definable ultrapower) | lesson 6 (1.53 stated; conservation proved by splitting instead) |
| HP IV.2(b)–(c) | SS_I(M), Thm 2.14, semiregular (2.15–2.16), regular (2.19–2.21) | lessons 1, 4 |

Kaye's *Models of Peano Arithmetic* (not available locally) treats standard systems, Scott sets and Tennenbaum's theorem; it is cited without section numbers.

## 7. Pedagogical plan

1. standard-system: intuition (what a model knows about a cut); examples of coded subsets (I itself is coded but not definable); figure of the separation lemma; quizzes on the choice of k and on multiplicative closure.
2. weak-konig-cuts: example of string codes (011 ↦ 14); idea of the proof before it ("go up and come back"); figure of the tree and the branch; quizzes on where exponential closure is used and on why θ requires all prefixes.
3. scott-tennenbaum: idea of the chain of theories; quiz on why the coded sets stay in 𝒳; Tennenbaum with the explicit algorithm; quiz on non-standardness.
4. semiregular-cuts: analogy with regular cardinals; figure of a coded function; example of a non-semiregular cut (n·c); quiz on least witnesses.
5. cofinal-extensions: picture of end vs cofinal; example ℕ ⊀₁ M for M ⊨ ¬Con(PA); figure of the coded witness function; quizzes on logical complexity and on strong collection.
6. collection-end-extensions: figures of underspill and of the splitting; quizzes on IΣₙ in K, on M ≠ K, on strong collection, and on why Πₙ₊₂ is sharp; exercise proving sharpness.

## 8. Sources (checked 2026-11-12 against the text files)

- Lesson 1: Wong Lecture 3 (definition of Cod(M/I)); HP Definition IV.2.13, Theorem IV.2.14; HP remarks to Chapter IV, item (a) (Scott 62, Friedman 73).
- Lesson 2: Wong Lectures 3–4 (Theorem 3.5, Lemma 3.7, proof in Lecture 4).
- Lesson 3: Scott 1962 (bibliography of Wong and HP); HP remarks to Chapter IV (a); Knight–Nadel JSL 47 (1982) 833–840 (Wong's bibliography); Gitman JSL 73 (2008) 845–860 (checked online); Tennenbaum, Notices AMS 6 (1959) 270 (HP bibliography).
- Lesson 4: Wong Lecture 5 (definition, Example 5.7, Lemma 5.8, Theorem 5.9); HP IV.2.15–2.16, 2.19–2.21; Kirby–Paris 1977 (LNM 619, 211–226, Wong's bibliography).
- Lesson 5: Wong Lecture 6 (Tarski–Vaught test, Theorem 6.4, Remark 6.5, Further exercises (b)–(e)); HP IV.1.19, 1.24, 1.25; Gaifman 1972 (Wong's bibliography).
- Lesson 6: Wong Lecture 6 (Theorems 6.1, 6.3, 6.6, splitting theorem, Further comments); HP IV.1.22, 1.53, 1.59, 1.61; Paris–Kirby 1978; Paris 1980 (LNM 834); Kaye JSL 56 (1991); Enayat–Mohsenipour AML 47 (2008) (all from Wong's bibliography); Sun 2025 (checked online).

## 9. Recent literature

Web search, 2026-11-12:
- M. Sun, *The Kaufmann–Clote question on end extensions of models of arithmetic and the weak regularity principle*, JSL 2025 (arXiv:2409.03527): every countable model of BΣₙ₊₂ has a proper Σₙ₊₂-elementary end extension satisfying BΣₙ₊₁, answering Clote's question (Wong's Question 6.11). Added to lesson 6.
- V. Gitman, *Scott's problem for proper Scott sets*, JSL 73 (2008): under PFA, every proper Scott set is a standard system. Added to lesson 3. No ZFC solution of the Scott set problem beyond ℵ₁ was found.

## 10. Open points

- Lessons 4 and 5 are at 50 minutes.
- The characterization of regular cuts by BΣ⁰₂ and the existence of semiregular non-regular cuts are admitted (HP IV.2.21; Kirby–Paris 1977).
- `fact-end-ext-converse` is stated from HP Theorem IV.1.53 (1); the text file of HP is partly garbled at that place, and the hypothesis n ≥ 1 was read from the proof (1.56–1.57). To be checked against the printed book.
- Underspill is an unlabeled exercise of fragments-of-arithmetic/definable-cuts; a label there would allow a proper citation.
- Kaye's book is cited without chapter numbers.

## 11. History

- **2026-11-12.** Course created: 6 lessons (standard-system, weak-konig-cuts, scott-tennenbaum, semiregular-cuts, cofinal-extensions, collection-end-extensions), figure generator `scripts/figures/cuts-and-extensions.py`.
