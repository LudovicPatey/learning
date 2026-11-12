# Design log of the tracks

This file records what each learning track is for, what it contains and why, and
the decisions taken when the tracks change (see "Designing tracks and courses" in
`AGENTS.md`). The tracks themselves are in `tracks.yaml`; each course has its own
log in `<course>/_design.md`.

The reader is a master's student who will do research in mathematical logic. A
track is the shortest sequence of courses after which such a student can read the
research literature of its area; everything else is a specialized course.

## Literature compared

- **Computability:**
  - Soare, *Turing Computability* (2016), Parts I–III;
  - Monin–Patey, *Computability theory* (the book this platform grew from);
  - Downey–Hirschfeldt, Chapter 2.
- **Randomness:**
  - Downey–Hirschfeldt, *Algorithmic Randomness and Complexity* (2010);
  - Nies, *Computability and Randomness* (2009);
  - the randomness chapter of Monin–Patey.
- **Reverse mathematics:**
  - Simpson, *Subsystems of Second Order Arithmetic* (2009);
  - Hirschfeldt, *Slicing the Truth* (2014);
  - Dzhafarov–Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs* (2022).
- **Higher computability:**
  - Sacks, *Higher Recursion Theory* (1990);
  - Chong–Yu, *Recursion Theory: Computational Aspects of Definability* (2015);
  - the higher computability chapter of Monin–Patey.
- **Computable analysis:** Weihrauch, *Computable Analysis* (2000).

## Computability theory

**Objective.** The common language of the other tracks: the models of computation and
their equivalence, c.e. sets and reductions, relative computability and the jump, the
arithmetic hierarchy, the first priority arguments, Π⁰₁ classes and basis theorems, and
the notions of computational weakness and strength measured by growth of functions.

**Techniques.** The track teaches, in this order:
- diagonalization (countability, fundamentals);
- arithmetization and normal forms (models of computation);
- the fixed point theorem (fundamentals);
- finite extensions and the limit lemma (Turing degrees);
- quantifier counting (arithmetic hierarchy);
- finite injury priority (c.e. degrees);
- compactness and forcing with Π⁰₁ classes (Π⁰₁ classes);
- domination and escape arguments (immunity and growth).

These are the techniques used without comment in the research literature of all four
areas.

**Comparison.**
- **Soare and Monin–Patey.** The track follows the common core of Soare (Parts I–II)
  and Monin–Patey.
- **Immunity and growth (from 2026-11-12, in the track).** Soare treats immunity,
  domination and DNC functions in Chapters 4–5, and Monin–Patey in a chapter of the
  main sequence. The randomness track depends on them: Martin-Löf randomness uses DNC
  functions and computably dominated degrees. Until 2026-11-12 the course was
  specialized; a core course depending on a specialized one was inconsistent.
- **Kept specialized:**
  - **Cohen genericity:** the finite extension method and 1-genericity are already in
    the Turing degrees course; the full theory of n-genericity is needed only by some
    readers.
  - **Structure of the Turing degrees** (exact pairs, embeddings, minimal degrees), as in
    Soare Part III.
  - **Infinite injury.**

**Excluded, with reasons.**
- **Strong reducibilities and Post's program** (Soare 3.8, Downey–Hirschfeldt 2.20). They
  are only mentioned in the course on c.e. degrees. A specialized course is possible
  later.
- **Lachlan games** (Soare Part IV). They are a presentation device rather than a body of
  results.
- **Computable structure theory.** It is not covered by the reference books of the
  platform, and would be a track of its own.

**Specialized course added on 2026-11-12.**
- **Effective forcing**: the forcing relation in general, its
  definability, forcing with trees (Sacks and Jockusch–Soare forcing), and the forcing
  question (Monin–Patey). It unifies techniques that are now spread over the Cohen
  genericity, Π⁰₁ classes, minimal degrees and Ramsey courses.

**Planned.**
- **Mass problems and natural degrees** (Monin–Patey): a specialized course, later.

## Algorithmic randomness

**Objective.** Randomness of infinite sequences through its three classical approaches —
incompressibility, effective null sets, and betting strategies — and their equivalence.

**Techniques.**
- Kolmogorov complexity and the KC theorem;
- effective measure arguments;
- universal tests;
- martingales and the savings trick;
- the interplay of randomness and Turing degrees (Kučera–Gács, DNC functions).

**Comparison.**
- Downey–Hirschfeldt (Chapters 3, 6, 7) and Nies (Chapters 2, 3, 7) both present the
  three approaches as the foundation of the area.
