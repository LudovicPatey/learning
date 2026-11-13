# Design log: End extensions of models of PA

## 1. Objectives

After the course, a student can:
- prove the low basis theorem inside a model of IΣ₁, and say which consequences of Σ₁ induction it uses;
- carry out Henkin's proof of the completeness theorem inside a model of IΣ₁, and see why the term model end extends the ground model;
- combine the arithmetized completeness theorem with consistency facts to build end extensions with prescribed properties, and recognize when they cannot be elementary;
- relate definable types, conservative extensions and end extensions;
- prove the MacDowell–Specker theorem by Gaifman's strongly definable types;
- describe extensions by strongly definable types through gaps, construct minimal types, and use them for minimal end extensions and automorphism groups.

**Role in the track.** Course 4 of the track "Models of arithmetic" (`content/tracks-design.md`, where it is listed as course 3 before the split of course 1). It provides the two methods of building end extensions used later: the arithmetized completeness theorem (recursive saturation, satisfaction classes, independence) and definable types (the converse of the Paris–Kirby theorem, stated in cuts-and-extensions; iterated extensions).

## 2. Prerequisites assumed

- First-order logic: completeness, compactness, Tarski–Vaught test, Gödel's incompleteness theorems (stated in `_course.yaml` and lesson 1).
- fragments-of-arithmetic: `def-end-extension`, `lem-delta0-absolute`, `cor-sigma1-upward`, `prop-standard-part`, `lem-pam-basic`, `lem-fo-collection-closure`, `thm-fo-parsons`, `thm-fo-isigma-ipi`, `prop-fo-least-number`, `thm-fo-paris-kirby`, `cor-overspill`, `thm-delta0-comprehension`, `def-ack-membership`, `thm-friedman-coded`, `prop-isigma1-exp`, `def-exp`.
- truth-and-provability: `fact-syntax`, `def-sat0`, `thm-sat0`, `def-sat-n`, `cor-snowing`, `lem-variable-bounds`, `cor-course-of-values-provable`, `thm-pr-provably-total`, `lem-isigma-star`.
- cuts-and-extensions: strings (`def-strings-model`, `lem-strings-model`), `thm-scott-wkl-cut`, `thm-end-ext-collection`, `fact-end-ext-converse`, `thm-splitting`, `ex-sup-elementary`.
- arithmetic-hierarchy: `thm-definable-arithmetic`, `thm-post`. pi01-classes: `thm-low-basis`, `prop-pi01-equivalent`, `thm-dnc2-no-computable`, `thm-pa-completions`.

## 3. Results, lesson by lesson

