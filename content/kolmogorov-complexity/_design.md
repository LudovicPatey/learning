# Design log: Kolmogorov complexity

This file is the memory of the course (see "Designing tracks and courses" in
`AGENTS.md`). It is not rendered.

## 1. Objectives

After the course, a student can:

- define plain complexity $C$ and prefix-free complexity $K$, prove the invariance
  theorems, and work with the $\leq^+$ calculus (computable maps do not increase
  complexity, pairs, lengths);
- use the counting argument to show that most strings are incompressible, and its
  refinements (few descriptions near the complexity, few strings near $C(n)$, the counting
  theorem for $K$);
- prove that $C$ is not computable (Berry), approximable from above and Turing equivalent
  to $\emptyset'$, state Chaitin's incompleteness theorem, and describe the lower envelope;
- characterize the computable sequences by the complexity of their initial segments
  (Chaitin) and explain, through the oscillation theorem, why $C$ cannot define random
  sequences;
- build prefix-free machines with the KC theorem, characterize $K$ as the least right-c.e.
  function satisfying the Kraft inequality, and prove the coding theorem;
- prove that $\Omega \equiv_T \emptyset'$ and that its prefixes are incompressible.

**Role in the track.** First core course of the randomness track
(`content/tracks-design.md`): it supplies the technique "Kolmogorov complexity and the KC
theorem" and the incompressibility paradigm. The next core course (Martin-Löf randomness)
uses `thm-kc`, `prop-k-basic`, `thm-coding` (through the measure lesson), `cor-no-c-random`
and `thm-omega` (randomness of Ω via Levin–Schnorr). The specialized course on K-trivial sets
uses `thm-chaitin-computable`, `prop-k-segments-computable`, `thm-coding`, `thm-kc`.

## 2. Prerequisites assumed

- Fundamentals: partial computable functions, indices $\Phi_e$, stages $\Phi_e(x)[s]$,
  c.e. sets, the halting set $\emptyset'$, dovetailing.
- Turing degrees (only `turing-reducibility`): $\leq_T$, $\equiv_T$, computation relative
  to $\emptyset'$. Added as a course prerequisite on 2026-11-12: the course states
  $C \equiv_T \emptyset'$ and $\Omega \equiv_T \emptyset'$, which need oracle computation.
- Not assumed: Cantor space topology and König's lemma (proved inline for binary trees in
  `computable-sequences`; forward pointer to `pi01-classes/computable-members`), measure
  (the uniform measure appears only through dyadic intervals and weights).

## 3. Results, lesson by lesson

1. **plain-complexity:** machines, optimal machines, invariance theorem (`thm-invariance`),
   basic properties (`prop-c-basic`), incompressible strings (`def-incompressible`,
   `prop-incompressible-count`), examples (`ex-compressible-strings`, including the entropy
   bound), pairs (`prop-c-pairs`) and the necessity of the log term. Exercises: shortest
   descriptions are incompressible; a $\log + 2\log\log$ pair bound.
2. **non-computability** (new, 2026-11-12): Berry paradox (`thm-c-not-computable`), Chaitin's
   incompleteness theorem (`thm-chaitin-incompleteness`, new label), $C \equiv_T \emptyset'$
   (`prop-c-degree`, new label), lower envelope (`thm-c-envelope`, moved from
   initial-segments). Exercises: dom $U$ computes $\emptyset'$ (`ex-domain-complete`), $C$
   computes $\emptyset'$ (`ex-c-complete`), the incompressible strings form an immune set and
   the compressible ones a simple set, no computable $f =^+ C$.
3. **initial-segments:** computable sequences have minimal segment complexity
   (`prop-computable-segments`), oscillation theorem (`thm-oscillation`), `cor-no-c-random`,
   remark on the characterization of 2-randomness by plain complexity (not proved).
   Exercises: failure of subadditivity for concatenation; Barzdins' $2\log n$ bound for c.e. sets.
4. **computable-sequences** (new, 2026-11-12): Chaitin's theorem (`thm-chaitin-computable`,
   moved here and now **proved**), counting lemmas (`lem-description-count`,
   `lem-few-segments`, new labels). Exercise: finitely many sequences with
   $C(X\uh n) \leq C(n) + d$.
