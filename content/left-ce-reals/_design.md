# Design log: Left-c.e. reals and Ω

This file is the memory of the course (see "Designing tracks and courses" in
`AGENTS.md`). It is not rendered.

## 1. Objectives

After the course, a student can:

- work with left-c.e. reals through left cuts, approximations, sums and halting
  probabilities, and relate their binary expansions and Turing degrees to c.e. sets;
- use Solovay reducibility: its characterization by approximations, its consequences
  for Turing degrees and initial segment complexity, the join given by addition, and the
  completeness of Ω;
- prove the Kučera–Slaman theorem and the theorem of Calude, Hertling, Khoussainov and
  Wang, and use them: all random left-c.e. reals are Solovay equivalent, have the same
  initial segment complexity up to a constant, and are weak truth-table complete;
- transfer a Solovay test along non-computable good stages (Downey–Hirschfeldt–Nies) and
  deduce that a random sum of two left-c.e. reals has a random summand;
- characterize Solovay functions by the randomness of $\sum_n 2^{-f(n)}$ (Bienvenu–Downey).

**Role.** Core course of the randomness track, added on 2026-11-17 when the track was
enlarged (`content/tracks-design.md`). It comes after `randomness-notions` and before
`randomness-degrees` and `k-trivials`. Left-c.e. reals are to algorithmic randomness what
c.e. sets are to computability theory; both reference books give them a chapter
(Downey–Hirschfeldt 5 and 9, Nies 1.8 and 3.2), and the K-trivial course uses Ω, Solovay
functions and the analogy between left-c.e. reals and c.e. sets.

## 2. Prerequisites assumed

- **Kolmogorov complexity:** prefix-free machines, the optimal machine $U$ and its
  construction (`thm-optimal-prefix-free`: $U(0^e 1 \tau) = \hat M_e(\tau)$), the KC
  theorem and the fact that the machine it builds has exactly one description per request
  (`thm-kc`), Ω and `thm-omega` (whose proof uses only the optimality of $U$), conditional
  prefix-free complexity and the conditional KC lemma (`lem-conditional-kc`, used in the
  last lesson).
- **Martin-Löf randomness:** measure (`prop-measure-effective`, `lem-prefix-free-generator`),
  the Levin–Schnorr theorem, Solovay tests (`def-solovay-test`, `thm-solovay`).
- C.e. degrees only as a remark (left-c.e. reals have c.e. degrees).

## 3. Results, lesson by lesson

1. **approximations** — Left-c.e. reals: Soare's equivalences (`prop-left-ce`), cut and
   expansion Turing equivalent (`prop-cut-expansion`), a left-c.e. real that is not
   strongly c.e. (`thm-not-strongly-ce`, Soare), closure properties, halting probabilities
   = weights of c.e. or computable prefix-free sets = measures of Σ⁰₁ classes
   (`thm-left-ce-halting`), $\Omega_M$ computes $\dom M$ with computable use
   (`prop-omega-m-domain`), every left-c.e. real is wtt below ∅′. Featured exercise: almost
   c.e. sets (CHKW). Further: closure, computable modulus, leftmost paths.