1. **low-basis-isigma1** (45 min). Trees and paths in a model (`def-ee-tree`, `lem-ee-tree-complexity`, `ex-ee-trees`); the jump of a path over M (`def-ee-jump`); low basis theorem in IΣ₁ (`thm-ee-low-basis`); classical version (`cor-ee-low-basis-classical`); relativization (`rem-ee-low-basis-relativized`); exercise: Kreisel basis theorem in IΣ₁ (`ex-ee-leftmost`).
2. **arithmetized-completeness** (45 min). Logic in IΣ₁ (`fact-ee-logic`, admitted); the arithmetized completeness theorem (`thm-ee-act`), with M ⊆ₑ K and a Δ₂-definable diagram; relativization (`rem-ee-act-relativized`); low completeness theorem (`cor-ee-low-completeness`).
3. **end-extensions-from-consistency** (40 min). Proper end extensions by a new constant (`lem-ee-proper-end`); IΣ₁ ⊢ Con(IΔ₀ + exp) (`fact-ee-con-efa`, admitted) and exponential end extensions of models of IΣ₁ (`thm-ee-exp-cut`); reflection (`fact-ee-reflection`, admitted) and Σₙ-elementary end extensions of models of PA (`thm-ee-sigma-n-end`); end extensions to PA + ¬Con(PA), not Σ₁-elementary (`thm-ee-not-elementary`); exercises `ex-ee-con-sigma1`, `ex-ee-cod-delta2`.
4. **definable-types** (45 min). Types (`def-ee-type`), M(p) as definable closure (`def-ee-mp`, `lem-ee-mp`), definable types (`def-ee-definable-type`, `ex-ee-realized-definable`), definable ⇔ conservative (`prop-ee-definable-conservative`), conservative ⇒ end (`prop-ee-conservative-end`, `cor-ee-definable-end`); types over ℕ coding a non-arithmetic set (`ex-ee-coding-type`); exercises `ex-ee-cod-def`, `ex-ee-unbounded-nonrealized`.
5. **macdowell-specker** (45 min). Strongly definable types (`def-ee-strongly-definable`), they are definable (`lem-ee-strongly-definable-definable`); cohesive sets in M (`lem-ee-cohesive`); Gaifman's existence theorem (`thm-ee-gaifman-sd`); MacDowell–Specker (`thm-ee-macdowell-specker`); a model of IΔ₀ has a proper elementary end extension iff it satisfies PA (`cor-ee-pa-characterization`); exercises `ex-ee-iterate-ms`, `ex-ee-forcing-unbounded`.
6. **gaps** (45 min). Skolem functions (`def-ee-skolem`), gaps (`def-ee-gap`, `lem-ee-gap-criterion`); one new gap (`prop-ee-one-gap`); canonical extensions; unique extension characterization (`thm-ee-unique-extension`); iteration along ordinals; exercises `ex-ee-iterated-gaps`, `ex-ee-sd-preserved`.
7. **minimal-types** (45 min). Rare types (`def-ee-rare`, `lem-ee-rare-syntactic`), the principle FAR in M (`lem-ee-far`), existence of minimal types (`thm-ee-minimal-exists`, `def-ee-minimal-type`); rare ⇒ definable from any element of the gap (`lem-ee-rare-definable`); minimal elementary end extensions (`def-ee-minimal-extension`, `thm-ee-minimal-extension`); indiscernibility (`prop-ee-indiscernible`); iteration along linear orders (`thm-ee-linear-order`); automorphism groups (`cor-ee-automorphisms`); exercise `ex-ee-rare-extension`.

Lessons 4–7 depend on cuts-and-extensions only, not on lessons 1–3: the two methods can be read independently.

## 4. Proof techniques

- **Least admissible guess** (lesson 1): the answers of ∅′ in the low basis construction are replaced by the ≺-least guess whose tree is unbounded, obtained by LΠ₁ for each length separately; coherence of the guesses is proved without induction. This avoids induction for Σ₀(Σ₁) formulas, which Hájek–Pudlák use.
- **Henkin's construction inside a model** (lesson 2), with properties of the complete theory checked on finite parts of the path, which are elements of M; numerals give the end extension.
- **Overspill on consistency statements** (lesson 3), to pass from all standard fragments to one non-standard fragment.
- **Adjoining a realization and taking the definable closure** (lesson 4), with a Łoś-type lemma; **conservativity gives end extension** by induction in M.
- **Cohesiveness inside the model** (lesson 5): a definable recursion of length M that decides a whole definable family at once; a countable chain handles all formulas, whatever the cardinality of M.
- **Gaps and Skolem functions** (lessons 6–7); **compactness to turn uniqueness into definability** (lessons 6–7: unique extension, rarity); **thinning by FAR** (lesson 7); **indiscernibility by induction on the length of tuples** (lesson 7).

## 5. Choices