- Until 2026-11-12 the track had only the first two: martingales were mentioned in one
  sentence. A core course **martingales** is added after Martin-Löf randomness. It covers
  martingales and Ville's theorem, c.e. martingales and Schnorr's theorem, and computable
  and Schnorr randomness defined by martingales.
- **Kept specialized:**
  - **Notions of randomness.** It assumes the martingale course for computable and
    Schnorr randomness.
  - **K-trivial sets.** Lowness is central in Nies's book, but it is a research topic
    built on the core rather than part of it.
  - **Higher randomness**, which needs the higher computability track.

## Reverse mathematics

**Objective.** The strength of theorems of ordinary mathematics:
- the axiom systems of second-order arithmetic and the Big Five;
- the computability-theoretic analysis of combinatorial principles below ACA₀, with
  Ramsey's theorem as the case study;
- first-order strength (induction and collection, conservation);
- the problem reducibilities that refine provability over RCA₀.

**Techniques.**
- Coding in RCA₀;
- ω-models and Turing ideals;
- reversals;
- Mathias forcing and cone avoidance;
- non-standard models and conservation;
- uniform (Weihrauch) reductions.

**Comparison.**
- **Simpson** organizes the subject around the Big Five.
- **Hirschfeldt** (*Slicing the Truth*) puts the analysis of Ramsey's theorem and of
  first-order strength at the center.
- **Dzhafarov–Mummert (2022)** add problem reducibilities as a basic tool, and treat
  induction and bounding as part of the core.
- The track follows the last two: from 2026-11-12 it includes induction and conservation,
  and reducibilities, previously specialized.

**Excluded.**
- The reverse mathematics of analysis, algebra and topology beyond the examples in the
  Big Five course (Simpson, Chapters III–VI). These are applications of the same
  techniques; examples are given in the Big Five course.
- β-models and the systems above Π¹₁-CA₀ (Simpson, Chapter VII).

## Higher computability

**Objective.** Computability along the computable ordinals:
- ordinal notations and ω₁ᶜᵏ;
- hyperarithmetic sets and Kleene's theorem Δ¹₁ = HYP;
- Σ¹₁ classes and their basis theorems;
- the analogy between Π¹₁ sets and c.e. sets: norms, stages, reduction and
  uniformization.

**Techniques.**
- Effective transfinite recursion;
- well-founded trees and ranks;
- the boundedness principle;
- Π¹₁ norms and stage comparison.

**Comparison.**
- Sacks (Parts A–B) and Chong–Yu (Chapters 1–5) build higher computability on these
  three pillars.
- The stage comparison and uniformization are what make the analogy with c.e. sets
  usable, and every later topic (higher randomness, Π¹₁ forcing) relies on them. For
  this reason the course on descriptive set theory, previously specialized, is part of
  the track from 2026-11-12.

**Excluded.**
- α-recursion theory and admissible ordinals beyond ω₁ᶜᵏ (Sacks, Parts C–D). They are a
  research topic of their own.

## Computable analysis (specialized course, written 2026-11-12)

Weihrauch's book is the reference. The platform needs one specialized course:
- computable reals and their representations;
- computable functions on the reals and their continuity;
- computable metric spaces;
- the computable content of classical theorems.

It connects the reverse mathematics of analysis (second-order arithmetic) with
Weihrauch reducibility (reducibilities). A track of its own is not planned.

## History

- **2026-11-12.** Initial log, written when the design rules were introduced.
  - Moved into tracks: immunity and growth (computability), induction and conservation
    and reducibilities (reverse mathematics), descriptive set theory (higher
    computability).
  - New core course planned: martingales (randomness).
  - New specialized courses planned: effective forcing, and computable analysis.
- **2026-11-12.** `kolmogorov-complexity` now builds on `turing-degrees`, since it proves
  that C and Ω are Turing equivalent to ∅′.
- **2026-11-12.** `cohen-genericity` now builds on `immunity-growth` (hyperimmune
  and DNC functions, computably dominated sets).
- **2026-11-12.** Specialized course `effective-forcing` written: notions of forcing, the
  forcing relation, Cohen and tree forcings, Sacks forcing, the forcing question, and
  Mathias forcing.
- **2026-11-12.** Core course `martingales` written and added to the randomness track:
  betting strategies, Ville's theorem, Schnorr's theorem, computable randomness, Schnorr
  randomness and the hierarchy of randomness notions.
- **2026-11-12.** Specialized course `computable-analysis` written: type-2 computability,
  representations, computable real functions, continuous functions and closed sets, and
  the Weihrauch degrees of the intermediate value theorem, the maximum and monotone
  convergence.
