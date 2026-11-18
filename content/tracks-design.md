# Design log of the tracks

This file records what each learning track is for, what it contains and why, and
the decisions taken when the tracks change (see "Designing tracks and courses" in
`AGENTS.md`). The tracks themselves are in `tracks.yaml`; each course has its own
log in `<course>/_design.md`.

The reader is a master's student who will do research in mathematical logic. A
track is the shortest sequence of courses after which such a student can read the
research literature of its area; everything else is a specialized course.

**Primary and secondary tracks.** The four tracks computability, algorithmic
randomness, reverse mathematics and higher computability are **primary**: they form
the common education of a researcher in the field, and the home page shows them. The
tracks lowness and avoidance, and models of arithmetic, are **secondary**
(`kind: secondary`): each is a research-oriented continuation that assumes a primary
track (computability theory, and the first-order part of reverse mathematics,
respectively), and they are shown only on the page of all tracks. A secondary track is
chosen when its subject is a specialization rather than a basis, but is long enough to
need its own dependency graph.

## Literature compared

- **Computability:**
  - Soare, *Turing Computability* (2016), Parts I–III;
  - Monin–Patey, *Computability theory* (the book this platform grew from);
  - Downey–Hirschfeldt, Chapter 2.
- **Randomness:**
  - Downey–Hirschfeldt, *Algorithmic Randomness and Complexity* (2010);
  - Nies, *Computability and Randomness* (2009);
  - the randomness chapter of Monin–Patey.
- **Reverse mathematics:**
  - Simpson, *Subsystems of Second Order Arithmetic* (2009);
  - Hirschfeldt, *Slicing the Truth* (2014);
  - Dzhafarov–Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs* (2022).
- **Higher computability:**
  - Sacks, *Higher Recursion Theory* (1990);
  - Chong–Yu, *Recursion Theory: Computational Aspects of Definability* (2015);
  - the higher computability chapter of Monin–Patey.
- **Computable analysis:** Weihrauch, *Computable Analysis* (2000).

## Computability theory

**Objective.** The common language of the other tracks: the models of computation and
their equivalence, c.e. sets and reductions, relative computability and the jump, the
arithmetic hierarchy, the first priority arguments, Π⁰₁ classes and basis theorems, and
the notions of computational weakness and strength measured by growth of functions.

**Techniques.** The track teaches, in this order:
- diagonalization (countability, fundamentals);
- arithmetization and normal forms (models of computation);
- the fixed point theorem (fundamentals);
- finite extensions and the limit lemma (Turing degrees);
- quantifier counting (arithmetic hierarchy);
- finite injury priority (c.e. degrees);
- compactness and forcing with Π⁰₁ classes (Π⁰₁ classes);
- domination and escape arguments (immunity and growth).

These are the techniques used without comment in the research literature of all four
areas.

**Comparison.**
- **Soare and Monin–Patey.** The track follows the common core of Soare (Parts I–II)
  and Monin–Patey.
- **Immunity and growth (from 2026-11-12, in the track).** Soare treats immunity,
  domination and DNC functions in Chapters 4–5, and Monin–Patey in a chapter of the
  main sequence. The randomness track depends on them: Martin-Löf randomness uses DNC
  functions and computably dominated degrees. Until 2026-11-12 the course was
  specialized; a core course depending on a specialized one was inconsistent.
- **Kept specialized:**
  - **Cohen genericity:** the finite extension method and 1-genericity are already in
    the Turing degrees course; the full theory of n-genericity is needed only by some
    readers.
  - **Structure of the Turing degrees** (exact pairs, embeddings, minimal degrees), as in
    Soare Part III.
  - **Infinite injury.**

**Excluded, with reasons.**
- **Strong reducibilities and Post's program** (Soare 3.8, Downey–Hirschfeldt 2.20). They
  are only mentioned in the course on c.e. degrees. A specialized course is possible
  later.
- **Lachlan games** (Soare Part IV). They are a presentation device rather than a body of
  results.
- **Computable structure theory.** A track of its own since 2026-11-18 (see below).

**Course added on 2026-11-12** (specialized at first; since 2026-11-13 the first course of
the track "Lowness and avoidance").
- **Effective forcing**: the forcing relation in general, its
  definability, forcing with trees (Sacks and Jockusch–Soare forcing), and the forcing
  question (Monin–Patey). It unifies techniques that are now spread over the Cohen
  genericity, Π⁰₁ classes, minimal degrees and Ramsey courses.

**Planned.**
- **Mass problems and natural degrees** (Monin–Patey): a specialized course, later.

## Algorithmic randomness

