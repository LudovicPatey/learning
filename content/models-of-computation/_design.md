# Design log: Models of computation

Not a lesson: files starting with `_` are not rendered. Read this file before revising
the course, keep to its objectives, and record every decision in the history.

## 1. Objectives

After the course, a student can:

- state each classical model of computation precisely, with its input and output
  conventions and its treatment of partiality: Turing machines (one and several tapes),
  unlimited register machines, primitive and partial recursive functions, LOOP and WHILE
  programs, the λ-calculus;
- write small programs in each model and **prove them correct** (invariants, induction on
  steps or rounds);
- prove that a function is primitive recursive from the closure properties, and code finite
  sequences, and hence any finite object, primitive recursively;
- show by **simulation** that two models compute the same functions, and by
  **arithmetization** that the step function of a machine is primitive recursive;
- prove that the Ackermann function is not primitive recursive (majorization, and a direct
  diagonalization), and state and prove Kleene's normal form theorem and the existence of a
  universal partial computable function;
- prove that the LOOP programs compute the primitive recursive functions, and that the WHILE
  programs and the λ-terms compute the partial recursive functions, including the proof that a
  λ-term has no normal form when the function is undefined;
- say what the Church–Turing thesis asserts, and how it is (and is not) used in proofs.

**Role in the track.** First course of the computability track (`tracks-design.md`). Its job
is to give the later courses a fixed definition of "partial computable function", the
universal function $\Phi_e$, the normal form $U(\mu s\, T(e, \vec x, s))$, and primitive
recursive coding. The track design names "arithmetization and normal forms" as the
technique taught here. The course also teaches simulation and induction on derivations,
which are used without comment later. It has no prerequisite.

## 2. Prerequisites assumed

Naive set theory (functions, countable sets), induction on $\nat$ and well-founded
induction (used for the Ackermann function), elementary number theory: unique prime
factorization, the Chinese remainder theorem, Euclid's proof of the infinitude of primes.
No logic is assumed; Gödel's theorems are only mentioned for motivation. The diagonal
argument for uncountability is cited forward once (an exercise of `turing-machines`,
pointing to `countability/diagonal-argument`).

## 3. Results, lesson by lesson

1. **what-is-an-algorithm.** Partial functions, Kleene equality (`not-kleene-eq`); Cantor
   pairing is a bijection (`prop-cantor-pairing-bijection`); bijective numeration of strings
   (`ex-bijective-numeration`).
2. **turing-machines.** Definition, configurations, computations (`def-turing-machine`,
   `def-tm-configuration`, `def-tm-run`); input/output conventions (`def-tm-computes`);
   examples of the conventions (`ex-tm-identity`); successor and addition machines verified
   (`prop-tm-successor`, `prop-tm-addition`).
3. **programming-turing-machines.** Doubling machine with markers (`prop-tm-doubling`);
   translation invariance (`lem-tm-translation`); sequential composition
   (`prop-tm-composition`); clean halting (`ex-tm-clean-halt`).
4. **multitape-machines** (new, 2026-11-12). $k$-tape machines (`def-multitape`); a linear
   2-tape doubling machine (`ex-two-tape-doubling`); simulation by one tape
   (`thm-multitape-simulation`); other variants; folding a two-way tape
   (`ex-one-way-tape`).
5. **register-machines.** URM, semantics (`def-urm`, `def-urm-semantics`,
   `def-urm-computes`); multiplication verified (`prop-urm-mult`); standard form,
   concatenation, subroutines (`lem-urm-concat`, `lem-urm-subroutine`); closure under
   composition (`thm-urm-composition`).
6. **primitive-recursion.** Definitions; totality and computability
   (`prop-pr-total-computable`); explicit transformations; predicates, cases, bounded sums,
   quantifiers and minimization (`prop-pr-cases`, `prop-pr-bounded-sums`,
   `cor-pr-bounded-quantifiers`, `prop-pr-bounded-mu`); the enumeration of primes
   (`prop-pr-primes`).
