# Design log: Immunity and growth of functions

## 1. Objectives

After the course, a student can:

- define immune, hyperimmune, simple, hypersimple, effectively immune and effectively simple sets, and give examples separating them;
- translate between hyperimmunity of a set and growth of its principal function, and between hyperimmune degree and computable domination;
- define truth-table reducibility, prove its characterization by total functionals, and use it to recognize computably dominated sets;
- build computably dominated sets by forcing with computable function trees;
- move between DNC, fixed-point free and effectively immune degrees, and use the amplified form of DNC (avoiding c.e. sets of bounded size);
- prove Arslanov's completeness criterion and its corollaries;
- prove Martin's domination theorem, Jockusch's list theorem, the highness of maximal sets, and the high-or-DNC theorem.

**Role in the track.** Last course of the computability track (since 2026-11-12, see
`content/tracks-design.md`). It teaches the "domination and escape" technique of the
track, and provides the notions of computational weakness (computably dominated) and
strength (hyperimmune, DNC, high) used without comment in the randomness, reverse
mathematics and degree-structure courses. The Martin-Löf randomness course uses
`def-dnc`, `thm-dnc-effectively-immune`, `thm-arslanov` and computable domination; the
minimal degree lesson uses the f-tree lemmas; Schnorr/Kurtz randomness uses hyperimmune
degrees.

## 2. Prerequisites assumed

- Fundamentals: SMN with parameters, the fixed point theorem and its parametrized form, padding, canonical indices $D_n$, c.e. sets, many-one reducibility.
- Turing degrees: oracle computations and use (`prop-oracle-stages`), the limit lemma, the computation function of a $\Delta^0_2$ approximation (`thm-computation-function`), low and high sets.
- Arithmetic hierarchy: Post's theorem relativized, $\mathrm{Tot}$ is $\Pi^0_2$-complete.
- C.e. degrees: simple sets and Post's simple set, a low simple set.
- Π⁰₁ classes: weak König's lemma, the computably dominated basis theorem and the definition of computably dominated sets, PA degrees and $\mathrm{DNC}_2$, the low basis theorem for PA sets.

## 3. Results, lesson by lesson

1. **immune-sets.** Immune sets; immune sets in every non-zero degree (prefix sets); disjoint strong arrays and hyperimmune sets; Kuznecov–Medvedev–Uspenskii: hyperimmune iff principal function hyperimmune; hyperimmune degree equals degree of a hyperimmune set. Examples: prefix set immune but not hyperimmune; Post's simple set not hypersimple.
2. **hypersimple-sets.** Dekker's deficiency sets: hypersimple sets in every non-zero c.e. degree; truth-table reducibility; Nerode's characterization by total functionals; Post's theorem (hypersimple sets are not tt-complete, admitted) and the resulting separation of $\leq_{tt}$ and $\leq_T$ on c.e. sets.
3. **computably-dominated.** F-trees; Miller–Martin: a non-computable computably dominated set computable in $\emptyset''$; Jockusch–Martin: computably dominated iff $\leq_T$ coincides with $\leq_{tt}$ below the set. Exercise: continuum many.
4. **dnc-functions.** DNC iff fixed-point free (Jockusch–Lerman–Soare–Solovay); DNC iff avoiding c.e. sets of bounded size iff effectively immune; Post's simple set is effectively simple; bounded DNC functions (remarks, admitted results).
5. **arslanov.** Arslanov's criterion; corollaries (PA c.e. sets, Martin's effectively simple theorem, low simple sets not effectively simple); Kučera's theorem (admitted).
6. **domination.** Martin's domination theorem; Jockusch's list theorem (now proved in full).
7. **high-or-dnc.** Maximal sets are high (Martin); Kjos-Hanssen–Merkle–Stephan: high or DNC iff computes a function almost everywhere different from all computable functions.

## 4. Proof techniques

