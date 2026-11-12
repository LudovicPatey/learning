# Design log: Cone avoidance and the forcing question

This file is the memory of the course (see "Designing tracks and courses" in
`AGENTS.md`). It is not rendered.

## 1. Objectives

After the course, a student can:

- state cone avoidance and strong cone avoidance as properties of problems, relate them
  to the preservation of weakness properties, and use them to build ω-models and prove
  non-reductions;
- explain why the definitions are relativized, and use relativization to combine problems
  (products, ω-reductions, finitely many colors);
- recognize the three-case argument in any proof of cone avoidance, and reduce it to the
  definability of a forcing question;
- design a forcing question with answers Σ⁰₁ relative to the condition, using
  over-approximation and compactness;
- prove that every set is Δ⁰₂ relative to a set avoiding a given cone, and that
  cohesiveness admits strong cone avoidance;
- use disjunctive forcing questions and Lachlan's disjunction, and prove Seetapun's
  theorem directly with them;
- prove preservation of non-Σ⁰₁ definitions and of hyperimmunities for WKL, COH, RT¹₂ and
  RT²₂, and relate both properties to cone avoidance (Downey, Greenberg,
  Harrison-Trainor, Patey, Turetsky).

**Role in the track.** Second course of the track "Lowness and avoidance"
(`tracks-design.md`), after `effective-forcing`. It is the place where the general method
of separation by preservation of a first-jump weakness property is explained and
exercised. The later courses of the track (`lowness`, `compactness-avoidance`,
`separation-design`, `jump-cone-avoidance`, `jump-compactness-avoidance`) reuse its
framework: Σ⁰₁(ℳ)-preserving questions, disjunctive questions, Scott ideals obtained by
preservation along WKL (`lem-scott-preservation`).

## 2. Prerequisites assumed

- `effective-forcing`: notions of forcing and sufficiently generic sets
  (`def-forcing-notion`, `def-generic-notion`, `lem-generic-set`), the forcing relation at
  level 1 (`def-forcing-relation`, `prop-forcing-basic`), forcing questions
  (`def-forcing-question`, `ex-cohen-question`, `thm-tree-question`,
  `thm-question-preservation`, `cor-question-jump-cone`, `def-question-compact`,
  `thm-question-hyperimmunity`), computable Mathias forcing (`prop-mathias-question`,
  `prop-mathias-dominant`, `cor-mathias-no-sigma2`).
- `ramsey-theorem`: Mathias conditions (`def-mathias-condition`), cone avoidance for COH
  (`thm-coh-cone-avoidance`), Scott ideals avoiding a cone (`lem-scott-cone`),
  Dzhafarov–Jockusch (`thm-dj-cone-avoidance`), Seetapun (`thm-seetapun`,
  `cor-rt22-not-aca`), Jockusch's coloring of triples (`prop-rt32-jump`), stable
  colorings (`def-stable-coloring`), Lachlan's disjunction (unlabeled, lesson
  `cone-avoidance`).
- `reducibilities`: problems (`def-problem`), weakness properties and preservation
  (`def-weakness`, `lem-preservation-ideal`, `thm-preservation-separation`), the exercise
  "P ≤_ω Q and Q preserves W imply P preserves W".
- `turing-degrees`: limit lemma, modulus and computation function (`thm-limit-lemma`,
  `def-modulus`, `cor-complete-domination`, `thm-computation-function`), high sets avoiding
  a cone (`thm-high-cone-avoidance`).
- `pi01-classes`, `big-five`: cone avoidance basis theorem, weak König's lemma, Scott
  ideals (`def-scott-ideal`).
- `immunity-growth`: hyperimmune functions (`def-hyperimmune-fn`), Martin's theorem.
- `arithmetic-hierarchy`: Post's theorem.

## 3. Results, lesson by lesson

1. **Avoidance properties of problems** (`avoidance-properties`): cone avoidance and strong
   cone avoidance (`def-cone-avoidance-problem`); equivalence with preservation of the
   classes W_C (`prop-cone-avoidance-preservation`); ω-models and non-reductions
   (`cor-cone-avoidance-model`); table of examples and counterexamples
   (`ex-cone-avoidance-problems`: RT¹₂, WKL, COH, RT²₂, RT³₂, J); closure under products
   and ω-reducibility (`prop-cone-avoidance-product`); exercises: an artificial problem with
   unrelativized but not relativized cone avoidance (`exr-unrelativized-cone`), RT²_k,
   WKL and COH not ω-reducible to RT¹₂.
