# Design log: Effective forcing

This file is the memory of the course (see "Designing tracks and courses" in
`AGENTS.md`). It is not rendered.

## 1. Objectives

After the course, a student can:

- describe a construction of computability theory as a notion of forcing (conditions,
  members, extension, dense sets), and recognize Cohen, Jockusch–Soare, computable Sacks
  and computable Mathias forcing as instances;
- prove the existence of generic filters, effectively when the dense sets are uniformly
  effectively dense, and read off properties of sufficiently generic sets from density
  statements proved in earlier courses;
- define the forcing relation for arithmetic formulas, prove extension, consistency and
  density, and the theorem on forcing and truth for n-generic filters;
- compute the complexity of forcing for Cohen forcing, and derive the jumps of n-generic
  sets and the preservation of the arithmetic hierarchy;
- compare tree forcings with Cohen forcing through the complexity of their conditions,
  and use the decision of Σ⁰₂ sentences on all members (generalized low₂ generic sets);
- state and use the properties of Sacks generic sets (computably dominated, minimal, not
  generalized low);
- define a forcing question, check its definability, compactness and merging, and derive
  cone avoidance for iterated jumps, preservation of hyperimmunity, and avoidance of PA
  degrees; analyze computable Mathias forcing with these tools.

**Role.** First course of the track "Lowness and avoidance" (`tracks-design.md`); it
was written on 2026-11-12 as a specialized course, before the track existed. It is the place
where the general framework of forcing is explained; the courses on Cohen genericity, Π⁰₁
classes, immunity and growth, structure of the Turing degrees and Ramsey's theorem use
particular cases of it and point here. It fixes for the track: notions of forcing and
members (`def-forcing-notion`), the conventions for Mathias conditions (stem, reservoir,
compatible strings, reservoirs in a class ℳ; `ex-forcing-notions` item 4, aligned with
`ramsey-theorem/def-mathias-condition`), sufficiently generic sets (`def-generic-notion`),
formulas with oracle Z ⊕ G (`def-forcing-formula`, `ex-forcing-formulas` item 4), the
strong forcing relation (`def-forcing-relation`), n-generic filters and forcing and truth,
and forcing questions (`def-forcing-question`, possibly restricted to some levels;
compactness and merging at level 1).

## 2. Prerequisites assumed

- Turing degrees: oracle computations, use principle (`thm-use-principle`,
  `prop-oracle-stages`), finite extension method (`def-dense`, `lem-meet-dense`,
  `thm-cone-avoidance`).
- Arithmetic hierarchy: relativized classes (`def-relativized-hierarchy`), Post's theorem
  (`thm-post`), strictness (`cor-hierarchy-strict`), c.e. characterizations
  (`thm-ce-characterizations`).
- Cohen genericity: sufficiently generic sets (`def-sufficiently-generic`, `def-d-generic`,
  `ex-generic-properties`), 1-genericity and forcing Σ⁰₁ (`prop-force-sigma1`),
  n-genericity (`def-relative-genericity`, `thm-generic-jumps`, `thm-n-generic-decides`,
  `thm-low-generic-exists`).
- Π⁰₁ classes: weak König's lemma, effective compactness (`prop-pi01-emptiness`,
  `prop-pi01-equivalent`), basis theorems and their lemmas (`thm-low-basis`,
  `thm-dominated-basis`, `lem-uniform-bound`, `lem-uniform-cone`,
  `thm-cone-avoidance-basis`), PA degrees (`def-pa-degree`, `thm-dnc2-no-computable`).
- Immunity and growth: f-trees and their lemmas (`def-function-tree`,
  `lem-ftree-noncomputable`, `lem-ftree-domination`, `thm-martin-miller-ftrees`),
  hyperimmune functions (`def-hyperimmune-fn`), dominant functions and Martin's theorem
  (`def-dominant`, `thm-martin-domination`).
- Structure of the Turing degrees (lesson `sacks-forcing` only): splitting trees
  (`lem-splitting-dichotomy`, `lem-splitting-consequences`, `thm-minimal-degree`),
  independence of the columns of a 1-generic set (`thm-generic-independent`).
