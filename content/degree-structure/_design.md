# Design log: Structure of the Turing degrees

## 1. Objectives

After the course, a student can:

- describe $\mathcal D$ as a partial order: upper semilattice, countable lower cones, uncountable upper cones, no lattice, no least upper bounds of strictly increasing sequences;
- build an exact pair for a countable ideal by finite extensions with locked columns;
- embed every countable partial order into the degrees below $\mathbf 0'$, through an independent sequence and a computable universal partial order, and build an antichain of size continuum by a perfect tree of finite extensions;
- build a minimal degree by forcing with computable function trees (Spector), explain the construction as a forcing whose conditions decide for all their paths whether a functional loses information, and analyze its effectivity ($\emptyset''$);
- relativize the construction, including with a growing oracle: minimal covers, minimal upper bounds of strictly increasing sequences;
- recognize classes of degrees without minimal elements: c.e., 1-generic, PA degrees, members of a $\Pi^0_1$ class of c.e. degree.

**Role.** Specialized course (`tracks-design.md`: "Kept specialized"), corresponding to Soare Part III and the structural parts of Soare Chapter 6. It is the reference course for **forcing with perfect trees** in the degree-theoretic setting; the specialized course `effective-forcing` (written in parallel, November 2026) cites the minimal degree construction as its example of forcing with perfect trees. The labels most likely to be cited are `thm-minimal-degree`, `lem-splitting-dichotomy`, `lem-splitting-consequences`, `def-e-splitting`, `lem-relativized-splitting`, `thm-exact-pair`, `cor-not-lattice` (cited by `turing-degrees/turing-reducibility` and `infinite-injury/minimal-pairs`).

## 2. Prerequisites assumed

- Turing reducibility, degrees, join, jump, countability of lower cones (`turing-degrees`: `prop-degree-countable`, `prop-join-lub`, `thm-jump`).
- Finite extensions and the Kleene–Post theorem (`thm-kleene-post`), 1-generic sets and their existence below $\emptyset'$ (`def-1-generic`, `prop-1-generic`).
- Function trees and forcing with computable perfect trees as introduced for computably dominated sets (`immunity-growth/computably-dominated`: `def-function-tree`, `ex-ftree`, `lem-ftree-noncomputable`, `lem-ftree-domination`, `thm-martin-miller-ftrees`); domination of the computation function (`thm-computation-function`).
- No minimal c.e. degree (`ce-degrees/sacks-splitting`, `cor-no-minimal-ce`).
- PA degrees and $\mathrm{DNC}_2$ (`pi01-classes/pa-degrees`, `thm-pa-characterization`; `thm-dnc2-no-computable`); emptiness of $\Pi^0_1$ classes (`prop-pi01-emptiness`).

## 3. Results, lesson by lesson

1. **exact-pairs.** Elementary properties (`prop-degrees-elementary`); ideals and examples (`ex-ideals`: principal, arithmetic, a non-ideal); exact pairs (`def-exact-pair`); Spector's exact pair theorem for countable ideals (`thm-exact-pair`); no least upper bound of strictly increasing sequences, $\mathcal D$ not a lattice (`cor-not-lattice`). Exercises: arithmetic degrees; $G, H \leq_T (\bigoplus A_n)'$; every upper bound is half of an exact pair (Soare Ex. 6.5.11).
2. **embeddings.** Computable independence (`def-independent`); columns of a 1-generic set are independent (`thm-generic-independent`); extension property and universality (`lem-extension-universal`), a computable universal partial order (`lem-computable-universal`); every countable partial order embeds below $\mathbf 0'$ (`thm-embedding`); an antichain of size continuum (`thm-continuum-antichain`). Exercises: embedding of the computable subsets; no 1-generic degree is minimal (`ex-generic-not-minimal`).
3. **minimal-degrees.** Minimal degrees (`def-minimal-degree`); $e$-splits and $e$-splitting trees (`def-e-splitting`); the dichotomy (`lem-splitting-dichotomy`) and its consequences (`lem-splitting-consequences`); Spector's theorem (`thm-minimal-degree`), with the forcing reading; Sacks's minimal degree below $\mathbf 0'$ (admitted). Exercises: a computably dominated minimal degree; outputs on a tree avoiding splits.
4. **minimal-covers** (new, 2026-11-12). Relativized splitting (`lem-relativized-splitting`); minimal covers (`def-minimal-cover`, `thm-minimal-cover`, moved from lesson 3); strong minimal covers (mentioned); minimal upper bounds (`def-minimal-upper-bound`, `thm-minimal-upper-bound`, Sacks); no PA degree is minimal (`prop-pa-not-minimal`). Exercises: no $\Pi^0_1$ class of minimal degrees and continuum many minimal degrees (moved from lesson 3); the Posner–Epstein non-computability lemma. Admitted: continuum many minimal upper bounds, Groszek–Slaman, Yates–Cooper, Kumabe–Lewis, Jockusch–Posner, Lachlan–Lebeuf, Martin and Paris on degrees bounding minimal degrees.

