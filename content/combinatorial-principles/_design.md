# Design log: Combinatorial principles below Ramsey's theorem for pairs

This file is the memory of the course (see "Designing tracks and courses" in
`AGENTS.md`). It is not rendered.

## 1. Objectives

After the course, a student can:

- state $\mathsf{CAC}$, $\mathsf{ADS}$, their stable and cohesive parts, $\mathsf{EM}$,
  $\mathsf{DNR}$ and $\mathsf{WWKL}$ in second-order arithmetic, and place each of them
  with respect to $\mathsf{RT}^2_2$, $\mathsf{WKL}_0$ and the Big Five;
- prove the implications of the course: $\mathsf{RT}^2_2 \to \mathsf{CAC} \to \mathsf{ADS}
  \to \mathsf{COH}$, the decompositions $\mathsf{ADS} = \mathsf{SADS} + \mathsf{CADS}$,
  $\mathsf{CAC} = \mathsf{SCAC} + \mathsf{ADS}$, $\mathsf{RT}^2_2 = \mathsf{EM} +
  \mathsf{ADS}$, Kreuzer's $\mathsf{EM} \to \mathsf B\Sigma^0_2$, and $\mathsf{WKL}_0 \to
  \mathsf{WWKL}_0 \to \mathsf{DNR}$;
- separate principles with ω-models built by computability: a computable order without
  computable solutions (finite injury), an ω-model of $\mathsf{WWKL}_0$ inside the degrees
  of a low random sequence, an ω-model of $\mathsf{ADS}$ without DNC functions (forcing
  and preservation);
- read the map of the zoo, and know where the separations that the course admits are
  proved.

**Role in the track.** Core course of the reverse mathematics track, added on 2026-11-18
(`content/tracks-design.md`), after `reducibilities` (its last lesson uses preservation of
weakness properties) and before `transfinite-recursion`.
The track had only Ramsey's theorem for pairs as a principle below $\mathsf{ACA}_0$
outside the Big Five; Hirschfeldt (*Slicing the Truth*, Chapter 9) and
Dzhafarov–Mummert (Chapter 9) give a whole chapter to the other principles, which are the
daily material of research in the area. The secondary track "Lowness and avoidance"
(courses `lowness`, `compactness-avoidance`, `separation-design`) proves the hard
separations; this course gives the implications, the easy separations, and the map, so
that the secondary track has a core course to refer to.

## 2. Prerequisites assumed

- **ramsey-theorem:** $\mathsf{RT}^n_k$ (`def-rt`), stable colorings and $\mathsf D^2_2$
  (`def-stable-coloring`, `prop-srt-d22`), cohesiveness (`def-cohesive`,
  `prop-coh-no-low`), the decomposition (`thm-rt22-decomposition`), Jockusch's bounds
  (`thm-jockusch-upper`, `thm-jockusch-no-delta2`), Seetapun (`cor-rt22-not-aca`),
  `cor-wkl-not-rt22`.
- **induction-conservation:** Hirst's theorem (`thm-hirst`), for Kreuzer's theorem.
- **ce-degrees:** the Friedberg–Muchnik theorem as the model of a finite injury argument.
- **second-order-arithmetic:** $\mathsf{RCA}_0$, bounded $\Sigma^0_1$ comprehension, Turing
  ideals (`thm-rca-turing-ideal`).
- **big-five:** Scott ideals (`prop-wkl-scott`), a Scott ideal of computably dominated sets
  (`ex-dominated-scott`).
- **immunity-growth:** DNC functions (`def-dnc`), computably dominated sets.
- **randomness:** universal tests and `cor-mlr-structure`, Kučera's translation lemma
  (`lem-kucera-translate`), Stephan's theorem (`thm-stephan`), randomness of columns
  (`ex-vl-columns`, van Lambalgen), `cor-random-dnc`, Sacks's theorem (`thm-sacks`).
- **reducibilities:** weakness properties and preservation (`def-weakness`,
  `lem-preservation-ideal`, `thm-preservation-separation`, `ex-preserve-two-problems`).
- Admitted from other courses: $\mathsf{COH}$ admits DNC avoidance
  (`compactness-avoidance/dnc-avoidance`, `thm-mathias-coh-preservation`), Liu's theorem
  (`cor-rt22-not-wwkl`), the coloring all of whose solutions compute DNC functions
  (`cor-rt22-dnc`), the separation of $\mathsf{EM}$ from $\mathsf{SRT}^2_2$
  (`cor-sd-em-not-srt22`), the low basis for $\mathsf{SADS}$
  (`lowness/stable-linear-orders`).

## 3. Results, lesson by lesson

