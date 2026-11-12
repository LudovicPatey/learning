# Design log: K-trivial sets

This file is the memory of the course (see "Designing tracks and courses" in
`AGENTS.md`). It is not rendered.

## 1. Objectives

After the course, a student can:

- state the definition of K-triviality, explain why it compares K(A↾n) with K(n) and not
  with a fixed bound, and give examples and non-examples (computable sets, Ω, sparse
  codings of random sets);
- prove Chaitin's counting theorem and derive that there are fewer than 2^{b+c} sets that
  are K-trivial with constant b, all Δ⁰₂; prove the closure under join;
- prove the closure under weak truth-table reductions and the weak truth-table
  incompleteness of K-trivial sets; use a Solovay function as a computable substitute
  for K(n);
- define the standard cost function, prove that obeying it implies K-triviality, and
  build a simple K-trivial set (and one below a given non-computable c.e. set);
- define lowness for K, lowness for Martin-Löf randomness and bases for randomness,
  prove the easy implications, and prove the hungry sets theorem;
- run the amplification argument with the fixed point theorem, and explain how the
  decanter and golden run methods extend it to Turing reductions and lowness;
- derive from the main theorem (admitted) the equivalence of the four notions and the
  ideal structure of the K-trivial sets.

**Role.** Specialized course (not in a track): `tracks-design.md` keeps K-triviality out
of the randomness track because lowness is a research topic built on the core. It builds
on `martin-lof-randomness` (Levin–Schnorr, Kučera–Gács, Sacks), `kolmogorov-complexity`
(KC theorem, coding theorem, Ω) and `ce-degrees` (simple sets, Post's construction). It is
cited by `ce-degrees/cone-avoidance` (`thm-solovay-ktrivial`, as a solution to Post's
problem without injury).

## 2. Prerequisites assumed

- **Kolmogorov complexity:** prefix-free machines and `prop-k-basic` (pairing, the bound
  |σ| + 2 log |σ|, Kraft inequality for K); `prop-k-segments-computable`; the KC theorem
  `thm-kc`; the coding theorem `thm-coding`; Ω and `thm-omega`; Chaitin's theorem on
  C-trivial sets `thm-chaitin-computable` (for comparison).
- **Martin-Löf randomness:** Levin–Schnorr (relativized), `thm-sacks`, `thm-kucera-gacs`.
- **Π⁰₁ classes:** `prop-isolated-computable` (relativized to ∅′).
- **Computability:** computable approximations `def-delta2-approximation`, uses
  `def-use`, many-one reductions and m-completeness of ∅′ (`def-many-one`,
  `thm-halting-complete`), the SMN and fixed point theorems (`cor-smn-parameters`,
  `thm-fixed-point`), simple sets and Post's construction (`def-simple`,
  `thm-post-simple`), permitting (used in an exercise, explained there).
- Van Lambalgen's theorem is mentioned once, in a solution, as a remark.

## 3. Results, lesson by lesson

1. **K-trivial sets** (`k-trivial-sets`): `def-k-trivial`, `ex-k-trivial` (new: computable
   sets, Ω, {2^i : i ∈ X}), `prop-k-trivial-basic`, the counting theorem
   `thm-k-trivial-count`, `cor-k-trivial-delta2` (finitely many sets per constant, Δ⁰₂),
   `prop-k-trivial-join`. Exercises: a computable set of lengths suffices; lower bound
   2^{b − 2 log b − O(1)} on the number of sets with constant b (new).
2. **Weak truth-table reductions and Solovay functions** (`solovay-functions`, new on
   2026-11-12): `prop-k-trivial-wtt` (new), `cor-k-trivial-wtt-incomplete` (new, via
   Ω ≤wtt ∅′), `def-solovay-function`, `prop-solovay-function`, `prop-solovay-ktrivial`
   (moved from lesson 1), the c.e. tree remark and c.e. covers (admitted). Exercises:
   no K-trivial set is random, A ⊕ Z and {2^i : i ∈ Z} are not K-trivial (moved from
   lesson 1); Solovay functions via Σ 2^{−g} (new).
3. **Cost functions and a c.e. K-trivial set** (`cost-functions`, retitled):
   `def-cost-ck`, `ex-cost-ck` (new), `thm-obey-ktrivial`, `thm-solovay-ktrivial`.
   Exercises: a K-trivial set neither c.e. nor co-c.e.; speed-up of approximations;
   permitting below a non-computable c.e. set (new).
4. **Lowness for randomness** (`lowness`): relativized K and MLR, `def-lowness-randomness`,
   `ex-lowness` (new: ∅′ has none of the properties), `prop-lowness-implications`.
   Exercise: low for K implies low.