5. **prefix-free-complexity:** prefix-free machines, Kraft inequality (`prop-kraft`) and
   Kraft's converse for sorted lengths (remark), optimal prefix-free machine
   (`thm-optimal-prefix-free`), properties of $K$ (`prop-k-basic`), $K$ exceeds length
   (`cor-k-above-length`), `prop-k-segments-computable`, mention of K-trivials.
6. **kc-theorem** (new, 2026-11-12, split from coding-theorem): bounded request sets
   (`def-request-set`), KC theorem (`thm-kc`), characterization of $K$ (`thm-k-minimal`),
   Chaitin's proof of $K \leq^+ |\sigma| + K(|\sigma|)$. Exercises: computable bounds with
   convergent series; request sets of weight $2^d$ and uniform families.
7. **coding-theorem:** output probability, coding theorem (`thm-coding`), counting theorem
   (`thm-k-counting`), Ω (`def-omega`, `thm-omega`). Exercises: few descriptions near $K$;
   few strings with $K(\sigma) < K(n) + b$.

## 4. Proof techniques

- **Counting argument** (fewer short descriptions than strings): lessons 1, 4, 7; its
  refinement through a small c.e. set and a description by position (`lem-description-count`).
- **Simulation with a self-delimiting prefix** (invariance, optimal prefix-free machine,
  doubled-bit codes): lessons 1 and 5.
- **Berry paradox / diagonalization against short descriptions**: lesson 2 (non-computability,
  incompleteness, envelope), lesson 7 (incompressibility of Ω).
- **Approximation from above and stage arguments** (searching for a stage after which no
  short description converges): lesson 2 exercises, lesson 7 (settled stages of Ω).
- **Using the length of the input as information**: lesson 3 (oscillation), the reason for
  prefix-free machines.
- **c.e. tree of bounded width → computable tree with the same paths; König's lemma;
  isolated paths are computable**: lesson 4.
- **Bounded request sets (KC)**: lessons 6 and 7; the main construction tool of the track.
- **Minimality of $K$ among right-c.e. Kraft functions**: lesson 6, used in exercises.

## 5. Choices

- **Split of the course into seven lessons (2026-11-12).** The former `coding-theorem`
  (2900 words) and `initial-segments` (with the new proof of Chaitin's theorem, 3500 words)
  exceeded the length of a lesson. The KC theorem has its own lesson because it is the main
  tool of the track and deserves examples and a figure; non-computability was separated from
  `plain-complexity` (which then had room for intuitions, examples and a figure) and grouped
  with the lower envelope, which is a Berry-type argument. Slugs `plain-complexity`,
  `initial-segments`, `prefix-free-complexity` and `coding-theorem` are kept, since other
  courses name them.
- **Chaitin's theorem is now proved** (it was admitted). It is a classical characterization,
  its proof teaches two reusable techniques (counting descriptions, c.e. trees of bounded
  width), and the analogous failure for $K$ (K-trivials) is a central topic of a later
  course. The counting lemma is stated with the bound $(d+1)^2 2^{d+c}$, which the proof
  given here yields cleanly; the books state $O(2^d)$, but their proofs as written are not
  explicit about the coding of $m$ (see open points). Any bound depending only on $d$
  suffices.
- **Chaitin's incompleteness theorem** is now a labeled theorem with proof (it was a
  paragraph): it is the logical form of the Berry argument and is often cited.
- **The KC proof** is Chaitin's construction with free strings of distinct lengths, as in
  Nies's Theorem 2.2.17, rather than Miller's organizational device (Downey–Hirschfeldt): the
  invariants are explicit and match the figure.
- **The coding theorem** is proved directly from KC (requests at powers of 2) rather than via
  semimeasures: semimeasures are not used elsewhere in the track.
