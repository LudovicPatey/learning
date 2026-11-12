# Design log: Cohen genericity

## 1. Objectives

After the course, a student can:

- translate a finite extension construction into a list of dense sets of strings, and a
  statement "there is a set with property P" into "every sufficiently generic set has
  property P" (co-meager classes);
- state and use the levels of genericity (weakly n-generic, n-generic) and know which
  level a given argument needs;
- prove Kurtz's theorem (weakly 1-generic degrees = hyperimmune degrees), the
  Demuth–Kučera theorem (1-generic sets compute no DNC function), relativized cone
  avoidance, the Posner–Robinson join theorem and Friedberg's jump inversion theorem,
  and compute the jumps of n-generic sets;
- combine genericity with coding.

**Role.** Specialized course (not in a track; `tracks-design.md`: the finite extension
method and 1-genericity are already in the Turing degrees course, and the full theory of
n-genericity is needed only by some readers). It is the reference for Cohen genericity
cited by other courses: `martin-lof-randomness/random-dnc` (`thm-generic-not-dnc`),
`immunity-growth/high-or-dnc` (`cor-high-not-dnc`).

**Relation with the course on effective forcing** (being written in parallel). This
course stays self-contained and specific to Cohen forcing with strings. Left to effective
forcing:

- the forcing relation for arithmetic formulas in general (Feferman's syntactic forcing,
  the semantic forcing relation, their equivalence for sufficiently generic sets, the
  definability of forcing: forcing a Σ⁰ₙ formula is Σ⁰ₙ), and the Baire property;
- forcing with other notions of conditions: trees (Sacks, Jockusch–Soare forcing with
  Π⁰₁ classes), Mathias forcing;
- the forcing question (Monin–Patey) as a general method for preservation proofs.

Here, Σ⁰ₙ properties are decided by iterating the lowness of 1-generic sets
(`lem-relative-generic-low`, `thm-generic-jumps`, `thm-n-generic-decides`); the forcing
relation is not defined. `n-genericity.md` says so and points to the effective forcing
course without a link (the course does not exist yet; add a `:ref{to=...}` once it does).

## 2. Prerequisites assumed

- **Turing degrees** (course prerequisite): dense sets of strings `def-dense`, the
  finite extension lemma `lem-meet-dense`, cone avoidance `thm-cone-avoidance`,
  1-generic sets `def-1-generic`, `prop-1-generic`, generalized lowness
  `thm-generic-low`, high incomplete sets `cor-high-incomplete`, the use principle
  `prop-oracle-stages`, the computation function `thm-computation-function`.
- **Arithmetic hierarchy**: Post's theorem (lesson `post-theorem`).
- **Immunity and growth** (course prerequisite from 2026-11-12): hyperimmune functions
  `def-hyperimmune-fn`, DNC functions `def-dnc`, computably dominated sets
  (`def-computably-dominated`, defined in pi01-classes, which immunity-growth requires).
- **Fundamentals**: fixed point theorem with parameters `thm-fixed-point-parameters`.
- Open and closed classes `def-open-closed` (pi01-classes): recalled inline in
  `baire-category`.

## 3. Results

1. **baire-category.** `def-d-generic`, `def-sufficiently-generic`,
   `ex-generic-properties`, `lem-dense-open`, `def-meager`, `ex-nowhere-dense` (new),
   `prop-generic-comeager`, `thm-baire-category`; aside on Banach–Mazur games (new);
   exercises: computable sets and the cone of ∅′ are meager; closed meager classes
   (new); `exr-density-meager`.
2. **weak-genericity.** `def-weakly-generic`, `ex-weakly-generic` (new),
   `def-hyperimmune-function` (now a recall of `def-hyperimmune-fn`), `thm-kurtz`,
   `cor-delta2-weak-generic`; Andrews–Gerdes–Miller at levels 2 and 3 (admitted);
   exercises: complements, principal function hyperimmune.
3. **one-genericity.** `def-relative-genericity`, `ex-relative-genericity` (new),
   `prop-force-sigma1`, `thm-1generic-decides` (with the converse of Jockusch–Posner,
   sketched), `thm-generic-not-dnc`, `cor-generic-not-pa`, `thm-generic-cone`,
   `cor-meager-degrees`; exercises: 1-generic not computable, halves incomparable,
   left-c.e. sets are not 1-generic (new).