2. **The forcing question as a method** (`forcing-question-method`): the three-case
   argument; the forcing question as a dividing line (figure `dividing-line`);
   over-approximation; Σ⁰₁(ℳ)-preserving questions (`def-question-local`) and the abstract
   cone avoidance theorem (`thm-local-cone-avoidance`); every set is Δ⁰₂ relative to a set
   avoiding a cone (`thm-delta2-cone-avoidance`), and strong cone avoidance reduces to Δ⁰₂
   instances (`cor-strong-delta2`); exercises: the necessary conditions for a forcing
   question are not sufficient (`exr-question-converse`), high cone-avoiding subsets.
3. **Strong cone avoidance and disjunctive questions** (`disjunctive-question`): COH admits
   strong cone avoidance (Wang, `thm-coh-strong-cone`); disjunctive notions of forcing and
   questions (`def-disjunctive-notion`); the abstract disjunctive lemma
   (`lem-disjunctive-cone`) and Lachlan's disjunction (`lem-disjunctive-construction`);
   the Dzhafarov–Jockusch forcing as an instance (text and exercise); exercise: a
   disjunctive construction avoids one cone at a time.
4. **Seetapun's theorem by a disjunctive forcing question** (`seetapun-forcing`): Seetapun
   conditions (`def-seetapun-forcing`, figure `seetapun-condition`), infinity
   (`lem-seetapun-infinity`), the question over all partitions of the reservoir
   (`lem-seetapun-question`), the theorem (`thm-seetapun-direct`); comparison with the
   proof through cohesiveness; exercises: cone-avoiding reservoirs (Seetapun's original
   setting), stable colorings without thinning.
5. **Preservation of non-Σ⁰₁ definitions** (`non-sigma1-definitions`): definition
   (`def-preserve-non-sigma1`), examples (`ex-non-sigma1`), implies cone avoidance
   (`prop-non-sigma1-cone`), equivalence admitted (`thm-non-sigma1-equivalence`); abstract
   theorems (`thm-local-non-sigma1`, `lem-disjunctive-non-sigma1`); Scott ideals by
   preservation (`lem-scott-preservation`); WKL, COH, RT¹₂ (strong), RT²₂
   (`thm-non-sigma1-examples`); one definition but not two (discussion, results of Patey
   and Wang); exercises: countably many definitions for WKL and COH, c.e. sets, strong
   preservation for COH.
6. **Preservation of hyperimmunities** (`hyperimmunities`): relative moduli
   (`def-relative-modulus`), Δ⁰₂ sets have moduli (`lem-delta2-modulus`), moduli and
   hyperimmunity (`lem-modulus-hyperimmune`); definition (`def-preserve-hyperimmunity`);
   preservation of hyperimmunity implies cone avoidance (`thm-hyperimmunity-cone`), converse
   admitted (`thm-hyperimmune-modulus`, `cor-hyperimmunity-equivalence`); compact questions
   (`thm-local-hyperimmunity`, `def-disjunctive-compact`, `lem-seetapun-compact`); WKL,
   COH, RT²₂ (`thm-hyperimmunity-examples`); summary figure `avoidance-relations`;
   exercises: monotone envelopes, WKL and RT³₂, strong preservation for RT¹₂, the
   unrelativized separation.

## 4. Proof techniques

- **The three-case argument** (cases: wrong value reachable, right value unreachable,
  otherwise the set is simple): lessons 2–4; the two-case version for definitions in
  lesson 5; the version with bounds for hyperimmunities in lesson 6.
- **Forcing questions relative to the condition** (Σ⁰₁(ℳ)-preservation): lessons 2–6.
- **Over-approximation** (asking the question for all levels of a tree, all partitions,
  all instances, so that compactness brings it down to Σ⁰₁): lessons 2–4.
- **Compactness used twice** (König's lemma for the complexity of the question, Scott
  ideals or the cone avoidance basis theorem for the witness of a negative answer): lesson 4.