- **Excluded:** conditional complexity and symmetry of information (Downey–Hirschfeldt 3.2,
  3.3, 3.10; Li–Vitányi): not used by the track, and a natural topic for a specialized
  course; monotone and process complexity (DH 3.15–3.16); Solovay functions and Solovay's
  estimates of the domain of $U$ (DH 3.12–3.13); Kummer's tt-completeness of the
  compressible strings (cited only); the Miller–Yu improved counting theorem; applications
  of incompressibility to combinatorics and complexity theory.

## 6. Comparison with the literature

- **Monin–Patey**, chapter "Kolmogorov complexity and random numbers"
  (`external-data/monin-patey/parts/aleatoire-algorithmique.tex`): the same core (invariance,
  random strings, non-computability, Turing completeness of $C$ as an exercise credited to
  Gács, pairs, oscillation as an exercise credited to Martin-Löf, Chaitin's theorem with
  proof, prefix-free complexity, Ω, KC, coding theorem). The course places Ω after the
  coding theorem and gives full proofs where the book uses exercises.
- **Downey–Hirschfeldt, Chapter 3** (Sections 3.1, 3.4–3.9, 3.11, 3.13) and 6.1 (randomness
  of Ω), 16.1 (Barzdins), 16.3 (Kummer). The course follows Section 3.4 for Chaitin's theorem.
- **Nies, Chapter 2** (Sections 2.1, 2.2, 2.4): the characterizations of $C$ and $K$ by
  counting/weight conditions, the machine existence theorem (KC), coding theorem through
  the characterization of $K$; Proposition 2.1.22 (lower envelope), 2.1.28 (the compressible
  strings form a simple wtt-complete set); Theorem 3.6.10 (2-randomness).
- **Li–Vitányi** and **Shen–Uspensky–Vereshchagin** (AMS 2017): the standard monographs;
  cited as further reading.

## 7. Pedagogical plan

1. `plain-complexity`: intuition for the invariance theorem (simulate given the index); the
   example $M_\sigma(\varepsilon) = \sigma$ showing why optimality is up to a constant;
   the counting argument named as the basic technique; examples of compressible strings
   (entropy); figure of the description of a pair; quizzes on delimitation.
2. `non-computability`: the Berry paradox as intuition; the $\Sigma^0_1$/$\Pi^0_1$ asymmetry;
   the idea of the reduction $\emptyset' \leq_T C$ before the exercises; schematic figure of
   $C(m)$ and its lower envelope.
3. `initial-segments`: figure of the oscillation proof; remark that $C$ still detects
   2-randomness infinitely often.
4. `computable-sequences`: outline of the proof before the lemmas; intuition for the counting
   lemma; non-uniformity of the proof named; quizzes on the choice of incompressible levels
   and on the stage claim.
5. `prefix-free-complexity`: self-delimiting reading as the motivation; examples and
   non-examples of prefix-free sets; figure of a prefix-free set and its dyadic intervals;
   Kraft's offline converse as the bridge to KC; intuition for trimming machines.
6. `kc-theorem`: examples of bounded and unbounded request sets; a counterexample to a naive
   online strategy; figure of the stages of the construction on four requests; intuition for
   the characterization of $K$; Chaitin's one-line proof of $K \leq^+ |\sigma| + K(|\sigma|)$.
7. `coding-theorem`: example of output probability carried by infinitely many descriptions;
   intuition for the proof by KC; figure of settled stages for Ω.

Figures are generated by `scripts/figures/kolmogorov-complexity.py` (six figures). The
former hand-written KC tree figure was replaced by the generated stage figure.

## 8. Sources

- plain-complexity: Kolmogorov 1965, Solomonoff 1964; DH 3.1 (Prop. 3.1.1, 3.1.3, 3.1.5);
  Nies 2.1 (Ex. 2.1.3, 2.1.7).
- non-computability: Chaitin 1974; DH 3.1, 16.3; Nies 2.1.22, 2.1.28; Kummer 1996;
  Monin–Patey (Gács attribution of $\emptyset' \leq_T C$, after Li–Vitányi Exercise 2.7.7 —
  not checked against Li–Vitányi).
- initial-segments: Martin-Löf 1966; Kolmogorov 1968; DH Theorem 3.1.4, 3.11, Theorem 16.1.1
  (Barzdins 1968); Nies Theorem 3.6.10, Nies–Stephan–Terwijn 2005, Miller 2004.
