# Design log: Fundamentals of computability

This file is the memory of the course (see "Designing tracks and courses" in `AGENTS.md`). Read it
before revising the course, and record every decision in the history.

## 1. Objectives

After the course, a student can:

- use the enumeration $\Phi_e$, its conventions (arity, partiality, $\simeq$) and its approximation by
  stages $\Phi_e(x)[s]$ without hesitation;
- apply the universal function and the parameter form of the SMN theorem, i.e. write "let $s(x)$ be
  an index of the program which, on input $y$, …" and know why $s$ is total;
- prove undecidability by diagonalization and by many-one reductions built with SMN;
- move between the descriptions of c.e. sets (domains, ranges, $\Sigma^0_1$ projections, c.e.
  approximations), and use dovetailing;
- build self-referential programs with Kleene's fixed point theorem;
- decide whether an index set is computable (Rice) or c.e. (Rice–Shapiro).

**Role in the track.** Third course of the computability track (`content/tracks-design.md`), after
*Countability and diagonalization* and *Models of computation*. It provides the common language
of every later course: $\Phi_e$, $W_e$, $W_e[s]$, $\emptyset'$, $\leq_m$, c.e. sets, SMN in parameter
form, and the fixed point theorem. The track design log assigns to it two of the track's techniques:
diagonalization (shared with the countability course) and the fixed point theorem. The course also
introduces approximation by stages and dovetailing, used without comment afterwards.

## 2. Prerequisites assumed

- From *Models of computation*: Turing machines and their input/output conventions
  (`def-tm-computes`), the translation lemma (`lem-tm-translation`), coding of finite sequences
  (`prop-seq-operations`), primitive recursion and bounded quantifiers, minimization, the
  equivalence of models (`thm-equivalence-models`), Kleene's normal form
  (`thm-kleene-normal-form-proof`) and the universal function (`cor-universal-function`); the
  Church–Turing thesis as a writing convention; Cantor pairing $\langle x, y \rangle$ and its inverses.
- From *Countability*: the diagonal argument (`thm-cantor-diagonal`), its general form and
  Lawvere's fixed point theorem (`cor-lawvere`, `prop-diagonal-partial`), effective
  diagonalization (`thm-effective-diagonal`), the halting set as a diagonal object
  (`cor-halting-diagonal`), principal functions of infinite sets (`lem-subsets-of-n`).

## 3. Results, lesson by lesson

1. **Programs as numbers.** Notation $\Phi^{(k)}_e$, $\simeq$; stages (`def-stage`) and their three
   properties (`prop-stage-properties`); computable sets and relations, closure
   (`prop-computable-closure`); uniformity.
2. **The universal function and the SMN theorem.** `thm-universal`; `thm-smn` with a complete proof
   for Turing machines; parameter form (`cor-smn-parameters`); standard uses (`ex-smn-uses`);
   padding (`lem-padding`, `cor-infinitely-many-indices`); acceptable numberings
   (`def-acceptable`, `prop-acceptable`); Rogers' isomorphism theorem and Friedberg's numbering
   (admitted, with references).
3. **The halting problem.** `thm-halting`; many-one reductions (`def-many-one`, `prop-many-one`);
   $\emptyset' \equiv_m H$, reductions to $\{e : \Phi_e(0)\converge\}$, to non-emptiness, and of
   both $\emptyset'$ and its complement to $\mathrm{Tot}$ (`prop-halting-variants`); undecidable
   problems of mathematics (admitted).
4. **Computably enumerable sets.** `def-ce`, `def-ce-approx`; five characterizations
   (`thm-ce-characterizations`); injective enumerations (`prop-ce-range`); Post's complementation
   theorem (`prop-computable-iff-ce-coce`); $\emptyset'$ c.e., its complement not
   (`thm-halting-ce`).
5. **Closure properties and complete sets.** Closure (`prop-ce-closure`); selection
   (`prop-selection`) and graph theorem (`prop-graph`); downward closure under $\leq_m$
   (`prop-ce-downward`); m-completeness of $\emptyset'$ (`thm-halting-complete`); $\mathrm{Tot}$
   neither c.e. nor co-c.e. (`cor-tot-not-ce`).
