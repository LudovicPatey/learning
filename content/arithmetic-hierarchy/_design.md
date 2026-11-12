# Design log: The arithmetic hierarchy

## 1. Objectives

After the course, a student can:

- place a set in the arithmetic hierarchy by writing a definition and counting quantifier
  blocks, using the closure properties (bounded quantifiers by collection);
- prove Post's theorem and use it in both directions: to bound the Turing degree of a set
  from its definition, and to bound the definitional complexity of a set computable or
  c.e. in an iterated jump;
- prove completeness results for index sets: static reductions at the second level, and
  marker constructions at the third, including the coding of a set into the complement;
- explain why the hierarchy is called arithmetic, express computations by formulas with
  the β-function, and derive Tarski's theorem and the first incompleteness theorem;
- choose the kind of index that carries the information needed in a construction, and
  prove by self-reference that a conversion is not uniform.

**Role in the track.** Fifth course of the computability track (`tracks-design.md`). It
teaches *quantifier counting*, the technique by which every later course measures the
complexity of requirements, of index sets and of the sets built. It is a prerequisite of
the c.e. degrees (simple sets use index sets), of infinite injury (Inf is used in the
high incomplete degree construction), of Π⁰₁ classes and Cohen genericity, and of the higher computability and
reverse mathematics tracks, which use Σ⁰ₙ/Π⁰ₙ without comment. The marker argument of
lesson 4 is the first construction by stages with actors of different priorities, before
the course on c.e. degrees.

## 2. Prerequisites assumed

- Models of computation: primitive recursive functions, bounded quantification, the
  normal form theorem (`thm-kleene-normal-form-proof`), Gödel's β-function (`lem-beta`,
  `def-beta`) from the lesson on coding sequences.
- Fundamentals: c.e. sets and their characterizations (`thm-ce-characterizations`,
  `prop-ce-closure`, `prop-computable-iff-ce-coce`), stages (`prop-stage-properties`),
  SMN in parameter form, the fixed point theorem and its self-reference corollary, Rice's
  theorem, many-one reductions and the m-completeness of ∅′.
- Turing degrees: oracle machines, the use principle (`prop-oracle-stages`), the jump
  theorem (`thm-jump`), the limit lemma, low sets, the relativized universal function and
  SMN theorem.

## 3. Results, lesson by lesson

1. **Σ⁰ₙ and Π⁰ₙ sets** (`sigma-pi-sets`). Definition; normal forms and contraction;
   closure under ∧, ∨, total computable substitution, bounded quantifiers (collection),
   and the matching unbounded quantifier; relativization; many-one reductions preserve
   the levels; Σ⁰ₙ-completeness. Examples: Tot, Fin, Cof, inclusion of c.e. sets.
2. **Post's theorem** (`post-theorem`). Σ⁰₁(Y′) = Σ⁰₂(Y) (`lem-sigma2-jump`); Post's
   theorem relativized (`thm-post`); strictness (`cor-hierarchy-strict`); Δ⁰₂ = limit
   computable, arithmetic = computable in some ∅⁽ⁿ⁾, downward closure of Δ⁰ₙ. Exercises:
   X ≤_T Y iff X′ ≤_m Y′; the Σ⁰₂ "cofinitely often" form; strictness by universal sets
   and diagonalization.
3. **Classifying index sets** (`index-sets`). The method (upper bound by counting, lower
   bound by reduction). Fin Σ⁰₂-complete, Inf and Tot Π⁰₂-complete.
4. **Σ⁰₃-complete sets** (`sigma3-complete`, new on 2026-11-12). Cof Σ⁰₃-complete by a
   marker argument; Rec Σ⁰₃-complete (Rogers), by coding ∅′ into the complement in the
   Π⁰₃ case; Tot^{∅′} Π⁰₃-complete as an exercise.
5. **Arithmetic definability** (`arithmetic-definability`). Bounded formulas define
   primitive recursive relations; Σ₁-definable = c.e.; definable = arithmetic, level by
   level; Tarski's undefinability of truth; first incompleteness theorem for true c.e.
   theories.