- **Scope as in tracks-design.** Two adjustments: (1) a lesson of applications of the arithmetized completeness theorem (lesson 3) was added, since without it the theorem has no use in the course; (2) Gaifman's lattice theorem (substructure lattice ≅ P(I)) is stated, not proved: the proof that every elementary substructure is generated by the indiscernibles it contains needs more than the course develops.
- **First-order arithmetized completeness theorem over IΣ₁** (Hájek–Pudlák) rather than Wong's second-order version over WKL₀: the track is first-order, and the low basis theorem in IΣ₁ was required. Its external form (Wong's) is the one used; Hájek–Pudlák's internal full satisfaction is not needed.
- **Binary trees only**, coded as in cuts-and-extensions, since the tree of completions is binary; Hájek–Pudlák's Δ₁-estimated trees of sequences are not needed.
- **Low basis proof reformulated** (least admissible guess). Its correctness is checked in full in the lesson; no published source with exactly this formulation was found, which is said in the notes.
- **Facts of logic in IΣ₁ admitted** (`fact-ee-logic`), with references to HP I.4(a) and I.4.32; formalizing Henkin conservativity in IΣ₁ is long and not instructive.
- **Consistency facts admitted**: IΣ₁ ⊢ Con(IΔ₀ + exp) (Simpson II.8.11), reflection (HP I.4.33–I.4.34), formalized second incompleteness (HP III.2).
- **Relativized versions** (`rem-ee-low-basis-relativized`, `rem-ee-act-relativized`) stated with the changes needed, used once (Σₙ-elementary end extensions, with the Σₙ₊₁-definable theory Tr).
- **M(p) as definable closure** in an elementary extension, instead of Wong's prime model of a term theory: shorter, and shows the link with the definable ultrapower (HP IV.1(b)).
- **Non-definable types over ℕ** by coding a non-arithmetic set: a counting argument does not work (there are 2^ℵ₀ definable types over ℕ as well), and this example also shows SSy(ℕ(p)) ∋ X.
- **MacDowell–Specker through strongly definable types directly**: Wong's Theorem 9.10 and his split into Theorem 10.1 + Lemma 10.2 are merged; COH is proved inside M (first-order) instead of in (M, Def(M)) ⊨ ACA₀.
- **Corollary: proper elementary end extension ⇔ PA** (HP IV.1.53(3)), proved by collection with full elementarity, without induction in K.
- **Rarity with one monotone majorant per Skolem function** instead of Wong's majorizing sequence of all Skolem functions.
- **Excluded**: the second-order ACT and Scott–Tanaka's theorem (Wong 4.13; stated with a pointer in lesson 3); the converse of the Paris–Kirby theorem (HP IV.1.53–1.57; pointer in lesson 5, admitted in cuts-and-extensions); the converses of Wong's Proposition 11.12 (stated); Blass's minimal cofinal extensions (stated); the lattice theorem (stated); Theorem 10.6 of Wong (gap characterization of strongly definable types); end extensions of models of second-order arithmetic (Wong 9.12); forcing reading of definable types (mentioned).

## 6. Comparison with the literature

| Source | Content | Here |
| --- | --- | --- |
| HP I.3(b) | low basis theorem in IΣ₁ (3.8), dyadic case (3.21) | lesson 1, different proof |
| HP I.4(a)–(b) | logic in IΣ₁, low ACT (4.27) | lesson 2 (facts admitted; external form) |
| HP I.4(c) | 4.33–4.34, consistency of fragments | lesson 3 (admitted) |
| HP IV.1(b), (e) | definable ultrapower, 1.53 | lessons 4–5 (remark; 1.53(3) proved) |
| Wong 4 | ACT over WKL₀, Cor 4.11, Thm 4.13 | lessons 2–3 (first-order form; 4.13 stated) |
| Wong 9 | definable types, conservative extensions, COH, Gaifman–Phillips, MS | lessons 4–5 |
| Wong 10 | strongly definable types, gaps, 10.4, 10.5 | lessons 5–6 |
| Wong 11 | rare types, FAR, minimal types, 11.6, 11.7, 11.10, 11.13–11.15 | lesson 7 |

Kaye's and Kossak–Schmerl's books are not available locally; Kossak–Schmerl is cited only through Wong.

## 7. Pedagogical plan

1. Intuition: the ∅′ answers of the classical proof replaced by a minimality condition; figure of the tree of guesses; quiz on why a least element and not a recursion; exercise on the Kreisel basis theorem.
2. Idea of Henkin's proof inside M; figure of the term model and the numerals; quiz on why the disjunction property (iii) is needed; corollary for ℕ (low completeness).
3. Idea of overspill on consistency; quizzes on IΣ*_b and on why only Σₙ-elementarity; an extension that is not Σ₁-elementary, and the exercise contrasting it with Σ₁-elementary ones.
4. Intuition of adding one element; Łoś-type lemma; examples (realized types, types over ℕ coding a set); quiz on the role of the definable functions.
5. Intuition of deciding a whole definable family at once; figure of the cohesive construction; quizzes on the countable chain and on where induction is used; exercises on large elementary end extensions and on forcing for bounded types.
6. Picture of gaps; figure of M(p) = M ∪ gap(d); quizzes on Case 1 and on strong definability versus definability.
7. Intuition of "realized at most once per gap"; figure of the rarity argument; quiz on which property gives which half of minimality.

