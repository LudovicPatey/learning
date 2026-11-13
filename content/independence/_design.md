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
- truth-and-provability: `def-provably-total`, `thm-pr-provably-total`, `thm-pmt`, the Ackermann exercise (lesson link), `def-delta0-star`, `lem-sat-tables`, `cor-snowing`.
- cuts-and-extensions: `def-semiregular`, `thm-semireg-isigma1`, `def-regular-cut`.
- models-of-computation / arithmetic-hierarchy: `prop-pr-bounded-mu`, `cor-pr-bounded-quantifiers`, `lem-bounded-computable`, `thm-ack-majorization`.
- ramsey-theorem: `thm-rt3-aca`, `prop-rt-basic`; big-five: `thm-konig-aca`; induction-conservation: `thm-aca0-pa`.
- computable-ordinals/ordinals: ordinal arithmetic (lesson link). Cantor normal form is recalled.

## 3. Results, lesson by lesson

1. **fast-growing** (45 min). `def-fgh` ($F_0(x) = x+1$, $F_{k+1}(x) = F_k^{(x)}(x+1)$), `ex-fgh-values`; formalization `fact-fgh-formal` (admitted in its routine details), `lem-fgh-isigma1` (values increase, iterates are coded, totality for standard $k$); `thm-kirby-paris-cut`: a countable $M \models$ IΣ₁ with $a \geq 1$ and $\nu$ non-standard has a semiregular cut containing $a$ and not $F_\nu(a)$. Exercise: IΣ₂ proves the totality of all $F_k$. Figure `catching`.
2. **indicators** (45 min). `lem-fgh-monotone`; `def-indicator`; `thm-indicator-main` (unprovability; bound on provably total functions); `prop-indicator-isigma1`; `cor-isigma1-fgh` (Kirby–Paris); `thm-isigma1-envelope` (provably total in IΣ₁ ⇒ bounded by $F_n + n$ ⇒ primitive recursive; this proves the converse of `thm-pmt`); `cor-pr-fgh-bound`.
3. **paris-harrington** (45 min). `def-relatively-large` ($\to_*$, PH, PH$_n$), `ex-relatively-large`; `thm-ph-true` (ACA₀ ⊢ PH$_n$, hence PA ⊢ PH$_n$); `def-regressive`; `lem-ph-regressive` (relatively large homogeneous sets give min-homogeneous sets, with a translation trick).
4. **diagonal-indiscernibles** (45 min). `def-diagonal-indiscernibles`, `ex-diagonal-indiscernibles`; `lem-diag-from-regressive`; `lem-diag-growth`; `thm-indiscernible-cut` (the cut of diagonal indiscernibles of non-standard length satisfies PA). Figure `indiscernible`.
5. **ph-unprovable** (35 min). `def-ph-indicator`; `thm-ph-indicator` (relative largeness of all arities up to $c$ is an indicator for PA, with a satisfaction table of non-standard size); `cor-ph-unprovable`; `cor-ph-envelope`.
6. **alpha-large** (40 min). `def-fundamental-sequence`; `def-alpha-large`, `ex-alpha-large`; `lem-large-sum`; `thm-large-fgh` ($L_{\omega^k} = F_k$); `cor-omega-omega-large`; `thm-schwichtenberg-wainer` (admitted); Ketonen–Solovay stated. Figure `omega-large`.
7. **arithmetic-with-top** (40 min). `def-coded-expansion`, `ex-coded-expansion`; `prop-top-truth` (truth by bounded formulas, LNP for all formulas); `thm-top-segment` (Paris, admitted); `def-ramsey-cut`; `thm-ramsey-cuts` and `thm-paris-bsigma-indicator` (admitted).

## 4. Proof techniques