- computable-sequences: Chaitin 1976; DH 3.4 (Lemmas 3.4.2–3.4.3, Theorems 3.4.1, 3.4.4);
  Loveland 1969; Monin–Patey "Chaitin's theorem".
- prefix-free-complexity: Levin 1974, Chaitin 1975, Kraft 1949; DH 3.5, 3.7 (Theorem 3.7.4);
  Nies 2.2, 2.4.1.
- kc-theorem: Levin 1971, Schnorr 1973 (Lemma 1), Chaitin 1975; DH 3.6 and footnote on the
  history, 3.7.8; Nies 2.2.17, 2.2.19.
- coding-theorem: Levin 1974, Chaitin 1975; DH 3.7.6, 3.9, 6.1.3, 9.2; Nies 2.2.25, 2.2.26;
  Calude–Hertling–Khoussainov–Wang (STACS 98), Kučera–Slaman 2001.

## 9. Recent literature

Checked (web search, 2026-11-12):
- Shen, Uspensky, Vereshchagin, *Kolmogorov Complexity and Algorithmic Randomness*, AMS
  Mathematical Surveys and Monographs 220 (2017): added as a reference; a modern textbook
  account of the same material.
- Shen, *Around Kolmogorov complexity: basic notions and results* (arXiv:1504.04955, 2015):
  presents Loveland's conditional form of the characterization of computable sequences with
  a short proof; no change to the course (the unconditional form is the one cited).
- Barmpalias and Lewis-Pye, *Differences of halting probabilities*, JCSS 89 (2017):
  research-level results on left-c.e. random reals; outside the scope of this course.
- The characterization of 2-randomness by infinitely often $C$-incompressible prefixes
  (Nies–Stephan–Terwijn 2005, Miller 2004) is not recent but gives a perspective on the
  oscillation theorem; added as a remark.
No simpler proof of Chaitin's theorem or of the KC theorem was found.

## 10. Open points

- The counting lemma `lem-description-count` is stated with $(d+1)^2 2^{d+c}$. Both DH
  (Lemma 3.4.2) and Monin–Patey state $O(2^d)$; as written, their proofs take $m = h(d)$
  or $2^{c+d}$ while $L_{m,k}$ counts $2^m$ descriptions, which does not give the stated
  bound directly. Whether $O(2^d)$ holds with a corrected argument was not checked.
- The attribution of the lower envelope theorem to Kolmogorov was removed from the
  theorem head (not verifiable); it is now attributed to Zvonkin–Levin's survey and Nies.
- The Gács attribution of $\emptyset' \leq_T C$ is taken from Monin–Patey (who cite
  Li–Vitányi, Exercise 2.7.7); Li–Vitányi was not available to check the exercise number.
- Nies (before Theorem 3.6.10) says Miller (2004) obtained "⇐", while the title of Miller's
  paper suggests "⇒"; the course says only "one implication".
- Possible later additions: conditional complexity and symmetry of information (a
  specialized course), Solovay functions.

## 11. History

- **2026-11-12 — design and pedagogy revision.** Design log written. Course split into seven
  lessons: new `non-computability` (from `plain-complexity`, with the lower envelope moved
  from `initial-segments`), new `computable-sequences` (Chaitin's theorem, now proved with
  two new lemmas), new `kc-theorem` (from `coding-theorem`). Labels moved:
  `thm-c-not-computable`, `thm-c-envelope` → non-computability; `thm-chaitin-computable` →
  computable-sequences; `def-request-set`, `thm-kc`, `thm-k-minimal` → kc-theorem. New
  labels: `thm-chaitin-incompleteness`, `prop-c-degree`, `ex-domain-complete`,
  `ex-c-complete`, `lem-description-count`, `lem-few-segments`. Course prerequisite
  `turing-degrees` added. Six generated figures (`scripts/figures/kolmogorov-complexity.py`);
  the hand-written KC figure was replaced. Intuitions, examples, counterexamples and quizzes
  added; references checked against DH, Nies and Monin–Patey; Gács attribution restored
  with its source.