- **Reservoirs in the class being preserved** (cone-avoiding reservoirs, Scott ideals
  obtained by preserving the property along WKL): lessons 3–6.
- **Disjunctive forcing and Lachlan's disjunction**: lessons 3–6.
- **Thinning by finitely many applications of the pigeonhole principle** to give limit
  colors to finitely many elements: lesson 4.
- **Relativization as a tool**: products of problems (lesson 1), making a set Δ⁰₂ by a
  cone-avoiding set and then using a modulus (lessons 2 and 6).

## 5. Choices

- **Overlaps handled by citation.** The abstract preservation theorems for sufficiently
  generic sets (cone avoidance, non-Σ⁰ₙ sets, hyperimmunity, PA degrees) are in
  `effective-forcing/forcing-question`; cone avoidance for COH, the Dzhafarov–Jockusch
  theorem and Seetapun's theorem through the decomposition are in `ramsey-theorem`;
  preservation of weakness properties and iterating and dovetailing are in
  `reducibilities/preservation`. The course cites them and proves only what they do not:
  the problem-level properties, the local version Σ⁰₁(ℳ) of the abstract theorems, the
  disjunctive versions, the direct proof of Seetapun's theorem, and the relations between
  the properties.
- **Σ⁰₁(ℳ)-preservation (new definition).** The monograph and `effective-forcing` state
  the abstract theorems for Σ⁰₁-preserving questions, while all applications to problems
  use questions that are Σ⁰₁ relative to the reservoir. One definition, parametrized by a
  class ℳ, covers computable reservoirs relative to Z, cone-avoiding reservoirs and
  reservoirs in a Scott ideal, and makes the three-case argument a theorem rather than a
  pattern.
- **Seetapun's theorem revisited directly.** The existing proof (`ramsey-theorem/seetapun`)
  goes through the decomposition, and its Dzhafarov–Jockusch step is already interpreted as
  a forcing question in `effective-forcing/mathias-forcing`. Revisiting it again would
  duplicate. The course instead proves Seetapun's theorem directly, with the forcing of
  the monograph's exercise (two stems homogeneous for the two colors, a question about all
  partitions of the reservoir). This is the original route (Seetapun's proof, in
  Dzhafarov–Mummert §8.3, with blobs and Seetapun trees), and it is the model for the
  design of notions of forcing for other Ramsey-type problems. The Scott ideal version is
  used, for consistency with `ramsey-theorem/cone-avoidance`; the cone-avoiding reservoir
  version is an exercise.
- **Shoenfield-type theorem.** `turing-degrees` proves the high set avoiding a cone and,
  in an exercise, the version for an arbitrary set. Lesson 2 restates it relativized as
  `thm-delta2-cone-avoidance`, proved through the forcing question, since it is used in
  lessons 2 and 6 (strong cone avoidance reduces to Δ⁰₂ instances; preservation of
  hyperimmunity implies cone avoidance).
- **Admitted results.** The two converse directions of the theorem of Downey et al.
  (cone avoidance implies preservation of non-Σ⁰₁ definitions, which uses cototal
  enumeration degrees; and every non-decreasing hyperimmune function is a modulus relative
  to some set, their Lemma 2.6) are stated without proof, as in the monograph. Solovay's
  characterization of sets with a modulus is mentioned only. The results on several
  definitions and several hyperimmunities (Patey, Wang) are stated with references.
- **Strong versions.** Strong cone avoidance appears in lessons 1–3; strong preservation
  of definitions and hyperimmunities only for RT¹₂ and COH, in exercises.
- **Six lessons.** The first plan had five; the lesson on disjunctive questions and
  Seetapun's theorem exceeded 4000 words and was split, with strong cone avoidance of COH
  moved from lesson 2 to lesson 3 so that lesson 2 stays within 45 minutes.