## 4. Proof techniques

| Technique | Where | Introduced in |
| --- | --- | --- |
| Finite extensions with restricted conditions (locked columns) | exact-pairs (`thm-exact-pair`) | turing-degrees/finite-extensions |
| Genericity giving independence (flipping a bit of one column) | embeddings (`thm-generic-independent`) | turing-degrees/finite-extensions |
| Greedy embedding through an extension property (Fraïssé-style) | embeddings (`lem-extension-universal`, `lem-computable-universal`) | here |
| Coding by columns, with a computable index set | embeddings (`thm-embedding`) | here |
| Perfect trees of finite extensions (continuum many sets) | embeddings (`thm-continuum-antichain`), minimal-covers (exercise) | immunity-growth (exercise) |
| Forcing with computable perfect trees (Sacks forcing); splitting/non-splitting dichotomy | minimal-degrees | immunity-growth/computably-dominated (domination dichotomy) |
| Effectivity analysis of a forcing construction ($\Sigma^0_2$ case distinction) | minimal-degrees, exact-pairs (exercise) | turing-degrees |
| Relativization of tree forcing; coding a set into the branching of a tree; growing oracle | minimal-covers | here |
| Nested $\Pi^0_1$ classes of relative DNC functions | minimal-covers (`prop-pa-not-minimal`) | pi01-classes/pa-degrees |

## 5. Choices

