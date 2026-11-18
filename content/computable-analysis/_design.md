# Design log: Computable analysis

This file is the memory of the course (see "Designing tracks and courses" in
`AGENTS.md`). It is not rendered.

## 1. Objectives

After the course, a student can:

- compute with names in Baire space (Type-2 computability), and prove that a problem is
  not computable by a continuity argument;
- compare representations of the reals (Cauchy, decimal, left, right), and explain why
  decimal expansions are inadequate although they have the same computable points;
- prove that computable real functions are continuous, that continuous functions are
  those computable relative to an oracle, and compute the arithmetic operations and
  limits with a known rate;
- use the effective compactness of [0, 1] to compute a modulus of uniform continuity and
  the maximum value of a function, and work with computable metric spaces, in particular
  C[0, 1] with the uniform metric;
- work with closed sets given by negative information (co-c.e. closed sets, the analogue
  of Π⁰₁ classes), and prove that closed choice on [0, 1] is equivalent to WKL;
- classify the intermediate value theorem, the Brouwer fixed point theorem in dimension
  one, the maximum and the monotone convergence theorem in the Weihrauch degrees, and
  compare with reverse mathematics.

**Role.** A specialized course (in no track), as planned in `content/tracks-design.md`
("Computable analysis"). It connects the reverse mathematics of analysis
(`second-order-arithmetic/real-numbers`, `second-order-arithmetic/analysis-in-rca0`,
`big-five`) with Weihrauch reducibility (`reducibilities/weihrauch`,
`reducibilities/parallelization`), and gives the computability-theoretic background
for the research literature on Weihrauch complexity in analysis.

## 2. Prerequisites assumed

- Turing degrees: Turing functionals, finite oracles and the use principle
  (`def-finite-oracle`, `prop-oracle-stages`, `thm-use-principle`).
- Π⁰₁ classes: topology of Cantor space (`def-open-closed`), Π⁰₁ classes and effective
  compactness (`prop-pi01-equivalent`, `prop-pi01-emptiness`), DNC₂ without computable
  member (`thm-dnc2-no-computable`), the low basis theorem (`thm-low-basis`).
- Second-order arithmetic: reals as fast Cauchy sequences (`def-real-rca`,
  `ex-real-equality`, `prop-rca-complete`), Specker sequences (`prop-specker`), codes of
  continuous functions (`def-continuous-code`) and the intermediate value theorem in RCA₀
  (`thm-ivt-rca`).
- Big Five: monotone convergence ↔ ACA₀ (`thm-monotone-aca`); Heine–Borel ↔ WKL₀ (lesson
  link only).
- Reducibilities: Weihrauch reducibility (`def-weihrauch`), LPO and LLPO
  (`def-lpo-llpo`), parallelization, J ≡ LPO^ (`thm-jump-lpo`) and WKL ≡ LLPO^
  (`thm-wkl-llpo`).

## 3. Results, lesson by lesson

1. **Computability on Baire space** (`type-two-computability`): computable partial
   functions on Baire space via Turing functionals (`def-type2-computable`), finite
   oracles (`lem-type2-finite`), examples (`ex-type2-functions`), computable ⇒ continuous
   (`thm-type2-continuous`), continuous ⇔ computable relative to an oracle
   (`thm-continuous-relative`); composition. Figure `use-continuity`.
2. **Representations and the real numbers** (`representations`): represented spaces,
   realizers (`def-representation`), reductions of representations
   (`def-representation-reduction`), Cauchy representation (`def-cauchy-representation`,
   `lem-cauchy-variants`), examples of computable reals (`ex-computable-reals`, including
   the uniform ternary coding x_A), decimal representation (`def-decimal-representation`,
   `prop-decimal-cauchy`: ρ₁₀ ≤ ρ, ρ ≰_t ρ₁₀, x ↦ 3x not decimal-continuous;
   `prop-decimal-points`: same computable points), left/right representations
   (`def-left-right`, `prop-left-right`: ρ ≡ ρ_< ∧ ρ_>, ρ_< ≰_t ρ). Featured exercise:
   the signed-digit representation is equivalent to ρ (`ex-signed-digit`). Figure `decimal-one`.