5. **The hungry sets theorem** (`hungry-sets`, new on 2026-11-12, split from `lowness`):
   `thm-hungry-sets`, `cor-lowness-equivalent` (moved). Exercises: a base for randomness
   is not complete; a set computed by Z₀ and by Z₁ ∈ MLR^{Z₀} is low for K (new).
6. **K-triviality and lowness** (`ktrivial-lowness`, new on 2026-11-12):
   `thm-wtt-amplification` (new, full proof), the decanter and golden run methods
   (informal), `thm-ktrivial-lowk` (moved, admitted), `cor-ktrivial-equivalent` (moved),
   further results (superlowness, cost function characterization, c.e. covers, the
   covering theorem) and the alternative route to the main theorem. Exercises: Turing
   incompleteness; K-triviality relative to a K-trivial set.

## 4. Proof techniques

- **Counting descriptions / coding theorem as a compactness principle** (lesson 1):
  bounded width of T_b gives finitely many paths, hence Δ⁰₂; reused in the join (a
  description by an index among few candidates).
- **Isolated paths of a tree computable in an oracle** (lesson 1, from Π⁰₁ classes);
  isolated paths of a c.e. tree via Solovay functions (lesson 2).
- **Recovering the length from the string** (lessons 1–2): the standard trick for
  initial segment complexity, used for wtt reductions and Solovay functions.
