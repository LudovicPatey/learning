# Design log: Oracles and Turing degrees

## 1. Objectives

After the course, a student can:

- define oracle computations precisely, with finite oracles and stages, and use the use principle in proofs;
- relativize the results of the course on fundamentals, and recognize when a relativized result is uniform in the oracle;
- manipulate Turing reducibility, degrees, joins and the jump, including one-one reductions between jumps;
- characterize the sets computable in ∅′ by limit approximations, and relate approximations to domination (modulus, computation function);
- build sets with prescribed properties by finite extensions, with control of the oracle needed (∅′ for Kleene–Post and 1-generic sets);
- control the jump of a constructed set: non-computable low sets (forcing the jump), high sets avoiding a cone (coding into the limit).

**Role in the track.** Fourth course of the computability track (`tracks-design.md`), after the fundamentals. It provides the language used by every later course: oracle computation, ≤_T, the jump, Δ⁰₂ approximations. It teaches two of the techniques listed for the track: *finite extensions* and *the limit lemma*. The arithmetic hierarchy, Post's problem, Π⁰₁ classes and immunity all assume it.

## 2. Prerequisites assumed

- Turing machines and their conventions (`models-of-computation`), coding of configurations, primitive recursive normal form (`fundamentals/programs-as-numbers`, `thm-kleene-normal-form-proof`).
- Universal function, SMN theorem, padding lemma, fixed point theorem, Rice's theorem (`fundamentals`).
- C.e. sets: characterizations, c.e. approximations, m-completeness of the halting set, closure of c.e. sets under m-reductions (`fundamentals/ce-sets`).
- Cantor space notation, pairing, principal functions, and the finite extension lemma (`countability/requirements`, `lem-finite-extension`).
- König's lemma (used in one exercise only).

## 3. Results, lesson by lesson

1. **oracle-computation.** Oracle machines and functionals; computations with finite oracles and stages (`prop-oracle-stages`: primitive recursiveness, monotonicity, approximation); use and use principle (`thm-use-principle`); continuity of functionals.
2. **relativization** (new, 2026-11-12). Relative computability and enumerability; relativization principle with a worked example (relativized complementation theorem, `ex-relativized-complementation`); relativized universal function and SMN theorem, uniform in the oracle; Baker–Gill–Solovay (admitted); functions as oracles.
3. **turing-reducibility.** ≤_T is a uniform preorder (`prop-turing-preorder`); degrees, countability of lower cones, no countable cofinal family of degrees (`prop-degree-countable`); join as least upper bound; c.e. sets below ∅′. Non-lattice facts are admitted and referred to `degree-structure`.
4. **turing-jump.** Jump theorem (`thm-jump`): X′ is X-c.e., 1-complete, strictly above X, monotone; degree invariance and iterated jumps; Tot, Inf, Fin computable in ∅″; exercise: X ≤_T Y iff X′ ≤_1 Y′.
5. **limit-computability.** Shoenfield's limit lemma (relativized); moduli; complete sets characterized by domination of the modulus of ∅′; domination of the computation function (Miller–Martin) and its consequence that non-zero Δ⁰₂ degrees are hyperimmune (stated).
6. **finite-extensions.** Meeting dense sets (`lem-meet-dense`), Kleene–Post, cone avoidance, 1-generic sets (existence below ∅′, not c.e. nor co-c.e.).
7. **low-and-high.** Basic properties of low sets; 1-generic sets are GL₁, hence non-computable low sets exist; high sets avoiding a cone, hence high incomplete sets. Jump inversion and high incomplete c.e. sets are admitted.

## 4. Proof techniques

