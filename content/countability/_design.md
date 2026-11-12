# Design log: Countability and diagonalization

## 1. Objectives

After the course, a student can:

- compare sets by injections, surjections and bijections, and prove equipotence with
  Cantor–Bernstein by exhibiting two injections;
- show that the sets built from integers by finite means are countable, by listings
  with repetitions, dovetailing and coding, and say where choice is used;
- run a diagonal argument in its general form (Lawvere), and apply it to $2^\mathbb N$,
  $\mathbb N^\mathbb N$, power sets and $\mathbb R$;
- compute with the standard codings of Cantor space ($X \oplus Y$, $\bigoplus_n X_n$,
  unary coding of Baire space) and prove that the usual uncountable sets have the
  cardinality of the continuum;
- diagonalize effectively (against uniformly computable lists, against $\Phi_e$),
  explain why partial functions escape diagonalization, and prove the undecidability
  of the halting set;
- organize a construction as a list of requirements met by finite extensions.

**Role in the track.** Second course of the computability track (after models of
computation, before fundamentals). `tracks-design.md` assigns it the first technique
of the track: diagonalization. The course also introduces the objects and codings used
without comment afterwards: Cantor space, strings, prefixes, the pairing function,
joins, principal functions, and the finite extension method, which the Turing degrees
course takes up (`turing-degrees/finite-extensions`).

## 2. Prerequisites assumed

- Lessons 1–6: naive set theory (functions, images, induction on $\mathbb N$), real
  numbers as a complete ordered field, decimal and binary expansions, primes and unique
  factorization. No logic.
- Lessons 7–8: from `models-of-computation`, the universal function
  (`cor-universal-function`), the numbering $\Phi_e$, closure of partial computable
  functions under composition and $\mu$, and the diagonal argument against primitive
  recursive functions (`thm-pr-diagonal`).

## 3. Results

1. **Equipotence** (`equipotence`): left and right inverses; equipotence is an
   equivalence; pigeonhole principle; finite sets are not equipotent to proper subsets;
   subpotence is a preorder compatible with equipotence; surjections from subsets of
   $\mathbb N$ give injections back.
2. **Cantor–Bernstein** (`cantor-bernstein`): the lemma for $B \subseteq A$; the
   theorem; the explicit bijection and König's chains; role of choice and of excluded
   middle; Myhill's isomorphism theorem mentioned.
3. **Countable sets** (`countable-sets`): principal function of an infinite subset of
   $\mathbb N$; three characterizations; subsets and images; $\mathbb N$ is the smallest
   infinity (dependent choice); Dedekind-infinite sets.
4. **Countable constructions** (`countable-constructions`): Cantor pairing; products and
   $\mathbb N^k$; $\mathbb Z$, $\mathbb Q$; unions with given enumerations; strings over a
   countable alphabet; finite subsets of $\mathbb N$; algebraic numbers.
5. **The diagonal argument** (`diagonal-argument`): $2^\mathbb N$ uncountable; diagonal
   lemma and Lawvere's fixed point theorem; Baire space; Cantor's theorem on power sets;
   Russell; $\mathbb R$ uncountable by decimal digits.
6. **The continuum** (`continuum`): $|\mathbb N^\mathbb N| = |2^\mathbb N|$; joins and
   countable joins; $2^\mathbb N$, $\mathcal P(\mathbb N)$, $\mathbb N^\mathbb N$,
   $[0,1]$, $\mathbb R$ equipotent; $\mathbb R^2$, $\mathbb R^\mathbb N$; removing a
   countable set; Cantor set (admitted facts); CH and its independence (admitted).
7. **Diagonalization and computation** (`diagonalization-and-computation`): counting;
   effective diagonalization; $\mathrm{Tot}$ not computable; $\Phi_e(e) + 1$ has no total
   computable extension; halting set not computable.
8. **Diagonalization by requirements** (`requirements`): finite extension lemma;
   sequences differing infinitely often from each member of a list (computably so when
   the list is uniformly computable); bi-immune sets.