**Objective.** Randomness of infinite sequences through its three classical approaches —
incompressibility, effective null sets, and betting strategies — and their equivalence.

**Techniques.**
- Kolmogorov complexity and the KC theorem;
- effective measure arguments;
- universal tests;
- martingales and the savings trick;
- the interplay of randomness and Turing degrees (Kučera–Gács, DNC functions).

**Comparison.**
- Downey–Hirschfeldt (Chapters 3, 6, 7) and Nies (Chapters 2, 3, 7) both present the
  three approaches as the foundation of the area.
- Until 2026-11-12 the track had only the first two: martingales were mentioned in one
  sentence. A core course **martingales** is added after Martin-Löf randomness. It covers
  martingales and Ville's theorem, c.e. martingales and Schnorr's theorem, and computable
  and Schnorr randomness defined by martingales.
- **Enlarged on 2026-11-17** (from three to seven courses, about 11 to about 30 hours),
  after a comparison with the core parts of Downey–Hirschfeldt (Chapters 3–9 and 11) and
  Nies (Chapters 2–5 and 7), both of which go well beyond the three approaches:
  - `kolmogorov-complexity` gains three lessons: conditional complexity and the symmetry of
    information for C and K, and the comparison of C and K (Levin, Solovay); DH 3.2–3.3,
    3.10, Chapter 4; Nies 2.3–2.4.
  - `randomness-notions` (relative randomness, van Lambalgen, 2-randomness, weak
    2-randomness) becomes core: every reference treats it in its core chapters (DH 6.8–6.9,
    7.2; Nies 3.4–3.6).
  - New core course `left-ce-reals`: left-c.e. reals and halting probabilities, Solovay
    reducibility, Kučera–Slaman, Calude–Hertling–Khoussainov–Wang, Demuth's splitting,
    Solovay functions (DH 5, 9.1–9.5; Nies 3.2). Left-c.e. reals are to randomness what
    c.e. sets are to computability.
  - New core course `randomness-degrees`: Kučera's theorems on c.e. sets, Stephan's
    theorem, randomness for computable measures, Demuth's theorem, Kautz's 0-1 law and the
    properties of almost every degree (DH 6.10, 6.12, 8; Nies 4).
  - `k-trivials` becomes the last core course: lowness for randomness and K-triviality are
    where both reference books end their core material.
  The order is: Kolmogorov complexity, Martin-Löf randomness, martingales, notions of
  randomness, left-c.e. reals, randomness and Turing degrees, K-trivial sets.
- **Kept specialized:** **higher randomness**, which needs the higher computability track.
- **Possible specialized courses:** effective dimension (DH 13); randomness and analysis
  (differentiability, density, ergodic theorems); stochasticity and Kolmogorov–Loveland
  randomness (DH 7.4–7.5); strong jump traceability (DH 14).

## Reverse mathematics

**Objective.** The strength of theorems of ordinary mathematics:
- the axiom systems of second-order arithmetic and the Big Five;
- the computability-theoretic analysis of combinatorial principles below ACA₀, with
  Ramsey's theorem as the case study, and the other principles of the zoo below it;
- first-order strength (induction and collection, conservation);
- the problem reducibilities that refine provability over RCA₀;
- the theory of countable well-orderings and the equivalents of ATR₀.

**Techniques.**
- Coding in RCA₀;
- ω-models and Turing ideals;
- reversals;
- Mathias forcing and cone avoidance;
- non-standard models and conservation;
- uniform (Weihrauch) reductions;
- preservation of weakness properties (combinatorial principles);
- arithmetic transfinite induction, ranking trees into well-orderings, and
  pseudohierarchies (transfinite recursion).

**Comparison.**
- **Simpson** organizes the subject around the Big Five.
- **Hirschfeldt** (*Slicing the Truth*) puts the analysis of Ramsey's theorem and of
  first-order strength at the center.
- **Dzhafarov–Mummert (2022)** add problem reducibilities as a basic tool, and treat
  induction and bounding as part of the core.
- The track follows the last two: from 2026-11-12 it includes induction and conservation,
  and reducibilities, previously specialized.
