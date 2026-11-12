# Design log: Martingales and randomness

This file is the memory of the course (see "Designing tracks and courses" in
`AGENTS.md`). It is not rendered.

## 1. Objectives

After the course, a student can:

- formalize betting strategies as martingales and supermartingales, and use Kolmogorov's
  inequality to bound the measure of the sequences on which a strategy wins much;
- prove Ville's theorem (null classes are exactly the classes contained in success sets),
  and use the savings trick to turn success into convergence of the capital to infinity;
- prove Schnorr's theorem (Martin-Löf randomness is the failure of every c.e.
  (super)martingale) and construct a universal c.e. martingale and an optimal c.e.
  supermartingale;
- work with computable martingales: reduction to rational values, the law of large
  numbers and Church stochasticity, convergence along computably random sequences;
- build a computably random sequence that is not Martin-Löf random, by diagonalizing
  against a combined martingale and compressing the construction;
- prove the equivalence of the martingale and test definitions of Schnorr randomness, and
  use total Solovay tests;
- characterize Kurtz randomness by martingales, place the four notions in a strict
  hierarchy, and prove that the upper three coincide outside the high degrees.

**Role in the track.** The randomness track (`content/tracks-design.md`) is Kolmogorov
complexity → Martin-Löf randomness → martingales. The course gives the third classical
approach to randomness, unpredictability, and completes the equivalence of the three
approaches for Martin-Löf randomness (Levin–Schnorr in the previous course, Schnorr's
theorem here). It introduces the weaker notions defined by computable strategies, which
the specialized course `randomness-notions` uses. In the terms of the track, it teaches
"martingales and the savings trick", and contributes to "effective measure arguments"
(Kolmogorov's inequality, total Solovay tests) and to "the interplay of randomness and
Turing degrees" (highness and the separations).

## 2. Prerequisites assumed

- **Martin-Löf randomness:** the measure on Cantor space (`fact-lebesgue-measure`,
  `lem-prefix-free-generator`, `prop-measure-effective`, `def-null`, `ex-null-classes`),
  Martin-Löf tests and the universal test (`def-ml-test`, `ex-ml-tests`,
  `thm-universal-test`), Solovay tests (`def-solovay-test`), Kurtz randomness and weak
  1-genericity (`ex-kurtz`), the Levin–Schnorr theorem (`thm-levin-schnorr`) and the
  ample excess lemma (`thm-ample-excess`); the exercise of `random-dnc` on random sets of
  c.e. degree (cited by lesson link).
- **Kolmogorov complexity:** the optimal prefix-free machine, `prop-k-basic`.
- **Immunity and growth:** Martin's domination theorem `thm-martin-domination`,
  `cor-high-hyperimmune`.
- **Turing degrees:** 1-generic sets `prop-1-generic`; highness `def-high`.
- **Π⁰₁ classes:** `prop-pi01-equivalent`.

## 3. Results, lesson by lesson

1. **Martingales** (`betting-strategies`): `def-martingale`, examples `ex-martingales`
   (elementary martingales E_τ, the measure martingales d_C, the proportional strategies
   p_δ), `lem-martingale-basic` (growth bound, sums, a martingale above a
   supermartingale), `lem-non-ascending` (leftmost non-ascending path),
   `lem-kolmogorov-inequality`. Exercises: an explicit martingale for the class of
   `ex-null-classes` (1); martingales and measures; the closed classes where a
   supermartingale stays below b.
2. **Ville's theorem and the savings trick** (`ville-theorem`): `prop-success-null`,
   `thm-ville` (with convergence to infinity), Ville's critique of von Mises (prose),
   `prop-savings`. Exercises: countable unions of success sets; the savings property and
   convergence.
3. **C.e. martingales and Schnorr's theorem** (`schnorr-theorem`): `def-ce-martingale`
   (c.e. and computable martingales), `ex-ce-martingales`, `lem-ce-sum`,
   `thm-schnorr-martingales`, `cor-universal-ce-martingale`, the savings trick for c.e.
   martingales (remark), `thm-optimal-supermartingale`; no optimal c.e. martingale
   (admitted). Exercises: the martingale Σ 2^{-K(τ)} E_τ and the ample excess lemma;
   partial computable martingales `ex-partial-martingale`.
4. **Computable randomness** (`computable-randomness`): `def-computably-random`,
   `lem-rational-martingale`, `prop-cr-basic` (ML ⇒ CR, no universal computable
   martingale, computable sequences), `lem-proportional`, `prop-cr-lln`,
   `thm-cr-limits`. Exercises: Church stochasticity; supermartingales; tails.
5. **A computably random sequence that is not Martin-Löf random** (`cr-construction`):
   `thm-cr-not-mlr` (X ≤_T ∅′, K(X↾n) ≤ (log(n+1)+2)² + c). Exercise: slower
   introduction of candidates gives K(X↾n) ≤ h(n) log n.
6. **Schnorr randomness** (`schnorr-randomness`): `def-schnorr-random` (orders,
   h-success), `ex-schnorr-success` (law of large numbers, computable sequences),
   `def-schnorr-test`, `lem-computable-generator`, `lem-weight-martingale`,
   `thm-schnorr-tests-martingales`, `thm-total-solovay`, `cor-clopen-solovay`,
   `prop-no-universal-schnorr`. Exercise: runs of zeros through a total Solovay test.
7. **The hierarchy of randomness notions** (`randomness-hierarchy`):
   `thm-kurtz-martingales` (Wang), `prop-hierarchy`, `prop-kurtz-not-schnorr`,
   separation of Schnorr and computable randomness (admitted), `thm-nst-nonhigh`,
   `cor-nst`; partial computable and Kolmogorov–Loveland randomness, `q-kl-mlr`.
   Exercises: an explicit Kurtz failure; Schnorr random sets of c.e. degree are high;
   Kurtz's original definition.

## 4. Proof techniques

- **Kolmogorov's inequality / stopping at a prefix-free set** (lesson 1), used in every
  later lesson to turn strategies into covers.
- **The dictionary between covers and strategies** (lessons 2–3): d_U for an open class U,
  and the classes {d > 2^k}; effective versions in Schnorr's theorem, Schnorr's
  characterization of Schnorr tests and Wang's theorem.
- **Universal objects by trimming and weighting** (lesson 3): the optimal supermartingale,
  parallel to the universal test of the previous course.
- **Savings** (lesson 2): one copy of the strategy per threshold, stopped when the
  threshold is passed.
- **Switching between strategies along a sequence** (lesson 4, convergence theorem).
- **Leftmost non-ascending path** (lessons 1, 4, 6): every supermartingale fails along a
  path computable from it; no universal computable martingale, no universal Schnorr test.
- **Diagonalization against a combined martingale, with an oracle deciding goodness up to
  a length** (lesson 5), and **compression of a construction** (lesson 5), giving low
  initial segment complexity.
- **Weights growing with the length** (lesson 6, `lem-weight-martingale`): a set of strings
  of computable weight becomes a martingale that succeeds at a computable rate.
- **Domination and escape** (lesson 7): Martin's theorem turns non-highness into a
  computable function that exceeds the entry times infinitely often.

## 5. Choices

- **Seven lessons.** A first draft had five lessons (martingales and Ville; Schnorr's
  theorem and savings; computable randomness with the separation; Schnorr randomness;
  hierarchy). With complete proofs, quizzes and exercises, three of them exceeded 3300
  words. Ville's theorem and the savings trick were separated from the basic theory
  (both are non-effective statements about martingales, and the savings trick belongs
  with Ville's convergence statement), and the construction of a computably random
  non-ML-random sequence became its own lesson, since it introduces two techniques.
- **Order.** Non-effective theory first (lessons 1–2), then the effectivity levels from
  the strongest (c.e.) to the weakest (Kurtz). This follows Nies (Chapter 7) and the
  logical order of the definitions; Downey–Hirschfeldt split the material between
  Chapter 6 (c.e.) and Chapter 7 (weaker notions).
- **Schnorr randomness defined by martingales.** The course defines Schnorr randomness by
  computable martingales and orders (Schnorr's original definition, as in
  Downey–Hirschfeldt 7.1.4) and proves the equivalence with Schnorr tests. The specialized
  course `randomness-notions` defines it by tests (`def-schnorr-kurtz`); the two
  definitions are related by `thm-schnorr-tests-martingales`. The course gives its own
  labelled definition of Schnorr tests (`def-schnorr-test`) because a core course cannot
  depend on a specialized one.
- **Proof of the test-to-martingale direction.** `lem-weight-martingale` is a
  reformulation of Nies, Lemma 7.3.4, stated for sequences of computable sets of strings
  with computable weight, so that it covers both Schnorr tests and total Solovay tests
  (the latter need individual lengths at least n, ensured by `lem-computable-generator`).
  The martingale is the explicit sum Σ 2^{g(|σ|)−|σ|} E_σ, simpler to verify than the
  E_k/F_k decomposition of Nies.
- **Separation of computable and Martin-Löf randomness.** Nies (Theorem 7.4.8) builds a
  computably random sequence of low complexity using the oracle Tot (which candidates are
  total). The course decides only "ψ_e is defined and a martingale up to length n+1", a
  Σ⁰₁ question, so that the sequence is Δ⁰₂; the compression uses the exit positions of
  the O(log n) candidates, giving K(X↾n) = O((log n)²), enough to contradict
  Levin–Schnorr. This proof is self-contained at the level of the course and keeps the
  essential technique of Nies's template.
- **Convergence theorem.** The proof in Downey–Hirschfeldt (Theorem 7.1.3) copies d
  multiplicatively, dividing by d(σ), which requires rational values; here d is copied
  additively with a fixed scaling factor and the switching uses rational approximations,
  so that the proof works for real-valued computable martingales.
- **Kurtz randomness.** Wang's characterization is proved; the direction (⇐) builds the
  null Π⁰₁ class directly instead of going through Kurtz null tests.
- **Admitted, with references:** existence of the Lebesgue measure (previous course); the
  null class in Ville's critique of von Mises (recurrence of the simple random walk);
  no optimal c.e. martingale (Downey–Griffiths–LaForte; D–H 6.3.12); Schnorr tests with
  measures exactly 2^{-n} (D–H 7.1.6); the separation of Schnorr and computable randomness
  (Wang 1996, 1999) and the converse of the Nies–Stephan–Terwijn theorem, every high degree
  contains separating sequences (D–H 8.11.6; Nies 7.5.9–7.5.10); partial computable
  randomness is strictly between (Nies 7.4.15, 7.5.7); ML ⇒ KL (D–H 7.5.5) and the result
  of Merkle et al. on halves.
- **Excluded:**
  - the martingale proof of the Kučera–Gács theorem (D–H 8.3.2) and the space lemma,
    which the design of `martin-lof-randomness` listed as possible material for this
    course: the theorem is already proved there by leftmost/rightmost coding, and the
    lesson count was reached. A candidate exercise or lesson for a later revision;
  - the Nies–Stephan–Terwijn constructions in high degrees (D–H 8.11.6, Nies 7.5): long
    and technical, a research-level topic;
  - martingale processes (Hitchcock–Lutz, Merkle–Mihailović–Slaman; D–H 6.3.4), computable
    measure machines (Downey–Griffiths), the Franklin–Stephan characterization: they refine
    the characterizations without new techniques at this level;
  - stochasticity beyond Church stochasticity (D–H 7.4), nonmonotonic randomness beyond
    definitions (D–H 7.5, Nies 7.6), effective dimension: specialized topics;
  - lowness for the weaker notions (Nies 8.3): belongs with `k-trivials`.

## 6. Comparison with the literature

- **Downey–Hirschfeldt.** Section 6.3 (6.3.1: Definition 6.3.1, Proposition 6.3.2,
  Kolmogorov's inequality 6.3.3, Schnorr's theorem 6.3.4, Corollary 6.3.5, optimal
  supermartingale 6.3.7, savings trick 6.3.8; 6.3.2: supermartingales and KM; 6.3.3: no
  optimal c.e. martingale 6.3.11–6.3.12; 6.3.4: martingale processes), Section 6.5
  (Ville's theorem on selection rules), Section 7.1 (computable randomness 7.1.1–7.1.3,
  Schnorr randomness 7.1.4–7.1.7, Franklin–Stephan 7.1.8, total Solovay tests
  7.1.9–7.1.10, no universal Schnorr test 7.1.11, limitations 7.1.12–7.1.13), Section 7.2
  (Kurtz randomness, Wang 7.2.13), Section 7.4–7.5 (stochasticity, nonmonotonic
  randomness, MSU 7.5.5), Section 8.11 (NST 8.11.1–8.11.6). D–H define success with limsup
  and Schnorr randomness with limsup d/h = ∞; the course uses "d ≥ h infinitely often"
  (Nies's form) and proves the equivalence in a remark.
- **Nies.** Chapter 7: 7.1 (martingales, supermartingales, Proposition 7.1.9, savings
  Exercise 7.1.14, Ville 7.1.15), 7.2 (c.e. supermartingales, Proposition 7.2.6, universal
  supermartingales and the martingale FS of Theorem 7.2.8), 7.3 (computable
  supermartingales, Theorem 7.3.3 and Lemma 7.3.4, Proposition 7.3.8, leftmost
  non-ascending strings 7.3.9–7.3.11), 7.4 (template, Theorem 7.4.8, compression lemma
  7.4.10, facile sets 7.4.11, partial computable randomness 7.4.15), 7.5 (high degrees),
  7.6 (selection rules, KL randomness). Section 3.5 (Schnorr tests, Proposition 3.5.13 for
  the NST theorem). The course follows Nies's order and template most closely.
- **Monin–Patey** (`external-data/monin-patey/parts/aleatoire-algorithmique.tex`): a
  single remark (martingales, Schnorr's theorem) at the end of the Levin–Schnorr section,
  referring to Downey–Hirschfeldt and Nies. The course is the platform's development of
  that remark.
- **Original papers:** Ville (1939), Schnorr (1971, monograph and Math. Systems Theory),
  Wang (1996, 1999), Downey–Griffiths (2004), Nies–Stephan–Terwijn (2005),
  Muchnik–Semenov–Uspensky (1998), Merkle–Miller–Nies–Reimann–Stephan (2006).

## 7. Pedagogical plan

1. `betting-strategies`: the betting game and the fairness condition before the
   definition; examples (constant, E_τ, d_C, proportional strategy with its exponential gain
   on biased sequences and loss on balanced ones); figure `fig-betting-tree` (the tree of
   p_{1/3} and a prefix-free set S illustrating Kolmogorov's inequality); intuition of the
   inequality (average capital at a stopping time; Markov's inequality); quizzes on the
   induction and the minimal elements.
2. `ville-theorem`: the dictionary covers ↔ strategies before the proof; quizzes on
   openness and on lim vs sup; Ville's critique of von Mises; figure `fig-savings` (exact
   values of d and d⁺ along one sequence); quizzes on the savings constant.
3. `schnorr-theorem`: what a c.e. martingale is for the gambler (unknown bets); the two
   effective translations before Schnorr's theorem; quiz on > vs ≥; universal and optimal
   objects compared with the universal test; savings for c.e. martingales.
4. `computable-randomness`: Schnorr's motivation; rational values; no universal object;
   the law of large numbers through the proportional strategy; convergence by switching
   strategies, with quizzes.
5. `cr-construction`: the idea (combined martingale, ∅′ decides goodness up to a length,
   compression) before the proof; figure `fig-exit-timeline` (the active intervals and the
   exit data that determine X↾n); quizzes on the normalization, the compression and the
   exits.
6. `schnorr-randomness`: Schnorr's critique (rate of success); examples (law of large
   numbers, computable sequences); figure `fig-success-panels` (Schnorr vs Kurtz failure);
   intuition of `lem-weight-martingale` (capital growing with the length, affordable by
   computable tails); quizzes.
7. `randomness-hierarchy`: table of the four martingale conditions; figure
   `fig-hierarchy`; intuition for highness (entry times and domination) before the NST
   proof; quizzes on the Solovay form and on the use of non-highness; the open question.

Figures are generated by `scripts/figures/martingales.py` (deterministic).

## 8. Sources, lesson by lesson (checked 2026-11-12 against the text files of the books)

1. `betting-strategies`: Ville 1939; D–H 6.3.1 (Def. 6.3.1, Prop. 6.3.2, Thm. 6.3.3); Nies
   7.1 (Def. 7.1.1, Fact 7.1.2, Examples 7.1.3–7.1.4, Prop. 7.1.6, Fact 7.1.7, Lemma 7.1.8,
   Prop. 7.1.9, Fact 7.1.12).
2. `ville-theorem`: Ville 1939; von Mises 1919; Wald 1936, 1937; Church 1940; D–H 6.2
   (history), 6.3.1, 6.5.1, 6.3.8, 7.1.8; Nies 7.1.14, 7.1.15; Franklin–Stephan, JSL 75
   (2010), 501–521.
3. `schnorr-theorem`: Schnorr, LNM 218 (1971) and Math. Systems Theory 5 (1971),
   246–258; Zvonkin–Levin, Russian Math. Surveys 25 (1970), 83–124;
   Downey–Griffiths–LaForte, MLQ 50 (2004), 613–627; D–H 6.3.4, 6.3.5, 6.3.7, 6.3.12, 6.3.2
   (KM); Nies 7.2.1, 7.2.6, 7.2.7, 7.2.8, 7.4.1.
4. `computable-randomness`: Schnorr 1971; Church 1940; D–H 7.1.1, 7.1.2, 7.1.3, 7.1.12,
   7.4.1; Nies 7.3.1, 7.3.8, 7.3.9, 7.3.11.
5. `cr-construction`: Schnorr 1971; Nies 7.4.8, 7.4.10, 7.4.11; D–H 7.4.2.
6. `schnorr-randomness`: Schnorr 1971; Downey–Griffiths, JSL 69 (2004), 533–554; D–H
   7.1.4–7.1.7, 7.1.9–7.1.11; Nies 3.5.8–3.5.10, 7.3.3, 7.3.4, Fact 1.8.26.
7. `randomness-hierarchy`: Kurtz 1981; Wang, thesis Heidelberg 1996, and IPL 69 (1999),
   115–118; Nies–Stephan–Terwijn, JSL 70 (2005), 515–535; Muchnik–Semenov–Uspensky, TCS 207
   (1998), 263–317; Merkle–Miller–Nies–Reimann–Stephan, APAL 138 (2006), 183–210; D–H
   7.2.13, 7.5.5, 8.11.2, 8.11.6; Nies 3.5.13, 7.4.15, 7.5.7, 7.5.9, 7.5.10, 7.6.19–7.6.21.

## 9. Recent literature

Checked on 2026-11-12:

- **Kolmogorov–Loveland randomness.** Whether KL randomness equals Martin-Löf randomness is
  still open; no resolution was found. T. Petrović, *Kolmogorov-Loveland betting
  strategies lose the Betting game on open sets*, arXiv:2403.19817 (2024), shows that the
  proof strategy that settled the corresponding question for broader classes of betting
  strategies does not apply to KL strategies; the same author's *Betting strategies with
  bounded splits* (arXiv:2212.14279) studies intermediate classes. Not cited in the lessons
  (preprints, details not checked against a published version); the lesson states the
  question as open.
- **Kastermans and Lempp** showed that injective randomness, a candidate intermediate
  notion, is weaker than Martin-Löf randomness (mentioned in search results; the
  bibliographic details were not checked, so it is not cited).
- No simpler proofs of Schnorr's theorem, of the Schnorr test characterization or of the
  NST theorem were found; the proofs given are the standard ones, with the modifications
  listed in section 5.

## 10. Open points

- **Durations.** `schnorr-randomness` has about 2630 words (48 minutes at 55 words per
  minute) and is set to 45, like `martin-lof-randomness/levin-schnorr`; the other lessons
  are within the rule.
- **Duplication with `randomness-notions/schnorr-kurtz`** (resolved on 2026-11-12: that
  lesson now cites this course instead of re-proving): that lesson defines Schnorr tests (`def-schnorr-kurtz` (2)), proves the
  implications Martin-Löf ⇒ Schnorr ⇒ Kurtz (`prop-notions-implications`), the law of large
  numbers for Schnorr randomness, and that weakly 1-generic sets are not Schnorr random
  (`prop-generic-kurtz`), and admits the NST theorem on non-high Schnorr random sets that
  this course proves (`thm-nst-nonhigh`). It should cite this course instead (see the
  report).
- **Bibliography of `martin-lof-randomness/levin-schnorr`:** it gives the title of
  Schnorr (1971) as "A unified approach to the definition of random sequences"; D–H's
  bibliography gives "... of a random sequence", used here. To be checked against the
  journal.
- **Possible additions:** the martingale proof of Kučera–Gács with the space lemma; the
  Franklin–Stephan characterization of Schnorr randomness by computable time bounds; the
  machine characterizations of Schnorr and Kurtz randomness.
- **Forward pointer kept on purpose:** `cr-construction` mentions, with a lesson link, the
  NST theorem proved in `randomness-hierarchy`; `schnorr-randomness` mentions Kurtz
  randomness, treated in the last lesson; `randomness-hierarchy` links to the specialized
  course `randomness-notions` for the collapse of Kurtz randomness in computably dominated
  degrees.
- **Course order:** `order: 3` coincides with `k-trivials`; the coordinator may renumber.

## 11. History

- **2026-11-12: course created.** Seven lessons, written after comparing D–H Chapters 6.3,
  7.1, 7.2, 8.11 and Nies Chapter 7. New generator `scripts/figures/martingales.py` with
  five figures (`fig-betting-tree`, `fig-savings`, `fig-exit-timeline`,
  `fig-success-panels`, `fig-hierarchy`). Five lessons were first drafted and split into
  seven to respect the lesson length.
