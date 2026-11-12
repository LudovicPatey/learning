# Design log: Post's problem and the priority method

## 1. Objectives

After the course, a student can:

- state Post's problem and Post's program, build a simple set, and prove that simple sets are not many-one complete through productive and creative sets;
- organize a construction by requirements, priorities, strategies, witnesses and initialization, and verify it by induction along the priority order;
- use restraints to preserve computations, and prove lowness through the limit lemma;
- use the length of agreement and Sacks' preservation strategy, which turns a non-computability hypothesis into the finiteness of restraints;
- combine strategies of different kinds in one construction, and distinguish bounded from unbounded finite injury;
- derive the first structural facts on the c.e. degrees: incomparable degrees, no minimal c.e. degree, every non-zero c.e. degree is the join of two incomparable low c.e. degrees.

**Role in the track.** Sixth course of the computability track (`tracks-design.md`), after the arithmetic hierarchy. It teaches the technique listed for it in the track design, *finite injury priority*. Later courses assume it: `immunity-growth` (simple sets, effectively simple sets, the low simple set), `k-trivials` (Post's construction, cost functions), `infinite-injury` (Sacks' preservation strategy, the minimal pair method), `degree-structure`.

## 2. Prerequisites assumed

- C.e. sets and their enumerations, injective enumeration of an infinite c.e. set (`prop-ce-range`), SMN theorem with parameters (`cor-smn-parameters`), padding lemma (`lem-padding`), canonical indices of finite sets, Rice's theorem (`fundamentals`).
- Many-one reducibility and m-completeness of ∅′ (`fundamentals/complete-sets`).
- Oracle computations with finite oracles and stages (`prop-oracle-stages`), use and use principle (`def-use`, `thm-use-principle`), relativized SMN (`thm-relativized-smn`), Turing reducibility and join (`turing-degrees`).
- Shoenfield's limit lemma (`thm-limit-lemma`), low sets (`prop-low-basic`), the Kleene–Post theorem (`thm-kleene-post`) as the model of a diagonalization by finite extensions.
- Quantifier counting (`arithmetic-hierarchy`), for one exercise on index sets.

Convention used throughout: a computation $\Phi^{A_s}_e(x)[s]$ that converges has use at most $s$ (it has fewer than $s$ steps); restraints are uses, and "injury" means the enumeration of a number at most the restraint.

## 3. Results, lesson by lesson

1. **simple-sets.** Post's problem (`def-post-problem`); immune and simple sets (`def-simple`), examples of non-simple sets (`ex-not-simple`); Post's simple set (`thm-post-simple`), which is effectively simple, hence Turing complete (`rem-post-set-complete`, Martin, proved in `immunity-growth`); productive and creative sets (`def-productive`), ∅′ creative (`prop-halting-creative`), productive sets contain infinite c.e. sets (`lem-productive-infinite`), productivity transfers along m-reductions (`prop-productive-reduction`), index sets that are productive (`ex-creative-index`); simple sets are not m-complete (`thm-simple-not-complete`). Admitted: Myhill's theorem, Post's theorem on hypersimple sets; Dekker's theorem is referred to `immunity-growth`.
2. **friedberg-muchnik.** The Friedberg–Muchnik theorem (`thm-friedberg-muchnik`) and the solution of Post's problem (`cor-post-problem`); preservation lemma (`lem-fm-preservation`), finite injury lemma (`lem-fm-finite-injury`); the general structure of a finite injury argument; bounded injury (2^i − 1, exercise); a uniformly c.e. independent sequence (exercise).
3. **low-simple-set.** A low simple set (`thm-low-simple`, `cor-low-simple-post`); restraint function (`def-restraint-function`), walls; lemmas `lem-low-coinfinite`, `lem-low-negative`, `lem-low-positive`. Exercises: superlowness (computably bounded changes), splitting a c.e. set into two low c.e. sets, with the Bickford–Mills obstruction to superlow halves.
4. **sacks-splitting.** Length of agreement (`def-length-agreement`); the Sacks splitting theorem (`thm-sacks-splitting`), main lemma (`lem-sacks-main`); the role of each hypothesis; unbounded injury; consequences: splitting ∅′, incomparable splittings (`cor-splitting-post`), no minimal c.e. degree (`cor-no-minimal-ce`). Exercise: why the restraint must cover the computation at the length of agreement.
5. **cone-avoidance** (new, 2026-11-12). Sacks' cone avoidance theorem for a simple set (`thm-sacks-cone-avoidance`); the halves of a Sacks splitting are low (`thm-low-splitting`); every non-zero c.e. degree is the join of two incomparable low c.e. degrees (`cor-low-join`); every c.e. degree strictly between 0 and 0′ has an incomparable c.e. degree (`cor-incomparable-ce`); outlook: density, minimal pairs, injury-free solutions. Admitted: density, minimal pairs (proved in `infinite-injury`), Kučera's solution.