1. **orders** — `def-orders-rca` (ascending and descending sequences as sets, as in
   Dzhafarov–Mummert), `def-cac-ads`, `ex-orders-solutions`, `prop-rt22-cac-ads`, stable
   linear orders and `prop-stable-order-solutions`. Featured: `ex-linear-extension` (used
   in lesson 3). Further: sets versus sequences, ADS as RT²₂ for transitive colorings,
   Erdős–Szekeres, examples of stable orders.
2. **computable-orders** — `thm-tennenbaum-denisov` (type ω + ω*), `cor-rca-not-ads`; the
   remark on Herrmann's order and the absence of low solutions. Featured:
   `ex-omega-order-computable`. Further: `ex-stable-order-immune`.
3. **stable-cohesive** — `thm-ads-coh` (lexicographic order of the columns),
   `def-sads-cads`, `prop-ads-decomposition`, small/large/isolated elements, `def-scac`,
   `prop-cac-decomposition`, a table of separations. Featured: `ex-sads-hyperimmune`
   (Csima–Mileti: SADS does not follow from WKL₀). Further: weakly stable orders
   (`ex-weakly-stable`), $\mathsf{CCAC} \to \mathsf{ADS}$ (`ex-ccac-ads`), examples of CADS.
4. **erdos-moser** — `def-tournament`, figure of a tournament, `thm-rt22-em-ads` (RT²₂ =
   EM + ADS; EM + SADS → SRT²₂), `thm-em-bsigma2` (Kreuzer), `prop-em-not-computable`,
   survey of separations. Featured: finite Erdős–Moser (`ex-finite-em`). Further:
   transitivity of tournaments and colorings, RT²₂ = EM + SADS + COH, upper bounds for EM.
5. **dnr-wwkl** — `def-dnr`, `def-wwkl`, `ex-wwkl-instances`, `thm-wwkl-dnr` (Giusto–
   Simpson), `thm-wwkl-random` (ω-models of WWKL₀ and randomness), `cor-wwkl-not-wkl`
   (Yu–Simpson). Featured: `ex-wwkl-dnr-models`. Further: threshold in WWKL, the low model,
   cone avoidance for WWKL, WKL₀ proves DNR.
6. **ads-dnr** — `thm-sads-preserves-dnc` (forcing with ascending sequences),
   `cor-ads-not-dnr`, the map of the course (figure `zoo`) and the table of
   non-implications. Further: SCAC preserves non-DNC degrees, the low random model, reading
   the map.
7. **disjunction-compactness** (added 2026-11-18) — `lem-preservation-reduction`
   (preservation passes down computable reductions), preservation of $k$ hyperimmunities
   as a measure of disjunction: `prop-srt-two-hyperimmunities` (proof from a
   bi-hyperimmune Δ⁰₂ set), `prop-sads-two-hyperimmunities` (Patey; proof through a
   transitive set given by EM), EM and WKL preserve countably many; constant-bound
   immunity as a measure of compactness: `fact-dnc-cb-immune` (Patey), CAC preserves it
   (Patey), hence ADS, SADS, SCAC, COH; the table of the course with both columns.
   Featured: `ex-read-two-columns`. Further: $\mathsf D^2_k$ and $k$ hyperimmunities,
   c.b.-immunity between immunity and hyperimmunity, COH ≤_c ADS.

## 4. Proof techniques

- **Finite injury with a moving cut** (lesson 2): the order is fixed, the cut moves;
  requirements protect elements; extra requirements $\mathcal P_z$ for the order type.
  Explicitly compared with Friedberg–Muchnik.
- **Coding by comparison with the order of ℕ** (lessons 1, 3): the partial order "same
  direction as ℕ", transitive colorings.