- **Enlarged on 2026-11-18** (from five to seven courses), after a comparison with the
  three books. Two gaps remained:
  - *Below RT²₂*, the track had Ramsey's theorem only, while Hirschfeldt (Chapter 9) and
    Dzhafarov–Mummert (Chapter 9) give a chapter to the other principles, which are the
    daily material of the research literature. New core course
    `combinatorial-principles`: CAC and ADS with a computable order of type ω + ω* without
    computable solutions, ADS → COH and the stable/cohesive decompositions, the
    Erdős–Moser theorem (RT²₂ = EM + ADS, EM → BΣ⁰₂), DNR and WWKL₀ with their ω-models,
    and ADS ⊬ DNR by preservation, with a map of the zoo. The hard separations stay in the
    secondary track "Lowness and avoidance", to which the course points.
  - *Above ACA₀*, ATR₀ and Π¹₁-CA₀ had a single survey lesson with all equivalents
    admitted, while Simpson gives them Chapters V–VI and Dzhafarov–Mummert Sections 12.1
    and 12.3. New core course `transfinite-recursion`: well-orderings and comparison maps,
    pseudohierarchies and the perfect set theorem, Σ¹₁ separation, unique paths,
    comparability (Friedman), open and clopen determinacy (Steel), all with proofs. It
    builds on the higher computability track (hyperarithmetic sets) for motivation only.
  The order is: second-order arithmetic, Big Five, Ramsey's theorem, induction and
  conservation, reducibilities, combinatorial principles, transfinite recursion.

**Excluded.**
- The reverse mathematics of analysis, algebra and topology beyond the examples in the
  Big Five course (Simpson, Chapters III–VI). These are applications of the same
  techniques; examples are given in the Big Five course. A specialized course on
  countable algebra (vector spaces, ideals, orderable groups, divisible groups) is a
  possible addition.
- Π¹₁-CA₀ beyond the survey of the Big Five course and the notes of the transfinite
  recursion course (perfect kernels, Σ⁰₁ ∧ Π⁰₁ determinacy), β-models and the systems above
  Π¹₁-CA₀ (Simpson, Chapter VII).
- The atomic model theorem and the reverse mathematics of model theory (Hirschfeldt,
  Section 9.3): planned for the computable structure theory track.

## Higher computability

**Objective.** Computability along the computable ordinals:
- ordinal notations and ω₁ᶜᵏ;
- hyperarithmetic sets and Kleene's theorem Δ¹₁ = HYP;
- Σ¹₁ classes and their basis theorems;
- the analogy between Π¹₁ sets and c.e. sets: norms, stages, reduction and
  uniformization.

**Techniques.**
- Effective transfinite recursion;
- well-founded trees and ranks;
- the boundedness principle;
- Π¹₁ norms and stage comparison.

**Comparison.**
- Sacks (Parts A–B) and Chong–Yu (Chapters 1–5) build higher computability on these
  three pillars.
- The stage comparison and uniformization are what make the analogy with c.e. sets
  usable, and every later topic (higher randomness, Π¹₁ forcing) relies on them. For
  this reason the course on descriptive set theory, previously specialized, is part of
  the track from 2026-11-12.

**Enlarged on 2026-11-17** with the core course `sigma11-basis` (hyperarithmetic
reducibility and the hyperjump, Spector's collapse theorem, the Gandy and Kreisel basis
theorems, Gandy forcing, Π¹₁ singletons), written from Monin–Patey's chapters "Beyond
hyperarithmetic" and "Σ¹₁ and Π¹₁ classes". The Gandy basis theorem, admitted until then,
is now proved.

**Written on 2026-11-17**, once Sacks and Chong–Yu were added to `external-data/`:
- `admissible-sets` (*Admissible sets and constructibility*): Kripke–Platek set theory,
  L_α, ω-models of KP, ω₁ᶜᵏ as the second admissible ordinal, HYP = P(ℕ) ∩ L_{ω₁ᶜᵏ}, the
  Spector–Gandy theorem, ω₁ˣ admissible; Sacks's converse stated. Barwise compactness,
  first planned, is left out (a model-theoretic topic).
- `hyperarithmetic-forcing` (*Forcing over the hyperarithmetic sets*): the ramified analytic
  hierarchy, Feferman's Cohen forcing, incomparable hyperdegrees, perfect forcing and a
  minimal hyperdegree (Gandy–Sacks).
The track is now: computable ordinals, hyperarithmetic sets, effective descriptive set
theory, Σ¹₁ classes and the hyperjump, admissible sets, forcing over HYP.

**Excluded.**
- α-recursion theory and admissible ordinals beyond ω₁ᶜᵏ (Sacks, Parts C–D). They are a
  research topic of their own.

## Models of arithmetic

**Objective.** The model theory of first-order arithmetic and of its fragments. After the
track, a student can work in non-standard models of fragments of PA, relate the axioms of
induction and collection to the structure of cuts and end extensions, construct models
with prescribed properties (end extensions, recursively saturated models, satisfaction
classes), and prove the independence of combinatorial statements by indicators. The
track is the first-order counterpart of the reverse mathematics track: its last courses
are the tools behind the conservation results of that track.