## 4. Proof techniques

| Technique | Where taught | Where used later |
| --- | --- | --- |
| Diagonalization read as an algorithm (productive functions) | simple-sets (`prop-halting-creative`, `lem-productive-infinite`) | immunity-growth (effective immunity, fixed points) |
| Requirements acting once, with a size constraint (counting argument) | simple-sets (Post), low-simple-set, cone-avoidance | k-trivials (cost functions) |
| Finite injury with initialization and fresh witnesses | friedberg-muchnik | infinite-injury, degree-structure |
| Restraints read directly by positive requirements (walls) | low-simple-set | cone-avoidance |
| Lowness through the limit lemma (preserve Φ^A_e(e)) | low-simple-set, cone-avoidance (`thm-low-splitting`) | immunity-growth, pi01-classes (comparison with the low basis theorem) |
| Length of agreement and Sacks' preservation strategy | sacks-splitting | cone-avoidance, infinite-injury (minimal pairs) |
| Bounded versus unbounded finite injury | friedberg-muchnik (2^i − 1), low-simple-set (e), sacks-splitting (unbounded) | — |
| Induction along the priority order, carrying the finiteness of restraints | all priority lessons; explicitly in sacks-splitting | infinite-injury |

The course names the technique of each proof, refers to the lesson where it was introduced, and the end of `friedberg-muchnik` lists the four ingredients of a finite injury argument (requirements, strategies with outcomes, injury and initialization, induction).

## 5. Choices

**Included.**
- *Simple, productive and creative sets.* They explain Post's program and why the priority method was needed, and they are used in `immunity-growth` and `k-trivials`. The proof that m-complete sets have productive complements is short and teaches the "effective diagonalization" view.
- *Friedberg–Muchnik first.* It is the historical solution, the canonical bounded-injury argument, and continues the Kleene–Post theorem of `turing-degrees` directly (same requirements, computable instead of ∅′-computable construction). Soare (2016) puts the low simple set first, as "probably the easiest" solution; we keep Friedberg–Muchnik first because it introduces initialization and fresh witnesses, and because diagonalization requirements are more familiar than preservation requirements at this point.
- *Low simple set.* It introduces negative requirements, restraints as walls, and lowness by the limit lemma, which reappear in every later construction of a low c.e. set.
- *Sacks splitting.* The first unbounded finite injury argument, and the first preservation of an agreement rather than of a single computation; it gives the first structural results on the c.e. degrees.
- *Cone avoidance and low splittings* (added 2026-11-12, in a new lesson). Soare's Section 7.4 isolates the preservation strategy in a simpler setting (one set, bounded injury from the positive side), and his Theorem 7.5.1 states that the halves are low. Placing these after the splitting theorem lets the lesson show that the preservation strategy is a module that combines with other requirements, and contrasts bounded with unbounded injury side by side. Before this revision, the Sacks lesson had about 3500 words with the new material; splitting it kept the existing labels in place (the labeled corollaries stay in `sacks-splitting`) while keeping each lesson under about 2750 words.