| Technique | Where taught | Where used |
| --- | --- | --- |
| Use principle / continuity of functionals | oracle-computation | all later lessons |
| Search over finite oracles and stages (Σ⁰₁ witnesses of convergence) | oracle-computation (`prop-oracle-stages`) | transitivity, Kleene–Post, cone avoidance, generic lowness |
| Compactness (König's lemma) for total functionals | oracle-computation, exercise | Π⁰₁ classes course |
| Relativization, uniformity in the oracle | relativization | jump monotonicity, relativized limit lemma |
| Simulation of an oracle by a computation | turing-reducibility (transitivity) | jump monotonicity |
| Diagonalization against countably many reductions | turing-reducibility (`prop-degree-countable`), turing-jump (item 4) | |
| Approximation in the limit; the "will it change again?" question to ∅′ | limit-computability | low-and-high, ce-degrees, pi01-classes |
| Domination arguments (modulus, frames) | limit-computability | immunity-growth |
| Finite extensions, dense sets, effectivity analysis of a construction | finite-extensions | low-and-high, cohen-genericity, degree-structure |
| Forcing the jump | low-and-high (`thm-generic-low`) | cohen-genericity |
| Coding into the limit with conditions (σ, m) | low-and-high (`thm-high-cone-avoidance`) | infinite-injury (high incomplete c.e. sets) |

## 5. Choices

- **Oracle-tape model** (as in Soare, Definition 3.2.1) rather than query states: the use is then an initial segment and the use principle is immediate. The query-state model is mentioned in a quiz.
- **Finite oracles and stages made explicit** (`def-finite-oracle`). Every later construction quantifies over strings and stages; making the primitive recursive relation explicit removes all vagueness from "ask ∅′ whether some extension converges".
- **Relativization as its own lesson** (2026-11-12). The first lesson had 3100 words and two topics; the relativization part also deserved a worked example of relativizing a proof, and the distinction between X-computable and uniformly computable, which recurs in every later course. Labels moved with their statements; no label was renamed.
- **Function oracles** through their graphs, introduced once, in the relativization lesson.
- **Non-lattice structure admitted** in turing-reducibility, proved in the specialized course `degree-structure`, as decided in `tracks-design.md` (structure of the degrees is specialized).
- **Totality and finiteness** are only located below ∅″ here; their completeness belongs to the arithmetic hierarchy course, where Post's theorem is proved.
- **Computation function in the limit lemma lesson**, not in immunity-growth: it is the natural continuation of the modulus and gives the first domination argument. Hyperimmunity itself is left to immunity-growth.
- **1-generic sets in finite-extensions**, only to the extent needed for lowness: definition, existence below ∅′, non-c.e. The full theory (n-genericity, Posner–Robinson, measure/category) is in the specialized course `cohen-genericity`.
- **Low sets via genericity, not via priority.** The priority construction of a low c.e. set belongs to `ce-degrees`. Genericity gives non-computable low sets with the finite extension method alone, and introduces forcing the jump.
- **High sets by the finite-extension coding of Monin–Patey**, rather than by Friedberg's jump inversion (admitted) or by a maximal set (Martin). It reuses the technique of the cone avoidance proof and introduces conditions with an infinite component, the step towards forcing.
- **Excluded:** strong reducibilities (tt, wtt), Post's theorem and the arithmetic hierarchy, minimal degrees and exact pairs, Friedberg jump inversion (stated), low basis theorem (in pi01-classes), domination characterization of high degrees (immunity-growth), n-c.e. hierarchy beyond the d.c.e. exercise.

## 6. Comparison with the literature

- **Soare 2016.** Chapter 3 (§§3.1–3.6: oracle machines, use, jump theorem 3.4.3, limit lemma 3.6.2, moduli §3.5) and Chapter 6 (§6.1 Kleene–Post, §6.2 cone avoidance 6.2.6, §6.3 1-generic sets and forcing the jump, §6.4 Friedberg's criterion), Theorem 5.6.6 (computation function). The course follows Soare's order for the first half, but treats low and high sets together, with constructions, where Soare defines them in §3.6 and constructs them in Chapters 6–7. Soare's jump theorem includes the converse of monotonicity for 1-reducibility, added here as an exercise.
- **Monin–Patey,** chapter "Turing degrees": same sequence of topics (oracles, relativization, use, degrees, jump, limit computability with modulus and computation function, finite extensions, low and high degrees). The proof of the computation-function theorem and the high cone avoidance construction follow it. Monin–Patey prove lowness by a direct ∅′-construction forcing the jump; the course goes through 1-genericity, which yields the stronger GL₁ statement and is reused by `cohen-genericity`.
- **Downey–Hirschfeldt 2010,** §2.4 (reductions, use principle 2.4.1), §2.6 (limit lemma 2.6.1), §2.10 (Kleene–Post 2.10.2), §2.24 (genericity, Theorem 2.24.3: n-generic sets are GL_n). Their presentation is terser and stage-based.
- **Nies 2009,** §1.2 (Turing reducibility, jump, use principle), §1.4 (limit lemma 1.4.2), §1.5 (low and high), §1.6 (incomparable Δ⁰₂ sets).
- Differences: this course makes finite oracles and stages a definition, separates relativization into a lesson, and adds figures for the use, the join, the jump hierarchy, Δ⁰₂ approximations, frames, the Kleene–Post construction and the conditions of the high construction.

## 7. Pedagogical plan

- **oracle-computation.** Intuition: an infinite oracle, but a finite computation. Examples: two functionals (`ex-functionals`), one total for every oracle, one whose domain depends on the oracle; fast-growing oracles compute ∅′ (`ex-oracle-domination`); a computation with a string oracle that is undefined. Counterexample: finiteness of X is not computable by any functional (continuity). Figure: oracle machine and use.
- **relativization.** Intuition: proofs are algorithms. Examples: X-computable sets, a set X-computable for every X but not uniformly (`ex-relative-computability`, exercise); a proof relativized word for word. Warning: relativize the definitions of particular sets too.
- **turing-reducibility.** Intuition: adaptive finitely many questions; counting arguments. Examples: `ex-turing-reductions` (∅′ ≤ Tot). Counterexample: union is not an upper bound (quiz). Figure: the join.
- **turing-jump.** Intuition: relativized diagonalization plus uniformity. Examples: `ex-jumps` (K^X, jump of a computable set, ∅″). Counterexample: X′ ≤_T Y′ does not imply X ≤_T Y (low sets), while X′ ≤_1 Y′ does. Figure: the first jumps.
- **limit-computability.** Intuition: mind changes. Examples: co-c.e. approximation, non-uniqueness of approximations, Tot has none; modulus versus computation function on an explicit approximation (`ex-modulus-computation`). Why c(x) ≥ x is needed. Figures: Δ⁰₂ table, frames.
- **finite-extensions.** Intuition: requirements secured by finite information. Figure: Kleene–Post steps. Counterexample: cone avoidance fails for computable C. Example: 1-generic sets contain arbitrarily long blocks (`ex-1-generic`).
- **low-and-high.** Intuition: forcing the jump; coding ∅″ into the limit of columns. Counterexample: low sets not closed under join (admitted, Sacks splitting). Figure: conditions (σ, m).

## 8. Sources (checked against the books, 2026-11-12)

- oracle-computation: Turing 1939; Kleene–Post 1954; Soare 2016 Definition 3.2.1, Theorem 3.3.9; Downey–Hirschfeldt Proposition 2.4.1 (use = 1 + largest query, as here; Soare uses the largest query).
- relativization: Soare 2016 §4.4 (relativization as a principle); Monin–Patey, relativized SMN theorems; Baker–Gill–Solovay 1975.
- turing-reducibility: Post 1944; Kleene–Post 1954; Spector 1956; Soare 2016 §3.4 and Theorem 6.5.3 (Kleene–Post–Spector exact pairs); Nies §1.2.
- turing-jump: Kleene–Post 1954; Soare 2016 Theorem 3.4.3; Steel 1982; Slaman–Steel 1988; Lutz–Siskind 2023.
- limit-computability: Shoenfield 1959; Putnam 1965; Gold 1965; Soare 2016 Lemma 3.6.2, §3.5, Theorem 5.6.6, Corollary 5.6.7 (Miller and Martin 1968); Downey–Hirschfeldt Theorem 2.6.1; Nies Lemma 1.4.2; Monin–Patey, Proposition "Martin and Miller".
- finite-extensions: Kleene–Post 1954; Soare 2016 Theorems 6.1.1, 6.2.6, §6.3; Downey–Hirschfeldt Theorem 2.10.2, §2.24, §8.12 (de Leeuw–Moore–Shannon–Shapiro, Sacks); Jockusch 1980; Feferman 1965.
- low-and-high: Jockusch 1980 (Downey–Hirschfeldt Theorem 2.24.3; Soare Exercise 6.3.4 credits Jockusch–Posner); Friedberg 1957 (Soare Theorem 6.4.1); Sacks 1963; Martin 1966 (Soare Theorem 4.5.6); Soare Theorem 7.5.1 (low splitting); Monin–Patey, section on high degrees.

## 9. Recent literature

- Checked whether more recent work changes the presentation of the elementary theory of the Turing degrees: no simpler proofs of the limit lemma, Kleene–Post or the computation-function theorem were found; the standard presentations (Soare 2016, Monin–Patey) are the ones followed.
- Martin's conjecture, which gives a perspective on why the jump is the canonical degree-invariant operation: Steel, JSL 47 (1982) 347–358; Slaman and Steel, Cabal Seminar 81–85, LNM 1333 (1988) 37–55; Lutz and Siskind, *Part 1 of Martin's conjecture for order-preserving and measure-preserving functions*, arXiv:2305.19646 (2023). A journal version (Journal of the AMS, 2024) is listed by some sources but was not confirmed; the course cites the arXiv version. Effect: a paragraph in the notes of the jump lesson.

## 10. Open points

- **Lesson lengths.** Without the further exercises, oracle-computation (≈2900 words) and finite-extensions (≈2900) still come out at about 53 minutes with the word-count rule, and limit-computability at about 48; their durations are set to the 45-minute maximum (2026-11-13). Possible further split: move 1-generic sets out of finite-extensions into a lesson with generic lowness; this would change lesson-level prerequisites in `degree-structure/embeddings.md`, `cohen-genericity` and `randomness-notions`.
- The low splitting (two low c.e. sets joining to ∅′) is admitted; `ce-degrees/sacks-splitting` proves the splitting without lowness.
- A figure for the forward direction of the limit lemma (approximations of ∅′ and the use) could be added.

## 11. Exercises

Every exercise has a label, an objective, a difficulty and a complete solution. The featured exercises stay in the text, after the material they practice; the others form the block of further exercises at the end of each lesson, outside the reading time.

**Featured exercises, and why.**

- oracle-computation: `ex-total-functional-use-bound` (computable bound on the use of a functional total on all oracles): the first compactness argument of the track, reused in the course on Π⁰₁ classes.
- relativization: `ex-relativized-rice` (a relativized proof done by the reader) and `ex-union-uniform` (uniform versus oracle-by-oracle computability, the distinction the lesson is about).
- turing-reducibility: `ex-turing-iff-join-ce` (≤_T through relative enumerability, used later for jumps) and `ex-principal-function-degree` (function oracles, cited by the relativization lesson).
- turing-jump: `ex-jump-one-one` (the converse of monotonicity for ≤_1, cited in the text) and `ex-jump-of-join` (the jump does not commute with the join).
- limit-computability: `ex-dce-limit` (the simplest approximations with bounded mind changes) and `ex-bounded-changes-use` (mind changes versus use, the link between approximations and reductions).
- finite-extensions: `ex-independent-sequence` (Kleene–Post for infinitely many sets, cited in the lesson on Turing reducibility).
- low-and-high: `ex-generic-gl1` (1-generic sets are exactly GL₁ in the sense of the definition) and `ex-coding-into-jump` (the high construction with an arbitrary set coded into the limit).

**Further exercises, lesson by lesson.**

- oracle-computation: computing with a finite oracle on an example; domains of functionals are unions of cylinders (no functional detects finiteness or infiniteness); convergence with a finite oracle is c.e. and not computable; the prefix-free set of minimal oracles of a computation; the hypothesis "total on every oracle" in the use bound; the use is computable from the oracle.
- relativization: computable oracles add nothing; relativized diagonal argument against total functions; a uniform enumeration of non-empty X-c.e. sets by a search; relativized selection is not computable (contrast with SMN); graph versus region below the graph as function oracles.
- turing-reducibility: monotonicity of the join; every non-zero degree contains a set neither c.e. nor co-c.e.; strict upper bounds for sequences of degrees; uncountably many degrees above every degree; the coding of a sequence is not an operation on degrees unless it is uniform.
- turing-jump: X from X′ uniformly; Tot-like index sets (emptiness, finiteness); variants of X′ that are 1-equivalent to it; uniform monotonicity of the jump; the diagonal set of `prop-degree-countable` is below W′; Cof below ∅‴; ∅^(ω) above all ∅^(n).
- limit-computability: the modulus of ∅′ escapes computable functions; closure of Δ⁰₂ approximations; the limit lemma for functions; bounded use gives bounded mind changes (ω-c.e. sets); a Δ⁰₂ approximation of ∅ whose modulus computes ∅′; a co-d.c.e. set that is not d.c.e.; modulus and computation function of a c.e. approximation.
- finite-extensions: upper bounds of sequences of degrees; complements of 1-generic sets; examples of dense sets; sets computed by every non-computable set; why 1-genericity quantifies over c.e. sets only; the even part of a 1-generic set is 1-generic; cone avoidance below C′ by e-splittings (difficulty 3).
- low-and-high: lowness through the limit lemma; closure properties of low and high sets; no GL₁ set computes ∅′; relative 1-genericity and a set G with A ⊕ G low for low A; the high cone-avoiding set can be computed in ∅″.

**Sources.** Soare 2016: Exercise 3.3.21 (`ex-relativized-selection`), Exercise 3.4.7 (`ex-coding-not-invariant`), Theorem 3.8.8 and Exercise 3.8.16 (`ex-bounded-use-changes`, `ex-co-dce`), Theorem 6.2.6 (`ex-cone-avoidance-jump`); Downey–Hirschfeldt 2010, Corollary 2.6.2 (ω-c.e. sets); Nies 2009, Exercise 1.4.7 (`ex-limit-lemma-functions`); Monin–Patey, section on high degrees (`ex-coding-into-jump`). The other exercises are standard consequences of the lessons. Checked against other courses to avoid duplicates: the halves of a 1-generic set (incomparability) and 2-generic sets are in `cohen-genericity`, the uniform fixed point theorem without oracle in `fundamentals`, completeness of Cof in `arithmetic-hierarchy`, open and closed classes in `pi01-classes`.

**Dropped.** A Δ⁰₂ approximation of a non-computable set whose least correct stage (without the condition c(x) ≥ x) is computably bounded (Soare 2016, Exercise 3.5.6): no short complete solution was written; the remark after `thm-computation-function` already explains the role of the condition.

## 12. History

- **2026-11-12.** Design revision. Split the first lesson: new lesson `relativization` (relativization principle with a worked example, uniformity, universal function and SMN theorem, function oracles, relativized Rice exercise, a non-uniformity exercise). New examples: `ex-functionals`, `ex-relative-computability`, `ex-relativized-complementation`, `ex-turing-reductions`, `ex-jumps`, `ex-delta2-approximations`, `ex-modulus-computation`, `ex-1-generic`; new quiz question on continuity; new exercises (X ≤_T Y iff X′ ≤_1 Y′; relativized Rice; non-uniformity). Five new figures (join, first jumps, frames, Kleene–Post steps, conditions of the high construction) generated by `scripts/figures/turing-degrees.py`. The theorem `thm-computation-function` is no longer called "Martin–Miller theorem" (not a standard name); it is attributed to Miller and Martin (1968) with Soare Theorem 5.6.6. References checked against Soare, Downey–Hirschfeldt, Nies and Monin–Patey; sources added to every lesson; the cone avoidance note now cites Sacks and de Leeuw–Moore–Shannon–Shapiro precisely; generic lowness credited to Jockusch (1980) with Soare's Jockusch–Posner attribution noted. Notes on Martin's conjecture added to the jump lesson. Durations recomputed. The prerequisite of finite-extensions now points to `countability/requirements`, after the split of the countability course.
- **2026-11-13.** Featured and further exercises: labels, objectives and difficulties for the 21 existing exercises; 12 kept in the text as featured exercises, placed after the material they practice, the others moved to a block of further exercises at the end of each lesson; 33 new further exercises (sources in section 11). Durations recomputed without the further exercises (oracle-computation, limit-computability and finite-extensions set to the 45-minute maximum). The lesson `relativization` now has `fundamentals/rice-theorem` as a prerequisite, since its featured exercise relativizes Rice's theorem.
- **2026-11-18.** Lutz–Siskind cited in its journal version (JAMS, published electronically 2024, doi:10.1090/jams/1046), checked on the AMS site.