**Techniques.**
- Coding finite sets and sequences inside weak theories;
- overspill and underspill;
- partial truth definitions;
- the arithmetized completeness theorem;
- definable types and ultrapowers;
- recursive saturation and back-and-forth;
- indicators.

**Literature compared.**
- Wong, *Model theory of arithmetic* (lecture notes, NUS and KGRC Vienna). It is a course of
  fifteen lectures:
  - the arithmetic hierarchy, collection, the weak König lemma in cuts, the arithmetized
    completeness theorem;
  - semiregular cuts, end and cofinal extensions;
  - recursive saturation and back-and-forth;
  - MacDowell–Specker, strongly definable and minimal types;
  - preservation, arithmetic with a top, satisfaction classes, forcing in arithmetic.
- Hájek–Pudlák, *Metamathematics of First-Order Arithmetic* (1998):
  - Part I: fragments, partial truth definitions, recursion theory and logic in fragments;
  - Part II: Ramsey-type independence, Paris–Harrington, α-large sets;
  - Part III: self-reference, definable cuts, interpretability;
  - Part IV: models of fragments, arithmetic with a top, indicators;
  - Part V: bounded arithmetic.
- Kaye, *Models of Peano Arithmetic* (1991), and Kossak–Schmerl, *The Structure of Models of
  Peano Arithmetic* (2006), not available locally.

**Courses, in order.**
(On 2026-11-13 the first planned course was split in two, because its lessons ran to
50–65 minutes: `fragments-of-arithmetic`, with the first-order hierarchy of induction and
collection proved, so that the track does not depend on the second-order course
`induction-conservation`; and `truth-and-provability`, with the provably total functions
of IΣ₁, partial truth definitions and finite axiomatizability. The track has six courses.)

1. **`fragments-of-arithmetic`** and **`truth-and-provability`**.
   - PA⁻ and the arithmetic hierarchy in models; IΔ₀ and exponentiation;
   - coding of finite sets and sequences in IΔ₀ + exp;
   - induction, least number principle and collection (IΣₙ, LΣₙ, BΣₙ); the theorems of
     Parsons and Paris–Kirby;
   - partial truth definitions and the finite axiomatizability of IΣₙ;
   - (Hájek–Pudlák I.1–I.2; Wong 1–2.)
2. **`cuts-and-extensions`.**
   - Cuts, overspill and underspill;
   - the standard system and Scott sets: the weak König lemma in cuts (Scott);
   - Tennenbaum's theorem;
   - end and cofinal extensions, and the preservation of formulas;
   - Friedman's and Paris–Kirby's characterizations of collection by end extensions;
   - semiregular and regular cuts;
   - (Wong 3–6; Hájek–Pudlák IV.1.)
3. **`end-extensions`.**
   - The arithmetized completeness theorem and the low basis theorem in IΣ₁;
   - elementary end extensions of models of PA (MacDowell–Specker);
   - definable and strongly definable types, Gaifman's minimal types and their
     consequences;
   - (Wong 4, 9–11; Hájek–Pudlák I.3–I.4, IV.1.)
4. **`recursive-saturation`.**
   - Recursively saturated models and their existence (Barwise–Ressayre);
   - back-and-forth, and Friedman's embedding theorem;
   - automorphisms (Smoryński, Kossak–Kotlarski);
   - satisfaction classes (Kotlarski–Krajewski–Lachlan, Lachlan);
   - (Wong 7–8, 12, 14.)
5. **`independence`.**
   - Indicators and the method of Paris and Kirby;
   - the Paris–Harrington principle and its unprovability in PA;
   - α-large sets and their growth;
   - arithmetic with a top;
   - (Hájek–Pudlák II, IV.2–IV.3; Wong 13.)

**State on 2026-11-13** (after writing and a polishing pass):
- six courses, 48 lessons, about 30 hours:

  | Course | Lessons |
  | --- | --- |
  | `fragments-of-arithmetic` | 9 |
  | `truth-and-provability` | 5 |
  | `cuts-and-extensions` | 8 |
  | `end-extensions` | 9 |
  | `recursive-saturation` | 8 |
  | `independence` | 9 |

- **Additions to the plan:** the converse of the Parsons–Mints–Takeuti theorem is proved
  (`independence`), and `end-extensions` adds a lesson of applications of the arithmetized
  completeness theorem.
- **Left out:** the preservation theorems of Wong's Lecture 12, which need the omitting
  types theorem.
- **Corrections:** two corrections to the proof of Lachlan's theorem in Wong's notes are
  recorded in the log of `recursive-saturation`.
- Each course log lists its open points.