## 8. Sources (checked 2026-11-12/13 against the text files)

- Lesson 1: HP I.3(b) (Definition 3.7, Theorem 3.8, Remark 3.21) and bibliographical remarks to Chapter I, item (3) (Jockusch–Soare 1972, Clote 1985, Hájek–Kučera 1989 — bibliography entries checked).
- Lesson 2: HP I.4(a)–(b) (4.10, 4.25, 4.27, 4.32) and remarks to Chapter I, item (4) (Hilbert–Bernays, McAloon 1978, Paris 1981); Wong Lecture 4 (ACT, Theorem 4.8 attributed to Simpson).
- Lesson 3: Simpson Theorem II.8.11 (text checked); Wong Fact 4.10, Corollary 4.11, Theorem 4.13 (Enayat; Tanaka 1997; bibliography of Wong); HP Theorem I.4.33, Corollary I.4.34 (checked); Wong introduction to Lecture 9 (countable models via recursive saturation).
- Lesson 4: Wong Lecture 9 (definitions, Propositions 9.3, 9.5, 9.6; Kossak–Schmerl §2.2.2 as cited by Wong); HP IV.1(b) and remarks to Chapter IV, item (1) (Skolem).
- Lesson 5: Wong Lecture 9 (Lemma 9.8, Theorem 9.10, Remark 9.11, Further comments: Mills 1978, Enayat 2008), Lecture 10 (Theorem 10.1, Lemma 10.2, Gaifman Prop. 2.23); HP Theorem IV.1.53(3) and 1.57; MacDowell–Specker 1961 (HP bibliography).
- Lesson 6: Wong Lecture 10 (§10.1, Lemma 10.3, Proposition 10.4 = Gaifman 4.8, Theorem 10.5 = Gaifman 2.10, §10.2, Further reading: Blass 1974, Kirby 1984).
- Lesson 7: Wong Lecture 11 (Definition after Kossak–Kotlarski–Schmerl 1993, Lemmas 11.1, 11.2, 11.5, Theorems 11.4, 11.6, 11.10, Proposition 11.7, Corollaries 11.13–11.14, Proposition 11.12, Question 11.15, Schmerl 2002).

## 9. Recent literature

Web search, 2026-11-13:
- A. Enayat, *63 years of the MacDowell–Specker theorem* (arXiv:2208.03156, 2022), a survey of the theorem and its generalizations; cited in lesson 5 as further reading.
- The existence of minimal cofinal elementary extensions for all non-standard models of PA (Kossak–Schmerl, Chapter 12, Question 2; Wong Question 11.15) is still listed as open in Enayat's lecture slides and in Schmerl's later papers (*The diversity of minimal cofinal extensions*, arXiv:2109.08130; *The pentagon as a substructure lattice of models of Peano arithmetic*, arXiv:1910.05284); no solution was found. Kept as open in lesson 7.
- Sun (2025), on the Kaufmann–Clote question, is already in cuts-and-extensions.

## 10. Open points

- Question 11.15 (minimal cofinal extensions) presented as open; a web search found no solution (section 9).
- The least admissible guess proof of the low basis theorem is a reformulation; a reference with this exact argument would be welcome.
- `fact-ee-reflection` (1) is derived from HP I.4.33–4.34 with an argument sketched in prose; the statement for theories with numerals of non-standard elements should be checked against the printed book (the text file is partly garbled there).
- Gaifman's lattice theorem is stated without proof.
- Lessons 1, 2 and 7 are at the upper limit (2570–2610 words without SVG).

## 11. History

- **2026-11-12.** Course created: 7 lessons (low-basis-isigma1, arithmetized-completeness, end-extensions-from-consistency, definable-types, macdowell-specker, gaps, minimal-types), figure generator `scripts/figures/end-extensions.py`.