- **Four lessons instead of three** (2026-11-12). The minimal degree lesson, with intuition, a figure and the forcing reading, would have exceeded 50 minutes with minimal covers and the exercises. The relativizations form a coherent second lesson: one lemma (relativized splitting) and two theorems (minimal covers, minimal upper bounds), followed by the classes without minimal degrees. `thm-minimal-cover` moved to the new lesson; no other course cited it.
- **Minimal upper bounds added.** They complete the picture of lesson 1 (an increasing sequence has no least upper bound, but has minimal ones) and teach a new technique, forcing with trees whose oracle grows, which is the basis of Sacks's and later constructions. The proof is short given the relativized lemma. Source: Soare Exercise 12.6.1 (Sacks).
- **PA degrees via relative DNC, not via randomness.** The previous version argued, in the notes, through a random set and van Lambalgen's theorem, which is in a course that is not a prerequisite (`randomness-notions`). The new proof (Monin–Patey, exercise) uses only `pi01-classes/pa-degrees` and is given in full.
- **Posner–Epstein lemma as an exercise.** It shows that the non-computability steps are redundant; it is instructive (a functional designed to be neither splitting nor non-splitting), but not needed for the main line.
- **Exact pairs for ideals, not only for sequences.** Kept from the previous version: it is the form used in coding arguments (Monin–Patey state it for ideals; Soare for ascending sequences with the ideal version as Exercise 6.5.12).
- **Universal partial order by the extension property.** Kept. Monin–Patey embed countable orders into $(\mathbb Q^2, \leq_{\mathrm{prod}})$; this is incorrect, since a product of two chains has order dimension at most 2 and the standard example $S_3$ has dimension 3 (see Open points). The extension-property construction is correct and also exhibits a reusable technique.
- **Sacks's minimal degree below $\mathbf 0'$ admitted.** Soare Chapter 13 needs partial trees and a finite injury construction; it would take a lesson of its own and teaches priority rather than forcing. Its idea is described in one paragraph.
- **Excluded.** Initial segment embeddings (Lerman's monograph; too long), the first-order theory of $\mathcal D$ and Slaman–Woodin definability (research level; mentioned), jump inversion for minimal degrees (Cooper), the full approximation method (Yates). Each is mentioned with a reference.
- **Order.** Exact pairs first (they only need finite extensions), embeddings second (genericity), minimal degrees last (trees); minimal covers and upper bounds after minimal degrees because they relativize it.

## 6. Comparison with the literature

- **Soare, *Turing Computability* (2016).** Section 6.1 (Kleene–Post finite extensions; Exercises 6.1.4–6.1.7: independent sequences, universal computable order, embedding below $\mathbf 0'$, $2^{\aleph_0}$ incomparable degrees); Section 6.5 (Theorem 6.5.3 Kleene–Post–Spector exact pairs for ascending sequences, Corollaries 6.5.4–6.5.5, Exercises 6.5.10–6.5.12); Part III, Chapter 12 (f-trees, e-splitting, e-black and e-white Lemmas 12.2.2–12.2.3, Posner–Epstein Lemma 12.2.1, Theorem 12.5.1, Exercises 12.6.1 minimal upper bounds and 12.6.2 continuum many minimal degrees), Chapter 13 (Sacks's minimal degree below $\mathbf 0'$). Soare uses partial f-trees and a colour terminology (e-black, e-white, e-gray); the course uses total trees and the "splitting / avoids splits" terminology of Monin–Patey, since only total trees are needed below $\emptyset''$.
- **Downey–Hirschfeldt (2010).** Section 2.4 (not a lattice, Kleene–Post), Section 2.17–2.18 (computably dominated sets, then Spector's theorem 2.18.2 with e-splitting trees; Yates–Cooper, Jockusch–Posner, Cooper stated). Same order as this course and `immunity-growth`.
- **Monin–Patey, chapter "Structure of the degrees"** (`structure-degres.tex`). Minimal degrees as Sacks-generic sets; minimal covers and strong minimal covers; Kleene–Post semilattice properties; Sacks's minimal upper bounds; exact pairs for countable sets closed under join, by a forcing with locked columns; embeddings; initial segments; first-order theory. The course follows their forcing reading and their exercise on PA degrees, and differs on the universal order (see above).
- **Lerman (1983)** is the reference for initial segments and the global theory; it was not available as a text file and is cited only for what it is known to contain.

## 7. Pedagogical plan

- **exact-pairs.** Example of ideals (principal, arithmetic, a union of cones that is not an ideal); why a non-principal ideal cannot be described by one degree; idea of the proof before it (diagonalize or else search among admissible extensions; the obstacle is the locked columns); figure of locked columns (`locked-columns`); three quiz questions; remark that a single upper bound does not suffice; counterexample for strictness in the corollary.
- **embeddings.** Why order preservation alone is trivial; examples of non-independent sequences; the idea of genericity (flip a bit of column $i$); why a computable universal order is needed; $(\mathbb Q, <)$ and an antichain lack the extension property; figure of the coding on the diamond (`diamond`); figure of the tree of strings for the antichain (`antichain`); technique named (perfect trees of finite extensions).
- **minimal-degrees.** Why finite extensions cannot give a minimal degree; examples of non-minimal degrees; examples of the two extreme functionals (identity, constant); figure of a splitting tree with decoding and of a tree avoiding splits (`splitting`); why the trees must be computable; the forcing reading (conditions, extension, dense families); why $\emptyset''$; the Sacks construction described.
- **minimal-covers.** Relativized lemma with the role of the oracle; the jump is never a minimal cover; idea of the minimal upper bound proof (growing oracle); coding subtrees; quiz on the role of $B_e$; the PA proof; the measure and category results for contrast.

## 8. Sources (checked against the books, 2026-11-12)

- exact-pairs: Kleene–Post 1954; Spector 1956; Soare §6.5 (Thm 6.5.3, Cor 6.5.4–6.5.5, Ex 6.5.10–6.5.12, checked); Downey–Hirschfeldt §2.4 (Kleene–Post credited with "not a lattice", checked); Monin–Patey, structure chapter (exact pairs, checked); Simpson 1977.
- embeddings: Soare §6.1, Ex 6.1.4–6.1.7 (checked); Shore 1997, AML 36, 233–253 (checked: countable embedding by Kleene–Post methods; Sacks's results on $\aleph_1$; Sacks's embedding conjecture open; Groszek–Slaman independence); Shoenfield 1960, PAMS 11, 61–62 (uncountable antichain with Zorn's lemma, checked through Soare's bibliography and the JSTOR description of Sacks's book); Sacks 1963 (continuum antichain without choice, crediting Lacombe; same source); Sacks 1961, Z. Math. Logik 7, 46–56 (bibliographic data from the Monin–Patey bibliography).
- minimal-degrees: Spector 1956; Shoenfield 1966 JSL 31, 539–544; Soare Ch. 12–13 (checked); Downey–Hirschfeldt §2.18, Thm 2.18.2 and footnote on Shoenfield's book (checked); Sacks 1961 Bull. AMS 67, 416–419 (checked against the AMS listing and Monin–Patey); Yates 1970 JSL 35, 243–266 and Cooper 1972 Ann. Math. Logic 4, 31–73 (checked in the Downey–Hirschfeldt bibliography).
- minimal-covers: Soare Lemma 12.2.1 (Posner–Epstein) and Ex 12.6.1 (Sacks) (checked); Monin–Patey (minimal covers, strong minimal covers, Ishmukhametov, Lewis survey, PA exercise, Groszek–Slaman 1997 APAL 87, Kumabe–Lewis 2009, Khan–Miller 2017; checked against their bibliography); Jockusch–Posner 1978 JSL 43, 715–724 (Downey–Hirschfeldt bibliography); Lachlan–Lebeuf 1976 JSL 41, 289–300 (Shore 1997); Martin (meager) and Paris (measure zero) on degrees bounding minimal degrees, as reported by Shore 1997.

## 9. Recent literature

- **Checked:** Khan and Miller, *Forcing with bushy trees*, Bull. Symb. Logic 23 (2017): a simpler, forcing-style presentation of Kumabe's minimal DNC degree (Kumabe–Lewis 2009). Cited in the notes of `minimal-covers`; it does not change the proofs of the course, which do not cover DNC minimal degrees.
- **Checked:** Monin–Patey (book in preparation) present minimal degrees as generics for computable Sacks forcing; the course adopts this reading in a paragraph of `minimal-degrees`.
- **Checked:** Barmpalias, Day and Lewis, *The typical Turing degree* (arXiv:1111.1064), a programme on measure- and category-typical degrees. Not used: the course only mentions the older results of Martin and Paris, through Shore 1997.
- **Checked:** Sacks's embedding conjecture (every partial order of size continuum with the countable predecessor property embeds into $\mathcal D$) is still described as open by Monin–Patey; no solution was found.
- Not found: a simpler proof of the exact pair theorem or of Spector's theorem than those given.

## 10. Open points

- **Monin–Patey error (outside this course).** Their proof of the countable embedding theorem embeds every countable partial order into $(\mathbb Q^2, \leq)$ with the product order. This is false: such an order has dimension at most 2, while the standard example $S_3$ ($a_i < b_j$ iff $i \neq j$, $i, j \leq 3$) has dimension 3. To report to the authors of the book.
- Lerman's monograph could not be checked; it is cited only generically.
- Shoenfield 1960 and Sacks 1963 were not read directly; attributions rest on Soare's bibliography, the JSTOR description of Sacks's book and Shore 1997.
- Durations: all four lessons are at 50 minutes (2650–2900 words), above the 45-minute target. A further split (for instance the antichain moved to a lesson with the embedding of larger orders) was not judged worthwhile.
- Possible addition: Sacks's minimal degree below $\mathbf 0'$ as a fifth lesson (partial trees, finite injury), if the course is extended.

## 11. History

- **2026-11-12.** Design and pedagogy revision. New lesson `minimal-covers` (relativized splitting, minimal covers moved from `minimal-degrees`, minimal upper bounds, PA degrees not minimal, Posner–Epstein exercise). Intuition paragraphs, examples and counterexamples added in all lessons; four figures generated by `scripts/figures/degree-structure.py` (locked columns, coding of the diamond, antichain tree, splitting trees). Attributions corrected: the continuum antichain (Shoenfield 1960 uncountable with choice; Lacombe and Sacks 1963 continuum without choice); the embedding theorem (Kleene–Post method, Sacks); Sacks's minimal degree below $\mathbf 0'$ described as a finite injury construction with partial trees (not "full approximation", which is Yates's method); Lerman's title completed; Soare section, theorem and exercise numbers added. The PA argument through randomness replaced by a self-contained proof. Exercises added: every upper bound is half of an exact pair; a computably dominated minimal degree; outputs on trees avoiding splits.