## 4. Proof techniques

- **Diagonalization**, in its four forms: Cantor's (L5), the general diagonal lemma and
  its fixed point reading (L5), effective diagonalization (L7), diagonalization against
  partial functions yielding a divergence point (L7).
- **Least element instead of choice** (L1 remark, L3, L8): the device that makes
  constructions over $\mathbb N$ explicit, and later computable.
- **Back-and-forth along chains / iteration of an injection** (L2).
- **Dovetailing** (L4), named there and linked to `prop-selection` in fundamentals.
- **Coding** of finite objects by integers (prime powers, pairing, binary sums: L4) and
  of sequences of sequences by one sequence (joins, unary coding: L6).
- **Two injections and Cantor–Bernstein** as the standard way to prove equipotence (L2,
  L6).
- **Finite extensions** with requirements, and splitting an infinitary requirement into
  finitary ones (L8). The lesson names forcing and priority as the next steps.

## 5. Choices

- **Set theory before computation.** The course starts from sets, without computability,
  because the diagonal argument and the codings are clearer without it; computation
  enters in the last two lessons. This follows the order of Monin–Patey (chapter
  *Cantor's infinity* before *Foundations of computability*).
- **Choice made explicit.** Each use of choice (countable unions, $\mathbb N$ smallest
  infinity, surjections) is signaled, and the least-element device shows how to avoid
  it over $\mathbb N$. Reason: the same device is what makes constructions computable.
- **Countable unions with given enumerations.** The proposition takes the enumerations as
  data, rather than invoking countable choice. Feferman–Lévy is mentioned and admitted.
- **Lawvere's form** of the diagonal argument is included because Kleene's fixed point
  theorem in fundamentals has the same shape.
- **Real numbers by digits 4/5** rather than Cantor's 1874 nested intervals (which is an
  exercise): it shows the care needed with double expansions.
- **Codings in Cantor space** ($\oplus$, $\bigoplus$, unary coding) are proved here because
  every later course uses them.
- **Excluded:** ordinals and cardinal arithmetic beyond comparisons (not needed in the
  track; the higher computability track treats ordinals); proofs of independence results
  (CH, Feferman–Lévy, Cohen's Dedekind-finite set), admitted with references; topology of
  Cantor space (in `pi01-classes`); Hartogs and Zermelo's theorems (admitted).
- **Split of two lessons (2026-11-12).** `countable-sets` (3100 words) was split into
  `countable-sets` (characterizations, smallest infinity) and `countable-constructions`
  (pairs, unions, strings, algebraic numbers); `diagonalization-and-computation` (3200
  words) into itself and `requirements` (finite extensions). Each half has one theme and
  fits the 25–45 minute range; the finite extension method gets its own lesson since the
  Turing degrees course builds on it.
- **Not split:** `equipotence` and `diagonal-argument` remain at about 3000 words
  (duration 55 by the word-count rule, which counts LaTeX tokens). Their parts are tightly
  linked (finite sets are needed for subpotence; Cantor's theorem on power sets is the
  general lemma applied). See open points.

## 6. Comparison with the literature

- **Monin–Patey**, chapter *Cantor's infinity* (sections *Equipotence and subpotence*,
  *Cantor–Bernstein's theorem*, *Countable sets*, *Cantor's diagonal argument*,
  *Non-computable reals*, *Cantor space*): the same material at a lighter level. The
  course adds full proofs of the finite-set facts, the explicit bijection and chains,
  the role of choice, Lawvere's lemma, the codings $\oplus$ and $\bigoplus$, the removal of
  countable sets, and the computational lessons. Monin–Patey's finite extension method
  is in the chapter *Turing degrees*, section *Finite extensions method*.
- **Soare (2016)**: §1.1.2 (the obstacle of diagonalization and partial functions, used
  in L7), §1.7.1 (Myhill isomorphism theorem, mentioned in L2), §6.1 (Kleene–Post
  finite extensions, L8). Soare does not treat cardinality.
