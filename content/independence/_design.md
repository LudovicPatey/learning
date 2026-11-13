# Design log: Indicators and independence

## 1. Objectives

After the course, a student can:
- prove an unprovability result by the method of indicators: define a largeness notion, build a cut satisfying the theory inside every interval of non-standard largeness, and apply the main theorem on indicators;
- build semiregular cuts by a construction by finite extensions in intervals $[a, F_\nu(a)]$, and deduce that the functions provably total in IΣ₁ are primitive recursive;
- prove the Paris–Harrington principle from Ramsey's theorem and König's lemma, and its unprovability in PA through diagonal indiscernibles;
- compute with α-large sets and relate them to fast-growing hierarchies;
- work with initial segments with a top and their coded expansions.

**Role in the track.** Course 6 (last) of the track "Models of arithmetic" (`content/tracks-design.md`). It uses the cuts of `cuts-and-extensions` (semiregular cuts) and the truth definitions and provably total functions of `truth-and-provability`, and completes the admitted direction of the Parsons–Mints–Takeuti theorem stated there (`thm-pmt`). It is independent of the parallel courses `end-extensions` and `recursive-saturation` (recursive saturation of structures with a top is mentioned in prose only).

## 2. Prerequisites assumed

- First-order logic: compactness, Löwenheim–Skolem; Gödel's theorems only in remarks.
- fragments-of-arithmetic: `def-cut`, `lem-cut-model`, `lem-delta0-absolute`, `cor-sigma1-upward`, `prop-idelta0-basic`, `fact-pairing`, `fact-exp`, `thm-fo-isigma-ipi`, `lem-fo-collection-closure`, `thm-fo-parsons`, `prop-fo-least-number`, `cor-overspill`, `def-ack-membership`, `def-coded-sequence`, `prop-seq-basic`, the pigeonhole exercise of `coding` (unlabeled, cited by lesson link).
- truth-and-provability: `def-provably-total`, `thm-pr-provably-total`, `thm-pmt` and `prop-ack-computations` (lesson `ackermann-isigma`, cited for the formalization by finite computations), `def-delta0-star`, `lem-sat-tables`, `cor-snowing`.
- cuts-and-extensions: `def-semiregular`, `thm-semireg-isigma1` (lesson `semiregular-cuts`), `def-regular-cut` (lesson `wkl-regular-cuts`).
- models-of-computation / arithmetic-hierarchy: `prop-pr-bounded-mu`, `cor-pr-bounded-quantifiers`, `lem-bounded-computable`, `thm-ack-majorization`.
- ramsey-theorem: `thm-rt3-aca`, `prop-rt-basic`; big-five: `thm-konig-aca`; induction-conservation: `thm-aca0-pa`.
- computable-ordinals/ordinals: ordinal arithmetic (lesson link). Cantor normal form is recalled.

## 3. Results, lesson by lesson

Durations are words of the body (without SVG lines) divided by 55, rounded to a multiple of 5.

1. **fast-growing** (30 min, 1700 words). `def-fgh` ($F_0(x) = x+1$, $F_{k+1}(x) = F_k^{(x)}(x+1)$), `ex-fgh-values`; formalization `fact-fgh-formal` (admitted in its routine details, after `prop-ack-computations`), `lem-fgh-isigma1` (values increase, iterates are coded, totality for standard $k$); `lem-fgh-monotone` (growth in $\nat$, moved here from lesson 3). Exercise: IΣ₂ proves the totality of all $F_k$.
2. **catching-cuts** (25 min, 1360 words; new, split from lesson 1). `thm-kirby-paris-cut`: a countable $M \models$ IΣ₁ with $a \geq 1$ and $\nu$ non-standard has a semiregular cut containing $a$ and not $F_\nu(a)$; remark that $\nu$ standard is impossible. Figure `catching` (regenerated).
3. **indicators** (45 min, 2440 words). `def-indicator` (normalization $x \leq y \wedge c \leq y$); `thm-indicator-main`; `prop-indicator-isigma1`; `cor-isigma1-fgh` (Kirby–Paris); `thm-isigma1-envelope` (proves the converse of `thm-pmt`); `cor-pr-fgh-bound`.
4. **paris-harrington** (35 min, 1870 words). `def-relatively-large`, `ex-relatively-large`; `thm-ph-true` (ACA₀ ⊢ PH$_n$, hence PA ⊢ PH$_n$); new exercise on $[a, b] \to_* (1)^1_1$; notes with recent work on RT²₂ and α-largeness.
5. **regressive-colorings** (40 min, 2200 words; new, from the second half of lesson 4 and the first section of the old diagonal-indiscernibles). `def-regressive`; `lem-ph-regressive`; the coloring $f_R$ and `lem-diag-from-regressive`; formalization in IΣ₁; exercise: min-homogeneity cannot be homogeneity.
6. **diagonal-indiscernibles** (35 min, 2020 words). `def-diagonal-indiscernibles`, `ex-diagonal-indiscernibles` (with an example and a non-example); `lem-diag-growth`; `thm-indiscernible-cut`. Figure `indiscernible` (regenerated: $b$ replaced by $h_\nu$).
7. **ph-unprovable** (35 min, 2030 words). `def-ph-indicator` (with the conjunct $x \leq y$); `thm-ph-indicator`; `cor-ph-unprovable`; `cor-ph-envelope`.
8. **alpha-large** (40 min, 2320 words). `def-fundamental-sequence`; `def-alpha-large`, `ex-alpha-large`; `lem-large-sum`; `thm-large-fgh`; `cor-omega-omega-large`; `thm-schwichtenberg-wainer` (admitted); Ketonen–Solovay stated. Figure `omega-large`.
9. **arithmetic-with-top** (40 min, 2330 words). `def-coded-expansion`, `ex-coded-expansion`; `prop-top-truth`; `thm-top-segment` (Paris, admitted); `def-ramsey-cut`; `thm-ramsey-cuts` and `thm-paris-bsigma-indicator` (admitted).