- Ramsey's theorem (lesson `mathias-forcing` only, since 2026-11-13): `def-mathias-condition`,
  `thm-coh-cone-avoidance`, `thm-dj-cone-avoidance`. Lesson 1 restates the Mathias
  conventions, so that the rest of the course can be read without it.

## 3. Results, lesson by lesson

1. **Notions of forcing** (`notions-of-forcing`): definition with closed classes of
   members and refinement (`def-forcing-notion`); four examples (`ex-forcing-notions`),
   with the Mathias conventions of the track; refinement fails for classes of positive
   measure (`rem-refinement-needed`); filters, density, genericity (`def-generic-filter`);
   Rasiowa–Sikorski (`lem-rasiowa-sikorski`); the generic set (`lem-generic-set`).
2. **Sufficiently generic sets** (`generic-sets`, new on 2026-11-13): sufficiently
   generic sets (`def-generic-notion`); density below a condition (`lem-dense-below`);
   properties recast from earlier courses (`ex-generic-notions`); effective genericity
   (`thm-effective-generic`, `ex-low-basis-forcing`); formulas in normal form
   (`def-forcing-formula`, `ex-forcing-formulas`).
3. **The forcing relation** (`forcing-relation`): forcing (`def-forcing-relation`,
   `ex-forcing-relation`: Cohen forces "G infinite", Jockusch–Soare forces totality only
   when true on all members, Sacks forces totality with a counterexample member); basic
   properties (`prop-forcing-basic`); n-generic filters (`def-n-generic-notion`); forcing
   and truth (`thm-forcing-truth`); forcing as density (`cor-forcing-density`); weak
   forcing (`exr-weak-forcing`).
4. **Definability of forcing for Cohen forcing** (`cohen-forcing`): forcing Σ⁰ₙ is Σ⁰ₙ
   (`thm-cohen-forcing-definable`); the two notions of n-genericity coincide
   (`thm-cohen-n-generic`); n-generic sets below ∅⁽ⁿ⁾ (second proof of
   `thm-low-generic-exists`); jumps (`cor-cohen-jumps`); preservation of the arithmetic
   hierarchy (`thm-cohen-preservation`) and of non-computability in ∅⁽ⁿ⁾
   (`cor-cohen-jump-cone`).
5. **Forcing with Π⁰₁ classes and perfect trees** (`forcing-with-trees`): complexity of
   Jockusch–Soare forcing, including a Π⁰₂-completeness result for forcing a Π⁰₁ sentence
   (`prop-js-complexity`); complexity of computable Sacks forcing
   (`prop-sacks-complexity`); deciding Σ⁰₂ sentences on all members by a Σ⁰₂ question
   (`prop-tree-sigma2`); G″ ≤ G′ ⊕ ∅″ (`thm-tree-gl2`); exercise: low₂ computably
   dominated members (`exr-low2-dominated`).
6. **Computable Sacks forcing** (`sacks-forcing`): generic sets are non-computable,
   computably dominated and minimal (`prop-sacks-generic`); not generalized low
   (`thm-sacks-not-gl1`); exercises: computable traceability; failure for Jockusch–Soare.
7. **The forcing question** (`forcing-question`): definition and Σ⁰ₙ-preservation
   (`def-forcing-question`), questions restricted to some levels; Cohen
   (`ex-cohen-question`); tree forcings at all levels (`thm-tree-question`); preservation
   of the hierarchy (`thm-question-preservation`, `cor-question-jump-cone`).
8. **Compactness and merging** (`compactness-merging`, new on 2026-11-13): compactness and
   hyperimmunity (`def-question-compact`, `thm-question-hyperimmunity`); merging and PA
   degrees (`def-question-merging`, `thm-question-pa`); table of the properties of the
   four questions; ω-merging and DNC functions (`exr-sacks-dnc`).