- **Hrbacek–Jech** and **Jech, *The Axiom of Choice***: set-theoretic background,
  independence results admitted in L2, L3, L4.
- **Downey–Hirschfeldt** §7.2.4: bi-immune sets (defined with c.e. sets; the lesson notes
  the equivalence with computable sets).
- Difference in emphasis: the course treats cardinality as preparation for computability,
  and keeps every argument explicit enough to be effectivized later.

## 7. Pedagogical plan

- **L1.** Galileo's paradox (figure: matching of $n$ with $n^2$). Example of
  injective/surjective maps on $\mathbb N$ and dependence on the codomain. Pigeonhole:
  intuition (remove the last hole and the last pigeon after an exchange). Counterexample
  in the quiz: surjection then injection gives nothing.
- **L2.** Figure of the sets $C_n$; example on $[0,1]$ and $[0,1)$; intuition
  (transport $B$ into $A$); figure of the three kinds of chains; counterexample for ordered
  and topological structure ($[0,1]$ versus $(0,1)$); constructive status (excluded
  middle) and Myhill's theorem as the effective analogue.
- **L3.** Examples of countable sets right after the definition; figure of first
  occurrences (listing with repetitions → injection); intuition for the smallest
  infinity; exercise on $|A \cup B| = |A|$.
- **L4.** Intuition for diagonal enumeration (rows fail, diagonals work), named
  dovetailing; pairing figure; ordering roots to avoid choice; new exercise on
  $2^x(2y+1) - 1$.
- **L5.** Examples of sets as sequences; diagonal table figure; three quizzes on why
  distinct positions, robustness, a worked case; reals with the 4/5 digits and the
  counterexample with 9s.
- **L6.** Unary coding figure; join figure (new); intuition for removing a countable
  set (room in columns); Cantor set figure.
- **L7.** Soare's three incompatible wishes motivate partial functions; figure of the
  table of $\Phi_e(x)$ with divergences and the row $\Phi_c = d$ (new); example of a
  sequence of computable functions that is not uniformly computable.
- **L8.** Intuition (maintain a finite string, secure each requirement); "secures"
  with an example; figure of the stages $\sigma_1 \prec \sigma_2 \prec \cdots$ (new);
  counterexamples to the hypothesis of the lemma (an unsecurable requirement, two
  conflicting ones) and the remedy by splitting; link to dense sets in the Turing
  degrees course.

Figures are generated by `scripts/figures/countability.py` (keys `galileo`, `cb-bands`,
`cb-chains`, `pairing`, `first-occurrences`, `diagonal`, `code-baire`, `join`,
`cantor-set`, `partial-table`, `finite-extension`).

## 8. Sources

- **L1:** Galileo, *Discorsi* (1638), First Day; Cantor 1878 (Crelle 84); Dedekind 1888;
  Hrbacek–Jech; Monin–Patey, *Equipotence and subpotence*.