6. **Kleene's fixed point theorem.** `thm-fixed-point`; Kleene's form (`cor-self-reference`);
   parameters (`thm-fixed-point-parameters`); infinitely many fixed points
   (`prop-infinitely-many-fixed-points`); halting set and $\{e : \Phi_e = \Phi_a\}$ by fixed points
   (`prop-halting-via-fixed-point`); minimal indices (exercise, Blum).
7. **Rice's theorem.** Index sets (`def-index-set`); `thm-rice`; the index set theorem
   (`prop-rice-reduction`) and examples.
8. **The Rice–Shapiro theorem.** Monotonicity and finiteness (`thm-rice-shapiro`); the
   characterization by c.e. lists of finite functions (`thm-rice-shapiro-converse`, proved since
   2026-11-12); examples (`cor-rice-shapiro-examples`); the version for classes of c.e. sets
   (exercise `ex-rice-shapiro-sets`).

## 4. Proof techniques

| Technique | Introduced / used |
| --- | --- |
| Approximation by stages (bounded simulation) | introduced in lesson 1 (`prop-stage-properties`, figure); used in the reductions of lesson 3, the enumerations of lessons 4–5, Rice–Shapiro (lesson 8) |
| Programs as data; SMN in parameter form | lesson 2; every reduction afterwards |
| Padding | lesson 2; index sets (lesson 7), injective reductions (exercise) |
| Diagonalization (effective) | countability course; lesson 3 (halting set, figure); lesson 6 (fixed point as a failed diagonal argument, Owings' figure) |
| Many-one reductions built by SMN | lesson 3; lessons 5, 7, 8 |
| Dovetailing | named in lesson 1, introduced in lesson 4 (figure); lesson 5 (closure, selection) |
| Self-reference by the fixed point theorem | lesson 6; Rice's theorem (lesson 7) |
| Finite information / continuity | Rice–Shapiro (lesson 8); announced for the use principle and computable analysis |

## 5. Choices

- **Order: halting problem before c.e. sets.** Undecidability is the motivation; c.e. sets are
  introduced as "sets whose membership can be confirmed", with $\emptyset'$ as first example.
  Soare does the same (1.6 before 2.1). Monin–Patey introduce c.e. sets first; we keep ours.
- **Fixed point theorem after c.e. sets, Rice after the fixed point theorem.** Rice is proved twice:
  by fixed points (illustrating the technique) and by reduction (giving the index set theorem).
- **SMN with a complete Turing-machine proof.** Kept: it is the one place where "the index is
  computed without running the program" is made concrete. The figure shows the machine $P_x$.
- **Acceptable numberings included, isomorphism theorem admitted.** The isomorphism theorem is a
  back-and-forth argument of little use later; the definition explains why the results do not depend
  on the model.
- **Split of the c.e. sets lesson (2026-11-12).** The former lesson `ce-sets` had 3200 words (about
  60 minutes). It is split into `ce-sets` (characterizations, complementation theorem) and
  `complete-sets` (closure, selection, m-completeness). All labels are kept; those of the second part
  moved to the new lesson.
- **Split of the Rice lesson and proof of the converse (2026-11-12).** The converse of Rice–Shapiro
  was admitted with a vague reference to Rogers and Odifreddi. Given the necessity part, the converse
  takes a paragraph (the set of codes of finite members of the class is $k^{-1}(P)$), so it is now
  proved. The lesson became too long and was split into `rice-theorem` and `rice-shapiro`.
- **Excluded:**
  - creative and productive sets, Myhill's isomorphism theorem, simple sets — in `ce-degrees`
    (`simple-sets`), where they serve Post's problem;
  - computably inseparable sets — an exercise of the countability course;
  - one-one reducibility beyond the definition — not needed later;
  - the recursion theorem with partial $f$ (Soare 2.2.7) — mentioned in a quiz only;
  - the Myhill–Shepherdson and Kreisel–Lacombe–Shoenfield theorems — cited, not proved; they belong
    to a course on effective operations or computable analysis;
  - Arslanov's completeness criterion — in `immunity-growth/dnc-functions`.

## 6. Comparison with the literature

- **Soare, *Turing Computability* (2016).** §1.5 (numbering, padding Lemma 1.5.2, enumeration
  Theorem 1.5.3, s-m-n Theorem 1.5.5), §1.6 (halting set, $\leq_m$ Def. 1.6.8, $K \leq_1 \mathrm{Tot}$
  Thm 1.6.11, index set Theorem 1.6.13, Rice Corollary 1.6.14, stages §1.6.4), §1.7 (Myhill
  isomorphism, acceptable numberings Thm 1.7.6), §2.1 (normal form 2.1.3, uniformization 2.1.8,
  graph 2.1.9, listing 2.1.10, union 2.1.11, reduction principle 2.1.12, complementation 2.1.14),
  §2.2 (recursion theorem 2.2.1, Owings' matrix §2.2.4, parameters 2.2.6, minimal indices Ex.
  2.2.9, Rice by fixed points Ex. 2.2.10). Differences: Soare states s-m-n with $s$ injective and
  works with $\leq_1$; we use $\leq_m$ throughout and a primitive recursive $S^m_n$. Soare does not
  prove Rice–Shapiro; we do. Soare's stage convention also bounds the output by $s$.
- **Monin–Patey, chapter *Foundations of computability*.** Same material in a more informal style
  (universal program, SMN, padding, fixed point theorem with a JavaScript quine, c.e. sets, halting
  problem); Rice's theorem is in the chapter *Arithmetic hierarchy*. Our course adds proofs at the
  level of Turing machines (SMN), reductions, m-completeness and Rice–Shapiro.
- **Downey–Hirschfeldt, Chapter 2.1–2.4.** A compressed summary (halting problem, Rice's theorem
  2.2.3, recursion theorem with Owings' explanation, reductions); used only for comparison.

## 7. Pedagogical plan

- **Lesson 1.** Program/datum duality; indices of the nowhere defined function (`ex-indices`);
  figure of the approximation of $W_e$ by stages (staircase $x < s$, columns that never converge);
  counterexample showing the computability of the conditions in definition by cases is needed;
  uniformity counterexample.
- **Lesson 2.** Interpreter intuition for the universal function; "SMN edits code, never runs it";
  figure of the tape of $P_x ; M_e$; quiz on $S^1_1$ of a non-halting program; example of an
  acceptable numbering (`ex-acceptable`) and Friedberg's as a non-example.
- **Lesson 3.** Diagonal table figure with $\downarrow/\uparrow$ entries; technique named; figure of a
  many-one reduction; example $A \equiv_m 2A$ for $A \neq \nat$, with $2\nat \not\leq_m \nat$ as the
  counterexample (`ex-many-one`).
- **Lesson 4.** Examples of c.e. sets (`ex-ce-sets`, including Diophantine sets); why c.e.
  approximations must be increasing (decreasing approximation of $\nat \setminus \emptyset'$,
  forward reference to the limit lemma); dovetailing figure.
- **Lesson 5.** Intuition paragraph before the m-completeness proof; example: no computable set is
  m-complete (`ex-m-complete`); Venn figure of computable / c.e. / co-c.e.
- **Lesson 6.** "The idea of the proof" paragraph (a program cannot contain its own index
  literally); Owings' matrix figure; paradox remark; quine example.
- **Lesson 7.** Why both hypotheses of Rice are needed; examples of the index set theorem
  (`ex-rice-reductions`).
- **Lesson 8.** Heuristic of finite observation; proof of the characterization; practical use of
  the two conditions.
- **Possible additions.** A figure for the Rice–Shapiro reduction (the program $h(e)$ switching
  from $f$ to $g$) if students find part 1 hard.

## 8. Sources (checked 2026-11-12)

- L1: Kleene 1936 (Math. Ann. 112), 1938 (JSL 3); Soare 2016 §1.5, §1.6.4; Monin–Patey, chapter
  *Foundations*, sections *Computable functions*, *Computable sets*.
- L2: Turing 1936; Kleene 1938 (SMN); Rogers 1958 (JSL 23, 331–341); Friedberg 1958 (JSL 23,
  309–316; checked in Soare's bibliography); Soare §§1.5, 1.7.
- L3: Turing 1936; Church 1936; Kalmár, Compositio Math. 4 (1937), 137–144 (checked on Numdam;
  the issue is dated 1936, the volume 1937); Post 1944 (checked in Soare's bibliography); Novikov
  1955, Boone 1959, Matiyasevich 1970, Davis 1973; Soare §1.6.
- L4: Post 1944; Soare §§1.6.1, 2.1 (theorem numbers checked); Monin–Patey section *Computably
  enumerable sets*.
- L5: Post 1944; Soare §2.1 (Theorems 2.1.8–2.1.12), §2.4.
- L6: Kleene 1938; Rogers 1967; Owings, Notre Dame J. Formal Logic 14 (1973), 95–99 (checked in
  Soare's bibliography); Blum, Information and Control 11 (1967), 257–265 (checked: the paper is
  cited in the literature for the immunity of the sets of minimal programs); Moschovakis 2010;
  Terwijn 2024 (arXiv:2402.03069); Soare §2.2.
- L7: Rice 1953 (Trans. AMS 74, 358–366; Soare's bibliography abbreviates the title); Soare
  Theorem 1.6.13, Corollary 1.6.14, Exercise 2.2.10; Monin–Patey section *Rice's theorem*.
- L8: Rice 1956 (JSL 21, 304–308), Shapiro 1956 (Trans. AMS 82, 281–299), Myhill–Shepherdson
  1955.

## 9. Recent literature

Checked (web search, November 2026): new proofs or presentations of the recursion theorem and of
Rice's theorem in the last fifteen years. Found:

- S. A. Terwijn, *Fixed point theorems in computability theory*, arXiv:2402.03069 (2024): a survey
  of fixed point theorems in computability theory, partial combinatory algebras and numberings.
  Added as a reference in lesson 6.
- G. A. Kavvos, *Kleene's two kinds of recursion*, arXiv:1602.06220 (2016), and
  arXiv:1712.09302 (2017) on intensional recursion: perspectives from programming language
  semantics (first and second recursion theorems, Lawvere-style fixed points); not used, as they
  are outside the scope of the course.
- Moschovakis (2010) remains the reference survey of applications.

No simpler proof of the fixed point theorem was found; Owings' "diagonal argument that fails"
(1973), already presented by Soare, was adopted as the figure of lesson 6.

## 10. Open points

- Rogers' book is cited without chapter numbers (no copy available to check).
- Attribution of the SMN theorem to Kleene 1938 and of Theorem `thm-fixed-point` in its
  index-transformation form to Rogers' book: standard, not checked against the originals.
- The prerequisites of `turing-degrees/oracle-computation` and `kolmogorov-complexity/plain-complexity`
  name `fundamentals/ce-sets`; the labels `thm-halting-complete`, `prop-ce-downward` and
  `prop-ce-closure`, used in the turing-degrees and arithmetic-hierarchy courses, are now in
  `fundamentals/complete-sets`. Lesson prerequisites there should be updated (outside this course).
- `arithmetic-hierarchy/index-sets` names `fundamentals/rice-theorem`; it does not cite the
  Rice–Shapiro labels, but `fundamentals/rice-shapiro` would be the natural prerequisite if it
  relies on the c.e. index sets.

## 11. History

- **2026-11-12 — design and pedagogy revision.** Design log written. Seven figures added, generated
  by `scripts/figures/fundamentals.py` (stages, SMN tape, halting diagonal, many-one reduction,
  dovetailing, c.e./co-c.e. classes, Owings' matrix). Lesson `ce-sets` split into `ce-sets` and
  `complete-sets`; lesson `rice-theorem` split into `rice-theorem` and `rice-shapiro`. The converse
  of the Rice–Shapiro theorem is now proved (`thm-rice-shapiro-converse`), with an exercise for
  classes of c.e. sets. New examples: `ex-indices`, `ex-acceptable`, `ex-many-one`, `ex-ce-sets`,
  `ex-m-complete`, `ex-rice-reductions`; intuition paragraphs for the fixed point theorem,
  m-completeness and Rice–Shapiro; counterexamples for the hypotheses of definition by cases,
  of c.e. approximations, of $\leq_m$ and of Rice's theorem. References checked against Soare 2016
  and Monin–Patey and made precise (section and theorem numbers); Kalmár 1937, Owings 1973 and
  Terwijn 2024 added; the unverifiable attribution of the selection theorem to Kleene removed.
  Durations recomputed from word counts.