9. **Mathias forcing and preservation** (`mathias-forcing`): the question at level 1
   (`prop-mathias-question`); cohesive sets avoiding a cone, preserving hyperimmunity and
   computing no DNC function (`thm-mathias-coh-preservation`); generic sets are high
   (`prop-mathias-dominant`); no Σ⁰₂-preserving question (`cor-mathias-no-sigma2`); the
   Dzhafarov–Jockusch question as a forcing question (discussion).

## 4. Proof techniques

- **Genericity and density** (Rasiowa–Sikorski, density below a condition): lesson 1,
  used throughout.
- **Compactness** to bring the forcing of Σ⁰₁ sentences down to Σ⁰₁: lessons 3 and 4 (weak
  König's lemma on the strings or nodes that have not converged).
- **Induction on formulas** with a semantic base and a universal clause through
  extensions: lesson 2 (properties of forcing, forcing and truth), lesson 6 (the forcing
  question for tree forcings).
- **Quantifier counting** on the forcing relation: lessons 3 and 4, exercises of lesson 4.
- **The density argument by comparison with a Σ⁰ₙ set** ("U ≠ A"): lesson 3, then lesson 6
  in abstract form; the figure `question-density`.
- **Decision on all members** (tree forcings at level 2): lesson 4, with the certificate
  argument for G″ ≤ G′ ⊕ ∅″ (genericity used only for termination).
- **Escape nodes** (a Π⁰₁ subclass with room outside it, coding a bit of the jump):
  lesson 5.
- **Self-reference through an index** (choosing i as an index of the partial function g):
  lesson 6, avoidance of PA and DNC degrees.
- **Domination by thinning the reservoir**: lesson 7.

## 5. Choices

- **Framework.** A notion of forcing is a preorder with a closed non-empty class of members
  for each condition and the refinement property. This follows the "Cantor forcings" of
  Monin–Patey, but with filters that meet the dense sets of conditions deciding prefixes,
  instead of maximal filters. Reason: in computable Sacks forcing, the conditions having a
  given set as a path do not always form a filter, so Monin–Patey's identification of
  maximal filters with members is not correct in general; the version used here avoids
  the issue and agrees with Dzhafarov–Mummert (valuation maps) and Hirschfeldt.
- **Formulas.** Normal form with a functional at the base (Σ⁰₁: Φ^G_e(x⃗)↓), as in
  Monin–Patey's "requirements", rather than the language of second-order arithmetic as in
  Dzhafarov–Mummert. Reason: complexity computations become quantifier counts, and the
  link with Σ⁰ₙ(G) relations is immediate from the course on the arithmetic hierarchy.
  Negation is the dual formula, so ¬¬φ = φ.
- **Forcing relation.** Level-1 sentences are forced when all members satisfy them; then an
  existential and a universal clause. This is Monin–Patey's syntactic relation ⊩*. The
  semantic relation of Monin–Patey ("every sufficiently generic filter containing c") is
  ill-defined as stated (sufficient genericity depends on a family of dense sets); it is
  replaced by `cor-forcing-density`, which fixes the family (n-generic filters), and by
  weak forcing in an exercise.
- **Forcing question.** Defined for Σ⁰ₙ sentences only, with two properties (positive answer
  gives an extension forcing φ, negative answer an extension forcing ¬φ). Monin–Patey
  define it for Σ and Π sentences; the version here suffices for all applications and
  avoids the clause for Π sentences. Σ⁰ₙ-preservation is defined per condition (all that the
  density arguments need); the tree construction proves the uniform version.
- **Compactness and merging at level 1 only.** The preservation of hyperimmunity and of
  non-PA degrees is proved at level 1, where it is used in reverse mathematics, and the
  versions for G⁽ⁿ⁾ are stated in a remark with reference. This keeps the formulas
  "Φ^G_e(m)↓ < k" simple.
- **Split of tree forcings into two lessons.** The material on Jockusch–Soare and Sacks
  forcing exceeded 3400 words; complexity and the level-2 decision form one lesson
  (`forcing-with-trees`), the properties of Sacks generic sets another (`sacks-forcing`).
- **Effective genericity** is placed in lesson 2, with the sufficiently generic sets (it
  was in the Cohen lesson until 2026-11-13).
- **Lesson lengths (2026-11-13).** Durations are words/55 rounded to 5, at most 45. Lessons
  1, 2 and 6 of the first version (2840, 2840 and 2780 words at "45 minutes") were too
  long. Lesson 1 was split into `notions-of-forcing` and `generic-sets`; the formulas
  section moved from `forcing-relation` to `generic-sets`; effective genericity moved from
  `cohen-forcing` to `generic-sets`; `forcing-question` was split into `forcing-question`
  and `compactness-merging`. Nine lessons in all.
- **Oracle order Z ⊕ G** in relativized formulas, as in the other courses of the track and
  in `ramsey-theorem` (it was G ⊕ Z until 2026-11-13).
- **Results of other courses are cited, not reproved**: the basis theorems, the f-tree
  lemmas, Spector's splitting lemmas, cone avoidance for cohesiveness and the
  Dzhafarov–Jockusch theorem. The course reproves only results whose new proof shows the
  framework (second proofs of `thm-generic-jumps` and `thm-low-generic-exists`).
- **Excluded.** Forcing over models of arithmetic and conservation results
  (Dzhafarov–Mummert 7.6; belongs to induction-conservation); forcing with Π⁰₁ classes of
  positive measure and Kautz's characterization of weak n-randomness (Downey–Hirschfeldt
  7.2.5; randomness area); Sacks's minimal degree below 0′ (full approximation, not a
  forcing argument in this sense; admitted in degree-structure); thin classes (exercise of
  Monin–Patey; specialized); iterated and product forcing; forcing questions for the
  pigeonhole principle at level 2 (research literature, cited).