**Relations with other tracks.**
- The course `induction-conservation` (reverse mathematics track) treats induction and
  collection for second-order schemes and the conservation theorems of Friedman and
  Harrington. It also contains Harrington's forcing in arithmetic, the last lecture of
  Wong. The new track cites it rather than duplicating it, and that course points to the
  first-order development here.
- The track assumes first-order logic: completeness and compactness, and Gödel's
  incompleteness theorems, as in Wong's prerequisites.

**Excluded, with reasons.**
- **Bounded arithmetic and complexity** (Hájek–Pudlák V). A topic of its own; a possible
  specialized course.
- **Self-reference, definable cuts and interpretability** (Hájek–Pudlák III). A possible
  specialized course.
- **Lattices of elementary substructures and other topics of Kossak–Schmerl.** Research
  topics beyond the scope of a first track.

## Lowness and avoidance

**Objective.** The separation of mathematical problems by preservation properties:
- cone avoidance, lowness, PA avoidance and their variants;
- the forcing question as the tool to establish them;
- control of the first and second jumps of generic sets.

After the track, a student can read current research articles on the reverse
mathematics of Ramsey-type theorems.

**Techniques.**
- The forcing question and its definability;
- compactness and merging of forcing questions;
- Mathias forcing and its variants;
- first-jump control (lowness, low₂ constructions);
- second-jump control (jump cone avoidance, non-high and jump-PA avoidance).

**Literature compared.**
- Patey, *Lowness and avoidance* (monograph, in `external-data/lowness-avoidance/`):
  - first jump control: cone avoidance, lowness, compactness avoidance, custom properties,
    conservation theorems, forcing design;
  - higher jump control: jump cone avoidance, jump compactness avoidance, higher jump cone
    avoidance.
- Hirschfeldt, *Slicing the Truth*, Chapter 6, and Dzhafarov–Mummert, Chapters 7–9, for the
  combinatorial principles.
- The research articles behind each chapter (Seetapun; Cholak–Jockusch–Slaman; Liu;
  Monin–Patey).

**Courses, in order.**
1. **`effective-forcing`** (existing course, written 2026-11-12): notions of forcing, the
   forcing relation, Cohen forcing and tree forcings, Sacks forcing, the forcing question,
   Mathias forcing. It becomes the first course of the track.
2. **`avoidance`.** Cone avoidance through the forcing question:
   - first examples;
   - Seetapun's theorem;
   - preservation of non-Σ⁰₁ definitions and of hyperimmunities.
3. **`lowness`.** First-jump control:
   - indices and coded Turing ideals;
   - the low basis theorem revisited;
   - weak preservation;
   - beyond ∅′;
   - low₂ solutions to RT²₂ (Cholak–Jockusch–Slaman).
4. **`compactness-avoidance`.**
   - PA avoidance and weak merging;
   - Ramsey-type weak König's lemma;
   - Liu's theorem (RT²₂ does not imply WKL);
   - randomness, closed classes and DNC avoidance.
5. **`separation-design`.**
   - Separations by custom properties (immunity and variants, the Erdős–Moser theorem,
     ADS and CAC);
   - the design of a notion of forcing (Erdős–Moser, free set theorem).
6. **`jump-cone-avoidance`.** Second-jump control:
   - use and first-jump control;
   - WKL, COH and partition regularity;
   - the pigeonhole principle: every instance has a solution of non-high degree
     (Monin–Patey).
7. **`jump-compactness-avoidance`.**
   - Jump PA avoidance;
   - Mathias forcing and COH, product largeness;
   - every Δ⁰₂ set has an infinite subset in it or its complement whose jump is not PA
     over ∅′ (Monin–Patey).

**State on 2026-11-13** (after writing and a polishing pass):
- seven courses, 66 lessons, about 43 hours:

  | Course | Lessons |
  | --- | --- |
  | `effective-forcing` | 9 |
  | `avoidance` | 9 |
  | `lowness` | 10 |
  | `compactness-avoidance` | 11 |
  | `separation-design` | 8 |
  | `jump-cone-avoidance` | 10 |
  | `jump-compactness-avoidance` | 9 |

- **Main theorems proved in full:**
  - Seetapun's theorem;
  - Cholak–Jockusch–Slaman (low₂ solutions for RT²₂);
  - Liu's theorem;
  - the Erdős–Moser separations;
  - Monin–Patey on non-high solutions of RT¹₂;
  - Monin–Patey on Δ⁰₂ sets and jump PA avoidance.
- **Errata to the monograph:** the courses correct a number of errors in the monograph.
  Each correction is recorded in the `_design.md` of the course that makes it, under
  "Choices" or "Comparison with the literature".