3. **Computable real functions** (`real-functions`): definition
   (`def-computable-real-function`), prefix intervals U_σ (`lem-prefix-interval`),
   continuity (`thm-real-continuous`), continuous ⇔ computable relative to an oracle, with
   codes as oracles (`thm-real-continuous-relative`), undecidability of order and
   semi-decidability of x < y (`prop-order-undecidable`), arithmetic
   (`thm-arithmetic-computable`), effective limits (`prop-effective-limit`). Featured
   exercises: exponential (`ex-exp`), positivity of computable functions
   (`ex-positive-search`). Figure `prefix-interval`.
4. **Continuous functions on the unit interval** (`continuous-functions`) and **Computable metric spaces** (`computable-metric-spaces`, split off 2026-11-17; from `def-computable-metric-space` on):
   rectangle names (`def-rectangle-name`), evaluation and computable functions ⇔
   computable names (`thm-rectangle-computable`), effective Heine–Borel
   (`lem-effective-heine-borel`), modulus of uniform continuity and maximum value
   (`thm-modulus-max`), the Pour-El–Richards characterization (remark), computable metric
   spaces (`def-computable-metric-space`, `ex-computable-metric-spaces`), δ_C ≡ δ_□
   (`thm-cauchy-rectangle`). Featured exercise: integral (`ex-integral`). Figure `lebesgue-number`.
5. **Closed sets and closed choice** (`closed-sets-and-choice`): ψ_> (`def-closed-negative`),
   examples (`ex-co-ce-closed`), co-c.e. closed sets = zero sets of computable functions
   (`thm-zero-sets`), problems on represented spaces (`def-problem-represented`), closed
   choice (`def-closed-choice`), C_[0,1] ≡_sW WKL (`thm-closed-choice-wkl`). Featured
   exercises: unique choice is computable (`ex-unique-choice`); LLPO ≤_sW C_[0,1]
   directly (`ex-llpo-closed-choice`). Figure `closed-choice-tree`.
6. **The intermediate value theorem** (`intermediate-value-theorem`): IVT
   (`def-ivt-problem`), trisection (`thm-trisection`), computable instances have
   computable solutions (`cor-ivt-computable-instances`), IVT has no continuous realizer
   (`thm-ivt-not-computable`), LLPO ≤_sW IVT ≤_sW WKL (`thm-ivt-llpo-wkl`), IVT^ ≡_W WKL
   and the Pour-El–Richards sequence (`cor-ivt-parallel`), admitted: IVT ≡ CC_[0,1] and
   strictness (`fact-ivt-connected-choice`), BFT₁ ≡_sW IVT (`thm-brouwer-one`).
   Featured exercise: inverses of increasing functions (`ex-inverse-increasing`). Figure
   `ivt-polygons`.
7. **The maximum and monotone convergence** (`maximum-and-limits`): MAX ≡_sW WKL
   (`thm-max-wkl`), computable functions with only non-computable maximum points and
   low maximum points (`cor-max-points`), MCT ≡_sW J (`thm-mct-jump`), table of
   classifications and comparison with reverse mathematics. Featured exercise: unique
   maximum points are computable (`ex-unique-max`).

## 4. Proof techniques

- **Continuity method** (the main negative technique): a realizer reads a finite prefix
  before committing to an output, so a problem whose solutions are not determined by any
  finite part of the input has no continuous realizer. Introduced in lesson 1
  (`thm-type2-continuous`, the function Z), used for decimal names (lesson 2), left names
  (lesson 2), order of reals (lesson 3), and IVT (lesson 6). It is the technique of the
  `reducibilities/weihrauch` lesson, named there "continuity argument".
- **Prefix extension**: a finite part of a name of x extends to names of all points near
  x (`lem-prefix-interval`); the basic tool of every continuity proof for reals.
- **Use principle / relativization**: computable ⇒ continuous, continuous ⇔ relatively
  computable (lessons 1, 3).