- **Excluded.**
  - The forcing-design methodology (stems, extendibility, block extendibility, the
    Erdős–Moser and free set theorems; monograph chapter *Forcing design*): it belongs to
    `separation-design`; lesson 4 points to it.
  - PA avoidance and merging (monograph chapter *Compactness avoidance*): it belongs to
    `compactness-avoidance`; `effective-forcing` already has `thm-question-pa`.
  - The exercises of the monograph on COH and Π⁰₁(∅′) classes (Jockusch–Stephan) and on
    low solutions of COH (Patey): they belong to `ramsey-theorem/cohesiveness` and to
    `lowness`.
  - The proof that RT²₂ does not preserve two non-Σ⁰₁ definitions: it needs a
    construction of a specific coloring (Patey 2016) and belongs to the custom properties
    course.
  - Lower bounds for RT³₂ beyond `prop-rt32-jump` (Hirschfeldt–Jockusch PA over ∅′):
    `ramsey-theorem`.

## 6. Comparison with the literature

- **Patey, *Lowness and avoidance*, chapter *Cone avoidance*** (main source):
  - *Context and motivation*: lesson 1 (with the proposition on ω-models replaced by a
    citation of `lem-preservation-ideal`);
  - *First examples*: lesson 2 (Cohen and Π⁰₁ classes cited; the Shoenfield forcing as
    `thm-delta2-cone-avoidance`);
  - *Forcing question*: lesson 2 (the dividing-line figure, the Σ⁰₁-preserving theorem in
    the local form);
  - *Seetapun's theorem*: lessons 3 and 4 (Wang's exercise as `thm-coh-strong-cone`; the
    disjunctive question; the Seetapun–Slaman exercise as `thm-seetapun-direct`);
  - *Preserving definitions*: lesson 5;
  - *Preserving hyperimmunities*: lesson 6.
  Differences: the monograph's exercise "a relation is a forcing question iff it answers
  yes on conditions forcing φ and no on conditions forcing ¬φ" is not correct as stated:
  the condition is necessary, but not sufficient (counterexample for Cohen forcing in
  `exr-question-converse`). The monograph's statement of the converse lemma of Downey et al.
  ("C ≰_T Z ⊕ G") and the last line of its proof of the converse corollary contain typos;
  the course follows the paper. The proof of the hyperimmunity theorem in the monograph
  refers to the wrong lemma for density; the course gives the proof in full.
