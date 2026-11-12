# Design log: Π⁰₁ classes

This file is the memory of the course (see "Designing tracks and courses" in
`AGENTS.md`). It is not rendered.

## 1. Objectives

After the course, a student can:

- work with binary trees, the topology of Cantor space and compactness, and prove weak
  König's lemma;
- describe Π⁰₁ classes in the equivalent ways used in the literature (computable trees,
  co-c.e. trees, Σ⁰₁ complements, functionals), uniformly in indices, and use effective
  compactness (emptiness is Σ⁰₁);
- decide which members of Π⁰₁ classes must be computable (isolated members, countable
  classes) and exhibit classes without computable members;
- prove the low, computably dominated and cone avoidance basis theorems, and recognize
  forcing with Π⁰₁ classes as a method;
- characterize the PA degrees and relate them to completions of Peano arithmetic;
- measure the strength of König's lemma for finitely branching trees (PA over ∅′).

**Role in the track.** The computability track (`content/tracks-design.md`) assigns this
course the technique "compactness and forcing with Π⁰₁ classes". It is used without comment
by the next core course (immunity and growth: computably dominated sets, DNC functions), by
the randomness track (Martin-Löf randomness: Π⁰₁ classes of randoms, basis theorems), and by
the reverse mathematics track (WKL₀ and its ω-models, König's lemma and ACA₀).

## 2. Prerequisites assumed

- Turing degrees: oracle computations and their stages (`prop-oracle-stages`), the jump,
  low sets (`prop-low-basic`), the limit lemma (`thm-limit-lemma`), the computation function
  of a Δ⁰₂ set (`thm-computation-function`), the finite extension method.
- Arithmetic hierarchy: Σ⁰ₙ/Π⁰ₙ classification of index sets, Post's theorem, lowness
  indices (`prop-no-lowness-index`), Σ₁ definability of c.e. sets (`cor-sigma1-ce`).
- Countability: the coding of Baire space into Cantor space (`prop-baire-cantor`).
- Fundamentals: SMN, indices.

## 3. Results, lesson by lesson

1. **Trees and Cantor space** (`cantor-space`, new on 2026-11-12): binary trees, weak König's
   lemma (`lem-weak-konig`), open and closed classes, closed = paths of a tree
   (`prop-closed-tree`), compactness (`prop-cantor-compact`). Exercises: clopen classes are
   finite unions of cylinders; uniform continuity of total functionals.
2. **Π⁰₁ classes and effective compactness** (`trees-and-classes`): definition and five
   equivalent descriptions (`prop-pi01-equivalent`), examples (separating sets, DNC₂,
   computable singletons), emptiness is Σ⁰₁ and extendibility is Π⁰₁
   (`prop-pi01-emptiness`). Exercises: closure under ∩ and ∪; characterization by c.e. set of
   disjoint cylinders; a computable listing of the non-empty Π⁰₁ classes.
3. **Computable members** (`computable-members`): Kreisel basis theorem
   (`prop-leftmost-path`), isolated members are computable (`prop-isolated-computable`),
   perfect classes have continuum many members (`thm-perfect-continuum`), countable classes
   have computable members (`cor-countable-computable`), DNC₂ has no computable member
   (`thm-dnc2-no-computable`).
4. **Basis theorems** (`basis-theorems`): low basis theorem (`thm-low-basis`) with the
   superlow remark (`rem-superlow`), computably dominated basis theorem
   (`thm-dominated-basis`, via `lem-uniform-bound`), cone avoidance (`thm-cone-avoidance-basis`,
   via `lem-uniform-cone`).
5. **PA degrees** (`pa-degrees`): three characterizations (`thm-pa-characterization`),
   consequences of the basis theorems (`cor-pa-basis`), completions of PA
   (`thm-pa-completions`); c.e. PA sets are complete and Solovay's degree-exact theorem
   are stated without proof.
6. **Finitely branching trees** (`finitely-branching-trees`): König's lemma (`lem-konig`),
   the unary coding (`prop-finitely-branching-coding`, `cor-bounded-pa`), a computable tree
   with at most two successors per node whose unique path computes ∅′
   (`thm-finitely-branching-jump`), König's lemma ≡ PA relative to ∅′ (`thm-konig-strength`).

## 4. Proof techniques

- **Pigeonhole on infinite trees** (weak König's lemma, König's lemma): lessons 1 and 6.
- **Compactness**, classical (lesson 1) and **effective** (lesson 2): the recurring tool;
  used in the computation of isolated members, in every basis theorem, in
  `lem-uniform-bound` and `lem-uniform-cone` (a common stage of convergence over a whole
  class), and in the PA characterization.
- **Forcing with Π⁰₁ classes** (Jockusch–Soare forcing): lesson 4, explicitly compared with
  the finite extension method of the Turing degrees course; used with a ∅′ oracle (low),
  ∅″ oracle (computably dominated) and non-effectively (cone avoidance).
- **Diagonalization** (DNC₂ has no computable member; Rosser's theorem): lessons 3 and 5.
- **SMN and racing enumerations** (PA characterization): lesson 5.
- **Coding** (unary coding of Baire space into Cantor space; coding stages of ∅′ into node
  labels; coding a Δ⁰₂ tree into a computable finitely branching tree via the limit lemma):
  lesson 6.
- **Splitting trees** (perfect classes): lesson 3; prepares the function trees of the
  immunity and growth course.

## 5. Choices

- **Split of the first lesson (2026-11-12).** The former first lesson covered trees, the
  topology of Cantor space and Π⁰₁ classes, and with the added examples and figures it
  reached about 3000 words. It now forms two lessons: `cantor-space` (combinatorics and
  topology, with two new exercises) and `trees-and-classes` (effective classes). The slug
  `trees-and-classes` keeps the Π⁰₁ class definitions, because other courses list it as a
  prerequisite for them (immunity-growth/hypersimple-sets, martin-lof-randomness/measure).
  Labels were moved, not renamed; numbering changes automatically.
- **Order.** Topology before effectivity, then computable members (the weakest positive and
  negative results), then basis theorems, then PA degrees (which use the basis theorems
  for low PA sets), then finitely branching trees (which use PA relative to ∅′). This is the
  order of Monin–Patey and of Soare Part II.
- **Direct proof of the PA characterization** (DNC₂ ⇒ separation ⇒ every Π⁰₁ class),
  without logic; completions of PA come after, with the two logical facts admitted. This
  keeps the computability content independent of Gödel numbering.
- **Admitted results, stated with references:** c.e. PA sets are complete (Jockusch–Soare;
  also follows from Arslanov's criterion, proved in immunity-growth); Solovay's theorem that
  PA degrees are exactly the degrees of completions; the Cantor–Bendixson analysis beyond
  the perfect kernel. They orient the reader without lengthening the course.
- **Superlow basis theorem as a remark** rather than a theorem: it needs truth-table
  reducibility, which the track defines only in immunity-growth.
- **Excluded:** thin classes, Cantor–Bendixson ranks and the complexity of members of
  countable classes (Cenzer–Remmel; specialized), the c.e. basis theorem as a separate
  statement (mentioned after the Kreisel basis theorem), the low antibasis and low₂/proper
  low basis theorems (Soare 9.6–9.7), Π⁰₁ classes of randoms (randomness track), index-set
  complexity of properties of Π⁰₁ classes beyond one exercise, Weihrauch degrees of WKL
  (reducibilities course), the forcing question (course on effective forcing, written 2026-11-12).
- **Cone avoidance** is proved directly and also derived from the low and computably
  dominated basis theorems (exercise), so that both arguments are available.

## 6. Comparison with the literature

- **Monin–Patey, chapter "Π⁰₁ classes"** (`external-data/monin-patey/parts/pi01-classes.tex`):
  same material and order (binary trees, topology, Π⁰₁ classes, basis theorems, perfect
  classes, PA degrees, finitely branching trees). Differences: the course separates
  computable members into a lesson, proves the PA characterization directly by separation
  rather than through theories, and omits the section on bases for perfect Π⁰₁ classes.
- **Soare 2016, Part II** (Chapters 8–10): Chapter 8 (open and closed classes, effective
  compactness, Theorem 8.5.1), Chapter 9 (basis and nonbasis theorems, 9.2–9.5), Chapter 10
  (PA degrees). Soare proves the low basis theorem early (Section 3.7); the course keeps all
  basis theorems together.
- **Downey–Hirschfeldt, Sections 2.19, 2.21, 2.22**: same results, with the PA degrees
  defined by completions and the Scott basis theorem proved logically.
- **Nies, Section 1.8**: Π⁰₁ classes and the basis theorems, with the left-c.e. leftmost
  path and the superlow refinement (Theorem 1.8.38).
- **Hirschfeldt, *Slicing the Truth*, Sections 3.1–3.2**: basis theorems as tools for reverse
  mathematics; the analysis of König's lemma (Exercises 3.24–3.27) is the model for lesson 6.
- **Simpson, Sections III.7 and IV.1**: the reverse-mathematical counterparts (KL ↔ ACA₀ with
  trees of at most two successors; WKL ↔ Heine–Borel).

## 7. Pedagogical plan

1. `cantor-space`: intuition of the invariant "infinitely many nodes above" before weak
   König's lemma; examples of trees (single path, non-extendible nodes, finite trees);
   examples of open/closed classes with counterexamples; figure of a tree with dead branches;
   figure of the compactness proof on a concrete cover; quiz on the pigeonhole step and on
   infinite branching.
2. `trees-and-classes`: intuition (conditions checkable on prefixes), remark that closed ≠
   Π⁰₁ (cardinality; explicit example in a quiz), examples (separating sets, DNC₂,
   singletons), intuition for effective compactness.
3. `computable-members`: examples of isolated and non-isolated members, intuition of the
   computation of isolated members and of the splitting construction; figure of the strings
   σ_ρ; remark on the Cantor–Bendixson analysis; DNC₂ named as a diagonal argument.
4. `basis-theorems`: comparison of forcing with strings and with Π⁰₁ classes; figure of the
   nested classes P₀ ⊇ P₁ ⊇ … with the decisions of the low basis construction; intuition and
   a counterexample (open class) for `lem-uniform-bound`; superlow remark.
5. `pa-degrees`: overview of the characterizations with a figure of the implications;
   remarks on universality, c.e. PA sets and Solovay's theorem.
6. `finitely-branching-trees`: examples of bounded and unbounded trees; intuition on why the
   lack of a computable bound carries information; figure of the tree whose path computes ∅′.

All figures are generated by `scripts/figures/pi01-classes.py` (deterministic output).

## 8. Sources, lesson by lesson (checked 2026-11-12)

1. `cantor-space`: Kőnig 1927. Soare 2016, Sections 8.1–8.3; Nies, Section 1.8 (Facts 1.8.3,
   1.8.4, Proposition 1.8.6); Simpson, Theorem IV.1.2.
2. `trees-and-classes`: Soare 2016, Theorem 8.5.1 and Theorem 9.3.2; Downey–Hirschfeldt,
   Section 2.19.1; Nies, Section 1.8; Hirschfeldt, Proposition 3.9; Dean–Walsh,
   arXiv:1612.06219, Section 4 (history); Jockusch–Soare TAMS 173 (1972); Cenzer–Remmel 1998.
3. `computable-members`: Kreisel basis theorem: Kreisel, BJPS 4 (1953), 107–129 (credited
   so by Cenzer–Remmel's draft book *Effectively Closed Sets* and by Hirschfeldt; Dean–Walsh
   locate the statement for primitive recursive trees at pp. 125–126); Monin–Patey cite
   Kreisel 1959 instead. Countable classes and the Cantor–Bendixson analysis: Kreisel 1959,
   Bull. Acad. Polon. 7, 621–626. First class without computable member: Kleene, ICM 1950
   (1952), 679–685 (Dean–Walsh, Section 4.2); Hirschfeldt (Corollary 3.7) credits Kreisel 1953.
   Soare 2016, Theorems 8.5.1 and 9.3.2; Nies, Facts 1.8.31, 1.8.33, 1.8.36; Cenzer et al.,
   APAL 31 (1986), 145–163.
4. `basis-theorems`: Jockusch–Soare, TAMS 173 (1972), 33–56. Soare 2016, Theorems 3.7.2 and
   9.5.1; Downey–Hirschfeldt, Theorems 2.19.8, 2.19.11, Corollary 2.19.9 (superlow,
   Schaefer); Nies, Theorems 1.8.37, 1.8.38, 1.8.42; Hirschfeldt, Theorems 3.10–3.14 (cone
   avoidance from the other two; Gandy–Kreisel–Tait 1960 for the primitive recursive
   version); Brattka–de Brecht–Pauly, APAL 163 (2012), 986–1008.
5. `pa-degrees`: Scott, Proc. Sympos. Pure Math. 5 (1962), 117–121; Jockusch–Soare, Pacific
   J. Math. 40 (1972), 605–616 (DNC₂ characterization with Solovay, per Downey–Hirschfeldt
   Theorem 2.22.2; c.e. PA sets complete, per Hirschfeldt Theorem 3.18) and TAMS 173 (1972)
   (separating sets, low PA degrees, per Hirschfeldt Theorems 3.17, 3.20, 3.21); Solovay
   (unpublished): Downey–Hirschfeldt Theorem 2.21.3, Hirschfeldt Theorem 3.16; Rosser, JSL 1
   (1936), 87–91. Soare 2016, Chapter 10; Downey–Hirschfeldt, Sections 2.21–2.22.
6. `finitely-branching-trees`: Kőnig 1927; Jockusch–Lewis–Remmel, JSL 56 (1991), 684–693
   (Hirschfeldt, Exercises 3.24, 3.27); coding of computably bounded trees: Jockusch–Soare
   (Hirschfeldt, Exercise 3.25); Simpson, Theorem III.7.2 and Chapter IV.

## 9. Recent literature

Checked on 2026-11-12:

- **Diamondstone, Dzhafarov, Soare, *Π⁰₁ classes, Peano arithmetic, randomness, and
  computable domination*, Notre Dame J. Formal Logic 51 (2010), 127–159.** A survey of the
  same material from a modern viewpoint. Not cited in the lessons; a candidate reference for
  a future revision of the PA degrees lesson.
- **Brattka, de Brecht, Pauly, *Closed choice and a uniform low basis theorem*, APAL 163
  (2012), 986–1008.** A uniform version of the low basis theorem in the Weihrauch lattice.
  Mentioned in the notes of `basis-theorems`.
- **Brattka, Gherardi, Marcone, *The Bolzano–Weierstrass theorem is the jump of weak König's
  lemma*, APAL 163 (2012), 623–655** (with an addendum in APAL 168 (2017)). The uniform
  counterpart of "König's lemma is WKL one jump up". Not added: the Weihrauch-degree
  statement for KL itself was not checked precisely.
- **Dean, Walsh, *The prehistory of the subsystems of second-order arithmetic*,
  arXiv:1612.06219 (2016).** Used to settle the attributions to Kleene (1952) and Kreisel
  (1953).
- **Monin–Patey, effective forcing chapter.** The forcing-question approach unifies the
  basis theorems; deferred to the course on effective forcing (tracks-design.md).

No simpler proof of the basis theorems was found; the presentation by decreasing sequences of
Π⁰₁ classes remains standard.

## 10. Open points

- The published version of Dean–Walsh (Review of Symbolic Logic) was not checked; the
  lessons cite the arXiv version.
- Kreisel 1953 and Kleene 1952 were not read directly; their attributions rest on Dean–Walsh,
  Cenzer–Remmel's draft and Hirschfeldt.
- `martin-lof-randomness/measure.md` refers to `pi01-classes/trees-and-classes` for the
  notation of cylinders; the notation is now introduced in `cantor-space` and recalled in
  `trees-and-classes`. The link could point to `cantor-space`.
- Course-level prerequisites: `computable-ordinals`, `hyperarithmetic` and `cohen-genericity`
  use this course at lesson level only (REVIEW-2026-11).
- A possible exercise or remark: the c.e. basis theorem (leftmost path of c.e. degree) is
  stated with a reference only.

## 11. History

- **2026-11-12.** Design and pedagogy revision. First lesson split into `cantor-space` (new)
  and `trees-and-classes` (renamed "Π⁰₁ classes and effective compactness"). Added examples
  after the main definitions, intuition paragraphs before the main proofs, a counterexample
  for `lem-uniform-bound`, remarks (superlow basis theorem `rem-superlow`, Cantor–Bendixson
  analysis, c.e. PA sets, Solovay's theorem), four new exercises (`ex-clopen`,
  `ex-uniform-continuity`, `ex-nonempty-indices`) and five new figures (compactness, perfect
  splitting, nested classes, PA characterizations, jump tree); the generator was made
  deterministic. References checked against Soare 2016, Downey–Hirschfeldt, Nies,
  Hirschfeldt, Simpson and Monin–Patey; attributions of the Kreisel basis theorem (1953),
  of the first class without computable member (Kleene 1952), and of the derivation of cone
  avoidance (given in Hirschfeldt's book) corrected or made precise; section and theorem
  numbers added. Durations recomputed.