- **Effective compactness** (search for a finite subcover justified by Heine–Borel):
  lesson 4 (modulus, maximum value), lesson 5 (closed choice, unique choice), lesson 7.
  Compared explicitly with effective compactness of Cantor space (`prop-pi01-emptiness`)
  and with the reverse-mathematical strength of Heine–Borel.
- **Coding into the Cantor set / ternary digits with gaps**: uniform decoding of sets
  from reals (`ex-computable-reals` (3), `thm-closed-choice-wkl`, `thm-mct-jump`).
- **Dyadic trees of uncovered intervals**: reducing closed choice to WKL (lesson 5).
- **Tent functions**: realizing a closed set as a zero set (lesson 5), used for MAX and
  in the proof that C_[0,1] ≤ MAX.
- **Parallelization** to make non-uniformity visible on computable instances (lesson 6,
  `cor-ivt-parallel`), as in `reducibilities/parallelization`.
- **Trisection** (searching a non-zero value in the middle third instead of deciding the
  sign at the midpoint): lesson 6.

## 5. Choices

- **Baire space and Turing functionals rather than Type-2 machines over a finite
  alphabet.** The platform defines oracle computation with sets as oracles; using
  functionals on graphs lets the course reuse the use principle and finite oracles
  directly. Type-2 machines are described and their equivalence explained (lesson 1).
- **Representations via Baire space, as in Brattka–Hertling–Weihrauch.** Weihrauch's
  book works on Σ^ω; the difference is inessential and is stated.
- **The Cauchy representation is defined exactly as the RCA₀ reals** (`def-real-rca`),
  so that RCA₀ codes and names coincide; the variant with |q_k − x| ≤ 2^{-k} is
  `lem-cauchy-variants`.
- **Decimal representation on [0, ∞) with the integer part as first entry**, so that
  names are elements of Baire space directly and the counterexample at 1 is about the
  integer part. Weihrauch's version (Theorem 4.1.13) works over ℝ with signs.
- **Two names for C[0, 1]**: rectangle names (codes of reverse mathematics, convenient
  for evaluation and semi-decision) and Cauchy names for the uniform metric (convenient
  for constructing instances and for continuity arguments). Their equivalence is proved
  (`thm-cauchy-rectangle`) through the computable modulus; this makes the dependence on
  the Heine–Borel theorem visible, which is the point of comparison with WKL₀.
- **Closed sets of [0, 1] only, by negative information.** The general definition for
  computable metric spaces is given in words; positive information (ψ_<) and compact sets
  (κ) are excluded: they are not needed for the classifications, and the course length is
  limited. Co-c.e. closed sets are related to Π⁰₁ classes.
- **Problems on represented spaces are reduced to problems on names**, so that the
  definition of `reducibilities/weihrauch` applies unchanged and its results are cited.
- **Classifications proved:** C_[0,1] ≡ WKL, MAX ≡ WKL, LLPO ≤ IVT ≤ WKL, IVT^ ≡ WKL,
  BFT₁ ≡ IVT, MCT ≡ J. **Admitted:** IVT ≡ CC_[0,1] (Brattka–Gherardi 2011), strictness
  of LLPO < IVT < WKL and non-idempotency of CC_[0,1] (Brattka–Le Roux–Miller–Pauly 2019),
  BFT_n ≡ WKL for n ≥ 2. The proof of IVT ≤ CC_[0,1] needs a careful construction of
  nested intervals, and the strictness results need the theory of fractals and
  non-idempotency; both are beyond the length of a lesson. They are stated as a `fact`
  with references.
- **Lesson 7 groups the maximum and monotone convergence**, which both rely on the
  closed choice and IVT lessons only through the classification table; MAX was first in
  lesson 5, and moved to keep lessons within 45 minutes.
- **Excluded:** computational complexity (Weihrauch Ch. 7, Ko), differentiation and
  analytic functions (Weihrauch 6.4–6.5; differentiation ≡ lim is mentioned only through
  the survey), compact sets and hyperspaces, the Pour-El–Richards first main theorem
  (computable ODE/wave equation counterexamples), Bolzano–Weierstrass (≡ WKL′, mentioned in
  the notes of lesson 7), randomness in analysis (Brattka–Miller–Nies), admissibility
  theory (Kreitz–Weihrauch, Schröder) beyond a remark.

