# Design log: Infinite injury priority arguments

## 1. Objectives

After the course, a student can:

- reduce the meet requirements of a minimal pair construction to one functional (Posner's trick), and state and prove the preservation of agreement between expansionary stages;
- explain why a strategy with an infinitary outcome forces the strategies of lower priority to guess its outcome, and why the guesses must be coherent (nested expansionary stages);
- define a tree of strategies, its priority order, the current path, initialization to the right of the current path, and the true path, and prove that the nodes of the true path are visited infinitely often and initialized finitely often;
- verify a tree construction along the true path, by a case analysis on the position of an acting node relative to the node under consideration;
- build a high incomplete c.e. set by coding Inf into the columns of a c.e. set, and show, with an explicit run, why a finite injury construction cannot do it.

**Role.** Specialized course (in no track of `tracks.yaml`; `tracks-design.md` lists it among the possible specialized courses of computability, "Infinite injury"). It is the natural continuation of `ce-degrees`, which teaches finite injury and Sacks' preservation strategy and states density and minimal pairs without proof (`ce-degrees/cone-avoidance`). Its technique, *infinite injury on a tree of strategies*, is the entry point to the research literature on the c.e. degrees.

## 2. Prerequisites assumed

- From `ce-degrees`: requirements and priorities, fresh followers and initialization (`thm-friedberg-muchnik`), the length of agreement and Sacks' preservation strategy (`def-length-agreement`, `lem-sacks-main`).
- From `turing-degrees`: oracle computations with stages and the convention that a convergent computation at stage s has use at most s (`prop-oracle-stages`), the use principle, the relativized limit lemma (`thm-limit-lemma`), the jump theorem (`thm-jump`), high sets and the forcing construction of a high incomplete set (`thm-high-cone-avoidance`).
- From `arithmetic-hierarchy`: Inf is Π⁰₂-complete (`thm-fin-complete`), ∅″ decides Inf (`prop-tot-double-jump`).
- Cantor pairing ⟨x, y⟩ = (x + y)(x + y + 1)/2 + y (`fundamentals`), increasing in y with ⟨x, y⟩ ≥ y; used in `high-incomplete`.
- A side reference to `degree-structure/exact-pairs` (`cor-not-lattice`), presented as a pointer, not a prerequisite.

## 3. Results, lesson by lesson

1. **minimal-pairs.** Minimal pairs (`def-minimal-pair`); the Lachlan–Yates theorem stated (`thm-minimal-pair`); Posner's trick (`lem-posner`), with the remark that A ≠ B is only used in the proof; length of agreement and expansionary stages relative to a set Q (`def-expansionary`), with an example of each outcome (`ex-expansionary`); total agreement gives unboundedly many expansionary stages (`prop-agreement-unbounded`); the preservation lemma (`lem-pair-module`, `cor-pair-module`). Exercises: the Boolean algebra 2² embeds in the c.e. degrees preserving 0, joins and meets; a strategy restraining always the same side makes that set computable.
2. **trees-of-strategies** (title "Guessing on a tree of strategies"). The strategy for N_e and its outcomes ∞ and f; the two versions of R_d; coherence between two N-requirements (why expansionary stages are relative to Q); the tree method, compared with Friedberg–Muchnik on a tree; the tree and the priority order (`def-strategy-tree`); the construction. Exercise: the priority order is linear, and which nodes have infinitely many nodes of higher priority.
3. **minimal-pair-verification** (new, title "The true path and the verification"). True path (`def-true-path`), example of a node acting infinitely often off the true path (`ex-true-path`), properties of the true path (`lem-true-path`); positive requirements (`lem-mp-positive`); the main lemma, one side changes between consecutive expansionary stages (`lem-mp-one-side`); negative requirements (`lem-mp-negative`); proof of `thm-minimal-pair`. Exercises: the true path is ∅″-computable (`ex-true-path-double-jump`); a minimal pair of simple sets.
4. **high-incomplete.** Sacks' theorem stated (`thm-high-incomplete`), `cor-high-incomplete-ce`; requirements G_e (coding Inf in columns) and P_i; coding suffices (`lem-hi-coding-suffices`); the finite injury version fails: an explicit c.e. set V and total functional Ψ for which P₀ is initialized infinitely often (`prop-hi-finite-injury`, new); the tree solution by timing; construction; true path (`lem-hi-true-path`); coding requirements (`lem-hi-coding`). Exercise: proof of `lem-hi-true-path` (`ex-hi-true-path`).
5. **high-incomplete-verification** (new). Preservation below an infinitary coding outcome (`lem-hi-preservation`), with the comparison with `prop-hi-finite-injury`; diagonalization (`lem-hi-diagonal`); proof of `thm-high-incomplete`. Further results stated: jump inversion, density, non-diamond, cappable degrees and prompt simplicity, minimal pairs of high degrees. Exercises: the true path is Turing equivalent to ∅″; cappable degrees are closed downward (non-cappable upward).

## 4. Proof techniques

| Technique | Where | Introduced in |
| --- | --- | --- |
| Posner's trick (one index for two oracles) | minimal-pairs | here |
| Length of agreement, expansionary stages | minimal-pairs | `ce-degrees/sacks-splitting` (length of agreement) |
| Preservation of agreement by alternating sides (value transport) | minimal-pairs, used in minimal-pair-verification | here |
| Guessing outcomes; tree of strategies; initialization to the right of the current path | trees-of-strategies | here (Friedberg–Muchnik on a tree as comparison) |
| True path: leftmost path visited infinitely often; induction along it | minimal-pair-verification, high-incomplete | here |
| Case analysis on the position of an acting node (prefix, left, below each outcome, right) | `lem-mp-one-side`, `lem-hi-preservation` | here |
| Coding a Π⁰₂-complete set into columns, read by the relativized limit lemma | high-incomplete | `turing-degrees/low-and-high` |
| Diagonalization with fresh followers (Friedberg–Muchnik) | positive requirements of both constructions | `ce-degrees/friedberg-muchnik` |
| Constructing a counterexample run of a construction (a c.e. set defined together with the construction) | `prop-hi-finite-injury` | here |

## 5. Choices

**Included.**
- *Two theorems, two kinds of infinitary strategy.* In the minimal pair construction the infinitary strategies enumerate nothing and only constrain the timing of the others; in the high incomplete construction they enumerate infinitely many numbers. Together they show the two ways in which infinite injury arises. This is also the choice of Downey–Hirschfeldt §2.14 (minimal pairs, then high c.e. degrees).
- *Preservation lemma as a statement about a sequence of stages* (`lem-pair-module`). It separates the combinatorics of agreement from the tree, and makes the verification of the construction a check of two conditions. Monin–Patey and the informal description of Downey–Hirschfeldt use alternating explicit restraints; the version without restraints is the one of Downey–Hirschfeldt's verification (Lemma 2.14.5), and needs less bookkeeping.
- *Coding Inf directly in the columns of H.* Downey–Hirschfeldt split the proof into a piecewise trivial set and a thick subset avoiding a cone (weak thickness lemma). The direct version needs only one construction and keeps the coding lemma of `turing-degrees/low-and-high` visible.
- *`prop-hi-finite-injury`* (new, 2026-11-12). It replaces the former Exercise 2 of `high-incomplete`, whose solution only illustrated the failure (it assumed properties of the fixed set W₀ and functional Φ₀, and that W₀ grew "at stages far apart"). The proposition makes the statement precise: the finite injury version run with an arbitrary c.e. set V (with a given enumeration) and functional Ψ in place of W₀ and Φ₀, and V defined together with the construction (growing at the stage after each action of P₀), so that no recursion theorem is needed. Justification: a finite injury verification uses no property of the particular W₀ and Φ₀, so it must work for every V and Ψ. It is placed in the main text because it is the counterexample that explains why the hypothesis "act only at α-expansionary stages" is needed.
- *Further results* stated without proof (jump inversion, density, non-diamond, cappable degrees, minimal pairs of high degrees), so that the student knows where the method leads.

**Excluded.**
- *Density, jump inversion in general, thickness lemma.* Each needs its own lesson or more (density is "one of the most complex infinite injury constructions", Monin–Patey); a later revision may add a lesson on the thickness lemma or on jump inversion, which reuse the tree of this course.
- *0‴-arguments* (Lachlan's nonsplitting theorem, Soare XIV): beyond the level of the course.
- *Lachlan games, pinball machines, true stages*: other presentation devices; mentioned in the notes of `trees-of-strategies` (true stages).
- *Prompt simplicity and the cappable degrees*: only stated; the proof that promptly simple sets are non-cappable (Nies §1.7) could become an exercise.

**Order and structure.** Revised 2026-11-12 from three to five lessons, since the former lessons 2 and 3 had about 2900 and 3150 words. The cut points: lesson 1 ends with the preservation lemma; lesson 2 contains the guessing argument (formerly at the end of lesson 1) and the tree; lesson 3 the true path and the verification; lessons 4 and 5 split the high incomplete construction after the coding requirements. No labeled statement was removed; moved statements are listed in the history.

## 6. Comparison with the literature

- **Downey–Hirschfeldt §2.14** (pp. 44–58): 2.14.1 priority trees (Friedberg–Muchnik on a tree), 2.14.2 minimal pairs (Theorem 2.14.1, Lemmas 2.14.4–2.14.5), 2.14.3 high c.e. degrees (via a piecewise trivial set and Theorem 2.14.9, weak thickness lemma, with "believable" computations), 2.14.4 thickness lemma, 2.15 density, 2.16 jump theorems (Sacks jump inversion, Theorem 2.16.4, sketched). The course follows 2.14.1–2.14.2 closely (tree {∞, f}, coherence remark, verification), and differs in 2.14.3 (direct coding, P-strategies instead of thickness).
- **Soare 1987** (not available as text; chapter numbers checked through citations in Nies and Downey–Hirschfeldt): Theorem IX.1.2 minimal pair; Theorem VIII.1.1 thickness lemma; Theorem VIII.3.1 Sacks' jump theorem; VIII.5 pinball machine; XI.2.3 Martin's characterization of high c.e. degrees by maximal sets; XIV.3.1 minimal pair of high c.e. degrees on a tree. Soare 2016 (*Turing Computability*) does not treat infinite injury beyond a historical remark (§16.1).
- **Monin–Patey**, chapter *Priority method and c.e. degrees*, section *Π⁰₂ priority method (infinite injury)*: minimal pairs with explicit alternating restraints and a tree figure; cappable degrees and prompt simplicity stated. Chapter *Turing degrees* proves a high incomplete set by forcing (the course `turing-degrees` follows it) and attributes high incomplete c.e. sets to Sacks' incomplete maximal set.
- **Nies** §1.7 (minimal pairs and promptly simple sets, p. 41) and §6.3 (pseudojump inversion; Corollary 6.3.4, a high incomplete c.e. set from two finite injury arguments; p. 251 notes that a direct proof uses infinite injury).

## 7. Pedagogical plan

- **minimal-pairs.** Intuition: one index per requirement, and agreement need only be protected on one side at a time. Example `ex-expansionary`: the identity functional (finitely many expansionary stages, A ∩ B = ∅) and a constant functional (infinitely many, though uninformative). Remark: Posner's hypothesis A ≠ B is a proof device. Figure *agreement*: the zigzag path carrying Δ(y) between the two sides. Counterexample in Exercise 2: restraining always the same side makes it computable.
- **trees-of-strategies.** Intuition: the outcome is Π⁰₂, so run one version per guess; coherence example (two N-requirements with disjoint expansionary stages). Comparison: Friedberg–Muchnik on a tree, guesses moving only left. Figure *tree*. Exercise on the priority order.
- **minimal-pair-verification.** Example `ex-true-path`: a node to the right of the true path acting infinitely often. Figure *regions*: the five groups of nodes around α and what each can do between consecutive α-expansionary stages. Quizzes: why leftmost, why left means higher priority, why the stage ends, why the true-path node.
- **high-incomplete.** Intuition: coding needs infinitely many enumerations; `prop-hi-finite-injury` shows the conflict with a concrete run (counterexample to the finite injury method); the tree resolves it by timing.
- **high-incomplete-verification.** Figure *column*: column 1 of H at the stage β acts, the restraint R_α, the cut s₀. Case 4 of `lem-hi-preservation` compared with the counterexample.

Possible additions: a figure of the current paths σ_s over a few stages; an exercise putting Friedberg–Muchnik on a tree (Downey–Hirschfeldt §2.14.1).

## 8. Sources

- **minimal-pairs.** Lachlan 1966 (Proc. LMS (3) 16, 537–569), Yates 1966 (JSL 31, 159–168): checked in the bibliography of Downey–Hirschfeldt. Posner's trick: Downey–Hirschfeldt §2.14.2, footnote. Preservation without restraints: Downey–Hirschfeldt, proof of Lemma 2.14.5. Soare 1987, Theorem IX.1.2 (via Nies p. 41). Monin–Patey section *Π⁰₂ priority method*.
- **trees-of-strategies.** Downey–Hirschfeldt §2.14.1 (Friedberg–Muchnik on a tree; true path computable in ∅″). Origin of trees: Lempp–Lerman 1995 (BSL 1, 189–201), who credit Lachlan 1975 (Ann. Math. Logic 9, 307–365), Harrington, and Soare's book, and attribute the 0⁽ⁿ⁾ classification to Harrington; checked in the text of Lempp–Lerman. Montalbán 2014 (JSL 79, 1315–1335) and Day–Greenberg–Harrison-Trainor–Turetsky 2024 (BSL 30, 199–226): checked on arXiv (1306.2623, 2211.07958).
- **minimal-pair-verification.** Downey–Hirschfeldt Lemmas 2.14.4–2.14.5.
- **high-incomplete.** Sacks 1963, *Recursive enumerability and the jump operator*, Trans. AMS 108, 223–239 (checked in Nies' bibliography; Downey–Hirschfeldt attribute the jump inversion theorem to *Degrees of Unsolvability*, 1963). Downey–Hirschfeldt §2.14.3 (high c.e. degrees via the weak thickness lemma, Theorem 2.14.9, attributed to Shoenfield) and §2.16. Soare 1987 VIII.1.1, VIII.3.1 (via Downey–Hirschfeldt p. 58 and Nies p. 161).
- **high-incomplete-verification.** Density: Sacks 1964 (Ann. Math. 80, 300–312), Downey–Hirschfeldt §2.15. Non-diamond: Lachlan 1966 (not checked against a book; standard attribution). Cappable degrees: Ambos-Spies–Jockusch–Shore–Soare 1984 (Trans. AMS 281, 109–128), Nies §1.7, Monin–Patey. Pseudojump inversion: Jockusch–Shore 1983 (Trans. AMS 275, 599–609; Nies dates it 1984, which is part II in JSL), Nies Corollary 6.3.4. Incomplete maximal set: Sacks 1964 (Michigan Math. J. 11, 193–205; Downey–Hirschfeldt p. 83). Maximal sets and high degrees: Martin 1966 (Z. Math. Logik 12, 295–310; Nies p. 28, Soare XI.2.3). Minimal pair of high degrees: Downey–Hirschfeldt end of §2.14.3 (exercise), Nies p. 251.

## 9. Recent literature

- **True stages.** Montalbán, *Priority arguments via true stages* (JSL 2014): ξ-true stages, at which the approximations to the ξ-th jump are correct; a dynamic version of Ash's metatheorem for iterated priority arguments. Day, Greenberg, Harrison-Trainor and Turetsky, *Iterated priority arguments in descriptive set theory* (BSL 2024): the "true stages machinery" applied to Wadge and Louveau-type theorems. I found no textbook presentation of the minimal pair or the high incomplete theorem by true stages; the method targets iterated (Δ⁰_α) arguments. Decision: mentioned in the notes of `trees-of-strategies`; the course keeps trees, which remain the standard presentation for 0″-arguments in Soare, Downey–Hirschfeldt and Monin–Patey.
- **Frameworks.** Lempp–Lerman 1995 and Lerman's *A Framework for Priority Arguments* (Lecture Notes in Logic 34, 2010) give iterated trees for 0⁽ⁿ⁾-arguments; beyond the course.
- **Injury-free routes to high incomplete degrees.** Pseudojump inversion (Jockusch–Shore 1983; Nies 2009 Corollary 6.3.4), and incomplete maximal sets (Sacks 1964 with Martin 1966). Added to the notes of `high-incomplete-verification`; they do not replace the tree construction, whose purpose is the technique.
- The lecture notes "S. Lempp, *Priority arguments in computability theory, model theory, and complexity theory*" formerly cited could not be found (Lempp's home page lists no such notes); replaced by Lempp–Lerman 1995.

## 10. Open points

- Soare 1987 is not available as text; its chapter and theorem numbers are cited only where Nies or Downey–Hirschfeldt cite them. The title of Chapter XIV is not checked.
- The non-diamond theorem (Lachlan 1966) is attributed from standard knowledge, not checked in the available books.
- Possible additions: a lesson on the thickness lemma or Sacks' jump inversion; an exercise putting Friedberg–Muchnik on a tree; a figure of the current paths over a few stages; the proof that promptly simple sets are non-cappable as an exercise (Nies §1.7).
- `high-incomplete` is about 2900 words (duration 55), above the target; a future revision could move the proof of `prop-hi-finite-injury` to a lesson of its own if more material on finite versus infinite injury is added.

## 11. History

- **2026-11-12.** Design and pedagogy revision. Split into five lessons: the guessing argument moved from `minimal-pairs` to `trees-of-strategies` (retitled "Guessing on a tree of strategies"); the true path (`def-true-path`, `ex-true-path` new, `lem-true-path`) and the verification of the minimal pair theorem (`lem-mp-positive`, `lem-mp-one-side`, `lem-mp-negative`, the proof of `thm-minimal-pair`, the exercises `ex-true-path-double-jump` and simple sets) moved to the new lesson `minimal-pair-verification`; `lem-hi-preservation`, `lem-hi-diagonal`, the proof of `thm-high-incomplete`, the further results and the exercise on the true path of the high construction moved to the new lesson `high-incomplete-verification`. New: `ex-expansionary`, `ex-true-path`, `prop-hi-finite-injury` (settles the open point of `docs/REVIEW-2026-11.md` on the former Exercise 2 of `high-incomplete`), `ex-hi-true-path`, an exercise on the priority order, an exercise on cappable degrees, a quiz question on the true-path node, three figures (*agreement*, *regions*, *column*) in `scripts/figures/infinite-injury.py`. References checked and corrected: Soare chapter ranges narrowed to verified theorem numbers; Lempp's lecture notes replaced by Lempp–Lerman 1995; the claim that Soare obtains the result by two finite injury arguments replaced by the pseudojump inversion route (Jockusch–Shore, Nies 6.3.4); Posner's trick and the restraint-free formulation attributed to Downey–Hirschfeldt; Monin–Patey section named.