## 6. Comparison with the literature

- **Monin–Patey, chapter "Effective forcing"** (`external-data/monin-patey/parts/
  forcing-effectif.tex`): the main source. Sections: fundamentals (lesson 1), forcing
  relation (lesson 2), forcing with trees (lessons 4–5), computational complexity and
  forcing question (lessons 4, 6). Differences: filters instead of maximal filters (see
  Choices); the semantic relation replaced by density; explicit proof of the
  Π⁰₂-completeness of forcing a Π⁰₁ sentence for Jockusch–Soare forcing (Monin–Patey give
  the upper bound); the proof that Sacks generic sets are not generalized low is written
  with an explicit subtree R; the "Cohen forcing" chapter (forcing-cohen.tex) is covered by
  lesson 3 together with the course on Cohen genericity.
- **Dzhafarov–Mummert, Chapter 7** (Sections 7.2–7.5): notions of forcing with valuation
  maps, Rasiowa–Sikorski, forcing relation with negation clause, n-genericity, forcing and
  truth (Theorem 7.4.6), effective forcing (7.5.6), Cohen definability (Lemma 7.5.10,
  Propositions 7.5.11–7.5.12), Jockusch–Soare low₂ hyperimmune-free paths (Proposition
  7.5.8, Corollary 7.5.9), Mathias highness (Example 7.3.6). The course uses the same
  results with Monin–Patey's base clause.
- **Hirschfeldt, Slicing the Truth, Section 2.3** (forcing, generic filters, effective
  density, Propositions 2.6–2.7) and **Section 6.5** (Mathias forcing, Definition 6.40).
- **Downey–Hirschfeldt, Section 2.24**: n-genericity, Feferman's forcing relation in a
  footnote, Jockusch–Posner equivalence; Section 7.2.5 for Solovay genericity (excluded).
- **Soare 2016, Chapter 6** (finite extensions and forcing the jump) and **Chapter 12**
  (minimal degrees by function trees, Part III): the special cases.

## 7. Pedagogical plan

1. `notions-of-forcing`: intuition of the common pattern; four examples with a figure
   (`four-notions`, conditions and extensions as classes drawn at depth 6); quiz on
   refinement and on finite members of Mathias conditions; recast of earlier results.
2. `forcing-relation`: intuition for the universal clause (Cohen "G infinite");
   three examples contrasting Cohen, Jockusch–Soare and Sacks; quizzes on refinement in
   item 3 and on the common extension in the truth theorem; exercises on Σ⁰₂ forcing and
   weak forcing.