7. **coding-sequences.** Prime power coding and its operations (`prop-seq-operations`);
   course-of-values recursion (`thm-course-of-values`); Gödel's β-function (`lem-beta`,
   example `ex-beta`).
8. **ackermann-function.** Termination and computability of $A$ (stack algorithm, example
   `ex-ack-stack`); monotonicity (`lem-ack-monotone`, `lem-ack-nesting`); majorization
   (`thm-ack-majorization`); $A$ is not primitive recursive (`cor-ack-not-pr`);
   diagonalization over derivations (`thm-pr-diagonal`); the graph of $A$ is primitive
   recursive (exercise, used in `mu-recursion`).
9. **mu-recursion.** Minimization on partial functions (`def-mu`); partial recursive
   functions (`def-partial-recursive`); they are computable; the Ackermann function is
   recursive (`prop-ackermann-recursive`); regular minimization (`def-regular-mu`); statement
   of the normal form theorem (`thm-kleene-normal-form`) and `cor-regular-mu`.
10. **loop-programs** (new, 2026-11-12). Syntax and semantics of LOOP and WHILE programs
    (`def-loop-while-syntax`, `def-loop-while-semantics`, `def-loop-while-computes`); LOOP
    programs are total (`prop-loop-total`); LOOP = primitive recursive (`thm-loop-pr`,
    Meyer–Ritchie); nesting depth 1 gives linear bounds (exercise).
11. **while-programs.** WHILE = partial recursive (`thm-while-partial-recursive`); one WHILE
    loop suffices (`cor-one-while`); WHILE ⊆ URM (`prop-while-urm`); URM ⊆ WHILE directly
    (exercise).
12. **lambda-calculus.** Terms, substitution, the substitution lemma (`lem-substitution`),
    α, β; Church–Rosser (`thm-church-rosser`, Tait–Martin-Löf proof with Takahashi's $M^*$,
    sketched) and uniqueness of normal forms (`cor-unique-normal-form`); standardization
    (`thm-normal-order`, admitted).
13. **lambda-programming** (new, 2026-11-12). Church numerals (`def-church-numerals`),
    λ-definability (`def-lambda-definable`), arithmetic (`prop-church-arithmetic`), booleans
    and pairs (`def-lambda-booleans`), Kleene's predecessor (`prop-lambda-pred`), fixed-point
    combinators (`thm-lambda-fixed-point`).
14. **lambda-definability.** Head reduction (`def-head-normal-form`); a term with a normal form
    has a finite head reduction (`lem-head-normal-order`, from standardization); head
    reduction in context (`lem-head-context`); head reduction of a term computing a numeral
    (`lem-numeral-head`); partial recursive ⇔ λ-definable (`thm-recursive-lambda-definable`,
    `thm-lambda-definable-recursive`), the partial case fully proved.
15. **equivalence-of-models.** Arithmetization of Turing machines
    (`prop-tm-partial-recursive`); Kleene's normal form, proved
    (`thm-kleene-normal-form-proof`); URM ⊆ Turing via multi-tape machines (`prop-urm-tm`);
    the equivalence theorem (`thm-equivalence-models`); the universal function
    (`cor-universal-function`).
16. **church-turing-thesis.** Status, Turing's analysis, Gandy's principles, axiomatizations
    of algorithms (Gurevich, Dershowitz–Gurevich), variants, use in proofs. No numbered
    theorem.

## 4. Proof techniques

- **Verification by invariants and induction on steps.** Introduced in `turing-machines`
  (successor and addition: one description of the configuration per phase), used for the
  doubling machine (an invariant per round, with a figure), the URM programs, the
  LOOP/WHILE compilations and the configuration-by-configuration proofs of simulations.
- **Simulation.** Introduced in `multitape-machines` (tracks and head marks; folding a
  tape), named again in `register-machines` (instruction sets), used in `while-programs`
  (WHILE → URM) and `equivalence-of-models` (URM → multi-tape machine). In later courses
  it reappears as relativization and as the simulation of one oracle machine by another.