4. **posner-robinson.** `thm-jockusch-shore`, `cor-posner-robinson` (now in the full
   form: for Z ≥ A ⊕ ∅′, A ⊕ G ≡ G′ ≡ G ⊕ ∅′ ≡ Z), `cor-jump-inversion`,
   `cor-high-not-dnc`; exercises: joins with ∅′, low G with A ⊕ G ≡ ∅′, no 2-generic G
   for A Δ⁰₂ incomplete (new).
5. **n-genericity.** `prop-generic-hierarchy`, `lem-relative-generic-low`,
   `thm-generic-jumps`, `thm-n-generic-decides`, `ex-n-generic-decides` (new),
   `thm-low-generic-exists`; separation of all the notions (section new, with the degree
   form of Kurtz's theorem admitted); exercises: GLₙ, 2-generic sets are not high (with
   the corollary: 1-generic sets compute no non-computable c.e. set).

## 4. Proof techniques

- **Finite extensions as dense sets** (all lessons; introduced in Turing degrees): the
  translation between constructions and co-meager classes (`prop-generic-comeager`).
- **Splitting / perfect tree of finite extensions**: `thm-baire-category`.
- **Escape (domination) arguments**: Kurtz (1 ⇒ 3), principal function exercise; from
  the course on immunity and growth.
- **Finite injury without restraints**: Kurtz (1 ⇒ 3); from the course on c.e. degrees.
- **Meet or avoid / forcing Σ⁰₁ properties**, "forcing the jump" (Soare):
  `thm-1generic-decides`, `thm-generic-low`, `lem-relative-generic-low`.
- **Fixed point theorem against a generic**: Demuth–Kučera.
- **Relativized cone avoidance**: `thm-generic-cone`, `cor-meager-degrees`.
- **Coding into a generic set** with decoding by a non-c.e. oracle: Jockusch–Shore.
- **Iterating lowness through the jumps**: `thm-generic-jumps`, `thm-n-generic-decides`.
- **Quantifier counting** for the complexity of W ∪ W^⊥: `prop-generic-hierarchy`.

## 5. Choices

- **Order** baire → weak → 1-generic → Posner–Robinson → n-generic, as in Monin–Patey's
  chapter. Weak genericity before 1-genericity because it is the simplest effective
  notion and Kurtz's theorem connects it to the course on immunity and growth.
- **No general forcing relation** (left to effective forcing, see §1). The jump approach
  is shorter and enough for every result of the course.
- **Kurtz's theorem in the "computes" form, proved; the degree form admitted.** The
  degree form (every hyperimmune degree contains a weakly 1-generic set,
  Downey–Hirschfeldt 2.24.14) needs a coding layer on top of the construction; it is
  only used for separations, which are stated with the admitted result.
- **Separation of n-genericity from weak n-genericity** through the degree form of
  Kurtz's theorem and `thm-generic-jumps` (Downey–Hirschfeldt, Corollary 2.24.20), which
  works at every level. Before 2026-11-12 the text used "no 1-generic set has c.e.
  degree (Jockusch)" for n = 1 and admitted the general case without reference. The
  c.e.-degree fact is now derived in the second exercise of `n-genericity`.
- **Posner–Robinson in the full form** Z ≥ A ⊕ ∅′ (Downey–Hirschfeldt 2.16.2, 2.24.4):
  it contains both previous corollaries (Z = A ⊕ ∅′; A = ∅′ gives jump inversion).
- **Proof of Demuth–Kučera by the fixed point theorem** (Monin–Patey), rather than
  Downey–Hirschfeldt's proof through a co-c.e. set of strings: it shows the fixed point
  technique of the fundamentals course at work.
- **Excluded:** pb-genericity and array computability (Downey–Hirschfeldt 2.24.21 ff.),
  1-generic sets are CEA (Jockusch, DH 2.24.9; a long combinatorial proof), the
  degrees below 1-generic degrees, elementary equivalence of the degrees below
  arithmetically generic degrees (Jockusch); Banach–Mazur games only as an aside.
  Reasons: length, and they belong to a course on the structure of the degrees.
- **Measure versus category** is mentioned (density ½, DNC functions, Barmpalias–Day–
  Lewis-Pye) but not developed; it belongs to the randomness track.

## 6. Comparison with the literature

- **Monin–Patey, chapter *Cohen forcing*.** Same material and order: Σ⁰₁ forcing (finite
  extension and topological approaches), effective genericity (weak 1-genericity and
  Kurtz, Andrews–Gerdes–Miller, 1-genericity, Demuth–Kučera, cone avoidance, Posner–
  Robinson via Jockusch–Shore, meager classes), Σ⁰ₙ forcing (semantic, syntactic,
  Baire property), arbitrarily generic sets. Differences: the course does not develop
  the forcing relation (left to effective forcing); its Kurtz construction is by one bit
  per stage instead of a recursive procedure; it adds the separations, the
  Banach–Mazur aside and the full Posner–Robinson statement.