3. `cohen-forcing`: effective genericity and the low basis theorem as example; complexity
   of forcing with quizzes on weak König's lemma and on the role of a decidable order;
   n-genericity; preservation, with a quiz on the "U ≠ A" argument.
4. `forcing-with-trees`: comparison of where each notion is complex; hardness example;
   decision on all members versus Cohen's failure; quiz on the role of G′.
5. `sacks-forcing`: comparison table in prose with Cohen generics; figure `escape-tree`
   for the non-GL₁ proof; quiz on the role of the escape nodes.
6. `forcing-question`: intuition (the question as an interface); table of properties of
   the four notions; figure `question-density`; quizzes on compactness and on the
   self-referential index.
7. `mathias-forcing`: the level-1 question, the highness obstruction, and the
   Dzhafarov–Jockusch disjunctive question as the model for Ramsey-type theorems.

Figures are generated by `scripts/figures/effective-forcing.py` (deterministic).

## 8. Sources, lesson by lesson (checked 2026-11-12)

1. Rasiowa–Sikorski, Fund. Math. 37 (1950); Cohen, PNAS 50 (1963); Feferman, Fund. Math. 56
   (1965); Jockusch–Soare, TAMS 173 (1972); Sacks, Proc. Symp. Pure Math. 13 (1971);
   Mathias, Ann. Math. Logic 12 (1977). Hirschfeldt §2.3 (Propositions 2.6, 2.7);
   Dzhafarov–Mummert §§7.2–7.3 (Definition 7.2.1, Theorem 7.3.3); Monin–Patey, *Effective
   forcing*, "Fundamentals of forcing".
2. Feferman 1965; Downey–Hirschfeldt §2.24 (footnote to Definition 2.24.1);
   Dzhafarov–Mummert §7.4 (Definition 7.4.1, Proposition 7.4.2, Theorem 7.4.6);
   Monin–Patey, "Forcing relation".
3. Jockusch 1980; Dzhafarov–Mummert Lemma 7.5.10, Propositions 7.5.11–7.5.12, Theorem
   7.5.6; Hirschfeldt Proposition 2.7; Downey–Hirschfeldt §2.24 (Jockusch–Posner);
   Monin–Patey, *Cohen genericity* and *Effective forcing*.
4. Jockusch–Soare 1972; Monin–Patey, "Forcing with trees", "Complexity of partial
   orders", "Forcing Σ⁰₁/Π⁰₁ requirements", "Forcing Σ⁰₂/Π⁰₂ requirements";
   Dzhafarov–Mummert Proposition 7.5.8, Corollary 7.5.9 (low₂ hyperimmune-free path).
5. Spector, Ann. of Math. 64 (1956); Miller–Martin, Z. Math. Logik 14 (1968);
   Terwijn–Zambella, JSL 66 (2001); Soare 2016 Chapter 12; Monin–Patey theorem on the
   continuity of the Turing jump, and the exercise on computable traceability.
6. Monin–Patey, *Effective forcing*, "Forcing question" (preservation of the arithmetic
   hierarchy, of hyperimmunity, of non-PA degrees; Π-merging); Monin–Patey, *Pigeons do
   not jump high*, Adv. Math. (2019), doi:10.1016/j.aim.2019.06.026, arXiv:1803.09771;
   Patey, arXiv:1509.05340.
7. Hirschfeldt §6.5; Dzhafarov–Mummert Examples 7.2.5, 7.2.10, 7.3.6, 7.3.9;
   Jockusch–Stephan, MLQ 39 (1993); Cholak–Jockusch–Slaman, JSL 66 (2001);
   Dzhafarov–Jockusch, JSL 74 (2009); Patey, *Iterative forcing and hyperimmunity in
   reverse mathematics*, Computability 6 (2017), doi:10.3233/COM-160062.

## 9. Recent literature

Checked on 2026-11-12 (web search):

- **Monin–Patey, *Pigeons do not jump high*** (Adv. Math. 2019): custom forcing relations
  and questions for variants of Mathias forcing, to build non-high solutions of the
  pigeonhole principle. Cited in lessons 6 and 7 as the research use of the forcing
  question at level 2. Volume and pages were not confirmed; the DOI was.