- **Coding and arithmetization.** Cantor pairing and string coding (`what-is-an-algorithm`),
  sequence coding and the β-function (`coding-sequences`), coding of LOOP and WHILE states
  (`loop-programs`, `while-programs`), of λ-terms (`lambda-definability`), of configurations and whole
  computations (`equivalence-of-models`). This is the technique named by the track.
- **Induction on derivations.** Named in `primitive-recursion` (`prop-pr-total-computable`);
  used in the majorization theorem, Meyer–Ritchie, λ-definability, and the computability of
  partial recursive functions.
- **Bounded search.** The difference between bounded and unbounded minimization is the
  thread from `primitive-recursion` to `mu-recursion` and the normal form.
- **Diagonalization.** Over derivations (`thm-pr-diagonal`) and by growth
  (`cor-ack-not-pr`); the course says why the diagonal argument does not apply to all partial
  computable functions, preparing `fundamentals/halting-problem`.
- **Fixed points.** The λ-calculus fixed-point combinators (`lambda-programming`), a first
  form of the recursion theorem of `fundamentals`.
- **Growth (majorization) arguments.** Every primitive recursive function is below a row of
  $A$ (`ackermann-function`); nesting depth 1 gives linear bounds (`loop-programs`). They
  prepare the domination arguments of `immunity-growth`.
- **Well-founded induction** on $\nat^2$ ordered lexicographically: definition and
  termination of $A$.
- **Compilation in both directions.** Each scheme becomes a program with fresh variables;
  a program becomes a function on codes of whole states, a loop becoming a primitive
  recursion or a search (`loop-programs`, `while-programs`); named in the introduction of
  `loop-programs`.