- **Downey–Hirschfeldt §2.24** (Genericity and weak genericity) and **§2.16** (jump
  theorems): the source for Kurtz's degree results (2.24.11–2.24.20), Jockusch's jump
  theorem (2.24.3), Posner–Robinson (2.16.2, 2.24.4). They prove Posner–Robinson with an
  immune set; the course uses a non-c.e. set (Monin–Patey), and mentions the variant.
- **Soare 2016 §6.3–6.4 and §14.1–14.2**: forcing the jump (Theorem 6.3.2, Jockusch–
  Posner), exercises on 1-generic sets (6.3.5), Friedberg (6.4.1), Baire category and
  Banach–Mazur games (14.1.2–14.1.3), finite extension paradigm (14.2).

## 7. Pedagogical plan

- **baire-category.** Intuition: a construction is a list of dense sets; the generic
  point of view. Examples: `ex-generic-properties` (with item 4, blocks), a
  non-example ("0 ∈ G"), `ex-nowhere-dense` (singleton, closed class, finite sets dense
  but meager; disjoint dense classes show why open is needed). Intuition before Baire
  (branching construction); **figure** `baire-splitting` (nested intervals). Banach–
  Mazur aside.
- **weak-genericity.** `ex-weakly-generic` (non-computable, blocks, finite
  modifications; non-dense sets are not controlled). Intuition before Kurtz: the
  obstacle (Σ⁰₁ question), the remedy (bounded search with f), why hyperimmunity.
  **Figure** `kurtz-blocks` for (3 ⇒ 2). Hypotheses: item 2 of the corollary shows (1 ⇒ 3)
  needs hyperimmunity.
- **one-genericity.** **Figure** `meet-or-avoid`. `ex-relative-genericity` (dependence on
  the oracle, no set generic relative to itself). Intuition before Demuth–Kučera.
  Counterexamples: weak genericity does not suffice for Demuth–Kučera (degree 0′);
  genericity relative to C is needed in cone avoidance (C = G).
- **posner-robinson.** Intuition: coding plus genericity, the decoding obstacle, the role
  of the non-c.e. oracle. **Figure** `jockusch-shore-coding`. Necessity of the
  hypotheses (A computable fails; Z ≥ ∅′). Exercise: 2-generic sets do not work.
- **n-genericity.** Method stated (iterate lowness). `ex-n-generic-decides` (totality of
  Φ^X_e, the Σ⁰₂ set of strings made explicit). Counterexample "X is finite" for the
  restriction to generic extensions. **Figure** `genericity-hierarchy` with the
  separating sets.

## 8. Sources (checked against the books on 2026-11-12)

- **baire-category.** Baire 1899; Cohen 1963; Feferman 1965; Jockusch 1980; Soare 2016
  §14.1 (Theorem 14.1.2 Baire, Theorem 14.1.3 Banach–Mazur, stated with player I as the
  player who wants to land in the class; Exercise 14.1.4 disjoint dense sets; Exercise
  14.1.6 first category); Oxtoby (general reference, chapter numbers not checked, so not
  given); Monin–Patey, *Cohen forcing*, topological approach.
- **weak-genericity.** Kurtz 1981 (thesis), Kurtz 1983 (JSL 48, 764–770, from the DH
  bibliography); Downey–Hirschfeldt Definition 2.24.10, Theorems 2.24.12 (principal
  function, our exercise for n = 0), 2.24.14, Corollary 2.24.19, Proposition 2.24.2
  (c.e. sets compute 1-generic sets); Andrews–Gerdes–Miller, APAL 165 (2014) 803–811
  (from the Monin–Patey bibliography); Monin–Patey section *Effective genericity* for
  both AGM results (weakly 2-generic ⇔ ∅′-hyperimmune; escaping functions computing no
  weakly 3-generic set).
- **one-genericity.** Jockusch 1980; Demuth–Kučera, CMUC 28 (1987) 85–94 (checked
  against the DH and MP bibliographies); Soare 2016 Theorem 6.3.2 (Jockusch–Posner),
  Exercise 6.3.5; DH Theorem 2.24.5; Barmpalias–Day–Lewis-Pye, PLMS 109 (2014) 1–39
  (checked online); Monin–Patey (left-c.e. exercise).