2. **solovay-reducibility** — Definition (`def-solovay-reducible`, with $f(q) \leq \alpha$),
   characterization by approximations (`prop-solovay-approximations`, CCHK), transitivity,
   examples, $\leq_S$ implies $\leq_T$ (`prop-solovay-turing`), Solovay's lemma on close
   strings and the domination of $K$ and $C$ (`lem-close-strings`,
   `thm-solovay-complexity`), reals above a random real are random (`cor-above-random`),
   the join (`prop-solovay-join`), completeness of Ω (`thm-omega-complete`). Featured: the
   computable reals form the least degree. Further: the easy half of the DHN
   characterization by sums, products, $r_{\emptyset'} <_S \Omega$.
3. **kucera-slaman** — Ω-like reals are random; the Kučera–Slaman theorem with the form
   with increments (`thm-kucera-slaman`); CHKW (`thm-chkw`); consequences
   (`cor-random-left-ce`: Solovay equivalence and equal complexity of random left-c.e.
   reals, Demuth's sum theorem, wtt-completeness). Featured: sums and products of random
   left-c.e. reals. Further: Turing completeness, density of halting probabilities, slow
   convergence through a Solovay test.
4. **random-sums** — Solovay tests of intervals (`lem-interval-test`), the theorem of
   Downey, Hirschfeldt and Nies (`thm-dhn-random`) with its two lemmas
   (`lem-dhn-s-infinite`, `lem-dhn-leaving`), Demuth's splitting corollary
   (`cor-demuth-split`); the DHN splitting theorem for incomplete degrees is admitted, and
   with it the definability of randomness in the Solovay degrees. Featured: interleaving
   the bits of Ω.
5. **solovay-functions-and-omega** — Solovay functions (`def-solovay-bound`), computable
   bounds and finite sums (`prop-computable-bound`), the Bienvenu–Downey theorem
   (`thm-bienvenu-downey`), existence of Solovay functions (`cor-solovay-functions-exist`).
   Featured: computable sums give non-tight bounds.

## 4. Proof techniques

- Approximations from below and their speed; dyadic decompositions of left-c.e. reals.
- The KC theorem to realize a left-c.e. real as a halting probability, and with conditions
  (last lesson).
- Solovay tests made of intervals; the Kučera–Slaman test placed above the approximation.
- Transfer of a test along a co-c.e. set of guesses that cannot be skipped
  (Downey–Hirschfeldt–Nies), a technique of independent interest.
- Prefixes of a random real as advice for the enumeration of Ω (Bienvenu–Downey).

## 5. Choices

- **Five lessons, no lesson on presentations.** The theory of presentations of left-c.e.
  reals (Downey–Hirschfeldt 5.3: ideals, Downey–LaForte) and the structure of Solovay
  degrees beyond the join (density, splitting, undecidability; DH 9.5, 9.8) are cited, not
  proved. They are research topics whose proofs are long priority arguments; the course
  keeps to what the rest of the track uses and to the characterization of the random
  left-c.e. reals.
- **The definition of $\leq_S$ allows $f(q) \leq \alpha$** instead of $f(q) < \alpha$
  (Downey–Hirschfeldt). The two agree (rational reals are computable); the weak form avoids
  case distinctions in the proofs of completeness of Ω.
- **The DHN characterization by sums** ($\alpha \leq_S \beta$ iff $d\beta - \alpha$ is
  left-c.e.) is admitted in one direction: its proof (DH Lemma 9.1.7) is a fiddly
  construction of increments, and the course obtains what it needs (the increments
  inequality used by CHKW) directly from the proof of the Kučera–Slaman theorem, which is
  stated in the form with increments.
- **Kučera–Slaman before CHKW.** DH prove CHKW from Lemma 9.1.7; here the increments come
  from the Kučera–Slaman test itself.
- **Solovay functions** are defined again in the last lesson (label `def-solovay-bound`),
  since the course on K-trivial sets, which defines them with a particular construction
  (`def-solovay-function`), comes later in the track. The two definitions are the same.
- Rettinger's theorem (random left-d.c.e. reals are left-c.e. or right-c.e.) is already an
  exercise of `martin-lof-randomness/levin-schnorr` (`ex-rettinger`); not repeated.

## 6. Comparison with the literature

- **Downey–Hirschfeldt:** Section 5.1 (lesson 1), 9.1 (lesson 2), 9.2 (lesson 3), 9.5.6–
  9.5.9 (lesson 4), 9.4 (lesson 5). Proofs follow DH, except CHKW (from the Kučera–Slaman
  increments) and the definition of $\leq_S$ (weak inequality).
- **Nies, Section 3.2** ("Left-c.e. reals and their randomness"): the same core, with Ω-like
  reals and the Kučera–Slaman theorem; Nies uses the term "left-c.e. reals" as here.
- **Monin–Patey** does not have a chapter on left-c.e. reals; Ω is treated in its chapter
  on Kolmogorov complexity.

## 7. Pedagogical plan

Each lesson begins with the analogy with c.e. sets (domains of machines, many-one
completeness, Myhill's theorem, splitting), states the intuition before the proof, and has
one figure for each of the two main constructions (the Kučera–Slaman test, the DHN
procedure). Figures: `scripts/figures/left-ce-reals.py`.

## 8. Sources (checked 2026-11-17)

- Downey–Hirschfeldt, Sections 5.1 (Theorems 5.1.2–5.1.11, Proposition 5.1.12), 9.1
  (Definition 9.1.1, Proposition 9.1.2, Lemma 9.1.3, Theorems 9.1.4 and 9.1.8,
  Proposition 9.1.5), 9.2 (Proposition 9.2.1, Theorems 9.2.2 and 9.2.3), 9.4
  (Theorem 9.4.1, Corollary 9.4.2), 9.5 (Theorem 9.5.1, Lemmas 9.5.6 and 9.5.7,
  Theorem 9.5.8, Corollary 9.5.9, Theorems 9.5.3, 9.5.10, 9.5.12), checked in the PDF.
- Original papers cited from DH's bibliography: Soare 1969; Calude–Hertling–Khoussainov–
  Wang 2001; Calude–Coles–Hertling–Khoussainov 1999; Kučera–Slaman 2001; Downey–
  Hirschfeldt–Nies 2002; Demuth 1975 and 1988; Bienvenu–Downey 2009.

## 9. Recent literature

- Barmpalias and Lewis-Pye (2017, "Differences of halting probabilities") and Miller (2017,
  "On work of Barmpalias and Lewis-Pye: a derivation on the d.c.e. reals") show that the
  ratio of the speeds of approximation of a left-c.e. real and of Ω is well defined in the
  limit: $\lim_s (\alpha - \alpha_s)/(\Omega - \Omega_s)$ exists, and is $0$ exactly for
  non-random $\alpha$. This is a sharp form of the Kučera–Slaman theorem, mentioned as
  possible addition (open points); bibliographic data to be checked before citing.

## 10. Open points

- Possible addition: the Barmpalias–Lewis-Pye limit theorem (section 9), which would give a
  quantitative version of lesson 3 and of the Downey–Hirschfeldt–Nies theorem.
- Possible addition: Kučera–Slaman's result that the measures of the components of a
  universal Martin-Löf test are Ω-like (mentioned in the notes of lesson 3, not proved).
- Demuth 1975 is cited after Kučera–Slaman's remark; not checked in the original.

## 11. Exercises

Featured: `ex-almost-ce` (lesson 1), `ex-computable-least` (2), `ex-sum-not-random` (3),
`ex-interleaved-omega` (4), `ex-computable-sum-not-solovay` (5). Further exercises: 3 + 3 +
3 + 3 + 2, covering definitions (closure, modulus), proofs (half of DHN's sum
characterization, the sign lemma), techniques (Solovay tests for slow convergence), and
links (Ω-likeness and Turing completeness).

## 12. History

- **2026-11-17: course written** as part of the enlargement of the randomness track (five
  lessons). Sources checked against the Downey–Hirschfeldt PDF.
- **2026-11-17: polishing pass.** All proofs checked again. Corrections: the splitting theorem of Downey, Hirschfeldt and Nies is stated for left-c.e. reals that are neither computable nor random (Downey–Hirschfeldt, Theorem 9.5.3, splits over every lesser degree), and the definability of randomness in the Solovay degrees for non-computable reals; the year of the paper of Calude, Coles, Hertling and Khoussainov (1999, as in the references); two hype words removed. New further exercises: `ex-one-minus-omega`, `ex-solovay-rational-shift`, `ex-omega-halves-optimal`.