6. **Codes for sets** (`codes`). Δ⁰₁, Σ⁰₁, canonical, Δ⁰ₙ₊₁, Σ⁰ₙ₊₁ and lowness indices;
   uniformity expressed by indices; non-uniformity of the conversions Σ⁰₁ → Δ⁰₁,
   Δ⁰₁ → size, Δ⁰₂ → lowness index, by self-reference.

## 4. Proof techniques

- **Quantifier counting** (lesson 1, named there; used in every lesson).
- **Collection** (bounding finitely many witnesses), lessons 1 and 5; Soare's variant with
  a coded finite sequence is mentioned in lesson 1.
- **Pairing / contraction of quantifiers**, lesson 1.
- **Use principle and guessing an oracle by a finite string**, lesson 2
  (`lem-sigma2-jump`).
- **Relativization and induction over oracles**, lesson 2 (Post's theorem is proved for all
  oracles at once); lesson 4, last exercise.
- **Diagonalization** with universal sets, lesson 2 (exercise), and against ∅⁽ⁿ⁺¹⁾ in
  Tarski's theorem, lesson 5.
- **Many-one reductions built with SMN**, lessons 3 and 4.
- **Marker (movable marker) arguments**, lesson 4; **coding** an extra set into the
  complement as a secondary strategy, lesson 4 (Rec).
- **Arithmetization with the β-function**, lesson 5.
- **Self-reference (fixed point theorem)** against an alleged conversion procedure,
  lesson 6, including the oracle version of the fixed point theorem.

## 5. Choices

- **Order: hierarchy, Post, index sets, definability, codes.** Post's theorem is placed
  immediately after the definition because the index-set lessons need it to deduce
  non-membership and degrees. Definability comes after the index sets: it is the
  justification of the name, but no other lesson of the track depends on it, and its
  proofs (β-function) are of a different nature. Codes come last since they use the
  fixed point theorem for oracle machines and low sets.
- **Rec is now proved, not admitted (2026-11-12).** Soare's proof (Theorem 4.3.5) is a
  small addition to the Cof construction, and it teaches a second technique (coding a set
  into the complement as a secondary strategy that is harmless when the primary
  strategy wins), which reappears in the classification of the simple sets and in many
  priority constructions. Admitting the result was the only gap in the classification
  table.
- **Split of the index-set lesson (2026-11-12).** With Rec, the lesson reached about 3200
  words. The second level (static reductions) and the third level (constructions in
  stages) are different in nature, so the lesson was split. The labels
  `thm-cof-complete` and the quizzes on markers moved to `sigma3-complete`; the course is
  not released yet, so no permanent URL is affected.
- **Marker construction kept, Soare's variant mentioned.** The course's construction (the
  least acting n enumerates all markers below the stage except the first n) differs from
  Soare's (only the marker of rank n moves). Both are correct; the existing quizzes test
  the course's version, so it was kept, and a remark (`rem-one-marker`) presents Soare's.
  The Rec proof was adapted to the course's version and checked in detail.
- **Definition of Δ⁰ₙ₊₁ index** as an index of a ∅⁽ⁿ⁾-computable characteristic
  function, as in Monin–Patey. Soare's convention (pairs of Σ indices; his Δ₀ index is our
  Δ⁰₁ index) is mentioned in lesson 6 to prevent confusion when reading his book.
- **Completeness defined with many-one reductions**, as in Monin–Patey, Downey–Hirschfeldt
  and Nies; Soare uses one-one reductions and notes the equivalence. Post's theorem
  gives one-one reductions to ∅⁽ⁿ⁾ anyway.
- **Excluded.**
  - Σ⁰₃ representation theorems (Soare 4.3.5): used in infinite-injury constructions;
    they belong to the course on infinite injury, and are pointed to in lesson 4.
  - The classification of further index sets (Ext, simple sets, Cpl Σ⁰₄-complete): the
    simple sets are an exercise of the course on c.e. degrees; the rest is specialized.
  - The ω-jump and the hyperarithmetic hierarchy beyond the remark True ≡_T ∅^(ω): they
    belong to the higher computability track.
  - Proofs in formal systems (that a computably axiomatized theory has c.e. theorems,
    Gödel's original and Rosser's forms): they belong to a logic course; lesson 5 admits
    the first and states the others.
  - The limit lemma in its strong form (n iterated limits): Nies 1.4.25 lists it as an
    exercise; it was not judged necessary.