## 6. Comparison with the literature

- **Weihrauch, *Computable Analysis* (2000):** Chapter 2 (Type-2 machines, continuity:
  Theorems 2.2.3–2.2.4; oracles: Section 2.3) → lesson 1; Sections 3.1–3.2 and 4.1–4.2
  (representations, Cauchy representation Definition 4.1.5, Lemma 4.1.6, Lemma 4.1.9,
  base-n fractions Theorem 4.1.13, Example 2.1.4 (7) for multiplication by 3) → lesson 2;
  Section 4.3 (Theorems 4.3.1, 4.3.2, 4.3.7, 4.3.11) and Theorem 4.1.16 → lesson 3;
  Section 6.1 (Definition 6.1.3, Definition 6.1.9, Lemma 6.1.10), Theorem 5.2.7
  (computable Heine–Borel), Corollary 6.2.5, Theorem 6.2.7, Theorem 6.4.1, Section 8.1
  (Definition 8.1.2, Example 8.1.3) → lesson 4; Definition 5.1.1, Theorem 6.2.9 →
  lesson 5; Section 6.3 (Theorems 6.3.2, 6.3.7, 6.3.8, Corollary 6.3.9, Theorem 6.3.11) →
  lesson 6. The course is shorter and uses Baire space; Weihrauch's general theory of
  computable topological spaces and admissibility is only mentioned.
- **Brattka–Hertling–Weihrauch, tutorial (2008):** same order for lessons 1–4, on Baire
  space.
- **Brattka–Gherardi–Pauly, survey (2021, arXiv 1707.03202, checked):** the Weihrauch
  classifications of lessons 5–7: Theorem 7.23 and Corollary 7.24 (choice on Cantor
  space and [0, 1]), Theorems 7.34–7.35 (IVT ≡ CC_[0,1], non-idempotency), Figure 2
  (strict chain LLPO < CC_[0,1] < WKL), Theorem 8.3 (MAX, BFT_n, IVT^), Corollary 8.4
  (non-uniform consequences), Theorem 8.9 (MCT ≡ lim).
- **Dzhafarov–Mummert (2022):** Proposition 3.7.4 (IVT not uniformly computable, same
  polygon idea), Theorem 10.4.3 (IVT ≡ choice on nested intervals), Section 10.5 (WKL₀
  and uniform continuity). The course proves the upper and lower bounds and admits the
  exact degree.
- **Simpson (2009):** II.4, II.6 (reals, codes, IVT), III.2 (MCT), IV.1–IV.2 (Heine–Borel,
  maximum, uniform continuity: Theorem IV.2.3), IV.7 (Brouwer: Theorem IV.7.7).
- **Pour-El–Richards (1989):** their definition of computable functions on compact
  intervals is shown equivalent (lesson 4); their computable sequence of IVT instances
  without computable sequence of zeros is `cor-ivt-parallel`.

## 7. Pedagogical plan

1. `type-two-computability`: intuition (reading an infinite input, writing an infinite
   output); figure of two inputs sharing a prefix and their outputs; examples including a
   Π⁰₂ domain and the discontinuous LPO function; quiz on the use of the maximum over
   i < n and on why domains need not be open; featured exercises on sup
   (`ex-sup-not-continuous`) and on preservation of computable points vs computability
   (`ex-computable-points`); natural domains moved to the further exercises
   (`ex-type2-domains`).
2. `representations`: intuition (a name is a description, a realizer works on all
   names); examples of computable reals with a uniform coding of sets; figure at the real
   1 for decimal names; counterexample of x ↦ 3x; non-uniform positive result on decimal
   points; left names with the continuity proof; quizzes on the special name and on the
   non-uniform case distinction; signed-digit exercise (`ex-signed-digit`) showing why overlapping digits
   help.