- **Cuts as models / the method of indicators** (lessons 1–2, 5): unprovability from the construction of a cut satisfying the theory and not closed under a function; envelopes from overspill on the degree of largeness.
- **Construction by finite extensions** (lesson 1): nested intervals, one requirement per stage, requirements listed with repetitions (countability of the model).
- **Lowering an index along a non-standard element** (lesson 1): the index $\nu - k$ stays non-standard, which replaces a new overspill at each stage.
- **Compactness via König's lemma** (lesson 3).
- **Counting / pigeonhole in the model** (lessons 1, 3, 4): with non-standard parameters.
- **Moving coordinates** (lesson 3), **translation** of an interval to strengthen relative largeness (lesson 3).
- **Truth reduction by indiscernibles** (lesson 4): unbounded quantifiers of the cut become bounded by indiscernibles.
- **A truth definition to handle all standard formulas at once** (lesson 5): a satisfaction table with a non-standard number of formulas.
- **Running a definition** (lesson 6): decomposition of large sets.
- **Bounding quantifiers by the top** (lesson 7).

## 5. Choices

- **Hierarchy.** HP's variant $F_{k+1}(x) = F_k^{(x)}(x+1)$ instead of Wong's $F_k^{(x+1)}(x)$, so that $F_k(x)$ is exactly the least end of an $\omega^k$-large interval (lesson 6).
- **Kirby–Paris construction with a lowering index.** Wong uses overspill at each stage and the monotonicity of the hierarchy in its index inside the model; the course keeps $s_k = F_{\nu-k}(r_k)$ exactly, which needs no monotonicity in $M$ (that monotonicity raises a $\Pi_2$-induction issue in IΣ₁). Pieces are chosen with left end $> r_k$, so that the left ends increase strictly and the supremum is a cut (Wong's version can repeat $r_k$).
- **Indicator as a three-place Σ₁ formula** $\iota(x, y, c)$ ("$[x, y]$ is $c$-large") rather than HP's function $Y(x, y)$: a maximum would not be Σ₁. The normalization $c \leq y$ makes $x$ non-standard in the envelope argument. Only the direction "non-standard largeness ⇒ cut" is used by the main theorem; the converse is proved for each concrete indicator.
- **PMT converse proved** (it was admitted in truth-and-provability): bound by $F_n + n$ and bounded minimization, rather than HP's provable equivalence with a primitive recursive derivation.
- **Paris–Harrington through regressive colorings and diagonal indiscernibles** (Kanamori–McAloon), not through HP's Paris sequences and restrainable cuts, nor through consistency statements: it is the shortest complete route to a cut satisfying PA. The reduction PH ⇒ min-homogeneity (lemma `lem-ph-regressive`), the growth lemma with $\lfloor\sqrt{y_2 - y_1}\rfloor$ (quantifier-free, so it fits the Δ*₀ setting of the satisfaction tables) and the packing of parameters into one variable are written for this course.
- **Indicator for PA with all arities up to $c$**, to avoid lowering the arity, which costs relative largeness.
- **Truth of PH in ACA₀** for each fixed arity, with conservation over PA (Friedman), citing `ramsey-theorem` and `big-five`; HP's sharper level-by-level provability (II.1.9) is stated.
- **Admitted:** the routine details of the formalization of $F_k$; Paris's refinement PH$_{u}$ ↔ Con(IΣ$_u$ + Tr(Π₁)); the Schwichtenberg–Wainer and Ketonen–Solovay theorems; Paris's theorem on models of TA′; $k$-Ramsey/extendable/restrainable cuts and the indicators for BΣₖ₊₁.
- **Excluded:** Paris sequences (described in prose), the PH ↔ consistency proofs (HP II.2), transfinite induction in fragments (HP II.3(b)), Ajtai's completeness theorem and the parity lower bound (Wong 13), recursive saturation of structures with a top (parallel course). The Kanamori–McAloon equivalence is used in one direction only.

## 6. Comparison with the literature

| Source | Content | Here |
| --- | --- | --- |
| Wong 5 | Grzegorczyk-type hierarchy, Thm 5.6, indicators (Further exercises) | lessons 1–2 |
| Wong 13 | arithmetic with a top, Prop 13.1, Ajtai, Thm 13.11 | lesson 7 (Ajtai excluded) |
| HP II.1 | Ramsey theorems and fragments, PH | lesson 3 |
| HP II.2 | PH and consistency | lesson 5 (stated) |
| HP II.3 | ordinals, α-large sets, Schwichtenberg–Wainer hierarchy | lesson 6 |
| HP IV.2 | TA′, short cuts, Ramsey/extendable/restrainable cuts | lesson 7 (stated) |
| HP IV.3 | envelopes, indicators, Paris sequences | lessons 2, 5 (different construction) |
| Kanamori–McAloon 1987 | regressive Ramsey, diagonal indiscernibles | lessons 3–5 |

Kaye's *Models of Peano Arithmetic* (Chapter 14 treats the Paris–Harrington theorem) was not available and is not cited.

## 7. Pedagogical plan

1. Values of $F_1, F_2, F_3$; quiz on $\Pi_1$ versus $\Pi_2$ induction; figure of nested intervals; quizzes on repetitions and on the non-standard index.
2. Quizzes on minimality and on non-standardness of $x$; exercise on monotone indicators.
3. The coloring of points showing that relative largeness forces exponential intervals; quiz on the role of the infinite homogeneous set; intuition for moving coordinates; quizzes on regressiveness and on the least coordinate; exercise: min-homogeneity cannot be homogeneity.
4. Examples of diagonal indiscernibility (parity, divisibility); figure; quizzes on the shift $x + 1$ and on the choice of tuples in the truth reduction.
5. Quizzes on the satisfaction table and on the parameters.
6. Examples $n$-large, ω-large, ω²-large ($[3, 39)$, matching $F_2(3) = 39$); figure; quizzes on normal form and on shortest segments; exercises computing $L_\alpha$.
7. Quiz on bounded translation; exercise: no definable proper cut in $[0, a]$.

## 8. Sources (checked 2026-11-13 against the text files)

- Lesson 1: Wong Lecture 5 (definition, Lemma 5.3–5.4, Prop 5.5, Thm 5.6 and its proof); HP II.3.22 (hierarchy); Kirby–Paris 1977 (Wong's bibliography).
- Lesson 2: HP IV.3.1–3.10 (Definition 3.9, Theorem 3.10, Corollary 3.7, envelope Definition 3.3); Wong Lecture 5 Further exercises; Parsons 1970, Mints 1971 (Wong's bibliography).
- Lesson 3: HP II.1.1–1.3, 1.9, 1.10, remarks to Chapter II; Simpson Lemma III.7.4, Theorem III.7.6 (checked); Paris–Harrington 1977 (Wong's bibliography); Kanamori–McAloon 1987 (from memory: APAL 33, 23–41).
- Lesson 4: Paris–Harrington 1977; Kanamori–McAloon 1987; HP II.2(d), IV.3.17, 3.23.
- Lesson 5: HP IV.3.20–3.24; HP II.2.1–2.3 (consistency statements).
- Lesson 6: HP II.3.12, 3.19–3.21, 3.22, 3.30, 3.32, 3.34, 3.36–3.37; HP IV.3.5, 3.8; Ketonen–Solovay 1981, Schwichtenberg 1971, Wainer 1970 (from memory).
- Lesson 7: Wong Lecture 13 (Prop 13.1, Further exercises, Thm 13.11); HP IV.2.1–2.22 and bibliographical remarks (Paris 1980, 1981; Cégielski–McAloon–Wilmers 1982, checked in HP's bibliography).

## 9. Recent literature

No web search was made in this session. The material is classical (1977–1987). Possible additions for a later revision: work on the strength of the Kanamori–McAloon and Paris–Harrington principles over weak theories, and on the reverse mathematics of Ramsey-type finite principles (e.g. results on the first-order strength of RT²₂ and of the "Paris–Harrington for pairs" principle); these were not checked and are not cited.

## 10. Open points

- The text file of HP is garbled in several formulas (II.3.36 comment, IV.3.20); the precise statements of the Ketonen–Solovay bounds and of Paris's indicator for BΣₖ₊₁ were read from the surrounding proofs and should be checked against the printed book.
- Kanamori–McAloon 1987, Ketonen–Solovay 1981, Schwichtenberg 1971 and Wainer 1970 bibliographic details are from memory.
- `fact-fgh-formal` is admitted in its details (pointer to the Ackermann exercise of truth-and-provability).
- Lessons 1–4 are at about 45 minutes.

## 11. History

- **2026-11-12.** Course created: 7 lessons (fast-growing, indicators, paris-harrington, diagonal-indiscernibles, ph-unprovable, alpha-large, arithmetic-with-top), figure generator `scripts/figures/independence.py`.