**Relations with other tracks.**
- The track builds on the reverse mathematics track:
  - `ramsey-theorem`, whose lessons on cone avoidance and Seetapun's theorem are the first
    examples here;
  - `reducibilities`, for preservation and ω-models;
  - `pi01-classes` and `immunity-growth`, for basis theorems, PA and DNC degrees.
- Results proved elsewhere are cited.

**Excluded, with reasons.**
- **Higher jump cone avoidance** (hyperarithmetic jump control). It needs the higher
  computability track; a possible specialized course.
- **Conservation theorems** (the isomorphism theorem for WKL, conservation over BΣ₂).
  These belong with `induction-conservation` and the models of arithmetic track; a possible
  specialized course.

## Computable analysis (specialized course, written 2026-11-12)

Weihrauch's book is the reference. The platform needs one specialized course:
- computable reals and their representations;
- computable functions on the reals and their continuity;
- computable metric spaces;
- the computable content of classical theorems.

It connects the reverse mathematics of analysis (second-order arithmetic) with
Weihrauch reducibility (reducibilities). A track of its own is not planned.

## Review of 2026-11-18

At the author's request, every track was reviewed for its pedagogical structure, without
following one book, and for recent results that should be included or that settle a
question presented as open.

- **Computability theory: entry course split.** `models-of-computation` had 16 lessons, and
  six of them (register machines, LOOP and WHILE programs, three lessons on the
  λ-calculus) are used by no later course. The core course now treats two formalizations,
  Turing machines and partial recursive functions, proves their equivalence in both
  directions (by arithmetization, and by clean multi-tape machines for the schemes), and
  ends with the normal form, the universal function and the thesis. The other models form
  the specialized course `other-models`, which ends with the equivalence of all five
  models. A reader reaches c.e. sets after ten lessons instead of sixteen. The rest of the
  track keeps its order: each course uses the techniques of the previous ones (see the
  list of techniques above). State of the art: Lutz–Siskind (Part 1 of Martin's
  conjecture for order-preserving functions) is now cited in its journal version (JAMS
  2024).
- **Algorithmic randomness: order kept.** An alternative would start with Martin-Löf tests,
  which need less machinery than prefix-free complexity. It was rejected: the
  Levin–Schnorr theorem, the central equivalence of the area, needs both, and the
  complexity course also serves the later courses (left-c.e. reals, K-triviality); Downey–
  Hirschfeldt and Nies make the same choice. State of the art: the covering problem
  (Bienvenu, Greenberg, Kučera, Nies and Turetsky; Day and Miller) is already in
  `k-trivials`; nothing found that changes the core courses.
- **Reverse mathematics: restructured earlier the same day** (sections above): the
  combinatorial principles are organized by preservation of hyperimmunities and of
  constant-bound immunity, and ATR₀ has a course of its own. State of the art: the
  first-order part of RT²₂ (Le Houérou, Levy Patey and Yokoyama 2024: Π⁰₄ conservation
  over BΣ⁰₂, and Π¹₁ conservation with the well-foundedness of ε₀) is in
  `induction-conservation/pigeonhole` and `independence/paris-harrington`, which present
  full Π¹₁ conservation over RCA₀ + BΣ⁰₂ as open. The question was solved in 2026
  by Y.-S. Hwang (*Π¹₁ conservation of Ramsey's theorem for pairs over BΣ⁰₂*, preprint on
  ResearchGate, October 2026, not yet refereed; the only reference available); both
  lessons now say so, and the first-order part of RT²₂ is IΣ₁ + BΣ₂.
  Whether CADS implies COH over RCA₀ is still presented as open; no resolution was found.
- **Higher computability: order kept** (hyperarithmetic sets, Π¹₁ sets and ordinal
  notations, the Σ¹₁ basis theorems, admissible sets, hyperarithmetic forcing), as
  enlarged on 2026-11-17: each course needs the previous one, and admissible sets come
  after the concrete theory so that they generalize something known.
- **Lowness and avoidance, models of arithmetic: kept as secondary tracks.** Their order
  (forcing, then avoidance, then lowness; fragments, then conservation, then
  independence) follows the dependencies of the results. The open questions cited in the
  arithmetic track (Scott set problem, minimal cofinal extensions, Paris's question whether
  IΔ₁ proves BΣ₁, and whether IΔ₀ + ¬exp proves BΣ₁) were not rechecked in this review; this is left for the
  next revision of those courses.
- **Computable structure theory.** New track of the same day (section above), organized by
  questions rather than by the chapters of one book.

## History

- **2026-11-12.** Initial log, written when the design rules were introduced.
  - Moved into tracks: immunity and growth (computability), induction and conservation
    and reducibilities (reverse mathematics), descriptive set theory (higher
    computability).
  - New core course planned: martingales (randomness).
  - New specialized courses planned: effective forcing, and computable analysis.