3. `real-functions`: intuition for continuity before the proof; figure of U_σ; quiz on the
   choice of a good name; codes as oracles linking to RCA₀; undecidability of order with
   semi-decidability; arithmetic with explicit error bounds; quiz on the search for a lower
   bound of |x|.
4. `continuous-functions`: rectangle names related to RCA₀ codes; effective Heine–Borel
   with its non-effective correctness proof; figure of the Lebesgue number; quizzes on why
   a finite subcover is needed and on the order modulus → polygon; remark comparing with
   WKL₀.
5. `closed-sets-and-choice`: intuition of negative information; Cantor-space analogue
   (Π⁰₁ classes); zero sets via tent functions; problems on represented spaces as problems
   on names; figure of the dyadic tree of uncovered intervals; quiz on decidability of the
   tree and on the Cantor set gaps; unique choice exercise (`ex-unique-choice`).
6. `intermediate-value-theorem`: bisection vs trisection; figure of the polygons g_a;
   continuity proof of non-computability; quiz on why the argument fails for unique zeros;
   LLPO and WKL bounds; parallelization; Brouwer in dimension one.
7. `maximum-and-limits`: maximum value computable vs maximum point not; quiz on the role of
   M; Lacombe–Specker corollary and low maximum points; uniform Specker construction for
   MCT with quiz on the complement of L; classification table and comparison with reverse
   mathematics.

## 8. Sources

- Lesson 1: Weihrauch 2.1–2.3 (Theorems 2.2.3, 2.2.4, Lemma 2.3.11), Brattka–Hertling–
  Weihrauch, Turing 1936–37, Grzegorczyk 1955, Lacombe 1955.
- Lesson 2: Weihrauch 2.1 (Example 2.1.4), 3.1–3.2, 4.1 (Definitions 4.1.3, 4.1.5, Lemmas
  4.1.6, 4.1.9, Theorem 4.1.13), 4.2, 7.2 (Definition 7.2.4); Turing 1937.
- Lesson 3: Weihrauch 3.2, 4.1.16, 4.3 (4.3.1, 4.3.2, 4.3.7, 4.3.11); Simpson II.6;
  Pour-El–Richards Ch. 0.
- Lesson 4: Weihrauch 5.2.7, 6.1 (6.1.3, 6.1.9, 6.1.10), 6.2.5, 6.2.7, 6.4.1, 8.1 (8.1.2,
  8.1.3); Brattka–Presser 2003; Simpson IV.2.3; Dzhafarov–Mummert 10.5.11–10.5.12.
- Lesson 5: Weihrauch 5.1.1, 6.2.9, 6.3.9; Brattka–Presser 2003; Gherardi–Marcone 2009;
  Brattka–Gherardi 2011; Brattka–de Brecht–Pauly 2012 (Corollary 4.6); BGP Theorem 7.23,
  Corollary 7.24.
- Lesson 6: Weihrauch 6.3 (6.3.2, 6.3.7, 6.3.8, 6.3.9, 6.3.11); Dzhafarov–Mummert 3.7.4,
  10.4.3; Brattka–Gherardi 2011 (Theorem 6.2); Brattka–Le Roux–Miller–Pauly 2019; BGP
  7.34, 7.35, 8.3, 8.4, Figure 2; Simpson II.6.6, IV.7.7; Pour-El–Richards 1989.
- Lesson 7: BGP 8.3, 8.4, 8.9; Brattka 2016; Brattka–Gherardi–Marcone 2012 (Fact 11.26);
  Brattka–Gherardi 2011 (Proposition 3.8); Specker 1949, 1959; Simpson II.6.6, III.2.2,
  IV.2.3, IV.7.7.

Section and theorem numbers of Weihrauch, Simpson and Dzhafarov–Mummert were checked
against the text files of the books; those of the BGP survey against arXiv 1707.03202.

## 9. Recent literature