- **Dzhafarov–Mummert**, Section 8.3 (Seetapun's original proof, 2-fold Mathias forcing
  with homogeneity clauses, Lachlan's disjunction, Lemma 8.3.7), Sections 3.6 and 4.6
  (preservation).
- **Hirschfeldt, *Slicing the Truth***, Section 6.7: Seetapun's theorem through cohesiveness
  (cited via `ramsey-theorem`).
- **Downey, Greenberg, Harrison-Trainor, Patey, Turetsky (2022)**: Theorem 2.1
  (equivalences), Corollary 2.4 (one cone implies ω cones), Lemmas 2.6, 2.8, 2.9,
  Corollaries 2.7, 2.10, 2.18, Theorems 2.11, 2.12 (unrelativized separations),
  Corollaries 3.4, 3.6 (k hyperimmunities and k definitions). Checked on the arXiv
  version (1903.04273v1).

## 7. Pedagogical plan

1. `avoidance-properties`: coding as the weakest strength; the table of examples with the
   two kinds of failure of strong cone avoidance (direct coding for WKL, growth for RT²₂);
   quizzes on the table and on relativization; the artificial problem as a warning.
2. `forcing-question-method`: the three-case argument stated before any definition; figure
   `dividing-line` (Jockusch–Soare and Cohen questions as the two extreme positions);
   over-approximation named; quizzes on the cases and on the graph of C.
3. `disjunctive-question`: why arbitrary instances force reservoirs to carry the weakness
   property; COH inherits strong cone avoidance from RT¹₂; disjunctive definitions with
   quizzes; the two-cones exercise.
4. `seetapun-forcing`: figure `seetapun-condition` (stems, reservoir, the split below ℓ and
   the thinned reservoir); quizzes on thinning, on the Scott ideal and on the side;
   comparison with the decomposition proof.
5. `non-sigma1-definitions`: Σ⁰₁ versus computable; examples (J, c.e. sets, ∅″); the
   two-case argument; the common scheme of the applications; one definition versus two.
6. `hyperimmunities`: the duality between coding and growth; moduli; the role of the set W
   in the relativized argument; compact questions; figure `avoidance-relations`.

Figures are generated by `scripts/figures/avoidance.py` (deterministic).

## 8. Sources, lesson by lesson (checked 2026-11-12)

1. Patey, monograph, *Cone avoidance*, §§ Context and motivation, First examples;
   Dzhafarov–Mummert Definition 3.6.11, Section 4.6, Section 8.3; Jockusch–Soare TAMS 173
   (1972); Dzhafarov–Jockusch JSL 74 (2009); Seetapun–Slaman NDJFL 36 (1995); Downey et al.
   JSL 87 (2022).
2. Monograph, §§ First examples, Forcing question; Monin–Patey, Adv. Math. 352 (2019),
   Lemma 2.4 (as stated in the monograph's list of contributions); Downey et al. Lemma 2.8
   (Patey's version of the Shoenfield forcing); `turing-degrees/low-and-high`.
3. Wang, Adv. Math. 261 (2014); monograph § Seetapun's theorem (exercise on COH, disjunctive
   question); Dzhafarov–Mummert Lemma 8.3.7, Definition 8.3.5; Downey et al. Corollary 2.4.
4. Seetapun–Slaman (1995); Dzhafarov–Mummert §8.3 (Remark 8.3.6, proof of Theorem 8.3.1);
   monograph exercise *Seetapun and Slaman*; Dzhafarov–Jockusch (2009); Cholak–Jockusch–
   Slaman JSL 66 (2001).
5. Wang, JSL 81 (2016), doi:10.1017/jsl.2016.10, arXiv:1408.1465; Patey, Israel J. Math.
   216 (2016), 905–955; Downey et al. Theorem 2.1, Lemma 2.13, Corollary 2.18; monograph
   § Preserving definitions.
6. Downey et al. Lemmas 2.6, 2.9, Corollaries 2.7, 2.10, Theorems 2.11, 2.12, Corollaries
   3.4, 3.6; Monin–Patey (2019) Lemma 2.6 (per the monograph); Patey, Computability 6
   (2017), 209–221; Solovay, TAMS 239 (1978); Jockusch–Soare (1972) Theorem 2.4 (as quoted
   by Downey et al.); monograph § Preserving hyperimmunities.

## 9. Recent literature

Checked on 2026-11-12 (web search and the arXiv text of Downey et al.):

- **Downey, Greenberg, Harrison-Trainor, Patey, Turetsky, *Relationships between
  computability-theoretic properties of problems*** (JSL 87 (2022), arXiv:1903.04273): the
  equivalences of lesson 6 and the failure of the unrelativized versions; it fixed the
  statements of the admitted results, which are garbled in the monograph, and supplied the
  example of the principal function of a Δ¹₁-random set and the unrelativized separation
  of the last exercise of lesson 6.
- **Wang, *The definability strength of combinatorial principles*** (JSL 81 (2016)):
  preservation of the arithmetic hierarchy; cited in lesson 5. Pages not confirmed; DOI
  confirmed.
- **Patey, *Ramsey-like theorems and moduli of computation*** (arXiv:1901.04388): all
  known failures of cone avoidance for Ramsey-like theorems come from instances whose
  solutions dominate moduli; not cited in the lessons (not read in full), a possible
  addition to lesson 6.
- No simpler proof of Seetapun's theorem than the two in the platform was found.

## 10. Open points

- Monin–Patey (2019) "Lemma 2.4" and "Lemma 2.6" are cited through the monograph's list of
  contributions; the paper itself was not checked.
- Solovay (1978) and Jockusch–Soare Theorem 2.4 are cited as quoted by the monograph and by
  Downey et al.
- The durations of lessons 2, 4 and 6 (45 minutes) are below the raw word count divided by 55
  (about 3000 words each, a large part of which is mathematics); the same convention as in
  `effective-forcing`.
- A proof of Lemma 2.6 of Downey et al. (every non-decreasing hyperimmune function is a
  modulus relative to some set) would fit lesson 6; the proof in the arXiv version needs a
  small correction in its Case 1 (the condition μ should fix column x up to f(x) + 1), so it
  was left admitted.
- Pointers to add in other courses (not done here, outside the allowed files): see the
  report.

## 11. History

- **2026-11-12.** Course created: six lessons, three figures
  (`scripts/figures/avoidance.py`), design log.