- **Patey, *Controlling iterated jumps of solutions to combinatorial problems*** (arXiv
  1509.05340): forcing relations with the complexity of the formulas forced, for Mathias
  forcing. Cited in lesson 6 (journal version not checked).
- **Patey, *Iterative forcing and hyperimmunity in reverse mathematics*** (Computability
  2017; CiE 2015 version): preservation of hyperimmunity as a separation tool. Cited in
  lesson 7; page numbers not checked.
- A 2025 arXiv paper (*Ramsey-like theorems and immunities*, arXiv:2508.15597) states the
  definitions of Σ⁰₁-preservation and Σ⁰₁-compactness of a forcing question in the same
  form as here; not cited, since it was not read in full.
- No survey of the forcing question was found.

The literature did not change the mathematics of the course; it fixed the attributions of
the forcing question and the choice of level-1 compactness and merging.

## 10. Open points

- Volume and page numbers of *Pigeons do not jump high* (Adv. Math. 2019) are not
  confirmed; it is cited by DOI. Patey's Computability paper is cited by DOI and arXiv
  number.
- The levels-n versions of the hyperimmunity and PA theorems are stated without proof;
  a later revision could prove them with formulas "Φ^{G⁽ⁿ⁾}_e(m)↓ < k".
- `ramsey-theorem` is a course-level prerequisite since 2026-11-13, because of lesson 9
  (cone avoidance for COH and the Dzhafarov–Jockusch argument); lessons 1–8 do not need it.
  Lesson 9 points forward to `avoidance` (Σ⁰₁(ℳ)-preservation, disjunctive questions) by
  lesson links.
- The theorem that Sacks generic sets are not generalized low is attributed to the
  Monin–Patey book; an original source was not found.
- `degree-structure` is a course-level prerequisite only because of lesson 6
  (`sacks-forcing`).
- Lessons of the later courses cite this course by lesson link in a few places
  (`avoidance/forcing-question-method` and `avoidance/hyperimmunities` cite
  `effective-forcing/forcing-question` for compactness and "Φ^G_e(m)↓ < k", now in
  `compactness-merging`; `lowness/forcing-the-jump` lists `effective-forcing/cohen-forcing`
  as a prerequisite for `thm-effective-generic`, now in `generic-sets`). Label references
  are unaffected.
- `lowness` writes the oracle as G ⊕ Z in four places; the track uses Z ⊕ G.

## 11. History

- **2026-11-12.** Course created: seven lessons, three figures
  (`scripts/figures/effective-forcing.py`), design log.
- **2026-11-13: polishing pass.** The course becomes the first course of the track
  "Lowness and avoidance". Structure: nine lessons (two new: `generic-sets`,
  `compactness-merging`); honest durations. Mathematics: f-tree paths justified against
  `def-function-tree`; precise failure for Jockusch–Soare in the exercise of lesson 2; the
  case of the empty string in the solution of `exr-weak-forcing`; wrong lesson numbers
  ("lesson 5" for the forcing question) and the misattributed exercise in the notes of
  `forcing-with-trees` fixed; questions restricted to some levels allowed in
  `def-forcing-question`, as used by Mathias forcing and by the later courses; the level-n
  hyperimmunity remark now requires compactness for Σ⁰ₙ₊₁ sentences (as in Monin–Patey);
  in `mathias-forcing`, computability of reservoirs is used by preservation, not by
  property 1. Consistency: Mathias conventions (stem, reservoir, compatible, reservoirs in
  a class ℳ) introduced in lesson 1, matching `def-mathias-condition`; oracle order Z ⊕ G.
  Pedagogy: remark on classes of positive measure (refinement is needed), quiz on effective
  genericity, the named technique "genericity by density", introductions of the new
  lessons. References: Jockusch 1980 and Spector 1956 added to lesson 1; arXiv number of
  Patey 2017 confirmed (1501.07709); volume and pages of *Pigeons do not jump high* still
  unconfirmed (DOI only).