- Brattka, Gherardi and Pauly, *Weihrauch complexity in computable analysis* (Handbook,
  2021; arXiv 1707.03202): read for the classifications and attributions; it fixed the
  attribution of C_[0,1] ≡ WKL (Brattka–de Brecht–Pauly 2012, not Brattka–Gherardi), the
  status of IVT (≡ CC_[0,1], strictly between LLPO and WKL by Figure 2 and
  non-idempotency), BFT₁ ≡ IVT, BFT_n ≡ WKL (n ≥ 2), MAX ≡ WKL, MCT ≡ lim.
- Brattka, Le Roux, Miller, Pauly, *Connected choice and the Brouwer fixed point theorem*
  (J. Math. Log. 2019): cited for BFT and connected choice.
- Dzhafarov–Mummert (2022): IVT ≡_sW B (choice on nested intervals), a presentation of
  connected choice adapted to reverse mathematics.
- Not used: newer work on the Weihrauch lattice (e.g. first-order part, Brattka–Pauly
  algebraic structure); it concerns the structure of the degrees, not this course.

## 10. Open points

- A proof of IVT ≤_sW CC_[0,1] (Brattka–Gherardi; Dzhafarov–Mummert 10.4.3 for nested
  intervals) could be added as an exercise if a clean argument for ψ_>-names is written.
  The easier half, CC_[0,1] ≤_sW IVT, is the exercise `ex-cc-ivt` (2026-11-13).