**Excluded, with reasons.**
- *Permitting* (Soare 5.2, Monin–Patey). Useful, but not needed by the later courses of the track; it appears in specialized courses where needed. A remark could be added later.
- *Hypersimple sets, Dekker's theorem, effectively simple sets and Arslanov's criterion.* They belong to `immunity-growth`, where they are proved; this course states them with forward references.
- *Myhill's isomorphism theorem.* Admitted with a reference; its proof uses the fixed point theorem and does not use priority.
- *Lachlan games* (Soare 2.5): a presentation device, excluded at the track level.
- *The Δ⁰₂ version of the preservation strategy* (Soare 7.6): mentioned only; it needs the maximal length of agreement, a variation without new ideas at this level.
- *Density and minimal pairs*: infinite injury, in the specialized course `infinite-injury`.

**Order.** simple-sets → friedberg-muchnik → low-simple-set → sacks-splitting → cone-avoidance. Each lesson adds one ingredient: requirements acting once; injury and initialization; restraints and lowness; preservation of agreement and unbounded injury; combination of strategies.

## 6. Comparison with the literature

- **Soare 2016.** §2.4 (productive and creative sets, Myhill's theorem 2.4.6), §5.1–5.4 (Post's problem and program, Post's simple set Theorem 5.2.3, hypersimple sets and Dekker's Theorem 5.3.6, Martin's Theorem 5.4.1), Chapter 7 (7.2 low simple set, 7.3 Friedberg–Muchnik, 7.4 cone avoidance, 7.5 Sacks splitting with low halves, 7.6 Δ⁰₂ cone). The course covers the same material, in a different order (Friedberg–Muchnik before the low simple set), and uses initialization and fresh witnesses in Friedberg–Muchnik where Soare uses restraint functions and witnesses in columns ω^[e].
- **Downey–Hirschfeldt.** §2.11 (Friedberg–Muchnik with followers, Theorem 2.11.1; a low c.e. set attributed to Friedberg, Theorem 2.11.2), §2.12.1 (Sacks splitting as unbounded finite injury), §2.14–2.15 (minimal pairs, density). The course's Friedberg–Muchnik construction is close to theirs.
- **Nies 2009.** §1.6: Post's simple set and its effective simplicity, low simple set (Theorem 1.6.4) and superlowness (Theorem 1.6.5), Friedberg–Muchnik (Theorem 1.6.8), low splitting (Exercise 1.6.10, Bickford–Mills remark), discussion of natural solutions; §4.2 and §5.3: injury-free solutions (Kučera; K-trivial sets).
- **Monin–Patey**, chapter *Priority method and c.e. degrees*: permitting, Friedberg–Muchnik with strategies described by states and outcomes, a low c.e. set (low simple set and low splitting as exercises), the Sacks cone avoidance theorem as a "Σ⁰₂ priority" argument, Sacks splitting as an exercise, then minimal pairs. The course borrows their emphasis on outcomes (passive and active satisfaction) and their classification of the Sacks strategy between finite and infinite injury; it differs by proving the splitting theorem in full and by including simple and creative sets.

## 7. Pedagogical plan

- **simple-sets.** Intuition before Post's construction (one chance per W_e, size constraint 2e, counting); figure `post-simple` (five sets W_e, the bars at 2e, the chosen elements, the resulting S); examples of non-simple sets (computable, ∅′ via padding); remark that Post's set is Turing complete (shows that simplicity does not solve Post's problem); productive sets introduced as effective failure of c.e.-ness; example of productive index sets (a strong Rice theorem). Quizzes on the bound 2e, the growing finite sets, and the m/T distinction.
- **friedberg-muchnik.** Intuition: Kleene–Post made computable, what goes wrong (no oracle questions, no removal). Figure `fm-strategy` (witness entering B, A frozen below the use, fresh region, injury by a higher witness); figure `injury-run` (a run with initializations). The four ingredients of finite injury summarized after the proof. Quizzes on freshness, on the role of the least requirement, on passive satisfaction.
- **low-simple-set.** Why lowness is phrased through the limit of g; the two kinds of strategies and their conflict; non-monotone restraint (worked example); figure `walls` (P₂ beyond the walls of N₀–N₂, injuring N₃); contrast with initialization. Quizzes on priority, preservation, the Δ⁰₂ approximation. Exercises: superlowness; low splitting.
- **sacks-splitting.** Intuition (why diagonalization and single preservation do not suffice); figure `agreement` (length of agreement before and after an element enters B; the protected disagreement); the two outcomes of the strategy; the role of each hypothesis (non-computable, c.e.; Δ⁰₂ version mentioned); unbounded injury. Quizzes on protecting the computation at l, the use of B c.e., the source of injuries.
- **cone-avoidance.** Idea paragraphs before each proof; bounded versus unbounded injury side by side; outlook. Quizzes on the injury count and on the hypotheses of the corollaries.

Possible further figures: a figure for the splitting rule (an element below two restraints placed on the opposite side), and one for the uses of the stages in `lem-fm-preservation`.

## 8. Sources (checked 2026-11-12)

- **simple-sets.** Post 1944; Dekker 1954, 1955; Myhill 1955; Martin 1966 (PAMS 17, 838–842, checked on the AMS site); Harrington–Soare 1991 (PNAS 88, 10242–10246, checked). Soare 2016 §2.4 (Def. 2.4.3, Thm 2.4.4 partial productive functions, Thm 2.4.6 Myhill), §5.1, §5.2 (Def. 5.2.1, Thm 5.2.3, Def. 5.2.4 effectively simple and the remark that Post's set is effectively simple), §5.3.3 (Thm 5.3.6 Dekker), §5.4.1 (Thm 5.4.1 Martin). Nies §1.6 (effective simplicity of Post's set, Prop. 4.1.13 for completeness).
- **friedberg-muchnik.** Muchnik 1956, Friedberg 1957 (references checked in Soare's bibliography). Soare 2016 §7.3 (Thm 7.3.1, Prop. 7.3.5 for |I_e| < 2^e); Downey–Hirschfeldt §2.11 (Thm 2.11.1, bound 2^j − 1); Nies Thm 1.6.8; Monin–Patey. Mytilinaios, JSL 54 (1989), 38–49 (checked on Cambridge Core: Σ₁ induction suffices for Friedberg–Muchnik and Sacks splitting); Chong–Li–Yang, BSL 20 (2014), 170–200 (checked).
- **low-simple-set.** Soare 2016 §7.2 (Thm 7.2.1, §7.2.5 walls, Lemma 7.2.3 for at most e injuries); Downey–Hirschfeldt Thm 2.11.2 (attribution to Friedberg of a low c.e. set); Nies Thm 1.6.4, Thm 1.6.5 (superlow), Def. 1.5.3 (superlow, Mohrherr), Exercise 1.6.10 and the Bickford–Mills remark after it; Monin–Patey (low c.e. set, exercises).
- **sacks-splitting.** Sacks 1963 (Annals 77, 211–231; in Soare's bibliography as the source of the splitting theorem); Spector 1956. Soare 2016 §7.4–7.6, remark after Lemma 7.5.7 (no computable bound on injuries); Downey–Hirschfeldt §2.12.1; Monin–Patey.
- **cone-avoidance.** Soare 2016 Thm 7.4.1 (cone avoidance, Sacks), Thm 7.5.1, Lemma 7.5.7, Cor. 7.5.3, 7.5.6, Exercise 7.6.3; Nies Exercise 1.6.10, §4.2 (Kučera's injury-free solution), §5.3; Kučera 1986 (LNCS 233, 493–500, checked on DBLP); Sacks 1964, Lachlan 1966, Yates 1966 (Downey–Hirschfeldt Thm 2.14.1 and §2.15).

**Corrections made in this revision.**
- References to Soare's book of 1987 were replaced by precise sections of Soare 2016, which could be checked; Odifreddi's book was removed from the references of `simple-sets` (its content could not be checked).
- Myhill's theorem is now referred to Soare 2016, Theorem 2.4.6; Dekker's theorem to Soare 2016, Theorem 5.3.6, and to `immunity-growth`.
- The statement "every non-computable c.e. degree contains a hypersimple set (Dekker 1954)" was rephrased as "every non-computable c.e. set is Turing equivalent to a hypersimple set", which is the form proved in `immunity-growth`.
- The quiz of `simple-sets` now points to Post's own set as a Turing complete simple set (justified by Martin's theorem) instead of an unreferenced claim.
- No mathematical error was found in the existing proofs.

## 9. Recent literature

Checked (November 2026), by web search and in the books:
- **Weak arithmetic.** Mytilinaios (1989) showed that the Friedberg–Muchnik and Sacks splitting constructions can be carried out with Σ₁ induction; Chong, Li and Yang (2014) survey the area. Secondary sources disagree on the exact attribution of the equivalence of Sacks splitting with IΣ₁ over a weak base (Mytilinaios or Mourad), and on Chong–Mourad for Friedberg–Muchnik in BΣ₁; these were not added. Mentioned in the notes of `friedberg-muchnik`.
- **Presentations.** Montalbán, *Priority arguments via true stages* (JSL 79 (2014), 1315–1335) gives a framework for iterated priority arguments by true stages. It concerns infinite and iterated injury rather than the finite injury of this course; recorded here for `infinite-injury`, not added.
- **Injury-free solutions.** Kučera (1986) and the K-trivial sets (Nies §4.2, §5.3) are older than fifteen years but give the modern perspective that priority is not necessary for Post's problem; mentioned in the outlook of `cone-avoidance`.
- **Post's program.** Harrington–Soare (1991) completed Post's program in a revised form (definable property in the lattice of c.e. sets); mentioned in `simple-sets`.
- No simpler proof of the Friedberg–Muchnik or Sacks splitting theorems in the last fifteen years was found. The question of a natural solution to Post's problem (Sacks' question) remains open; it is mentioned through Nies's discussion only.

## 10. Open points

- Lesson lengths: `simple-sets`, `sacks-splitting` and `cone-avoidance` are at about 2600–2750 words (50 minutes), slightly above the 45-minute target.
- A lesson on permitting could be added if a later course needs it (Soare §5.2, §5.5; Monin–Patey).
- The figure generator renders well in browsers; `rsvg-convert` collapses spaces at the start of `tspan` elements, which only affects previews.
- `docs/REVIEW-2026-11.md` had no open item for this course.
- The `immunity-growth` course states (`cor-arslanov` item 3) that the complement of the low simple set is not effectively immune; `rem-post-set-complete` refers to it.

## 11. History

- **2026-11-12.** Design and pedagogical revision. New lesson `cone-avoidance` (cone avoidance for a simple set, low halves of a Sacks splitting, two corollaries on the c.e. degrees, outlook moved from `sacks-splitting`). Four new figures (`post-simple`, `fm-strategy`, `walls`, `agreement`) in `scripts/figures/ce-degrees.py`; the existing `injury-run` is unchanged. Intuition paragraphs before the constructions, examples (non-simple sets, productive index sets, non-monotone restraint), a remark on the completeness of Post's set, a summary of the structure of finite injury arguments, the hypotheses and the unbounded injury of the Sacks construction, superlowness and the Bickford–Mills remark in exercises. References checked against Soare 2016, Downey–Hirschfeldt, Nies and Monin–Patey; Soare 1987 and Odifreddi replaced. Durations recomputed from word counts. All labels kept.