- **Lexicographic order of columns** (lesson 3, ADS → COH).
- **Stable/cohesive decomposition** (lessons 3, 4), as for Ramsey's theorem.
- **Blocks of colors** (Kreuzer's theorem), a first-order argument using the finite
  pigeonhole principle and Hirst's theorem.
- **Simple priority without restraint** (lesson 4, tournaments): cycles can be closed with
  any new element.
- **Measure counting and randomness** (lesson 5): blocks of $e + 2$ bits; Kučera's lemma;
  columns of a random sequence and Stephan's theorem.
- **Forcing with preconditions and conditions** (lesson 6): computations explored through
  a computable set of preconditions; failures reveal elements of the other part.
- **Preservation of a weakness property** (lesson 6), from the reducibilities course.
- **Measuring problems by families of weakness properties** (lesson 7): hyperimmunities
  for disjunction, constant-bound immunity for compactness; transfer along computable
  reductions.

## 5. Included, excluded, and why

- **Included:** the principles that both reference books treat at length and that appear
  in almost every paper of the area: CAC, ADS and their parts, EM, DNR, WWKL₀.
- **Excluded, to the courses of the secondary track:** the separations of ADS from CAC,
  of EM from SRT²₂, of RT²₂ from WWKL₀ and WKL₀ (Liu), and the low basis for SADS. They
  need the forcing design methods of `separation-design`, `compactness-avoidance` and
  `lowness`; this course states them and points there.
- **Excluded, to the computable structure theory track (planned 2026-11-18):** the atomic
  model theorem and its relatives (Hirschfeldt, Section 9.3), which need Henkin
  constructions and the theory of types.
- **Excluded:** the rainbow, polarized, free set and thin set theorems, Hindman's theorem,
  the tree theorems (Dzhafarov–Mummert, Sections 9.3–9.9). They are mentioned in the last
  lesson; each could be a specialized course.
- **First-order strength** is only touched (Kreuzer's theorem, $\mathsf{COH}$ conservative):
  the course on induction and conservation treats it.

## 6. Comparison with the literature

- Hirschfeldt, Chapter 9.1–9.2: same order of topics (ADS, CAC, decompositions,
  tournaments); WWKL and DNR are in Hirschfeldt's Chapter 4 and Section 9.1. The proof of
  Tennenbaum–Denisov here adds the requirements $\mathcal P_z$ to obtain the order type
  ω + ω* (Hirschfeldt leaves it as Exercise 9.12).
- Dzhafarov–Mummert, Sections 9.2, 9.5, 9.11, 9.12: the proofs of ADS → COH, of
  $\mathsf{CAC} = \mathsf{SCAC} + \mathsf{ADS}$, of Kreuzer's theorem, of WWKL → DNR and of
  the preservation of non-DNC degrees follow them.
- Two arguments of Dzhafarov–Mummert were corrected when writing the course:
  - the proof of Proposition 9.2.7 (ADS from transitive colorings) takes a minimal
    counterexample over pairs of $S$, but the element produced by the argument need not
    belong to $S$; the solution of `ex-ads-transitive` takes the minimum over all pairs;
  - the proof of Proposition 9.2.17 (SADS omits computably dominated solutions) places a
    number between two elements of $S$ in the order of ℕ in the ω-part, which does not
    follow; `ex-sads-hyperimmune` uses disjoint intervals and the $\leq_L$-least element of
    each, as in the proof that an immune part of a stable order is hyperimmune;
  - in the proof of Corollary 9.11.6 (WWKL₀ does not prove WKL₀), the step "a set random
    relative to a PA set is PA" is not valid; `cor-wwkl-not-wkl` derives the absence of PA
    sets from the fact that all sets of the model are computable from one low random
    sequence.
- `prop-em-not-computable` is a direct construction written for the course; the stronger
  theorem of Kach, Lerman, Solomon and Weber (no Σ⁰₂ solutions) is admitted.

## 7. Figures

Generated by `scripts/figures/combinatorial-principles.py`:
- `cut-construction` (computable-orders): an action of $\mathcal R_e$ moving the cut;
- `tournament` (erdos-moser): a tournament on five players with a transitive set and a
  cycle;
- `zoo` (ads-dnr): the implications of the course.

## 8. Sources

- D. R. Hirschfeldt, *Slicing the Truth*, Chapter 9 (Sections 9.1–9.2) and Section 4.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics*, Chapter 9.
- Hirschfeldt and Shore (2007); Tennenbaum (Rosenstein 1982), Denisov (Goncharov–Nurtazin
  1973); Kreuzer (2012); Lerman, Solomon and Towsner (2013); Yu and Simpson (1990); Giusto
  and Simpson (2000); Ambos-Spies, Kjos-Hanssen, Lempp and Slaman (2004); Csima and Mileti
  (2009); Chong, Lempp and Yang (2010); Chong, Slaman and Yang (2014); Monin and Patey
  (2021).

## 9. History

- 2026-11-18: course created, with five lessons; the first one, at 58 minutes of open
  text, was split into `orders` and `computable-orders`. The claim, in a first draft, that
  $\mathsf{SRT}^2_2$ is equivalent to $\mathsf{EM} + \mathsf{SADS}$ was reduced to the
  implication from $\mathsf{EM} + \mathsf{SADS}$, which is what the sources prove. A first
  draft of `prop-em-not-computable` without priority was wrong (weaker requirements could
  take the elements a stronger one needs) and was replaced by a priority version.
- 2026-11-18 (later): lesson 7 `disjunction-compactness` added at the author's request,
  to present the modern separation tools as intuitions: the number of preserved
  hyperimmunities measures how disjunctive a statement is, and preservation of
  constant-bound immunity measures the absence of compactness (DNR ≡ RWWKL being the
  weakest compactness). The hard preservation theorems are cited from `separation-design`
  and `compactness-avoidance`; the lesson proves the transfer lemma, the failures for
  SRT²₂ and SADS, and derives the table. Lesson 6 now points to it: its direct proof of
  ADS ⊬ DNR is the special case of the c.b.-immunity argument.
