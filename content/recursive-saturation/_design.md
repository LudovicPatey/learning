# Design log: Recursive saturation

## 1. Objectives

After the course, a student can:
- work with types, recursive types and coded types in models of arithmetic, and construct recursively saturated elementary extensions;
- run back-and-forth arguments between models of arithmetic, with complete types (isomorphism, homogeneity), with Σ₁ conditions bounded by an element (initial embeddings), and with types over a bounded part of the model (automorphisms fixing a cut);
- realize types of bounded complexity by overspill on partial truth definitions;
- prove resplendence by a Henkin construction with witnesses in the model, and use it to build expansions;
- construct full satisfaction classes, and prove that they force recursive saturation.

**Role in the track.** Course 5 of "Models of arithmetic" (`content/tracks-design.md`; course 4 in the list of that file, which predates the split of the first course), after `cuts-and-extensions` and in parallel with `end-extensions`. It is independent of `end-extensions` and `independence`, written at the same time: nothing here uses the arithmetized completeness theorem or MacDowell–Specker.

## 2. Prerequisites assumed

- First-order logic: compactness, Löwenheim–Skolem, elementary chains, the Tarski–Vaught test, Henkin's canonical model of a complete Henkin theory (stated in `_course.yaml` and lessons 1 and 5).
- fragments-of-arithmetic: `def-cut`, `prop-cuts-induction`, `def-ack-membership`, `lem-ack-basic`, `prop-seq-basic`, `thm-friedman-coded`, `lem-fo-collection-closure`, `thm-fo-parsons`, `fact-pairing`, `fact-exp`, `prop-isigma1-exp`, `lem-delta0-absolute`, `cor-sigma1-upward`, `thm-sigma1-complete`; the finite pigeonhole exercise of the lesson coding (lesson link).
- truth-and-provability: `fact-syntax`, `def-sat-table`, `def-sat0`, `thm-sat0`, `thm-sat-n`, `cor-snowing`, `lem-variable-bounds`, `thm-pr-provably-total`.
- cuts-and-extensions: `def-coded-subsets`, `thm-ssy-turing-ideal`, `ex-ssy-end-extension`, `cor-ssy-scott-set`, `thm-scott-converse` (its proof is reused twice), `ex-ssy-truth`, `ex-exp-cut-closed`.
- big-five/wkl0: lesson link only (countable Scott sets containing a given set).

## 3. Results, lesson by lesson

1. **recursively-saturated-models** (45 min). `def-rs-type`, `ex-rs-types`, `def-rec-sat`; existence (`thm-rs-existence`); models of definable elements are not recursively saturated (`prop-rs-definable`); `def-coded-type`; recursively saturated ⇔ every coded type realized (`thm-rs-coded-types`); realized complete types are coded, Th(M) ∈ SSy(M) (`prop-rs-realized-coded`, `cor-rs-complete-types`).
2. **back-and-forth** (40 min). `lem-bf-step`; isomorphism theorem (`thm-bf-isomorphism`); homogeneity (`cor-bf-homogeneous`); existence with prescribed theory and standard system (`thm-bf-existence`); classification (`cor-bf-classification`); exercise `ex-bf-elementary-embedding`.
3. **friedman-embedding** (45 min). Σₙ types coded (`lem-fe-types-coded`); coded Σₙ₊₁ types and bounded Πₙ₊₁ types realized (`lem-fe-realize`); Friedman's characterization of Σₙ₊₁-recursive saturation (`thm-fe-friedman-rs`); Friedman's embedding theorem for IΣ₁ (`thm-fe-friedman`), self-embeddings (`cor-fe-self`).
4. **automorphisms** (40 min). `ex-rs-same-type` and non-trivial automorphisms; `def-ifix`; fixed cuts are exponential (`prop-ifix-exponential`); `lem-aut-extend`, `lem-aut-move`; Smoryński's theorem (`thm-smorynski`).
5. **resplendence** (45 min). `def-resplendent`, `ex-resplendent`; Craig's trick (`lem-craig`); Barwise–Ressayre (`thm-barwise-ressayre`); `def-inductive-sat`; recursively saturated ⇔ inductive partial satisfaction class (`thm-inductive-sat`); exercise: Tarski's undefinability for partial classes.
6. **satisfaction-classes** (45 min). `def-sat-class`, `ex-sat-classes`; Enayat–Visser (`thm-enayat-visser`); KKL (`thm-kkl`); conservativity of CT⁻ (`cor-ct-conservative`); exercise: a full class making a false non-standard disjunction true.
7. **lachlan** (40 min). `lem-lachlan-partition`, `lem-lachlan-step`, `lem-lachlan-values`; Lachlan's theorem (`thm-lachlan`); characterization (`cor-lachlan-characterization`); CT₀ and disjunctive correctness (stated).