- **L2:** Borel 1898, Note I (Bernstein's proof); König 1906 (CRAS 143); Hartogs 1915
  (Math. Ann. 76); Jech 1973; Pradic–Brown, arXiv:1904.09193; Soare §1.7.1 (Theorem
  1.7.4, Myhill); Monin–Patey, *Cantor–Bernstein's theorem*.
- **L3:** Dedekind 1888; Jech 1973 (Cohen's model with an infinite Dedekind-finite set of
  reals); Hrbacek–Jech; Monin–Patey, *Countable sets*.
- **L4:** Cantor 1874 (Crelle 77); Gray 1994 (Amer. Math. Monthly 101); Feferman–Lévy
  1963 via Jech 1973; Monin–Patey, *Countable sets*.
- **L5:** Cantor 1891 (Jahresber. DMV 1); Lawvere 1969 (LNM 92); Yanofsky 2003 (BSL 9);
  Russell 1903; Gray 1994; Normann–Sanders 2022 (JSL 87); Monin–Patey, *Cantor's diagonal
  argument*.
- **L6:** Cantor 1878; Gödel 1938; Cohen 1963; Kunen 1980; Jech 2003; Kechris 1995;
  Monin–Patey, *Cantor space*.
- **L7:** Turing 1936; Soare §1.1.2; Rogers 1967; Odifreddi 1989; Monin–Patey, *Non-computable
  reals*.
- **L8:** Kleene–Post 1954; Friedberg 1957; Muchnik 1956; Jockusch 1969 (bi-immune
  degrees); Soare §6.1; Monin–Patey, chapter *Turing degrees*, *Finite extensions method*;
  Downey–Hirschfeldt §7.2.4.

Checked against the books on 2026-11-12: Monin–Patey section titles (LaTeX sources);
Soare §1.1.2 (pp. 4–5), §1.7.1 (Theorem 1.7.4), §6.1 (p. 131); Downey–Hirschfeldt §7.2.4
and its reference [186] for Jockusch 1969. The bibliographic data of the original papers
(Cantor, Dedekind, König, Hartogs, Gödel, Cohen, Turing, Kleene–Post) were not checked
against the books, which do not all cite them; they agree with the standard data.

## 9. Recent literature

Checked on 2026-11-12:

- **Pradic and Brown (arXiv:1904.09193, 2019; revised 2022):** in constructive set
  theory, Cantor–Bernstein implies excluded middle. Added to L2: the proof is explicit and
  choice-free, but not constructive.
- **Normann and Sanders, *On the uncountability of ℝ*, JSL 87 (2022):** "no injection
  $[0,1] \to \mathbb N$" for arbitrary third-order functions is not provable in
  $\mathsf Z_2^\omega$. Added as a note in L5.
- **Gray (1994):** Cantor's 1874 argument is constructive; cited in L4 and L5 (older than
  fifteen years, but the standard reference on this point).
- **Lawvere/Yanofsky:** the categorical diagonal lemma was already in the course.

No simpler proof of the core results was found; none of the course's statements were
affected.

## 10. Open points

- `equipotence` and `diagonal-argument` exceed 2700 words. A possible split of
  `diagonal-argument`: "The diagonal argument" (Cantor space, the theorem, the general
  lemma) and "Power sets and the real line". Not done, to keep the general lemma next to
  its main applications.
- The exercise on $\mathrm{Tot}$ in L7 refers forward to `prop-ce-range` of fundamentals,
  and L4 refers forward to `prop-selection`; these are pointers, not dependencies.
- `turing-degrees/finite-extensions` lists `countability/diagonalization-and-computation`
  as prerequisite; it should now list `countability/requirements`.
- The Cantor set facts (homeomorphism with $2^\mathbb N$) are admitted; a proof could be
  added if `pi01-classes` does not give one.

## 11. History

- **2026-11-12.** Design and pedagogy revision. Split `countable-sets` into
  `countable-sets` and `countable-constructions`, and `diagonalization-and-computation`
  into `diagonalization-and-computation` and `requirements`; all labels kept (moved with
  their statements). New figures: first occurrences (L3), join (L6), table of partial
  functions (L7), stages of a finite extension construction (L8). New examples
  (`ex-injective-surjective`, `ex-countable-sets`), intuitions before the pigeonhole
  proof, the Cantor–Bernstein proof, the smallest infinity, pairing (dovetailing), the
  removal of countable sets, partial functions and finite extensions. New remarks on
  structure (Cantor–Bernstein fails for orders and topology), excluded middle
  (Pradic–Brown) and Myhill's isomorphism theorem. New exercises: $|A \cup B| = |A|$,
  removal of a finite set, $2^x(2y+1) - 1$, bi-immune sets are not computable. New label
  `ex-no-uniform-computable-sets`, `ex-bi-immune`. Monin–Patey, Soare, Gray,
  Pradic–Brown, Normann–Sanders and Jockusch added to the references. Durations recomputed
  from word counts.