- **2026-11-12.** `kolmogorov-complexity` now builds on `turing-degrees`, since it proves
  that C and Ω are Turing equivalent to ∅′.
- **2026-11-12.** `cohen-genericity` now builds on `immunity-growth` (hyperimmune
  and DNC functions, computably dominated sets).
- **2026-11-12.** Specialized course `effective-forcing` written: notions of forcing, the
  forcing relation, Cohen and tree forcings, Sacks forcing, the forcing question, and
  Mathias forcing.
- **2026-11-12.** Core course `martingales` written and added to the randomness track:
  betting strategies, Ville's theorem, Schnorr's theorem, computable randomness, Schnorr
  randomness and the hierarchy of randomness notions.
- **2026-11-12.** Specialized course `computable-analysis` written: type-2 computability,
  representations, computable real functions, continuous functions and closed sets, and
  the Weihrauch degrees of the intermediate value theorem, the maximum and monotone
  convergence.
- **2026-11-12.** `randomness-notions` refocused on what the core course `martingales`
  leaves out: relative randomness and van Lambalgen's theorem, 2-randomness and weak
  2-randomness, and Kurtz randomness against computable domination. Its overlap with
  `martingales` is replaced by citations.
- **2026-11-13.** Two new tracks designed: models of arithmetic (after Wong's lecture
  notes and Hájek–Pudlák) and lowness and avoidance (after Patey's monograph). The
  specialized course `effective-forcing` becomes the first course of the second.
- **2026-11-13.** Courses `fragments-of-arithmetic` and `truth-and-provability` written
  (track models of arithmetic); `avoidance` and `lowness` written (track lowness and
  avoidance).
- **2026-11-13.** Both new tracks written in full and polished; long lessons split (no
  lesson exceeds 45 minutes at 55 words per minute); pointers added from the existing
  courses to the new tracks.
- **2026-11-13.** Tracks divided into primary and secondary ones: lowness and avoidance,
  and models of arithmetic, become secondary tracks, shown on the page of all tracks
  only.
- **2026-11-17.** Randomness and higher computability tracks enlarged after a comparison
  with the standard references (sections above). Randomness: `randomness-notions` and
  `k-trivials` become core; new core courses `left-ce-reals` and `randomness-degrees`;
  three lessons added to `kolmogorov-complexity`. Higher computability: new core course
  `sigma11-basis`; two further courses planned.
- **2026-11-17.** Higher computability: `admissible-sets` and `hyperarithmetic-forcing`
  written from Sacks and Chong–Yu, completing the planned enlargement.
- **2026-11-18.** Computable structure theory: third course `computable-categoricity` written
  (six lessons: Scott families, the characterization of relative computable categoricity,
  classical examples, categoricity on a cone, Nurtazin's theorem, computable dimension and
  degrees of categoricity).

## Computable structure theory

**Added on 2026-11-18**, at the author's request, once the reference books were available:
Ash and Knight, *Computable Structures and the Hyperarithmetical Hierarchy* (2000), and
Montalbán, *Computable Structure Theory: Within the Arithmetic* (draft of 2019, published
2021) and *Beyond the Arithmetic* (revised version of 2025). It is a **primary** track:
computable structure theory is one of the main areas of research in computability, with
its own monographs, and its basic notions (presentations, categoricity, degree spectra,
Scott rank) are used across the other areas (reverse mathematics of algebra, the atomic
model theorem, Borel reducibility).

**Objective.** The complexity of countable structures: their presentations and degree
spectra, the complexity of their relations and of their isomorphisms, and the infinitary
formulas that explain both.

**Techniques.**
- Building presentations as pull-backs of enumerations (Knight's coding);
- the back-and-forth method and its effective versions;
- generic presentations and forcing on presentations;
- finite injury and true stages in constructions of structures;
- infinitary formulas, Scott sentences and back-and-forth relations;
- (later) the α-priority method.

**Comparison and choices.**
- **Ash–Knight** is organized around the hyperarithmetical hierarchy: infinitary formulas
  first, then intrinsic definability and categoricity at all levels, then the
  metatheorems for α-systems. **Montalbán** separates the theory below one jump (Part I)
  from the transfinite theory (Part II), and develops the tools (r.i.c.e. relations,
  ∃-atomic structures, generic presentations) before the questions they answer.
  **Downey–Melnikov** (2025) start from effective classification and include
  uncountable structures. The survey of **Fokina, Harizanov and Melnikov** (*Turing's
  Legacy*, 2014) organizes the field by its questions.
- **Decision (2026-11-18, at the author's request that the track not follow one book).**
  The track is ordered by **questions**, each course answering one, and the tools are
  introduced where a question needs them:
  1. *Which structures have computable copies, and do two computable copies agree?*
     (`computable-structures`): presentations, Knight's theorem, decidable theories and
     their decidable models, computable algebra, the effective back-and-forth method and
     the first examples of computable categoricity. Concrete structures (orders, groups,
     fields, vector spaces, Boolean algebras) come before any general tool, so that the
     reader has examples on which to test the general theory.
  2. *Which relations can every copy compute or enumerate?* (`intrinsic-definability`):
     r.i.c.e. relations and the theorem of Ash, Knight, Manasse, Slaman and Chisholm, the
     jump of relations and complete relations, and the difference between intrinsic and
     relatively intrinsic notions (Ash–Nerode), which prepares the same difference for
     categoricity.
  3. *When are all copies computably isomorphic?* (`computable-categoricity`): Scott
     families, relative computable categoricity, the classical examples, relative versus
     plain categoricity, computable dimension, degrees of categoricity.
  4. *Which sets of degrees are degree spectra?* (`degree-spectra`): generic
     presentations, possible and impossible spectra, the jump of a structure, low
     structures.
  5. *How complicated is a structure to describe?* (`scott-analysis`): infinitary logic,
     back-and-forth relations, Scott sentences, Scott rank and Scott complexity.
  6. *What happens beyond one jump?* (`hyperarithmetic-structures`): computable
     infinitary formulas, intrinsic definability and relative Δ⁰_α-categoricity at all
     levels, pairs of structures.
  7. *Can countable structures be classified?* (`isomorphism-problem`): index sets, the
     complexity of isomorphism, structures of high Scott rank, effective
     bi-interpretability and computable embeddings of classes.
  This differs from Montalbán in three places: categoricity comes before degree spectra
  and generic presentations, being the more natural first question and needing only the
  finitary tools; effective model theory (decidable models, computable algebra) belongs to
  the first course; and Scott analysis is a course of its own, separate from the
  hyperarithmetic level, since Scott complexity is now the standard language of
  descriptive complexity. It differs from Ash–Knight in starting below one jump.

It builds on the computability track (finite injury, the arithmetic hierarchy), and from
course 5 on the higher computability track (computable ordinals, hyperarithmetic sets).

**State of the literature (checked 2026-11-18).**
- New reference: Downey and Melnikov, *Computable Structure Theory: A Unified Approach*
  (Springer, 2025), which treats countable and uncountable (Polish, profinite, locally
  compact) structures together, and Friedberg enumerations of classes of structures. It
  is not in `external-data/`; it is cited as further reading, and is the natural source
  for a later specialized course on computable topological structures.
- Montalbán's *Beyond the Arithmetic* is published (2026); the file used is the revised
  version of April 2025, and section numbers may differ slightly.
- **Scott complexity** (Alvir, Greenberg, Harrison-Trainor, Turetsky, JSL 2021, and
  Harrison-Trainor's survey, BSL): the least complexity of a Scott sentence, which is
  always Π_α, Σ_α or d-Σ_α (α a successor for the last two), never Σ₁ nor Σ₂. It refines
  Scott rank and is now the standard measure; the course `infinitary-logic` must present
  it, with Montalbán's robust Scott rank, instead of the older rank of Ash–Knight
  (Chapter 6). Recent work on the computability of optimal Scott sentences (2025) is
  further reading.
- **Degrees of categoricity** (Fokina, Kalimullin, Miller; Csima, Franklin, Shore;
  Csima and Harrison-Trainor): to be covered in `computable-categoricity`, with the open
  question, still open in 2025, whether every degree of categoricity is a strong degree
  of categoricity.
- **Punctual (online) structures** (Bazhenov, Downey, Kalimullin, Melnikov, Ng and others,
  surveyed in the BSL in 2019; recent work on primitive recursive categoricity spectra,
  2026): a sub-area of its own; a possible specialized course, outside the track.
- The results of course 1 (Knight's theorem, the characterization of r.i.c.e. relations,
  the jump of relations) are classical and not superseded.

**Excluded, for now.**
- Prime and atomic models, homogeneous models, the atomic model theorem and its reverse
  mathematics (Hirschfeldt, Section 9.3; Ash–Knight 9): a possible specialized course;
  decidable models of decidable theories are in the first course.
- The α-priority method and the metatheorems of Ash–Knight (Chapters 13–19): a possible
  specialized course after the track.
- Σ-small classes and the copy-versus-diagonalize game (Montalbán I, X), Vaught's
  conjecture (Montalbán II, XII): research topics.