- **posner-robinson.** Posner–Robinson, JSL 46 (1981) 714–722; Jockusch–Shore, JSL 49
  (1984) 1205–1236; DH Theorem 2.16.2 (attributed to Posner–Robinson, proof due to
  Jockusch–Shore) and 2.24.4 (1-generic version); Friedberg 1957, Soare Theorem 6.4.1;
  Shore–Slaman, Math. Res. Lett. 6 (1999) 711–722 (checked online); Day–Dzhafarov,
  arXiv:1209.3282 (introduction read).
- **n-genericity.** Feferman 1965; Jockusch 1980 (DH Theorem 2.24.3); Kurtz 1981, 1983
  (DH 2.24.11–2.24.14, 2.24.20); Soare Exercise 6.3.5; Monin–Patey sections on Σ⁰ₙ
  forcing and arbitrarily generic sets.

## 9. Recent literature

Checked (web search and the introduction of the papers):

- **Attribution of Posner–Robinson** (open point of REVIEW-2026-11). Downey–Hirschfeldt
  attribute the full join theorem to Posner–Robinson (1981) and the proof to
  Jockusch–Shore (1984); Day–Dzhafarov (2012) state that the Posner–Robinson
  construction is a Cohen forcing construction whose set can be taken 1-generic;
  Monin–Patey name the coding theorem after Jockusch–Shore. The notes now say this;
  the theorem keeps its label and name.
- **Shore–Slaman (1999)**: the extension to the n-th jump; **Day–Dzhafarov (2012)**:
  the set cannot be n-generic for n ≥ 2 nor 2-random, and at n = 1 weak 2-genericity
  already prevents it. Added to the notes of `posner-robinson`, with a new exercise
  proving the 2-generic case at n = 1 from `thm-generic-cone`.
- **Andrews–Gerdes–Miller (2014)**: restored the statement that the analogy with
  escaping functions breaks at weak 3-genericity, which the previous review had removed
  as unchecked; it is in Monin–Patey with proof.
- **Barmpalias–Day–Lewis-Pye (2014)**, *The typical Turing degree*: the systematic
  comparison of measure and category; cited in `one-genericity`.
- No simpler proof of the main theorems was found; the presentations of Monin–Patey
  and Downey–Hirschfeldt are the current standard ones.

## 10. Open points

- The venue of Day–Dzhafarov is given as an arXiv preprint (2012): the arXiv page says it
  was submitted to the proceedings of the 2011 Asian Logic Conference; the published
  version was not checked.
- The precise statement of Day–Dzhafarov at n = 1 (weak 2-genericity) is taken from
  their introduction; the exact hypotheses on A were not read.
- When the effective forcing course exists, link it from `n-genericity` (intro) and
  possibly from `one-genericity` (forcing the jump).
- `baire-category` cites `def-open-closed` (pi01-classes), now reachable through the
  course prerequisite immunity-growth; the definition is also recalled inline.
- `martin-lof-randomness/random-dnc` cites `thm-generic-not-dnc`; it could add
  `cohen-genericity/one-genericity` as a lesson prerequisite (decision for the
  coordinator, REVIEW-2026-11).

## 11. History

- **2026-11-12** — Design and pedagogical revision. Course prerequisite
  `immunity-growth` added (hyperimmune functions, DNC functions, computably dominated
  sets were redefined or used without prerequisite); lesson prerequisites
  `immunity-growth/immune-sets` (weak-genericity) and `immunity-growth/dnc-functions`
  (one-genericity). New labels: `ex-nowhere-dense`, `ex-weakly-generic`,
  `ex-relative-genericity`, `ex-n-generic-decides`; no label removed or moved.
  `cor-posner-robinson` strengthened to the full Posner–Robinson statement. New
  figures (generator `scripts/figures/cohen-genericity.py`): Baire splitting, Kurtz
  blocks, meet or avoid, Jockusch–Shore coding, genericity hierarchy. New section
  "Separating the notions" in `n-genericity`, replacing the unreferenced admitted
  separation; new section "Higher levels" in `weak-genericity`. New exercises: closed
  meager classes, left-c.e. sets are not 1-generic, 2-generic sets and
  Posner–Robinson. References checked against Downey–Hirschfeldt, Soare, Monin–Patey;
  unsupported claims removed (Jockusch "1-generic degrees are never c.e." is now
  derived and credited to Jockusch–Posner via Soare). Durations recomputed.