- The pointer from `reducibilities/weihrauch` ("the intermediate value theorem does not
  uniformly admit computable solutions") and from `second-order-arithmetic/analysis-in-rca0`
  (end of the IVT section) could link to `computable-analysis/intermediate-value-theorem`.
- :ref{#ex-left-ce-specker} (`second-order-arithmetic/real-numbers`) on left-c.e. reals is
  cited as is;
  `martin-lof-randomness/measure` also defines left-c.e. reals (by monotone sequences),
  consistent with `def-left-right`.

## 11. Exercises

**Featured exercises** (in the text, after the material they practice). They were chosen
because each trains the central technique of its lesson on a new object, or because a
later lesson cites it.

- `type-two-computability`: `ex-sup-not-continuous` (the continuity method in its
  simplest form) and `ex-computable-points` (preserving computable points is weaker than
  computability), after the continuity theorem.
- `representations`: `ex-signed-digit`, at the end of the decimal section: overlapping
  digits are the positive counterpart of `prop-decimal-cauchy`.
- `real-functions`: `ex-positive-search` (semi-decision composed with a realizer, used
  again for trisection), after the order section; `ex-exp` (tail bounds and effective
  limits), after the arithmetic section.
- `computable-metric-spaces`: `ex-integral`, at the end: the simplest use of δ_C. (`continuous-functions` has no featured exercise; its further exercises are `ex-cover-semidecidable` and `ex-max-subinterval`, added 2026-11-17.)
- `closed-sets-and-choice`: `ex-unique-choice` (cited by lessons 6 and 7 and by further
  exercises), after the zero sets; `ex-llpo-closed-choice`, after closed choice.
- `intermediate-value-theorem`: `ex-inverse-increasing`, after the non-computability of
  IVT: it shows what strict monotonicity buys.
- `maximum-and-limits`: `ex-unique-max`, after the classification of MAX.

**Further exercises** (block at the end of each lesson; existing ones moved there keep
their labels).

- `type-two-computability`: natural domains (`ex-type2-domains`, moved); least zero and
  number of zeros (domain, continuity); a computable total function on Baire space that
  is not uniformly continuous (contrast with `ex-uniform-continuity`); effective form of
  `thm-continuous-relative` with a c.e. set of pairs; the embedding of Baire space into
  Cantor space and its Π⁰₂ range.
- `representations`: dyadic names; left names under addition and negation, with the
  continuity argument; the naive Cauchy representation (no rate); an effective diagonal
  argument against computable sequences of reals.
- `real-functions`: floor on ℝ \ ℤ (moved); √x with a precision adapted to its modulus;
  overlapping conditions (computable on names, never extensional), preparing multi-valued
  problems; supremum of a bounded sequence (left-c.e., not computable, continuity
  argument); decidable Dedekind cuts; moduli of convergence of null sequences.
- `continuous-functions`: Cantor space (`ex-cantor-cauchy`, moved, cited in
  `ex-computable-metric-spaces`); modulus directly from a δ_C-name (where compactness
  is really used); running maximum; values at rationals do not name a function (continuity
  argument); composition.
- `closed-sets-and-choice`: characterization by disjoint rational intervals (moved);
  unions and intersections; semi-decidable properties (emptiness, non-membership) and
  non-emptiness not semi-decidable; the maximum of a closed set is right-c.e. only;
  finite co-c.e. closed sets have computable points but choice among two points is not
  computable.
- `intermediate-value-theorem`: IVT with f(0)f(1) < 0 (`ex-ivt-sign`, moved); IVT with
  non-strict inequalities; trisection for polynomials; non-decreasing instances are not
  easier; LPO ≰_W IVT; CC_[0,1] ≤_sW IVT (difficulty 3, the easier half of
  `fact-ivt-connected-choice`).
- `maximum-and-limits`: lim_ℝ ≡_W J (`ex-lim-jump`, moved); IVT, BFT₁ ≤_sW MAX directly;
  the least maximum point is left-c.e. only; SUP ≡_sW MCT; maximum points of computably
  dominated degree; MAX <_W MCT.

**Sources.** Weihrauch 2000: Exercise 2.2.9 (`ex-baire-into-cantor`), Exercise 4.1.13 (a),
(c) (`ex-naive-cauchy`), Exercise 4.2.4 (`ex-modulus-convergence`), Exercise 4.2.11 (part 1
of `ex-sup-left-ce`); checked in the text version of the book. `ex-cc-ivt` gives one
direction of Brattka–Gherardi 2011, Theorem 6.2 (IVT ≡ CC_[0,1]), with a proof written for
the course (sign of each interval of the name found by effective compactness). The other
new exercises are written for the course, as consequences or variants of the lessons.
`ex-diagonal-reals` is Cantor's nested interval argument made effective.

**Not included.** The binary analogue of `ex-computable-reals` (3) is in
`martin-lof-randomness/measure`. The computable points of the naive Cauchy representation
(the reals computable in ∅′) were left out: the proof through the limit lemma is longer
than the exercise warrants.

## 12. History

- **2026-11-12: course created.** Seven lessons, figure generator
  `scripts/figures/computable-analysis.py` (six figures). Design as above; the maximum was
  moved from the closed-choice lesson to a final lesson with monotone convergence to keep
  lessons within 45 minutes.
- **2026-11-13: featured and further exercises.** Every exercise labeled, with an
  objective and a difficulty; one or two featured exercises per lesson placed after the
  material they practice, the others moved to a block of further exercises; 31 new
  exercises (section 11). Positional references to exercises replaced by labels
  (`ex-cantor-cauchy`, `ex-unique-choice`, `ex-left-ce-specker`); in the notes of
  `representations`, the signed-digit representation is attributed to Weihrauch's
  Definition 7.2.4 (the sentence read as if it were Turing's).
- **2026-11-17: split of `continuous-functions`.** The lesson read in about 46 minutes of open text. Rectangle names, effective Heine–Borel and the modulus and maximum stay in `continuous-functions` (retitled "Continuous functions on the unit interval"), with the remark on WKL₀ moved there; computable metric spaces, δ_C ≡ δ_□ and all the further exercises on δ_C form the new lesson `computable-metric-spaces`, which `closed-sets-and-choice` now requires. New exercises for `continuous-functions`: covering of [0, 1] by a computable sequence of intervals is semi-decidable but not decidable (`ex-cover-semidecidable`); maximum on a rational subinterval (`ex-max-subinterval`). All labels unchanged. Durations recomputed by the open-text rule (AGENTS.md; `npm run durations`): quizzes, solutions, hints and further exercises are no longer counted.
- **2026-11-18 (polishing pass).** `continuous-functions` had no featured exercise: `ex-cover-semidecidable` moved into the text. Exercises moved between the text and the further exercises keep their text, hence their hash and endorsements.