- **KC theorem with accounting** (lessons 3 and 5): the weight of requests is charged to
  the descriptions of U (lesson 3), to the cost of changes (lesson 3), or to the measure
  of disjoint open sets (hungry sets, lesson 5; Nies's "accounting method").
- **Cost functions, "do what is cheap"** (lesson 3): Post's construction with a cost
  restriction, requirement-free in the sense that requirements do not interact; with
  permitting in an exercise.
- **A construction for each parameter, a randomness hypothesis selects the good one**
  (lesson 5).
- **Amplification with the fixed point theorem** (lesson 6): force the opponent to pay
  many times for one payment of ours; the fixed point theorem gives the construction a
  reduction of the set it builds; running all constants in parallel.
- **Decanter and golden run** (lesson 6): described, not proved.

## 5. Choices

- **Six lessons instead of three (2026-11-12).** With the intuitions, examples and figures
  required by the revision, the three lessons would have reached 3200–3700 words. The
  split follows the themes: definition and counting (1); the robustness of the definition
  (2); cost functions (3); lowness notions (4); the hungry sets theorem, the main
  technique of the lowness part, as its own lesson (5); the main theorem and its
  technique (6). Moved labels (all inside the course; no external citer): to
  `solovay-functions`: `def-solovay-function`, `prop-solovay-function`,
  `prop-solovay-ktrivial`; to `hungry-sets`: `thm-hungry-sets`, `cor-lowness-equivalent`;
  to `ktrivial-lowness`: `thm-ktrivial-lowk`, `cor-ktrivial-equivalent`. The only external
  citation of the course, `thm-solovay-ktrivial` (from `ce-degrees/cone-avoidance`, as a
  forward pointer), stays in `cost-functions`.
- **Amplification proved in full.** The course had no proof using the characteristic
  technique of K-triviality beyond cost functions and hungry sets. The weak truth-table
  case of incompleteness is the one case where the amplification argument gives a
  complete and short proof (one page), and it is the first step of the decanter method
  (Downey–Hirschfeldt 11.3.1). The proof given here avoids the recursion theorem for the
  coding constant by running strategies S_j for all j in parallel, with budget 2^{−j} and
  threshold 2j; the fixed point theorem is used once, to give the construction a
  reduction of the c.e. set it builds. The easier proof through Ω ≤wtt ∅′ is kept in
  lesson 2, so that the two proofs can be compared.
- **Decanter and golden run described, not proved.** A complete proof of Turing
  incompleteness (decanter) or of lowness (golden run, Nies Section 5.4, 15 pages) would
  need a lesson of its own and a careful formalization of nested procedures with
  garbage quotas. The description is precise about what is built (k-sets, goals and
  quotas, the properties of a golden run as in Nies, Lemma 5.4.9) and gives references.
  A full lesson on the decanter method is an open option (section 10).
- **Main theorem admitted.** As before, with precise references (Nies 5.4.1; DH 11.4.1,
  11.4.9) and the alternative route of Bienvenu, Day, Greenberg, Kučera, Miller, Nies and
  Turetsky, now spelled out step by step.
- **Solovay functions kept** for their use as a computable substitute for K and for the c.e.
  tree remark; the elementary proof of the Turing c.e. cover (BDMN 2015, Corollary 4.13)
  is not given, since it needs a Solovay function that is an order and the K-triviality
  of c.e. trees; it is stated with its reference.
- **Permitting exercise** added to lesson 3 to show that cost function constructions
  combine with the classical methods of the c.e. degrees.
- **Excluded:** the function G(b) counting K-trivial sets (Downey–Miller–Yu) beyond the
  lower bound exercise; C-triviality (in `kolmogorov-complexity`); the Σ⁰₃ index set and
  listing of K-trivial sets; ML-cupping and covering beyond a statement; lowness for weak
  2-randomness; LR-reducibility; strongly jump-traceable sets; K-trivial sets in
  computable metric spaces. These are research topics; the course stops at the
  equivalence theorem and its immediate consequences.

## 6. Comparison with the literature

- **Nies, *Computability and Randomness*, Chapter 5.** Nies starts from the lowness notions
  (5.1, with the hungry sets theorem 5.1.22 and Kučera's promptly simple base 5.1.19),
  then K-triviality (5.2), cost functions (5.3), the golden run (5.4) and consequences
  (5.5). The course starts from K-triviality, as Downey–Hirschfeldt do, because its
  definition only needs the Kolmogorov course and the counting theorem gives the first
  results; the lowness notions come after the construction, when they are needed to
  state the main theorem. Nies's direct construction of a K-trivial set via the
  promptly simple base is not used; the cost function construction is.
- **Downey–Hirschfeldt, Chapter 11.** Same order as the course for 11.1 (K-triviality,
  basic construction, Solovay functions), 11.2 (lowness, Muchnik's low for K set, not
  included), 11.3 (decanter: wtt case 11.3.2, Turing incompleteness 11.3.1), 11.4 (golden
  run), 11.5 (cost functions), 11.7 (hungry sets, with the conclusion "K-trivial").
  Downey–Hirschfeldt prove the wtt case with a single constant known by the recursion
  theorem; the course runs all constants in parallel instead.
- **Bienvenu–Shen (2015), tutorial.** Presents Solovay's construction, Turing
  incompleteness and the main theorem as games between two players who increase weights.
  The course uses the "opponent" language in the intuition of lesson 6, and refers to the
  tutorial for a readable full proof.

## 7. Pedagogical plan

1. `k-trivial-sets`: why compare with K(n) (oscillation of K); examples and non-examples
   (`ex-k-trivial`); intuition of the counting theorem (descriptions of σ are descriptions
   of |σ|); figure of a tree of bounded width with two paths and a dead branch
   (`bounded-width-tree`); the counting argument as a compactness principle; intuition
   of the join (pay for n once).
2. `solovay-functions`: robustness of the definition as the theme; why n must be
   recovered from the length (quiz); why 2 log n is not a Solovay function; Solovay's
   idea of encoding a description and its stage; quiz on the tight arguments.
3. `cost-functions`: waste of descriptions as the intuition; figure of the cost of a
   change (`standard-cost`); the limit condition; examples (computable sets, finite sets,
   Ω); the accounting in two parts; Post's construction with a cost restriction.
4. `lowness`: lowness as invariance of a relativized notion; ∅′ as the counterexample to
   all three properties (`ex-lowness`); quizzes on the implications.
5. `hungry-sets`: the difficulty (A unknown, many candidate oracle prefixes) and the
   solution (requests pay for themselves in measure) before the proof; figure of hungry
   sets and of V_d (`hungry-sets`); three quizzes.
6. `ktrivial-lowness`: amplification explained as a game with an opponent; figure of the
   forced versions (`amplification`); quizzes on where wtt is used and on the number of
   followers; the failure for Turing reductions, the drip-feed strategy, nested
   procedures (decanters), certified computations (golden run).

## 8. Sources

Checked against the text versions of the books on 2026-11-12.

- `k-trivial-sets`: Nies 2.2.26 (counting theorem), 5.2.1, 5.2.4, 5.2.17; DH 3.7.6
  (counting theorem, Chaitin 1975), 11.1.1 (Chaitin [IBM J. 1977]), 11.1.3 (Zambella
  1990), 11.1.4, 11.1.10–11.1.11 (Downey–Miller–Yu). Papers: Chaitin 1975 (JACM 22),
  1976 (TCS 2), 1977 (IBM J. Res. Dev. 21); Zambella 1990; DHNS 2003.
- `solovay-functions`: Nies 5.2.18; DH 3.12.1, 3.12.3, 11.1.8, 11.1.9. Papers:
  Friedberg–Rogers 1959; Solovay 1975; Bienvenu–Downey 2009; Bienvenu–Downey–Nies–Merkle
  2015 (Corollary 4.13 read in the arXiv version 1603.08351).
- `cost-functions`: Nies 5.3.1–5.3.4, 5.3.10, 5.3.11, 5.5.2; DH 11.1.5 (attributed
  "Zambella, after Solovay"), 11.5.1, 11.5.3; DH 11.1.1 for the variations (below any
  non-zero c.e. degree). Papers: Solovay 1975; Zambella 1990; Kučera–Terwijn 1999; DHNS
  2003; Nies 2005.
- `lowness`: Nies 5.1.1, 5.1.2, 5.1.7, 5.1.8, 5.1.18, 5.2.3; DH 11.2.1, 11.2.3, 11.7.1.
  Papers: Zambella 1990; Kučera 1993; Kučera–Terwijn 1999.
- `hungry-sets`: Nies 5.1.21, 5.1.22 (attributed to Hirschfeldt–Nies–Stephan 2007); DH
  11.7.2, 11.7.3. Papers: Nies 2005; HNS 2007.
- `ktrivial-lowness`: DH 11.3.1, 11.3.2 (wtt case), 11.4.1, 11.4.9, 11.5.3, 11.6.1; Nies
  5.4.1, 5.4.9 (golden run), 5.5.2–5.5.6. Papers: DHNS 2003; Nies 2005; HNS 2007;
  Miller–Nies 2006 (Problem 4.6); BDGKMNT 2014; BGKNT 2016; Day–Miller (arXiv 1304.2789);
  Bienvenu–Shen 2015; BDMN 2015.

## 9. Recent literature

Checked on 2026-11-12 (web search and the arXiv versions of the papers):

- **Bienvenu, Day, Greenberg, Kučera, Miller, Nies, Turetsky, BSL 20 (2014)** and
  **Bienvenu, Greenberg, Kučera, Nies, Turetsky, JEMS 18 (2016), 773–812**, with **Day and
  Miller** (arXiv 1304.2789): the ML-covering problem (Miller–Nies 2006, Problem 4.6;
  Nies, Open question 5.1.24 for c.e. sets) is solved positively. The course states the
  result and the alternative route to the main theorem; the previous text said that this
  route "uses hungry sets and the c.e. trees", now spelled out: Turing c.e. cover (BDMN),
  covering, Hirschfeldt–Nies–Stephan (Z random relative to C), hungry sets.
- **Bienvenu, Downey, Nies, Merkle, JCSS 81 (2015), 1575–1591**: journal version of the
  Solovay function papers; elementary proof that every K-trivial set is Turing below a
  c.e. K-trivial set (Corollary 4.13). Used as a reference; replaced the STACS 2011
  reference.
- **Bienvenu and Shen, LNCS 9300 (2015)**: game presentation of the decanter and golden run
  arguments. Cited as a readable source for the admitted theorem.
- No simpler proof of the main theorem that avoids all priority-like combinatorics was
  found; the BDGKMNT route moves the difficulty to the covering theorem.

## 10. Open points

- **Chaitin's papers.** DH cite the Δ⁰₂ result as Chaitin, *Nonrecursive infinite strings
  with simple initial segments*, IBM J. Res. Dev. 21 (1977), 350–359, 496; the paper with
  these pages is titled *Algorithmic information theory* (confirmed by bibliographic
  records). Nies attributes the result, and the finiteness of the classes [T_b], to
  Chaitin (1976, TCS 2). The course cites both papers and names the 1977 paper by its
  published title; the exact location of the Δ⁰₂ proof was not checked against the
  papers themselves (REVIEW-2026-11 item).
- **Day–Miller.** Only the arXiv version (2013) was checked; the journal reference
  (Mathematical Research Letters, 2015, as remembered) should be confirmed before it is
  cited.
- **A lesson on the decanter method** with a complete proof of Turing incompleteness
  could be added, following DH 11.3 or the game version of Bienvenu–Shen. It would teach
  the core technique of the area; it needs a careful formalization (about 3000 words).
- Durations of `cost-functions` and `ktrivial-lowness` are 50 minutes, slightly above
  the 45-minute guideline; both contain complete constructions that are hard to split.

## 11. History

- **2026-11-12.** Design and pedagogy revision. The course grows from three to six
  lessons: `solovay-functions` (wtt closure and incompleteness, Solovay functions moved
  from lesson 1), `hungry-sets` (split from `lowness`), `ktrivial-lowness` (the main
  theorem moved from `lowness`, with a new full proof of the amplification argument in
  the wtt case and a description of the decanter and golden run methods). New statements:
  `ex-k-trivial`, `prop-k-trivial-wtt`, `cor-k-trivial-wtt-incomplete`, `ex-cost-ck`,
  `ex-lowness`, `thm-wtt-amplification`. Four figures (generator
  `scripts/figures/k-trivials.py`). New exercises: lower bound on the number of K-trivial
  sets, Solovay functions via Σ 2^{−g}, permitting, common lower bounds of relatively
  random sets, K-triviality relative to a K-trivial set. References checked against Nies
  and Downey–Hirschfeldt: attribution of the counting theorem to Chaitin 1975, of the
  bound on the number of sets to Zambella (DH), of the first c.e. construction to
  Zambella after Solovay (DH 11.1.5), of the cost function form to DHNS 2003; the title of
  Chaitin's 1977 paper corrected; the STACS 2011 reference replaced by BDMN 2015; the
  alternative route to the main theorem made precise.