- **Confluence by parallel reduction** (Tait–Martin-Löf, Takahashi's triangle property),
  `lambda-calculus`.
- **Non-termination by head reduction.** To show that a term has no normal form, show that
  its head reduction is infinite, following it through applications and substitutions
  (`lem-head-context`) (`lambda-definability`).

## 5. Choices

**Included, with reasons.**
- *Several models, each developed far enough to program in it.* The equivalence of the
  models is only convincing if each model is seen to be usable; and later courses use
  Turing machines (oracle machines, conventions of `def-tm-computes`), register-style
  programs (informal algorithms), and primitive recursion (coding, Σ⁰₁ normal forms).
- *Turing machines with explicit conventions* ($x+1$ strokes, clean final configuration,
  two-way tape). The clean output convention makes sequential composition a matter of
  renaming states plus translation invariance; it costs the exercise `ex-tm-clean-halt`.
- *Multi-tape machines* are needed by `prop-urm-tm`; they also give the course its first
  example of a simulation. Since 2026-11-12 they have a lesson of their own (see History).
- *URM (Shepherdson–Sturgis, Cutland's notation)* rather than a counter machine with
  decrement: the instruction set is small, and the subroutine discipline (standard form,
  $P[\ell_1, \dots, \ell_k \to \ell]$) is the clearest place to teach register hygiene, which
  the LOOP/WHILE proofs reuse.
- *Prime power coding* rather than iterated Cantor pairing as the main sequence coding: it
  is Gödel's and Kleene's, it makes length and projections easy to define, and the
  bijective coding by pairing is left as an exercise. The β-function is included because the
  arithmetic hierarchy and reverse mathematics courses need sequences defined with $+$ and
  $\cdot$ only.
- *Ackermann's function with two proofs of non-primitive-recursiveness* (growth and
  diagonalization): the first teaches majorization, which returns in the growth arguments of
  `immunity-growth`; the second is the pattern of all later diagonalizations.
- *λ-calculus*: it is one of the three historical definitions, the fixed-point combinators
  anticipate the recursion theorem, and Church–Rosser is the first confluence argument the
  students meet.
- *The Ackermann–Péter function in Robinson's form* rather than Ackermann's three-argument
  function or the hierarchy $A_n$ of Monin–Patey: its monotonicity lemmas are the shortest,
  and its rows are visibly iterates of one another (table and identity
  $A(x+1, y) = A(x, \cdot)^{y+1}(1)$ in the lesson).
- *LOOP and WHILE programs* make "for versus while" coincide with "primitive recursion
  versus μ", and give the cheapest proof that partial recursive functions are
  URM-computable.
- *Arithmetization of Turing machines* (not of register machines, as in Monin–Patey), so that
  the indexing of the normal form theorem is the Turing-machine indexing used by Soare and by
  `fundamentals`.
- *Head reduction in the lesson on λ-definability* rather than in `lambda-calculus`: it is
  needed only there, and keeps `lambda-calculus` within the length limit.

**Excluded, with reasons.**
- *Post systems, Markov algorithms, cellular automata, combinatory logic.* They add
  nothing to the equivalence proofs; they are mentioned at most in the thesis lesson.
- *Complexity of simulations* (beyond the quadratic slowdown, given as a quiz). It belongs to
  complexity theory; the course states only what is needed to explain the robustness of
  the notion.
- *The Grzegorczyk hierarchy and Péter's multiple recursion.* Only mentioned in the notes of
  `ackermann-function` and `while-programs`; a specialized course could treat subrecursive
  hierarchies.
- *A full proof of the standardization theorem* (`thm-normal-order`): admitted with
  references (Curry–Feys, Barendregt, Takahashi), since it is long and its technique is not
  used later. Since 2026-11-12 it is the only admitted fact in the λ-calculus lessons: the two
  facts about head normal forms formerly admitted for partial λ-definability (solvability,
  Barendregt) are replaced by `lem-head-normal-order`, derived from standardization, and the
  elementary lemmas `lem-head-context` and `lem-numeral-head`.
- *The theory of solvability and Böhm trees.* Only the name "unsolvable" is mentioned; head
  reduction is enough for the course.

**Order.** Machines first (Turing, then URM), then definitions by schemes (primitive
recursion, coding, Ackermann, minimization), then structured programs, which connect the
two, then the λ-calculus, and finally the equivalence proof and the thesis. The normal form
theorem is stated in `mu-recursion`, used in `while-programs` and `lambda-definability`, and
proved in `equivalence-of-models`; the proof does not depend on these uses, and the lessons
say so. Proving the normal form earlier would require arithmetizing Turing machines before
the recursive functions are complete, which was judged worse. On 2026-11-12 the former lesson
"LOOP and WHILE programs" was split into `loop-programs` and `while-programs`, and the former
"Computing with λ-terms" into `lambda-programming` (data and recursion) and
`lambda-definability` (head reduction and the equivalence theorem), because both exceeded the
length limit and each half has one main theorem. `loop-programs` is placed after
`mu-recursion` so that its introduction can compare `for` loops with unbounded search. `register-machines` only
depends on `what-is-an-algorithm`, and `lambda-calculus` likewise, so a reader may take
them in any order.

## 6. Comparison with the literature

- **Monin–Patey**, chapter "Church–Turing thesis" (`external-data/monin-patey/parts/
  church-turing.tex`): history of the Entscheidungsproblem; informal presentation of
  recursive functions, λ-calculus and Turing machines; then a detailed study using register
  machines with **structured programs** (following Durand–Rozière), primitive recursive
  functions, LOOP-programs = primitive recursive, the Ackermann function (hierarchy
  $A_n$, majorization as an exercise, diagonalization over codes), and the arithmetization
  of structured programs with list coding to get the universal program. Differences: the
  course treats Turing machines and the λ-calculus formally and proves their equivalence
  with the other models, where Monin–Patey describe them informally; it separates goto
  programs (URM) from structured ones; it proves majorization in full. Monin–Patey credit
  the theorem "every partial recursive function is computed by a structured program" to
  Wang (1957), Péter (1958) and Ershov (1958); the course credits LOOP to Meyer–Ritchie
  (1967), which is the source of the LOOP language and of the LOOP = primitive recursive
  theorem, and mentions Böhm–Jacopini for the elimination of jumps.
- **Soare, *Turing Computability* (2016)**, Chapter 1 (§1.4 Turing machines, with the
  alphabet $\{B, 1\}$, a partial transition function, input in $x+1$ strokes and output the
  number of $1$s on the tape) and Chapter 17 (history: §17.2.2 primitive recursive functions
  in Kleene's form, §17.2.3 Ackermann's function and the majorization theorem, credited there
  to Hermes 1969, §17.3 Turing's analysis). Soare does not prove the equivalence of the
  models. The course uses a stricter output convention (see `turing-machines`, notes).
- **Downey–Hirschfeldt** §2.1 (machines and coding, briefly) and §2.8 (primitive recursive
  functions, Ackermann function without proof).
- **Cutland (1980)**: the URM, its notation, and the method of proving the equivalence via
  register machines; the course follows Cutland for `register-machines`.
- **Kleene, *Introduction to Metamathematics* (1952)**: primitive recursion, the normal form
  theorem, Turing machines with $y+1$ tallies (§67).
- **Boolos–Burgess–Jeffrey**, chapter 3: Turing machines with a clean final configuration.
- **Sipser**, chapter 3: multi-tape and non-deterministic machines, with the simulations
  used in `multitape-machines`.
- **Barendregt (1984)**: λ-calculus; Church–Rosser by parallel reduction, standardization,
  solvability. The course proves partial λ-definability with head reduction only, instead of
  the theory of solvable terms. Chapter numbers are not cited (no copy available).
- **Hindley–Seldin (2008)**: an introduction to the λ-calculus at the level of the course
  (*not checked*, no copy).
- **Soare (2016) §§1.5.2–1.5.3** code Turing configurations and prove the enumeration
  theorem; §17.2.4 records that partial functions are due to Kleene (1938). The course
  arithmetizes configurations as two half-tapes read from the head, which makes the step
  function a definition by cases.
- **Monin–Patey** on Ackermann: the hierarchy $A_n$ computed with a stack, majorization as an
  exercise following Cori–Lascar; on structured programs: the theorem of Wang, Péter and
  Ershov, proved with register programs and list coding. The course proves majorization in
  full and arithmetizes Turing machines.

## 7. Pedagogical plan

For each lesson: intuitions, examples, counterexamples, figures (✓ = present).

1. **what-is-an-algorithm.** Features of algorithms with a quiz of examples and non-examples
   (✓); examples of partial functions, including one whose totality is an open problem (✓);
   Cantor pairing figure (✓); bijective numeration with a table and the reason for digits
   $1, \dots, m$ (✓); the word "arithmetization" introduced (✓).
2. **turing-machines.** Anatomy figure (✓); state diagram of $M_S$ (✓); run of $M_S$ on
   input $1$ as a space-time diagram (✓, 2026-11-12); example of the conventions: same
   machine computing the identity in arity 1 and the empty function in arity 2, and a
   machine halting only in non-standard configurations (✓); quiz on why $x+1$ strokes (✓).
3. **programming-turing-machines.** Doubling machine, with a figure of the rounds showing
   the invariant (✓); why markers are needed (quiz ✓); why translation invariance is needed
   for composition (✓).
4. **multitape-machines.** Intuition: why the definition must not depend on the variant (✓);
   a 2-tape doubling machine contrasted with the quadratic 1-tape one (✓); intuition of the
   simulation before the proof (✓); tracks figure (✓); folding exercise (✓).
5. **register-machines.** Programs verified by induction (✓); a non-standard-form program
   (✓); register layout figure for closure under composition (✓); the obstacle
   (interference of scratch registers) stated before the proof (✓). A flow diagram of the
   multiplication program could be added.
6. **primitive-recursion.** Recursion as a `for` loop, fixed parameters, one recursion
   variable (✓); the derivation of truncated subtraction spelled out, derivation tree of
   multiplication (✓); quizzes on fixed parameters and on why bounded search (✓).
7. **coding-sequences.** Worked example of a code and its decoding (✓); course-of-values
   figure (✓); the idea of the β-function before the proof, and a worked example with
   $c = 1521$ (✓).
8. **ackermann-function.** The two techniques announced (✓); table of the first rows and the
   rows as iterates (✓); stack trace of $A(1, 1)$ (✓, `ex-ack-stack`); intuition of
   majorization before the proof (✓); quizzes on the critical steps (✓). A figure of the
   growth of the rows was judged unnecessary after the table.
9. **mu-recursion.** The price of unbounded search (✓); the two ways a search can fail, with a
   figure (✓, `mu-search`); the quiz on the $g(\vec x, z)\converge$ clause (✓);
   counterexample exercise on domains (✓); why regular minimization is a poor definition (✓).
10. **loop-programs.** Compilation in both directions explained before the proofs (✓); fixed
    versus re-evaluated loop bounds (quiz ✓); the predecessor program (✓); nesting depth
    exercise (✓).
11. **while-programs.** A while loop as a search (✓); the minimization program (✓); layout of
    the URM translation of a LOOP instruction, with a figure (✓, `loop-urm`).
12. **lambda-calculus.** Overview of Church–Rosser and standardization (✓); variable capture
    (✓); $\Omega$ and the reduction graph of $(\lambda x. y)\Omega$ (✓, `k-omega`);
    $\mathsf K \mathsf I \Omega$ under both strategies (✓); Church–Rosser diamond (✓).
13. **lambda-programming.** Data represented by their use (✓); numerals as iterators (✓);
    Kleene's predecessor with a figure of the pairs (✓, `lambda-pred`); fixed points and the
    factorial (✓).
14. **lambda-definability.** Head reduction with examples, including $\lambda x.\, x\, \Omega$
    (head normal form without normal form, quiz ✓); the failure of the naive composition term
    for partial functions (quiz ✓); the infinite head reduction of the search (✓).
15. **equivalence-of-models.** Diagram of implications (✓, `equivalence-cycle`); simulation and
    arithmetization named (✓); coding of a configuration with the reversed left part (✓,
    `tm-configuration-code`, quiz ✓).
16. **church-turing-thesis.** What would refute the thesis (quiz ✓); Turing's analysis and its
    constraints (quiz ✓); axiomatizations; variants (quiz ✓).

## 8. Sources

Checked against the books available in `external-data/` (Soare 2016, Downey–Hirschfeldt,
Monin–Patey) unless marked *not checked*.

- **what-is-an-algorithm.** Hilbert–Ackermann 1928; Church 1936; Turing 1936; Soare §1.1
  and §§17.1–17.3 (checked). Fueter–Pólya 1923, Lew–Rosenberg 1978, Vsemirnov 2001
  (bibliographic data checked against Nathanson 2016, *Amer. Math. Monthly* 123,
  1001–1012, arXiv:1512.08261).
- **turing-machines.** Turing 1936; Post 1936; Kleene IM §67 (title and page of §67
  checked in the table of contents; the $y+1$ tallies are from memory, *not checked*
  against the text); Soare §1.4 (checked); Boolos–Burgess–Jeffrey ch. 3 (*not checked*, no
  copy); Radó 1962 (*not checked*, standard reference); bbchallenge 2025 (checked on arXiv:
  $S(5) = 47\,176\,870$, Coq proof).
- **programming-turing-machines.** Turing 1936 (skeleton tables); Soare §1.4;
  Boolos–Burgess–Jeffrey ch. 3.
- **multitape-machines.** Hartmanis–Stearns 1965 (quadratic simulation); Sipser ch. 3
  (*not checked*, no copy).
- **register-machines.** Shepherdson–Sturgis 1963; Minsky 1967; Cutland 1980 (*not
  checked*, no copy); Monin–Patey for the other variants (Melzak, Lambek, Elgot–Robinson).
- **primitive-recursion.** Dedekind 1888, Skolem 1923, Gödel 1931, Kleene 1936: as in
  Soare §§17.2.1–17.2.2 (checked); Downey–Hirschfeldt §2.8 (checked); Péter 1951;
  Odifreddi I.
- **coding-sequences.** Gödel 1931 (β-function, prime powers); Soare §17.2.2 (prime power
  coding used by Gödel and Kleene, checked); Péter 1951; Kleene 1952.
- **ackermann-function.** Ackermann 1928; Péter 1935; Robinson 1948; Grzegorczyk 1953;
  Soare §17.2.3 (checked; it attributes the two-argument function to Hermes's reduction of
  Ackermann's idea, while the course follows the usual attribution to Péter in Robinson's
  form); Monin–Patey, chapter "Church–Turing thesis" (checked).
- **mu-recursion.** Kleene 1936 (*General recursive functions*); Kleene 1938 (*On notation
  for ordinal numbers*, partial functions: Soare §17.2.4, checked); Kleene IM chapters XI–XII
  (titles checked in the table of contents); Soare §17.2; Monin–Patey.
- **loop-programs, while-programs.** Meyer–Ritchie 1967; Böhm–Jacopini 1966; Harel 1980;
  Wang 1957 and Péter 1958 (data from the Monin–Patey bibliography); Monin–Patey. The
  identity $\mathcal L_n = \mathcal E^{n+1}$ ($n \geq 2$) of Meyer–Ritchie is *not checked*.
- **lambda-calculus.** Church–Rosser 1936; Curry–Feys 1958; Barendregt 1984 (chapter
  numbers removed, *not checked*); Takahashi 1995 (bibliographic data checked).
- **lambda-programming.** Kleene 1981 (*Origins of recursive function theory*) for the
  predecessor; Turing 1937 (*The p-function*); Barendregt; Hindley–Seldin.
- **lambda-definability.** Kleene 1936 (*λ-definability and recursiveness*); Barendregt;
  Hindley–Seldin.
- **equivalence-of-models.** Kleene 1936; Turing 1937 (*Computability and λ-definability*);
  Soare §1.5 (checked); Monin–Patey (checked); Cutland 1980 and Odifreddi 1989 chapter I
  (*not checked*, no copy).
- **church-turing-thesis.** Turing 1936 §9; Kleene IM §62 (checked in the table of contents);
  Gandy 1980 and Sieg 2009 (data checked in Soare's bibliography); Soare §1.1 and §§17.2–17.3
  (checked); Monin–Patey; Gurevich 2000; Dershowitz–Gurevich 2008; Shor 1997;
  Accattoli–Dal Lago 2016 (bibliographic data checked).

## 9. Recent literature

Checked on 2026-11-12:
- **Fueter–Pólya.** Vsemirnov (2001) gave an elementary proof of the uniqueness of the
  quadratic pairing polynomials, presented by Nathanson (2016), who also records that
  Lew–Rosenberg (1978) excluded degrees 3 and 4 and that higher degrees are open. Added to
  the notes and to the solution of the first exercise of `what-is-an-algorithm`.
- **Busy beaver.** The value $S(5) = 47\,176\,870$ was determined by the bbchallenge
  Collaboration (arXiv:2509.12337, 2025), with a proof checked in Coq. Added as a remark to
  the notes of `turing-machines`, as an illustration that small machines are hard to
  analyze; the busy beaver function itself belongs to `fundamentals`.
- No recent work changes the presentation of the equivalence proofs; the classical proofs
  are kept.
- **Parallel reduction.** Takahashi (*Information and Computation* 118, 1995) proves
  Church–Rosser with the complete development $M^*$ (triangle property) and standardization
  with parallel reductions. Credited in `lambda-calculus`; a complete proof of
  standardization along these lines is the natural way to remove the last admitted theorem.
- **Cost of β-reduction.** Accattoli and Dal Lago (*LMCS* 12(1), 2016) show that the number
  of normal-order steps to normal form is a reasonable cost model. Added to the extended
  thesis in `church-turing-thesis`.
- **Axiomatizations of algorithms.** Gurevich (*ACM TOCL* 1, 2000) and Dershowitz–Gurevich
  (*BSL* 14, 2008) derive the thesis from postulates on sequential algorithms. Added to
  `church-turing-thesis`, with the remark that the informal content moves into the
  postulates.
- Nothing recent changes the results on the Ackermann function, minimization or LOOP/WHILE
  programs.

## 10. Open points

- Kleene IM §67: confirm the $y + 1$ tallies against the text, and the convention of
  Boolos–Burgess–Jeffrey chapter 3 (positive integers in monadic notation, clean final
  configuration).
- Possible figure: a flow diagram of a URM program.
- The standardization theorem is admitted. A proof (Takahashi's) would need about one lesson,
  possibly as an appendix lesson or an exercise sequence.
- `lambda-programming` is short (about 20 minutes); it could receive more exercises
  (lists, Scott numerals) if it seems too light.
- `equivalence-of-models` is at the limit (about 50 minutes). Its parts depend on each other
  (the coding of configurations is used by the normal form and the universal function), so
  it was not split.
- Not checked: Odifreddi chapter I, Cutland, Hindley–Seldin, and the Meyer–Ritchie identity
  $\mathcal L_n = \mathcal E^{n+1}$.
- A specialized course on subrecursive hierarchies (Grzegorczyk, fast-growing hierarchy,
  provably total functions) would continue `ackermann-function` and `while-programs`.

## 11. History

- **2026-11-12.** Design revision of lessons 1–6 and creation of this log (the log covers the
  whole course; lessons 8–16 were revised separately the same day, see below).
  - The multi-tape part of `programming-turing-machines` became a new lesson
    `multitape-machines` ("Variants of Turing machines"): the old lesson was over the length
    limit, and the robustness of the model deserves its own lesson, introducing simulation
    as a technique. Labels `def-multitape` and `thm-multitape-simulation` moved with it, unchanged.
    New: a linear 2-tape doubling machine (`ex-two-tape-doubling`) and the folding exercise
    (`ex-one-way-tape`).
  - New figures (generator `scripts/figures/models-of-computation.py`, section "lessons 2-6"):
    run of the successor machine, rounds of the doubling machine, register layout for
    composition, derivation tree of multiplication, course-of-values recursion.
  - New examples: `ex-bijective-numeration`, `ex-tm-identity`, `ex-beta`, partial functions,
    a code and its decoding, a derivation spelled out, standard form.
  - Techniques named where they first occur: arithmetization, invariants, simulation,
    induction on derivations.
  - References checked against Soare and Downey–Hirschfeldt and completed; recent
    literature on Fueter–Pólya and the busy beaver added.
  - Durations recomputed as words/55 rounded to 5, counting each formula as one word and
    excluding SVG and table rules.
- **2026-11-12.** Design revision of lessons 8–16 (formerly 7–13), merged into this log.
  - Splits: `while-programs` → `loop-programs` + `while-programs`; the former
    `lambda-definability` → `lambda-programming` + `lambda-definability`, with the section on
    head reduction moved there from `lambda-calculus`. All labels kept. Labels that moved:
    to `loop-programs`: `def-loop-while-syntax`, `def-loop-while-semantics`,
    `def-loop-while-computes`, `prop-loop-total`, `thm-loop-pr`; to `lambda-programming`:
    `def-church-numerals`, `def-lambda-definable`, `prop-church-arithmetic`,
    `def-lambda-booleans`, `prop-lambda-pred`, `thm-lambda-fixed-point`; from
    `lambda-calculus` to `lambda-definability`: `def-head-normal-form`,
    `lem-head-normal-order`, `lem-head-context`.
  - The partial case of λ-definability is now proved from standardization alone (new
    `lem-head-normal-order`, `lem-head-context`, `lem-numeral-head`); the substitution lemma
    became `lem-substitution`.
  - New figures (generator sections 6–11): `mu-search`, `loop-urm`, `k-omega`, `lambda-pred`,
    `tm-configuration-code`, `equivalence-cycle`. New example `ex-ack-stack`, table of
    Ackermann values, new quizzes on head reduction and on Turing's analysis.
  - Corrections: partial recursive functions dated to Kleene 1938; Soare citations in the
    thesis lesson (§1.1, §§17.2–17.3); Barendregt chapter numbers removed; `prop-urm-tm` stated
    with the tape conventions of `def-multitape`, and `multitape-machines` made a prerequisite
    of `equivalence-of-models`.
  - Recent literature: Takahashi 1995, Accattoli–Dal Lago 2016, Gurevich 2000,
    Dershowitz–Gurevich 2008.
  - Durations recomputed with the convention above: 45, 35, 30, 30, 40, 20, 40, 50, 30.