## 4. Proof techniques

- **Cuts as models / the method of indicators** (lessons 2–3, 7): unprovability from the construction of a cut satisfying the theory and not closed under a function; envelopes from overspill on the degree of largeness.
- **Construction by finite extensions** (lesson 2): nested intervals, one requirement per stage, requirements listed with repetitions (countability of the model).
- **Lowering an index along a non-standard element** (lesson 2): the index $\nu - k$ stays non-standard, which replaces a new overspill at each stage.
- **Compactness via König's lemma** (lesson 4).
- **Counting / pigeonhole in the model** (lessons 2, 5): with non-standard parameters.
- **Moving coordinates** and **translation** of an interval to strengthen relative largeness (lesson 5).
- **Truth reduction by indiscernibles** (lesson 6): unbounded quantifiers of the cut become bounded by indiscernibles.
- **A truth definition to handle all standard formulas at once** (lesson 7): a satisfaction table with a non-standard number of formulas.
- **Running a definition** (lesson 8): decomposition of large sets.
- **Bounding quantifiers by the top** (lesson 9).

## 5. Choices

- **Hierarchy.** HP's variant $F_{k+1}(x) = F_k^{(x)}(x+1)$ instead of Wong's $F_k^{(x+1)}(x)$, so that $F_k(x)$ is exactly the least end of an $\omega^k$-large interval (lesson 8).
- **Kirby–Paris construction with a lowering index.** Wong uses overspill at each stage and the monotonicity of the hierarchy in its index inside the model; the course keeps $s_k = F_{\nu-k}(r_k)$ exactly, which needs no monotonicity in $M$ (that monotonicity raises a $\Pi_2$-induction issue in IΣ₁). Pieces are chosen with left end $> r_k$, so that the left ends increase strictly and the supremum is a cut (Wong's version can repeat $r_k$).
- **Indicator as a three-place Σ₁ formula** $\iota(x, y, c)$ ("$[x, y]$ is $c$-large") rather than HP's function $Y(x, y)$: a maximum would not be Σ₁. The normalization $x \leq y \wedge c \leq y$: $c \leq y$ makes $x$ non-standard in the envelope argument, and $x \leq y$ is needed there to apply the definition, which only concerns pairs $a \leq b$ (added 2026-11-13). Only the direction "non-standard largeness ⇒ cut" is used by the main theorem; the converse is proved for each concrete indicator.
- **PMT converse proved** (it was admitted in truth-and-provability): bound by $F_n + n$ and bounded minimization, rather than HP's provable equivalence with a primitive recursive derivation.
- **Paris–Harrington through regressive colorings and diagonal indiscernibles** (Kanamori–McAloon), not through HP's Paris sequences and restrainable cuts, nor through consistency statements: it is the shortest complete route to a cut satisfying PA. The reduction PH ⇒ min-homogeneity (lemma `lem-ph-regressive`), the growth lemma with $\lfloor\sqrt{y_2 - y_1}\rfloor$ (quantifier-free, so it fits the Δ*₀ setting of the satisfaction tables) and the packing of parameters into one variable are written for this course.
- **Indicator for PA with all arities up to $c$**, to avoid lowering the arity, which costs relative largeness.
- **Truth of PH in ACA₀** for each fixed arity, with conservation over PA (Friedman), citing `ramsey-theorem` and `big-five`; HP's sharper level-by-level provability (II.1.9) is stated.
- **Admitted:** the routine details of the formalization of $F_k$; Paris's refinement PH$_{u}$ ↔ Con(IΣ$_u$ + Tr(Π₁)); the Schwichtenberg–Wainer and Ketonen–Solovay theorems; Paris's theorem on models of TA′; $k$-Ramsey/extendable/restrainable cuts and the indicators for BΣₖ₊₁.
- **Excluded:** Paris sequences (described in prose), the PH ↔ consistency proofs (HP II.2), transfinite induction in fragments (HP II.3(b)), Ajtai's completeness theorem and the parity lower bound (Wong 13), recursive saturation of structures with a top (parallel course). The Kanamori–McAloon equivalence is used in one direction only.

## 6. Comparison with the literature

| Source | Content | Here |
| --- | --- | --- |
| Wong 5 | Grzegorczyk-type hierarchy, Thm 5.6, indicators (Further exercises) | lessons 1–3 |
| Wong 13 | arithmetic with a top, Prop 13.1, Ajtai, Thm 13.11 | lesson 9 (Ajtai excluded) |
| HP II.1 | Ramsey theorems and fragments, PH | lesson 4 |
| HP II.2 | PH and consistency | lesson 7 (stated) |
| HP II.3 | ordinals, α-large sets, Schwichtenberg–Wainer hierarchy | lesson 8 |
| HP IV.2 | TA′, short cuts, Ramsey/extendable/restrainable cuts | lesson 9 (stated) |
| HP IV.3 | envelopes, indicators, Paris sequences | lessons 3, 7 (different construction) |
| Kanamori–McAloon 1987 | regressive Ramsey, diagonal indiscernibles | lessons 5–7 |

Kaye's *Models of Peano Arithmetic* (Chapter 14 treats the Paris–Harrington theorem) was not available and is not cited.

## 7. Pedagogical plan

1. Values of $F_1, F_2, F_3$; quiz on $\Pi_1$ versus $\Pi_2$ induction.
2. Figure of nested intervals (each row magnifies the chosen piece); quizzes on repetitions and on the non-standard index; remark: no cut satisfying IΣ₁ between $a$ and $F_k(a)$ for standard $k$.
3. Quizzes on minimality and on non-standardness of $x$; exercise on monotone indicators.
4. The coloring of points showing that relative largeness forces exponential intervals; quiz on the role of the infinite homogeneous set; exercise on moving the left endpoint.
5. Intuition for moving coordinates; quizzes on regressiveness, on the least coordinate and on the shift $x + 1$; exercise: min-homogeneity cannot be homogeneity.
6. Examples and a non-example of diagonal indiscernibility (parity, divisibility); figure; quiz on the choice of tuples in the truth reduction.
7. Quizzes on the satisfaction table and on the parameters.
8. Examples $n$-large, ω-large, ω²-large ($[3, 39)$, matching $F_2(3) = 39$); figure; quizzes on normal form and on shortest segments; exercises computing $L_\alpha$.
9. Quiz on bounded translation; exercise: no definable proper cut in $[0, a]$.

## 8. Sources (checked 2026-11-13 against the text files and online)

- Lessons 1–2: Wong Lecture 5 (definition, Thm 5.6 and its proof); HP II.3.22 (hierarchy), II.3.24–3.29 (derivations); Kirby–Paris 1977.
- Lesson 3: HP IV.3.1–3.10 (Definition 3.9, Theorem 3.10 (i)–(iv), Lemma 3.4, Corollary 3.7, envelope Definition 3.3); Wong Lecture 5 Further exercises; Parsons 1970, Mints 1971; Bovykin 2009 (page range not verified, removed).
- Lesson 4: HP II.1.9, 1.10, II.2.2–2.3; Simpson Lemma III.7.4, Theorem III.7.6; McAloon 1985 and Dzhafarov–Mummert Theorem 8.1.6 (∀n RTⁿ ↔ ACA′₀, checked in the text file); Patey–Yokoyama 2018, Kołodziejczyk–Yokoyama 2020 (checked online), arXiv preprints 2005.06854, 2402.11616, 2404.18974, 2602.08778 (abstracts checked on arXiv); Bovykin–Weiermann 2017 (bibliographic data from citing papers).
- Lesson 5: Kanamori–McAloon 1987, APAL 33, 23–41 (checked online).
- Lesson 6: Paris–Harrington 1977; Kanamori–McAloon 1987; HP II.2(d), IV.3.17, 3.23.
- Lesson 7: HP IV.3.20–3.24; HP II.2.1–2.3 (consistency statements).
- Lesson 8: HP II.3.12, 3.19–3.22, 3.30, 3.32, 3.34, 3.36–3.37; HP IV.3.5, 3.8; Ketonen–Solovay 1981, Annals 113, 267–314 (checked online); Schwichtenberg 1971, Wainer 1970 (from memory).
- Lesson 9: Wong Lecture 13 (Prop 13.1, Further exercises, Thm 13.11); HP IV.2.1–2.22 (Theorem 2.2, Corollary 2.3, Definitions 2.10, 2.15, 2.17, 2.19, Theorems 2.16, 2.21, 2.22 checked); Paris 1980 (LNM 834, 312–337, checked online), Paris 1981; Cégielski–McAloon–Wilmers 1982.

## 9. Recent literature (web search, 2026-11-13)

The first-order strength of Ramsey's theorem for pairs is the main recent application of the ideas of this course (α-largeness of Ketonen–Solovay as a measure of finite combinatorial strength, cuts built in large intervals):
- Patey and Yokoyama, *The proof-theoretic strength of Ramsey's theorem for pairs and two colors*, Adv. Math. 330 (2018), 1034–1070: RCA₀ + RT²₂ is ∀Π⁰₃-conservative over RCA₀, through α-large homogeneous sets.
- Kołodziejczyk and Yokoyama, *Some upper bounds on ordinal-valued Ramsey numbers for colourings of pairs*, Selecta Math. 26 (2020), 56: $\omega^{300n}$-large sets suffice for $\omega^n$-large homogeneous sets of 2-colorings of pairs.
- Kołodziejczyk, Wong and Yokoyama, *Ramsey's theorem for pairs, collection, and proof size*, arXiv:2005.06854 (journal publication not verified): polynomial proof translation.
- Le Houérou, Levy Patey and Yokoyama, arXiv:2404.18974 (∀Π⁰₄-conservation of WKL₀ + RT²₂ over RCA₀ + BΣ⁰₂) and arXiv:2402.11616 (Π¹₁-conservation over RCA₀ + BΣ⁰₂ + WF(ε₀)).
- Le Houérou and Patey, arXiv:2602.08778 (2026): ω^{nk+3}-largeness suffices for k-colorings of pairs, tight up to an additive constant; and arXiv:2602.11906 (polytime translation for ∀Σ⁰₃ consequences of RT²₂; not cited in the lessons).
- Bovykin and Weiermann, APAL 168 (2017), 1700–1709 (densities).
- Open: whether RT²₂ is Π¹₁-conservative over RCA₀ + BΣ⁰₂.

These are cited in the notes of lesson 4 (paris-harrington), with a pointer from lesson 8. No recent work was found that changes the classical statements of the course. A future specialized course could treat the first-order part of RT²₂ with these tools.

## 10. Open points

- The text file of HP is garbled in several formulas (II.2.2, II.3.36 comment, IV.3.20); the precise statements of the Ketonen–Solovay bounds and of Paris's indicator for BΣₖ₊₁ were read from the surrounding proofs and should be checked against the printed book. The Ketonen–Solovay bound is now stated without a numerical constant.
- Schwichtenberg 1971 and Wainer 1970 bibliographic details are from memory; Kołodziejczyk–Wong–Yokoyama's journal version not identified.
- `fact-fgh-formal` is admitted in its details (pointer to `prop-ack-computations`).
- The fact that every countable non-standard model of IΣ₁ has cofinally many proper cuts isomorphic to it, used by HP IV.3.10 (ii), is mentioned only through the citation.
- Lesson 3 is at 44 minutes; further additions should go to the exercises of lesson 2 or be split.

## 11. History

- **2026-11-12.** Course created: 7 lessons (fast-growing, indicators, paris-harrington, diagonal-indiscernibles, ph-unprovable, alpha-large, arithmetic-with-top), figure generator `scripts/figures/independence.py`.
- **2026-11-13: polishing pass.** Word counts had been measured wrongly (single-line SVG, so `sed '/<svg/,/<\/svg>/d'` deleted the rest of the file); four lessons were at 46 minutes. Split into 9 lessons: `catching-cuts` from fast-growing, `regressive-colorings` from paris-harrington and diagonal-indiscernibles; `lem-fgh-monotone` moved to fast-growing; labels unchanged. Mathematical fixes: normalization $x \leq y$ in `def-indicator` and `def-ph-indicator` (needed in part 2 of `thm-indicator-main`); the claim that standard instances follow from the converse implication corrected; figure `catching` was wrong (the chosen next interval contained a value of the coded function and spanned three pieces) and regenerated; figure `indiscernible` no longer shows the undefined $b$; Σ₁ inductions with $x$ fixed made explicit; example 2 of `ex-coded-expansion` had a wrong bound; short cuts closed under the operations; base of the construction in `thm-top-segment`; attribution of PH ↔ Con(PA + Tr(Π₁)); smaller corrections listed in the polish report. Recent literature searched and cited (section 9).
