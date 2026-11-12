# Design log: Reducibilities between problems

## 1. Objectives

After the course, a student can:

- formulate a Π¹₂ theorem as a problem, and see that the problem fixes a presentation of
  instances (`RT¹_{<∞}` versus `RT¹_k`, `KL` versus bounded `KL`);
- prove ω-reductions with Turing ideals, and separations by preservation of a weakness
  property (iterating and dovetailing);
- use the Hirschfeldt–Jockusch game, and count applications of a problem;
- distinguish ω-reducibility, computable and strong computable reducibility, and
  Weihrauch and strong Weihrauch reducibility, and place each relative to provability
  over RCA₀;
- prove that one application of WKL is as good as many (Scott's theorem), and use cylinders;
- prove Weihrauch non-reductions by continuity, and by transfer through parallelization.

**Role in the track.** Last course of the reverse mathematics track (since 2026-11-12, see
`content/tracks-design.md`). The track's earlier courses measure strength by provability
over RCA₀ and by ω-models; this course gives the finer, computational measures that
Dzhafarov–Mummert treat as basic, and the "uniform (Weihrauch) reductions" technique listed
for the track. It also links to computable analysis (planned specialized course), through
LPO, LLPO and Weihrauch's book.

## 2. Prerequisites assumed

- Turing ideals, jump ideals, Scott ideals and their characterization by PA degrees
  (big-five/aca0, big-five/wkl0: `prop-wkl-scott`, `thm-low-scott`, `thm-konig-aca`,
  `thm-aca-equivalents`).
- Π⁰₁ classes: low, computably dominated and cone avoidance basis theorems, PA degrees and
  DNC₂ (`thm-pa-characterization`), leftmost paths, finitely branching trees
  (`thm-konig-strength`, `thm-finitely-branching-jump`).
- Ramsey's theorem: Jockusch's bounds, cohesiveness, Seetapun's theorem and the
  Dzhafarov–Jockusch theorem (ramsey-theorem).
- Hirst's theorem `RT¹_{<∞}` ↔ BΣ⁰₂ and the non-provability of BΣ⁰₂ in RCA₀
  (induction-conservation/pigeonhole), used only for the comparison with provability.
- Absoluteness of arithmetic formulas for ω-models (`prop-omega-absolute`); the IVT in RCA₀.

## 3. Results, lesson by lesson

1. **omega-reducibility** — problems; satisfaction by Turing ideals; `≤ω`;
   `RT¹_{<∞} ≤ω Id` although RCA₀ does not prove it; `KL ≡ω J`, `WKL ≤ω J`
   (`prop-kl-j`); Hirschfeldt–Jockusch game theorem (`thm-game-omega`).
2. **preservation** (new, split from lesson 1) — weakness properties, preservation
   (`def-weakness`), `lem-preservation-ideal`, `thm-preservation-separation`,
   `J, KL ≰ω WKL`, `J ≰ω RT²₂` (`cor-wkl-not-j`); cone avoidance; Monin–Patey separation of
   COH and RT²₂ from SRT²₂ (admitted).
3. **computable-reducibility** — `≤c`, `≤sc`, problems admitting computable solutions;
   `prop-c-omega`; counting rounds; `KL ≤²ω J` but `KL ≰c J` (`prop-kl-not-c-j`); bounded
   KL is `≤c J`; `≤c` and provability over RCA₀ are incomparable (both directions).
4. **wkl-reductions** (new, split from lesson 3) — Scott's theorem (`thm-scott-pa`);
   `P ≤ω WKL ⇔ P ≤c WKL` (`thm-wkl-omega-c`); universal instances; cylinders
   (`def-cylinder`, `prop-cylinder`, `prop-wkl-cylinder`); `Id ≰sc RT¹₂`.
5. **weihrauch** — `≤W`, `≤sW`, uniformly admitting computable solutions; diagram of
   implications; `RT¹₂` admits computable solutions but not uniformly
   (`prop-rt12-not-uniform`); `RT¹_{k+1} ≰W RT¹_k` (admitted); LPO, LLPO; `LLPO ≤W LPO`,
   LLPO not uniformly solvable (`prop-llpo-lpo`); exercises `LLPO ≤sW LPO`, `KL_b ≤W J`,
   a direct continuity proof of `LPO ≰W LLPO`.
6. **parallelization** (new, split from lesson 5) — parallelization; `J ≡W LPO^`
   (`thm-jump-lpo`); `WKL ≡W LLPO^` (`thm-wkl-llpo`); `LLPO <W LPO` (`cor-lpo-not-llpo`);
   exercises: closure operator, `J ≤W RT¹₂^`, finitely many applications of LPO,
   `KL ≤W J⁽²⁾`.

## 4. Proof techniques

- **Building Turing ideals as unions of chains** (Lessons 1–2, 4): iterating and
  dovetailing (`lem-preservation-ideal`), the dovetailed strategy in `thm-game-omega`, the
  tower of PA sets in `thm-scott-pa`.
- **Preservation of a weakness property** (Lesson 2): the standard separation method; named
  and referred to in later lessons.
- **Coding a whole construction into one Π⁰₁ class** (Lesson 4, Scott's theorem): one PA set
  makes all choices of the tower at once.
- **Counting resources of a single application** (Lesson 3, `prop-kl-not-c-j`; Lesson 6,
  finitely many LPO).
- **Coding the instance into the solutions** (Lesson 4, cylinders), and its obstruction by
  strong cone avoidance (Dzhafarov–Jockusch).
- **Continuity arguments** (Lesson 5): use principle, finite information; a direct proof of
  `LPO ≰W LLPO` as an exercise.
- **Transfer through parallelization** (Lesson 6): a Turing-degree separation becomes a
  separation of problems with numerical solutions.
- **Uniformizing a classical proof** (Lesson 6, `WKL ≤W LLPO^`): isolate the non-uniform
  choice and hand it to a problem.

## 5. Choices

- **Split into six lessons.** The three lessons were 2100–2550 words before the revision;
  intuition, examples and figures pushed two of them to 3200–3700. Each was split at a
  natural seam: ω-reducibility / preservation, computable reducibility / reductions to WKL,
  Weihrauch reducibility / parallelization. All labels are kept, only moved; no lesson of
  another course cited them.
- **Order ω → c → W.** From the coarsest to the finest, as in Hirschfeldt–Jockusch; the
  reader already knows ω-models from the Big Five course. Dzhafarov–Mummert go the other way
  (identity, computable, Weihrauch, then ω-models); our order lets each lesson explain what
  the previous reducibility cannot see.
- **Terminology.** "Computably true" (previous version: every instance computes a solution)
  replaced by Dzhafarov–Mummert's "admits computable solutions" and "uniformly admits
  computable solutions"; D–M reserve "computably true" for REC ⊨ P. Hirschfeldt's
  "uniform reducibility" is mentioned as a synonym of Weihrauch reducibility.
- **Comparison with provability** added (D–M §5.11): `KL` versus `J`, and `RT¹_{<∞}`, in
  both directions. It uses the induction-conservation course, now a prerequisite.
- **Bounded KL.** `KL_b` (instances with a bound) is introduced as an exercise to explain
  why `KL ≰c J`, and because Dzhafarov–Mummert's Proposition 4.2.9 is incorrect (see 6).
- **Included as statements only:** cone avoidance for countably many cones (DGHPT 2022),
  Monin–Patey 2021, `RT¹_{k+1} ≰W RT¹_k`, Jockusch–Stephan. Their proofs need Mathias forcing
  arguments beyond the scope of the course.
- **Excluded:** the algebraic structure of the Weihrauch lattice (meets, joins, compositional
  product beyond a mention, jumps of problems), represented spaces, `C_N`, `lim`, the
  Weihrauch classification of analysis theorems (BGP survey Sections 6–8). They belong to
  the planned computable analysis course. Generalized Weihrauch reducibility of
  Hirschfeldt–Jockusch and the reductions of Dzhafarov–Mummert §4.5 beyond a remark are left
  out to keep the course short.

## 6. Comparison with the literature

- **Dzhafarov–Mummert, Chapters 3–4 and §5.11.** Same notions; our definition of problem
  requires non-empty solution sets. D–M Proposition 4.2.9 states `KL ≡c TJ`; its proof
  computes `Ext(T)` from `T′` via Proposition 2.8.5, which assumes a computably bounded tree.
  For unbounded finitely branching trees the claim is false (`prop-kl-not-c-j`, from
  `thm-konig-strength`). The lesson says so in its notes. No erratum was found online
  (search 2026-11-12).
- **Hirschfeldt–Jockusch (2016)** is the source of the game and of `thm-wkl-omega-c`.
- **Hirschfeldt, *Slicing the Truth*, §2.2** defines computable, strong and uniform
  reducibility; §4.5 ω-models.
- **Brattka–Gherardi–Pauly survey.** History of Weihrauch reducibility (Bibliographic
  remarks of Section 3: introduced by Weihrauch in the late 1980s, two technical reports of
  1992), `LLPO <W LPO` (Prop. 7.17, Weihrauch 1992, Thm 4.2), `WKL ≡sW LLPO^`
  (Thm 7.23, Brattka–Gherardi 2011, Thm 8.2), `LPO^ ≡sW lim ≡sW J` (Thm 6.7). The survey works
  with represented spaces and partial multi-valued functions; we keep the reverse-mathematics
  formulation with sets.
- **Weihrauch, *Computable Analysis* (2000).** Representations and computable real
  functions; Weihrauch reducibility proper is not developed there (Section 8.2, "Degrees of
  discontinuity", is the closest). Not cited in the lessons for that reason.

## 7. Pedagogical plan

1. Intuition: a Turing ideal as the resources of a mathematician; why KL needs two jumps
   (bound, then extendibility). Examples: REC satisfies RT¹₂, not WKL; RT¹_{<∞} ≤ω Id.
   Figure: a play of G(J → KL). Quiz on the game.
2. Intuition: the obstacle (later instances) and the remedy (dovetailing). Counterexample:
   preservation needs `Z ⊕ Y`, not `Y` (Sacks splitting). Exercise with computably
   dominated sets. The Monin–Patey example shows that choosing `W` is the creative step.
3. Figure: square diagrams of `≤c`, `≤sc`. Examples: WKL ≤sc KL, Id ≤c Q. Bounded KL.
   Incomparability with provability.
4. Intuition for Scott's theorem (a tower is one member of one Π⁰₁ class). Figure: the tower.
   Universal instances. Cylinders, and why RT¹₂ is not one.
5. Figures: Weihrauch diagrams; implications between the reducibilities; the two colorings of
   the continuity argument. Examples: WKL ≤sW KL, Id ≤W RT¹₂ but not ≤sW, J × J ≤W J.
   LLPO explained as choosing a true one of two Π⁰₁ statements, with examples.
6. Intuition: parallel versus sequential use; each LLPO instance decides one branching.
   Figure: the death stage and the instance q_σ. Examples: Id^, J^, RT¹₂^. Quiz on why
   computable reductions do not parallelize.

Possible additions: a figure for the preservation chain (judged redundant with the game
figure), and the Weihrauch degrees of `RT¹_k` with a proof.

## 8. Sources (checked 2026-11-12)

- Lesson 1: Hirschfeldt–Jockusch 2016; D–M §3.1, §4.6 (Def. 4.6.4), §4.7 (Thm 4.7.5);
  Hirschfeldt §2.2, §4.5. KL/J: `thm-konig-strength` (pi01-classes), D–M Prop. 3.6.10.
- Lesson 2: D–M Def. 3.6.11, Thm 4.6.13, Cor. 4.6.14–4.6.15; Jockusch–Soare 1972 (cone
  avoidance basis); Seetapun–Slaman 1995; DGHPT 2022; Jockusch–Stephan 1993; Monin–Patey
  2021 (abstract checked on arXiv 1905.08427).
- Lesson 3: Dzhafarov 2015; D–M §4.2, §4.4, §4.5, §5.11 (Figure 5.1); D–M Prop. 2.8.5 and
  4.2.9 (error); Hirschfeldt §2.2.
- Lesson 4: Scott 1962; Hirschfeldt–Jockusch 2016; D–M Ex. 4.8.1, Prop. 4.5.5;
  Brattka–Gherardi 2011 (cylinders, per BGP Section 3 remarks); Dzhafarov–Jockusch 2009.
- Lesson 5: Weihrauch 1992 (Informatik Berichte 130); BGP survey Prop. 7.17;
  Gherardi–Marcone 2009; DDHMS 2016; Brattka–Rakotoniaina 2017; D–M §3.7
  (Prop. 3.7.4, IVT), §4.3 (Prop. 4.3.7 with all three attributions), §4.4, Figure 4.6.
- Lesson 6: Brattka–Gherardi 2011 (Thm 8.2); BGP Thm 6.7; Brattka–Gherardi–Marcone 2012;
  D–M Def. 3.1.5, Ex. 3.9.4 (`RT¹₂^` codes the jump), §4.5 (compositional product).

## 9. Recent literature

- Checked: Monin–Patey, *SRT²₂ does not imply RT²₂ in ω-models* (Adv. Math. 389, 2021):
  answers a question of Chong–Slaman–Yang by a preservation argument (jumps not of PA
  degree over ∅′). Added to Lesson 2 as the example of a well-chosen weakness property.
- DGHPT 2022 (cone avoidance for countably many cones): already cited, kept.
- BGP survey (2021) used for history and attributions; it resolves the open point of
  `docs/REVIEW-2026-11.md` on "in the 1980s": the lessons now say "late 1980s, two technical
  reports of 1992".
- Searched for an erratum to D–M Prop. 4.2.9: none found.
- Not added: the extensive Weihrauch classification of RT^n_k (Brattka–Rakotoniaina 2017,
  cited), and later work on the first-order part and the jumps of problems; they would need
  the lattice structure excluded above.

## 10. Open points

- Report D–M Proposition 4.2.9 to the authors or check a newer printing.
- Exact attribution of LPO and LLPO in constructive mathematics (Bishop) is not given in
  the lessons; add it if checked.
- The course prerequisite `induction-conservation` was added; the coordinator should check
  the track graph.
- A proof of `RT¹_{k+1} ≰W RT¹_k` could be an exercise (D–M Exercise 4.8.4).

## 11. History

- **2026-11-12.** Design and pedagogy revision. Split into six lessons (new: `preservation`,
  `wkl-reductions`, `parallelization`); labels kept and moved within the course. Terminology
  aligned with Dzhafarov–Mummert ("admits computable solutions"). Added: intuition paragraphs,
  examples after definitions, comparison with provability (`RT¹_{<∞}`, KL), bounded KL and the
  correction of D–M Prop. 4.2.9, universal instances, a direct continuity proof of
  `LPO ≰W LLPO`, Monin–Patey example, parallelization examples and exercises, seven figures
  (`scripts/figures/reducibilities.py`). History of Weihrauch reducibility corrected ("late
  1980s, reports of 1992"); attribution of `RT¹_{k+1} ≰W RT¹_k` completed with DDHMS; section
  numbers of D–M, Slicing and BGP checked.