- **Coding by prefixes** (immune sets in every degree): lesson 1.
- **Partition into intervals defined by iterating a computable bound** (strong arrays): lesson 1, reused for maximal sets (lesson 7) and in the exercises.
- **True (non-deficient) stages** of an enumeration: lesson 2; announced as a tool of infinite injury.
- **Compactness** (weak König's lemma) to bound computations on all oracles: lesson 2 (total functionals), lesson 3 (f-tree Case 2, by finiteness of a level).
- **Forcing with computable perfect trees** (Spector; Miller–Martin): lesson 3, with the partial/total dichotomy. Compared with the Π⁰₁-class proof of the basis theorem.
- **Diagonalization against truth-table reductions with a hyperimmune clock**: lesson 3 and exercise 2 of lesson 1.
- **SMN self-reference and the fixed point theorem as a trap**: lessons 4 and 5.
- **Settling of c.e. approximations recognized by the oracle**: lesson 5.
- **Limit approximations of Tot, and Σ⁰₂(A) definitions of Tot via a dominant function**: lesson 6.
- **Partial computable functions with no computable completion** (the DNC₂ diagonal): lesson 6, (⇐) of Jockusch's theorem.
- **Escape arguments** (a non-dominant function is beaten by a computable one infinitely often): lessons 6 and 7.

## 5. Choices

- **Split into seven lessons (2026-11-12).** The four lessons were 2400–2700 words each, at
  the upper limit; with intuitions, examples and figures they would have exceeded 3000. The
  splits follow the mathematics:
  - Dekker's theorem goes with truth-table reducibility (`hypersimple-sets`): both come from
    Post's program, and Post's theorem on hypersimple sets is the natural place to separate
    $\leq_{tt}$ from $\leq_T$.
  - Arslanov's criterion gets its own lesson (`arslanov`): it is a distinct technique
    (fixed points plus c.e. approximation) and the most cited result of the course.
  - Applications of Martin's theorem (`high-or-dnc`: maximal sets, Kjos-Hanssen–Merkle–Stephan)
    are separated from the theorem and Jockusch's list theorem (`domination`).
  - Labels were moved, never renamed or deleted. No version of the course was released, so
    no permanent URL changes.
- **Jockusch's list theorem is now proved** (previously admitted). The (⇒) direction
  follows Soare 2016, Theorem 4.8.2 (rows that are either a total program or finite); the
  (⇐) direction is a cleaned-up version of Monin–Patey's argument, with the DNC₂ diagonal.
  Note: Monin–Patey's proof of (2 ⇒ 3) lists the sets $Y_e(n) = \Phi_e(n)[g(n)]$ and their
  finite modifications and claims they are exactly the computable sets; this is not correct
  for partial $\Phi_e$ (the course's old text already noticed this). Soare's trick of
  freezing a row at 0 after the first failure fixes it.
- **Theorem name.** `thm-martin-miller-ftrees` is now displayed as "Miller–Martin", the
  author order of the 1968 paper and of Downey–Hirschfeldt.
- **Admitted results** (with references): Post's theorem that hypersimple sets are not
  tt-complete (Friedberg–Rogers for wtt); existence of maximal sets (Friedberg); Yates's
  complete maximal set and Martin's characterization of degrees of maximal sets; Jockusch's
  DNC_k theorem; Ambos-Spies–Kjos-Hanssen–Lempp–Slaman; Kučera's theorem on Δ⁰₂ DNC
  functions; high 1-generic sets (proved in the specialized Cohen genericity course).
- **Excluded.** Hyperhypersimple sets beyond a remark (they belong to the lattice of c.e.
  sets); the full theory of $\mathrm{DNC}_h$ and bushy tree forcing (research level,
  pointers given); traceability (belongs to the randomness track, with lowness notions);
  Kučera's priority-free solution of Post's problem (needs randomness or a longer
  construction; mentioned).
- **Order.** Sets (immunity) before degrees (growth); weakness (computably dominated)
  before strength (DNC, high); Arslanov before Martin, because the high-or-DNC theorem uses
  the amplified DNC property and Martin's theorem.

## 6. Comparison with the literature

- **Monin–Patey, chapter *Immunity and function growth*.** Same material and order except
  that the course treats hyperimmunity before DNC (MP: immune, DNC, Arslanov, hyperimmune,
  computably dominated, Martin, high or DNC). Putting hyperimmunity first lets the course
  pass from sets to degrees once, and puts the f-tree construction next to the Π⁰₁ basis
  theorem it parallels. The course adds Dekker's theorem and Post's tt-results, which MP
  does not treat, and treats maximal sets in the text rather than as an exercise.
- **Soare 2016.** Martin's theorem §4.5.2 (Theorem 4.5.6), Jockusch's lists §4.8.2
  (Theorem 4.8.2), arrays and hyperimmune sets §5.3 (Theorem 5.3.3 KMU, Theorem 5.3.6
  Dekker), Martin and Arslanov §5.4 (Theorems 5.4.1, 5.4.3), hyperimmune-free degrees §5.6
  (Theorem 5.6.4, tt characterization), Yates's maximal set §5.7. Soare does not build
  hyperimmune-free degrees by f-trees in Chapter 5.
- **Downey–Hirschfeldt.** §2.17 (Miller–Martin 2.17.3, continuum many 2.17.4,
  Jockusch–Martin 2.17.7), §2.22 (JLSS 2.22.1, Arslanov 2.22.3, Kučera 2.22.5), §8.16
  (Kjos-Hanssen–Merkle–Stephan, autocomplexity).
- **Nies.** §1.5 (hyperimmune sets and degrees), §4.1 (DNC functions, Proposition 4.1.4,
  completeness criterion Theorem 4.1.11, Martin Proposition 4.1.13, exercises 4.1.15 on
  Friedberg–Rogers and 4.3.5 on DNC_k).

## 7. Pedagogical plan

- **immune-sets.** Intuition: listing versus pointing to blocks. Examples: Post's set
  (immune complement); prefix set (immune, not hyperimmune); Post's set not hypersimple.
  Counterexamples for the hypotheses of the definition of arrays (disjointness; canonical
  versus c.e. indices). Figure: the interval array of the proof of the KMU theorem.
- **hypersimple-sets.** Intuition: deficient stages record late small elements. Figure:
  enumeration plotted with non-deficient stages. Examples of tt-reductions (m-reductions,
  complement of ∅′, deficiency sets). Compactness named for total functionals.
- **computably-dominated.** Intuition: why finite extensions fail (Δ⁰₂), why trees help.
  Example: interleaving f-tree. Figure: an f-tree inside the binary tree. Technique:
  forcing with perfect trees; parallel with the Π⁰₁ basis theorem.
- **dnc-functions.** Intuition: self-referential programs; amplification of DNC; a map of
  the proof of the main theorem. Example: Post's set effectively simple. Remarks on bounded
  DNC.
- **arslanov.** Intuition before the proof, with a stage figure. Necessity of the c.e.
  hypothesis (low PA sets), where it is used. Post's set complete.
- **domination.** Figure contrasting hyperimmune and dominant growth. Intuition for both
  directions of Martin's theorem and for Jockusch's theorem; quiz on each new proof.
- **high-or-dnc.** Intuition for maximal sets (complement cannot be split) and for the
  diagonal step of KMS. Quiz on the counting threshold $2n$. Exercises: maximal sets are
  hypersimple; computably dominated case.

Possible further figures: the intervals $I_n$ of the maximal-set proof; the Case 2 search
of the f-tree lemma.

## 8. Sources (checked against the books, 2026-11-12)

- Lesson 1: Post 1944; Soare 2016 Definition 5.3.1, Theorem 5.3.3 (KMU), §5.6; Miller–Martin 1968; DH §2.17; MP sections *Immune sets*, *Hyperimmune functions*.
- Lesson 2: Dekker 1954 (Soare Theorem 5.3.6, which also gives $D \leq_{tt} A$); Post 1944; Friedberg–Rogers 1959 (Nies Exercise 4.1.15; Soare §5.7); Soare Theorem 3.8.5 (Nerode) for total functionals; Yates complete maximal set (Soare §5.7).
- Lesson 3: Spector 1956; Miller–Martin 1968 (DH Theorems 2.17.3, 2.17.4); Jockusch 1969 and Martin unpublished (DH Proposition 2.17.7; Soare Theorem 5.6.4); MP section *Computably dominated degrees*.
- Lesson 4: JLSS 1989 (DH Theorem 2.22.1; Nies 4.1.4; Soare Exercise 5.4.5 attributes it to Jockusch); Martin 1966a (Nies 4.1.13); MP section *DNC functions*; Jockusch 1989 (Nies Exercise 4.3.5); Ambos-Spies–Kjos-Hanssen–Lempp–Slaman, JSL 69 (2004) 1089–1104.
- Lesson 5: Arslanov 1981, title as in DH's bibliography (Soviet Math. 25, 1–10); Soare Theorem 5.4.3; DH Theorem 2.22.3; Nies Theorem 4.1.11; Kučera 1986, LNCS 233, 493–500 (DH Theorem 2.22.5).
- Lesson 6: Martin 1966b (Soare Theorem 4.5.6); Jockusch 1972 (Soare Theorem 4.8.2); MP section *Martin's domination theorem*; Soare Theorem 4.6.1 (low₂).
- Lesson 7: Friedberg 1958; Martin 1966b; Kjos-Hanssen–Merkle–Stephan, Trans. AMS 363 (2011) 5465–5480, **Theorem 5.1** (checked in the arXiv version, arXiv:0901.3933, Section 5 "Characterizing high or DNR degrees"); MP section *High or DNC degrees*.

## 9. Recent literature

Checked (web search, 2026-11-12):

- Kjos-Hanssen, Merkle, Stephan (2011): confirmed that the high-or-DNC theorem is Theorem 5.1
  of the Transactions paper, with further equivalent conditions in terms of plain
  complexity. No change to the proof, which matches theirs and Monin–Patey's.
- Khan and Miller, *Forcing with bushy trees*, Bulletin of Symbolic Logic 23 (2017): bushy
  tree forcing is now the standard technique for building DNC functions with weak
  computational power (e.g. slow-growing DNC functions computing no Kurtz random). Not
  added: research level; a natural topic for the planned specialized course on effective
  forcing.
- Kumabe and Lewis, *A fixed-point-free minimal degree*, Journal of the London Mathematical
  Society 80 (2009), 785–797: a DNC degree can be minimal. Not added; candidate for the
  degree-structure course.
- No simpler proof of Arslanov's criterion or of Martin's theorem was found; the textbook
  proofs are already short.

## 10. Open points

- The Martin-Löf randomness lesson `randomness-and-degrees` cites `thm-arslanov`, now in
  the lesson `arslanov`; its lesson prerequisites list only `immunity-growth/dnc-functions`.
  Add `immunity-growth/arslanov`.
- `fundamentals/_design.md` says Arslanov's criterion is in `immunity-growth/dnc-functions`;
  it is now in `immunity-growth/arslanov`.
- `high-or-dnc` cites `cor-high-not-dnc` from the specialized course `cohen-genericity`, as
  an example only; the text says so.
- Post's theorem that hypersimple sets are not tt-complete is admitted. A proof (about one
  page) could be added to `hypersimple-sets` if the lesson has room.
- `computably-dominated` is about 2900 words (50 minutes), above the target; a further split
  (f-trees / truth-table characterization) is possible but would leave two short lessons.

## 11. History

- **2026-11-12.** Design and pedagogy revision (this log created).
  - Split from four to seven lessons: new `hypersimple-sets` (Dekker, truth-table
    reducibility, Post's theorem), `arslanov`, `high-or-dnc` (maximal sets, KMS). Labels
    moved without renaming.
  - Jockusch's list theorem proved in full (previously admitted).
  - New examples: prefix sets (immune, not hyperimmune), Post's simple set (not
    hypersimple; effectively simple, hence complete), interleaving f-trees, tt-reductions.
  - New figures (generator `scripts/figures/immunity-growth.py`): interval array, deficiency
    stages, f-tree, hyperimmune versus dominant growth, stages in Arslanov's proof.
  - New exercises: subsets of hyperimmune sets; deficiency sets are tt-reducible; tt is
    transitive; effectively immune sets below c.e. sets; Δ⁰₂ non-DNC sets; fixed points
    below incomplete c.e. sets; maximal sets are hypersimple; computably dominated case of
    KMS. New quizzes on Jockusch's theorem and maximal sets.
  - References rechecked against Soare 2016, Downey–Hirschfeldt, Nies, Monin–Patey;
    Soare 1987 references replaced by checked Soare 2016 sections; Arslanov's title
    corrected; "Miller–Martin" order; attribution of the effective-immunity
    characterization to Jockusch removed (not checkable); Nerode credited for total
    functionals (per Soare).