## 6. Comparison with the literature

- **Soare, *Turing Computability* (2016), Chapter 4.** Sections 4.1 (levels, Theorem 4.1.4
  closure, placing Fin, Cof, Rec), 4.2 (Post's theorem 4.2.2, hierarchy theorem 4.2.3,
  indices 4.2.4), 4.3 (Fin/Tot 4.3.2, movable markers 4.3.2, Cof 4.3.3, Rec 4.3.5–4.3.6,
  Σ⁰₃ representations 4.3.9–4.3.11), 4.4 (relativized Post, lowₙ/highₙ). The course
  follows the same results for lessons 1–4; it proves bounded quantification by collection
  instead of coded sequences, proves Post's theorem through the one-quantifier lemma, and
  uses a different marker construction. Indices of finite and computable sets: Soare 2.3
  (Nonconversion Theorem 2.3.3, Theorem 2.3.7, Exercise 2.3.13).
- **Monin–Patey, chapter *Arithmetic hierarchy*.** Same definitions; closure presented as
  uniform unions and intersections; Post's theorem proved by first showing ∅⁽ⁿ⁾ is
  Σ⁰ₙ-complete; the section *Arithmetic codes* is the source of lesson 6 (canonical codes,
  lowness codes, the two fixed point exercises). Definability is in the chapter *Formal
  interlude*, section on the incompleteness theorems.
- **Downey–Hirschfeldt, Sections 2.5–2.6.** A short version: Post's theorem 2.6.4 and the
  index sets Fin, Tot, Inf, Cof (Theorem 2.6.5, proof sketched). No Rec.
- **Nies, Section 1.4.** Post's theorem 1.4.13, the Σ⁰₂ approximation 1.4.17 (close to the
  third exercise of lesson 2), and the index sets as Exercises 1.4.20–1.4.21.
- The course is closer to Soare in content and to Monin–Patey in conventions.

## 7. Pedagogical plan

1. `sigma-pi-sets`: intuition of quantifiers as unbounded searches; figure of the
   hierarchy (generator: `hierarchy`); examples Tot, Fin, Cof; worked example of the
   inclusion relation with the explicit prefix manipulation; counterexample for
   unbounded collection (∀z ∃y y > z); counterexample for countable unions (exercise).
2. `post-theorem`: the remark after the lemma (one jump for one quantifier); table of the
   first levels; remark on relativization as the engine of the induction; counterexample
   showing that Σ⁰ₙ is not closed under ≤_T (complement of ∅⁽ⁿ⁾).
3. `index-sets`: how the quantifiers of a definition are matched with those of "W_e is
   finite"; intuition of the set V_x before the proof for Fin.
4. `sigma3-complete`: intuition of markers before the proof; figure of a run of the
   construction (generator: `markers`); remark on Soare's variant; intuition of the
   coding strategy before the Rec proof; quizzes on the choice of the least acting n, on
   keeping n markers, and on the coding.
5. `arithmetic-definability`: intuition that halting computations are finite objects
   checked by bounded formulas, and that the β-function replaces the missing sequence
   quantifier. Possible later addition: a figure of the β-coding of a short sequence.
6. `codes`: worked example of the three kinds of index of D₅ = {0, 2} and of an index of
   ∅ that is not a Δ⁰₁ index; figure of the conversions (generator: `indices`); the two
   points of care in self-reference arguments.

## 8. Sources (checked 2026-11-12)

- Lesson 1: Kleene 1943 (Trans. AMS 53, 41–73) and Mostowski 1947 (Fund. Math. 34,
  81–112) for the hierarchy; Soare 2016 §4.1 (Theorem 4.1.4, Proposition 4.1.7 for the
  inclusion example); Downey–Hirschfeldt §2.5; Nies §1.4; Monin–Patey.