## 4. Proof techniques

- **Coding a type by an element** (lesson 1): a coded type becomes a recursive type with the code as an extra parameter. Used in lessons 2–3.
- **Back-and-forth** in three forms: equality of complete types (lesson 2); Σ₁ facts transferred with witnesses below a fixed d, for initial embeddings (lesson 3); equality of types over the elements below a decreasing bound above a cut (lesson 4).
- **Overspill on a truth definition** (lesson 3), and on an inductive satisfaction class (lesson 5): "recursive saturation is overspill at ℕ".
- **Tables of behavior** coded below 2^{a²}, transferred through the inductive condition, with the pigeonhole principle (lesson 4).
- **Henkin construction with witnesses in the model**, through Craig's trick (lesson 5).
- **Locality of Tarski's clauses**: recursion on the rank of a finite set of formulas, compactness, chains, resplendence (lesson 6); standardly many unravellings of the clauses (lesson 7).
- **Scott's chain of completions in a Scott set**, extended by realizing steps (lesson 2).

## 5. Choices

- **Scope.** Recursive saturation, back-and-forth, Friedman, automorphisms, resplendence, satisfaction classes, as in tracks-design. **Excluded: the preservation theorems of Wong's Lecture 12** (Paris–Kirby characterization of Π*ₙ₊₁ by n-elementary end extensions, Kaye and Motohashi for cofinal extensions). They need the omitting types theorem, which no course proves, and they are about building end and cofinal extensions; with 7 lessons of at most 45 minutes there is no room. They fit a later revision of `end-extensions` or a specialized course. Also excluded: Kossak–Kotlarski's extension theorem (stated in the notes of lesson 4; Wong leaves it as exercises), chronic resplendence (stated), Barwise's converse "resplendent ⇒ recursively saturated" (stated), Wong's Theorem 8.5 on Σₙ-elementary self-embeddings (stated), the arithmetized-completeness remark 7.5 (depends on end-extensions).
- **Order.** The three back-and-forth lessons (2–4) come before resplendence (5), which feeds satisfaction classes (6–7). Resplendence is placed just before its main use.
- **Base theories.** Lessons 1–2 work in IΔ₀ + exp (Wong's level, enough for standard systems); lesson 3 in IΣ₁, because the partial truth definitions of `truth-and-provability` are built in IΣ₁ (Wong uses IΔ₀ + exp truth definitions); lessons 4 and 7 in PA; lesson 6 in IΣ₁ (Wong: IΔ₀ + exp), for the syntax of `fact-syntax`.
- **Coded types** (lesson 1): `thm-rs-coded-types` uses the implication form, which works for incomplete types; Wong's Proposition 8.1 is restricted to complete types. The complete-type converse (Wong 8.13) is mentioned in the notes.
- **Existence with prescribed invariants** (`thm-bf-existence`) is proved by adding realizing steps to the proof of `thm-scott-converse`; Wong does not prove it. It yields the classification by standard systems.
- **Friedman's theorem without recursive saturation.** Wong proves the self-embedding theorem for recursively saturated models and remarks (8.7) that less suffices. The course proves Friedman's two-model criterion for countable non-standard models of IΣ₁ directly, with `lem-fe-realize` (coded Σ₁ types, and Π₁ types with a bound) instead of recursive saturation. The forth step uses Δ₀ types bounded by d, the back step bounded Π₁ types, which is why item 2 of the lemma needs the bound v < a.
- **Smoryński's theorem**: the inductive condition uses single elements x < b, with pairs ⟨a, c⟩ coded below 2^{a²}; the pigeonhole principle is obtained from the exercise of fragments-of-arithmetic/coding by coding the definable map as a sequence (Wong proves an injective coded pigeonhole principle instead).
- **Inductive partial satisfaction classes** (Wong 7, exercises (a)–(c)) are a theorem of lesson 5, as the first application of resplendence and as a contrast with full classes.
- **Lachlan's proof: two corrections to the presentation in Wong 14.4.**
  1. Wong makes the differences θᵢ ∧ ¬θᵢ₊₁ non-empty by θ′ᵢ₊₁ = θᵢ₊₁ ∧ ∃v′ < v θ′ᵢ(v′); this need not keep the sets non-empty when solutions are bounded. The course uses instead the pairing θ*ᵢ(⟨a, b⟩) ⇔ θᵢ(a) ∧ b ≥ i, which makes every difference non-empty and keeps realizability.
  2. Wong's βᵢ₊₁ uses a flat disjunction ⋁_{k ≤ i} of cases. For non-standard i, after unravelling the case k₀ the remaining disjunction is non-standard, and a full satisfaction class may make it true (the δ pathology), so the claim Bᵢ₊₁ = A_{k₀+1} does not follow. The course nests the cases ("if, else if"): γ_{i,k} = (∃v(βᵢ ∧ α_k) ∧ α_{k+1}) ∨ (¬∃v(βᵢ ∧ α_k) ∧ γ_{i,k+1}); at k₀ the tail is a conjunct of a false conjunction. The contradiction is then derived from lem-lachlan-values without Wong's (†)/(‡) in their stated form.
- **Assignments** are the total assignments of `truth-and-provability` (numbers read as functions), not Wong's assignments with domain the free variables; Tarski's clauses are adapted to all constructors of the coding (including bounded quantifiers with variable bounds).

## 6. Comparison with the literature

| Source | Content | Here |
| --- | --- | --- |
| Wong 7 | definitions, existence, Prop 7.1, Thm 7.4, Craig, Barwise–Ressayre, exercises on partial inductive classes | lessons 1, 3, 5 |
| Wong 8 | Prop 8.1, Thm 8.3, Rem 8.4, Thm 8.5, Rem 8.7, Thm 8.8, Lemmas 8.9–8.10, Thm 8.11 (exercises), Prop 8.13 | lessons 1–4 |
| Wong 12 | preservation (omitting types) | excluded |
| Wong 14 | satisfaction classes, Enayat–Visser, KKL, δ pathology, Lachlan, chronic resplendence | lessons 5–7 |
| HP | no chapter on recursive saturation; partial satisfaction (I.1(d)) used through truth-and-provability | — |

Kaye's *Models of PA* (Chapters on recursive saturation, resplendence, automorphisms) and Kossak–Schmerl are not available locally; cited without chapter numbers.

## 7. Pedagogical plan

1. Saturation vs recursive saturation; examples of types (standard part, p_X, non-definable element); why each restriction is needed; quiz on implication vs equivalence in coded types; exercise on elementary chains.
2. Zigzag figure; the back-and-forth lemma as the whole content; quizzes on the back step and on the enumeration of pairs; counting 2^ℵ₀ models; exercises: end extensions, elementary embeddings.
3. Idea of overspill on Sat before the lemma; quiz on the bound in item 2; figure of the image below d; quiz on collection in the back step; counterexamples with ¬Con(PA) and with different standard systems; exercise on self-embeddings below a.
4. Non-trivial automorphisms from homogeneity; idea of tables before the lemmas; quizzes on d ≥ 2^{a²} and on the decreasing bound; figure; counterexample cut {x < aⁿ}; exercises on fixed points.
5. Saturation of elements vs expansions; examples (homogeneity as resplendence; ℕ not resplendent); quizzes on v ≠ cᵢ and finitely many parameters; inductive classes as a contrast; Tarski exercise.
6. Locality of the clauses as the main idea; examples (ℕ, standard formulas, Sat₀); rank figure; quizzes on finite parts and on closure of F₀; conservativity; δ exercise.
7. Strategy before the proof; figure of the descent; quizzes on non-emptiness and on the nested form; disjunctive correctness; exercises.

## 8. Sources (checked 2026-11-13 against the text files)

- Lesson 1: Wong Lecture 7 (definitions, existence paragraph), Lecture 8 (Prop 8.1, Remark 8.2, Prop 8.13); Barwise–Schlipf JSL 41 (1976) and Schlipf JSL 43 (1978) from Wong's bibliography.
- Lesson 2: Wong Theorem 8.3, Remark 8.4; Scott 1962.
- Lesson 3: Wong Theorem 7.4 (Friedman 1973, LNM 337), Theorem 8.5, Remarks 8.6–8.7; Ressayre 1987 and Dimitracopoulos–Paris 1988 (attribution checked online, bibliographic details from memory).
- Lesson 4: Wong Theorem 8.8, Lemmas 8.9–8.10, Theorem 8.11; Smoryński 1982, Kotlarski 1984, Kossak–Kotlarski 1988 (Wong's bibliography).
- Lesson 5: Wong Theorem 7.6 (Barwise IV.5.7; Ressayre 1977, Theorem 2.3), Craig 1953, Theorem 7.7, further exercises (a)–(c), Theorem 14.5 (Schlipf 1977).
- Lesson 6: Wong Lecture 14 (definitions, Theorems 14.2–14.3, δ example, remarks on uncountable models: Lachlan 1981 p. 296, Smith 1989); Krajewski 1976; KKL 1981; Enayat–Visser 2015; Kotlarski 1986, 1991.
- Lesson 7: Wong Theorem 14.4; Lachlan 1981; Enayat–Pakhomov, AML 58 (2019) 753–766 (checked online).

## 9. Recent literature

Web search, 2026-11-13 (the first attempt on 2026-11-12 failed on a usage limit):
- Self-embeddings: the extension of Friedman's theorem to IΣ₁ (Ressayre; Dimitracopoulos–Paris) and Ressayre's converse were confirmed through Bahrami–Enayat, *Fixed points of self-embeddings of models of arithmetic* (APAL 2018, arXiv:1703.02588), and Enayat's paper on Tanaka's self-embedding theorem for WKL₀. Used in lesson 3 (notes).
- Satisfaction classes: Enayat–Pakhomov 2019 (CT⁻ + disjunctive correctness = CT₀, proves Con(PA)); Cieśliński–Łełyk–Wcisło (JML 2023) on the halves of disjunctive correctness; Enayat on approximate disjunctive correctness (RSL 2024). Enayat–Pakhomov is mentioned in lesson 7; Cieśliński's book (2017) is cited in lesson 6.

## 10. Open points

- Bibliographic details of Ressayre 1987, Dimitracopoulos–Paris 1988 and Bahrami–Enayat 2018 (volume, pages) were written from memory and should be checked against the papers; Bahrami–Enayat was removed from the lesson for this reason.
- Lachlan's theorem is stated for PA as in the sources; the proof given uses only IΣ₁-level coding, but no source was checked for the weaker statement, so it is not claimed.
- `thm-bf-existence` has no direct source reference (Kaye and Kossak–Schmerl treat the classification; chapter numbers not checked).
- The translation φ ↦ φ* of `lem-variable-bounds` is asserted to be primitive recursive (lesson 3); this is clear from its proof but not stated in truth-and-provability. A remark there would help.
- Preservation theorems (Wong 12) are not covered anywhere in the track.

## 11. History

- **2026-11-12/13.** Course created: 7 lessons (recursively-saturated-models, back-and-forth, friedman-embedding, automorphisms, resplendence, satisfaction-classes, lachlan), figure generator `scripts/figures/recursive-saturation.py` (figures zigzag, friedman, smorynski, ranks, lachlan).