- Lesson 2: Post 1948 (Bull. AMS 54, 641–642, abstract; reference checked in Soare's
  bibliography); Kleene–Post 1954 (Ann. of Math. 59, 379–407); Soare Theorems 4.2.2, 4.2.3,
  4.4.2; Downey–Hirschfeldt Theorem 2.6.4; Nies Theorem 1.4.13 and Proposition 1.4.17.
- Lesson 3: Soare Theorem 4.3.2; Downey–Hirschfeldt Theorem 2.6.5; Nies Exercise 1.4.20.
- Lesson 4: Soare §4.3.2–4.3.5 (Theorem 4.3.3, Theorem 4.3.5 and Corollary 4.3.6
  attributing Rec to Rogers, Remark 4.3.8); Downey–Hirschfeldt Theorem 2.6.5; Nies
  Exercises 1.4.20–1.4.21.
- Lesson 5: Gödel 1931; Tarski 1936 (Studia Philosophica 1, 261–405); Rosser 1936 (JSL 1,
  87–91); Kaye 1991 Theorem 3.3 as cited by Nies §1.4; Monin–Patey, *Formal interlude*.
- Lesson 6: Soare §2.3 and Definition 4.2.4; Nies Definition 1.1.14 (strong indices);
  Monin–Patey, section *Arithmetic codes*.

## 9. Recent literature

Checked on 2026-11-12 by web search for simpler proofs or new presentations of Post's
theorem and of index set classifications. Nothing changes the core material, which is
classical. Found: work on index sets in other settings (classes of c.e. equivalence
relations, computable structures), which belongs to specialized courses; and a 2024
arXiv preprint (arXiv:2410.15795, by T. Kihara according to the search results) studying
Σ⁰₃/Π⁰₃-complete problems under a realizability-based reducibility. It was not read in
full and is not cited in the course. Lempp's paper on hyperarithmetical index sets
describes the shift from geometric (marker) arguments to inductive ones at higher
levels; it is not used.

## 10. Open points

- The attribution of the notation Σ⁰ₙ/Π⁰ₙ to Addison was removed because it could not be
  checked against the available books; restore it with a precise reference if found
  (candidate: Addison, Fund. Math. 46 (1959), 123–135).
- The previous claims that Post's theorem is proved in Kleene's *Introduction to
  Metamathematics* and that its jump formulation "follows Kleene and Post (1954)" were
  removed as unverified. Check Kleene 1943 and 1952 for the hierarchy theorem via
  enumeration (the diagonal exercise of lesson 2) and attribute it if confirmed.
- Tarski's paper: the volume of Studia Philosophica is dated 1935, the offprint appeared
  1935/1936; the course says 1936. Check if a standard date is wanted.
- Durations: by the word-count rule, `sigma-pi-sets` and `arithmetic-definability` are
  50 minutes, slightly above the 45-minute target; the word count is inflated by
  formulas. A split of `arithmetic-definability` (definability vs. Tarski and Gödel)
  is possible if it grows.
- `index-sets` is now short (25 minutes). It could receive Soare's single reduction
  (Σ⁰₂, Π⁰₂) ≤₁ (Fin, Tot) or a figure of the set V_x.

## 11. History

- **2026-11-12.** Design and pedagogy revision. Wrote this log. Split `index-sets` into
  `index-sets` (method, second level) and the new lesson `sigma3-complete` (Cof, and Rec
  now proved by coding ∅′, following Soare Theorem 4.3.5). Added: intuition paragraphs in
  every lesson; the method of quantifier counting named, with the worked example
  `ex-inclusion-pi2`; a remark on relativization and a table of the first levels in
  Post's theorem; an exercise proving strictness by universal sets; `rem-one-marker` on
  Soare's marker variant; `thm-rec-complete` with quizzes; the Π⁰₃-completeness of
  Tot^{∅′} as an exercise; `ex-indices` and the comparison of index conventions with
  Soare; two new figures (`markers`, `indices`) in `scripts/figures/arithmetic-hierarchy.py`.
  References checked against Soare 2016, Downey–Hirschfeldt, Nies and Monin–Patey;
  Soare 1987 section numbers replaced by verified Soare 2016 ones; unverifiable
  attributions removed (see Open points).
