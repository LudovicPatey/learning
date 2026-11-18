---
title: Computable models of theories
summary: Decidable structures and the elementary diagram; the effective completeness theorem, by which every complete decidable theory has a decidable model; every consistent computable theory has a model of low degree, and models in every PA degree; computable and decidable are different (Tennenbaum); a computable field in which irreducibility of polynomials is undecidable (Fröhlich, Shepherdson).
duration: 30
prerequisites: [presentations, pi01-classes/basis-theorems]
---

The first question about a structure is whether it has a computable copy. For structures given as models of a first-order theory, the completeness theorem provides models, and its proof, by Henkin's method, is a construction that can be made effective. This lesson shows how far it goes: a complete decidable theory has a model in which every first-order property is decidable; a theory with computable axioms has models of low degree, though not always a computable one. It ends with a classical example from algebra, where a computable field fails to decide a basic algebraic question, so that the copy chosen matters.

## Decidable structures

Besides the atomic diagram $D(\mathcal M)$ of an ω-presentation, consider its **elementary diagram** $D^c(\mathcal M)$, the set of first-order formulas $\varphi(x_0, \ldots, x_n)$, with the variables $x_j$ naming the elements $j$, that are true in $\mathcal M$. The presentation is **decidable** if $D^c(\mathcal M)$ is computable. A decidable presentation is computable, since atomic formulas are formulas, and its theory $\mathrm{Th}(\mathcal M)$, the set of sentences true in it, is computable. A theory $T$, a set of sentences closed under consequence, is **decidable** if it is a computable set.

:::example{#ex-decidable-structures}
1. The theory of dense linear orders without endpoints is complete and decidable, and the standard presentation of $(\mathbb Q; <)$ is decidable: by quantifier elimination, every formula is equivalent, computably, to a quantifier-free one.
2. The standard model of arithmetic $(\nat; +, \times)$ is computable, but its theory is not decidable, not even arithmetic. Computable and decidable are different notions.
3. The theory of algebraically closed fields of characteristic $0$ is complete and decidable (Tarski), by quantifier elimination; the field of algebraic numbers has a decidable presentation.
:::

## The effective completeness theorem

:::theorem{#thm-decidable-model}
Every complete decidable theory $T$ in a computable vocabulary has a decidable model, with an infinite or finite domain according to the models of $T$.
:::

**Intuition.** Henkin's proof builds a model out of names. Add infinitely many new constants, list all the sentences of the expanded language, and decide each one in turn, keeping the set of decisions consistent with $T$ and adding a witness constant each time an existential sentence is accepted. The model is made of the constants, two constants being identified when the decisions say they are equal. Every step requires a consistency test; when $T$ is complete and decidable, this test is computable.

:::proof{of=thm-decidable-model}
Let $C = \{ c_0, c_1, \ldots \}$ be new constants and $(\psi_n)$ an effective list of the sentences of the vocabulary with $C$. We build finite sets $S_0 \subseteq S_1 \subseteq \cdots$ of such sentences, each consistent with $T$.

*Consistency is decidable.* Let $S$ be finite, with constants among $c_0, \ldots, c_k$. Then $T \cup S$ is consistent if and only if $T \not\vdash \neg \exists x_0 \ldots x_k \bigwedge S(\bar x)$, where $\bigwedge S(\bar x)$ replaces each $c_i$ by $x_i$; this is the usual lemma on new constants. Since $T$ is complete, this holds if and only if the sentence $\exists \bar x \bigwedge S(\bar x)$ belongs to $T$, which is decidable.

*Construction.* Let $S_0 = \emptyset$. At step $n$, if $T \cup S_n \cup \{ \psi_n \}$ is consistent, add $\psi_n$, and if $\psi_n$ is of the form $\exists x\, \chi(x)$, add also $\chi(c)$ for the first constant $c$ not occurring in $S_n$ or $\psi_n$; this preserves consistency, since $c$ is new. Otherwise add $\neg \psi_n$, which is then consistent with $T \cup S_n$. Let $H = \bigcup_n S_n$, a computable set of sentences: whether $\psi_n \in H$ is decided at step $n$.

*The model.* $H$ is complete (it contains $\psi$ or $\neg\psi$ for every $\psi$), consistent with $T$, contains $T$ (every sentence of $T$ is consistent with $T \cup S_n$ and is added when listed), and has witnesses: if $\exists x\, \chi(x) \in H$, then $\chi(c) \in H$ for some $c$. Let $c \sim d$ if $c = d \in H$; it is a computable equivalence relation, compatible with the symbols. The quotient structure, interpreting each symbol as $H$ prescribes, satisfies, by induction on formulas, $\varphi(c_{i_1}, \ldots) $ if and only if $\varphi(c_{i_1}, \ldots) \in H$; the witness property handles existential quantifiers. So it is a model of $T$, and its elementary diagram, as a congruence presentation on $C$, is $H$, which is computable. Taking the least constant of each class gives a decidable presentation on a subset of $\nat$, or on $\nat$ if the model is infinite.
:::

:::quiz[the effective completeness theorem]
Where is the completeness of $T$ used?

- [x] In the consistency test: for a complete theory, $T \cup S$ is consistent exactly when the existential closure of $\bigwedge S$ belongs to $T$, a single membership question that the decidability of $T$ answers.
- [ ] To make the set $H$ complete.

  $H$ is complete for any $T$, since each sentence or its negation is added; completeness of $T$ makes the choice computable.
- [ ] To add the witnesses.

  Witnesses are added for any consistent set, by choosing a new constant.
:::

If $T$ is only computably axiomatizable and consistent, the same construction can be carried out relative to an oracle that decides consistency, and less is enough. The finite sets of decisions that are consistent with $T$ form a computable tree, after a standard pruning (Ash–Knight, Theorem 3.15): its paths are exactly the completions of $T$, and every completion yields a model as above.

:::corollary{#cor-low-model}
Every consistent computably axiomatizable theory has a completion of low degree, hence a model whose elementary diagram is low. More precisely, every PA degree computes a completion and a model, with elementary diagram computable in it.
:::

:::proof{of=cor-low-model}
The completions of $T$ are the paths of a computable binary tree; it has a low path by the low basis theorem (:ref{#thm-low-basis}), and every PA set computes a path, since a PA set computes a member of every non-empty $\Pi^0_1$ class (:ref{#def-pa-degree} and the course on $\Pi^0_1$ classes). A completion $\hat T$ is a complete theory decidable in its own degree, and the proof of :ref{#thm-decidable-model} relativized to $\hat T$ gives a model whose elementary diagram is computable in $\hat T$.
:::

The low model cannot in general be replaced by a computable one. Peano arithmetic is computably axiomatized, and by Tennenbaum's theorem (:ref{#thm-tennenbaum}, in the course on models of arithmetic), its only computable model is the standard one. A theory such as $\mathrm{PA} + \neg\mathrm{Con}(\mathrm{PA})$, which has no standard model, therefore has no computable model at all, although it has low ones. Computability of a model is a matter of the atomic diagram; the corollary controls the full elementary diagram, and that is the price.

## Computable algebra

Algebra offers the first examples where the choice of the computable copy matters. A **computable field** is a field with a computable presentation. The field $\mathbb Q$, and every finite extension of it given by generators and relations, has a **splitting algorithm**: one can decide whether a polynomial with coefficients in the field is irreducible (Kronecker). For arbitrary computable fields, this fails.

:::proposition[Fröhlich, Shepherdson]{#prop-no-splitting}
There is a computable field in which the set of polynomials of degree $2$ that have a root is not computable.
:::

:::proof{of=prop-no-splitting}
Let $K = \emptyset'$ and $F = \mathbb Q(\sqrt{p_i} : i \in K)$, where $p_i$ is the $i$-th prime. The field $\overline{\mathbb Q}$ of algebraic numbers has a computable presentation, with numbers given by their minimal polynomials and isolating data. Inside it, $F$ is the subfield generated by the c.e. set $\{ \sqrt{p_i} : i \in K \}$, so its domain is a c.e. set closed under the field operations, and the pull-back of a computable enumeration of it is a computable copy of $F$. In $F$, the polynomial $x^2 - p_i$ has a root if and only if $\sqrt{p_i} \in F$, which, by the classical theorem that the square roots of distinct primes are linearly independent over $\mathbb Q$ (Besicovitch), holds if and only if $i \in K$. A procedure deciding which polynomials of degree $2$ have a root would decide $K$.
:::

So computability of a structure does not give computability of its natural relations: having a root is r.i.c.e. (search for one), and here it is not computable. This is the subject of the next course. Rabin (1960) showed that every computable field has a computable algebraic closure, into which it embeds computably; whether the image of the field in its closure is computable is exactly the question of the splitting algorithm (Ash–Knight, Section 3.17, and Downey–Melnikov, *Computable Structure Theory*, treat computable algebra in detail).

::::exercise{#ex-decidable-dlo-model difficulty=1 objective="Run the effective completeness theorem on a simple complete theory, and compare the model built with the standard one."}
Let $T$ be the theory of an infinite set with no structure (the empty vocabulary). Show that $T$ is complete and decidable, and describe the model built by the proof of :ref{#thm-decidable-model}. Is it isomorphic to $(\nat)$, and is the isomorphism computable?

:::solution
$T$ is axiomatized by the sentences "there are at least $n$ elements", a computable set; it is complete, since any two countably infinite sets are isomorphic, and by the Łoś–Vaught test; a complete computably axiomatized theory is decidable (enumerate the consequences of the axioms and of their negations, one of which appears). The construction decides equalities $c_i = c_j$ consistently with $T$; since all the new constants can be kept distinct, consistency never forces an equality, but the construction may accept some equalities $c_i = c_j$ when they are listed before their negations, since they are consistent. The model is the set of classes of the computable equivalence $\sim$; it is infinite, since the axioms force infinitely many distinct elements. Choosing the least constant of each class gives a computable set of representatives, and listing it in increasing order gives a computable bijection with $\nat$; so the model is computably isomorphic to $\nat$ with no structure.
:::
::::

## Notes and references

The effective completeness theorem is folklore from the 1950s; Ash and Knight present it through a computable tree of attempts (Sections 3.10, 3.13 and 3.14, Theorem 3.15 and Corollary 3.16, the latter due to Jockusch and Soare, 1972). The example of a computable field without a splitting algorithm is due to Fröhlich and Shepherdson (1956), and Rabin's theorem to Rabin (1960). Tennenbaum's theorem is from 1959.

- C. J. Ash and J. F. Knight, *Computable Structures and the Hyperarithmetical Hierarchy*, Chapter 3.
- A. Fröhlich and J. C. Shepherdson, *Effective procedures in field theory*, Philosophical Transactions of the Royal Society A 248 (1956), 407–432.
- M. O. Rabin, *Computable algebra, general theory and theory of computable fields*, Transactions of the American Mathematical Society 95 (1960), 341–360.
- C. G. Jockusch and R. I. Soare, *Π⁰₁ classes and degrees of theories*, Transactions of the American Mathematical Society 173 (1972), 33–56.
- R. G. Downey and A. Melnikov, *Computable Structure Theory: A Unified Approach*, Springer, 2025.

:::::exercises
::::exercise{#ex-decidable-theory-of-model difficulty=1 objective="Compare the complexity of the theory, the atomic diagram and the elementary diagram of a presentation."}
Show that for every ω-presentation $\mathcal M$, $D(\mathcal M) \leq_T D^c(\mathcal M)$ and $\mathrm{Th}(\mathcal M) \leq_T D^c(\mathcal M)$, and that $D^c(\mathcal M) \leq_T D(\mathcal M)^{(\omega)}$. Give a structure for which $D(\mathcal M)$ is computable and $\mathrm{Th}(\mathcal M)$ is not arithmetic.

:::solution
Atomic formulas and sentences are formulas, so $D(\mathcal M)$ and $\mathrm{Th}(\mathcal M)$ are subsets of $D^c(\mathcal M)$ under computable codings, decided by it. A formula with $n$ quantifiers is $\Sigma^0_n$ or $\Pi^0_n$ relative to $D(\mathcal M)$, uniformly in the formula (Ash–Knight, Theorem 3.19), so its truth is decided by $D(\mathcal M)^{(n)}$, and $D^c(\mathcal M)$ is computable in the join of all these jumps, $D(\mathcal M)^{(\omega)}$. For $\mathcal M = (\nat; +, \times)$, $D(\mathcal M)$ is computable and $\mathrm{Th}(\mathcal M)$ is true arithmetic, which is not arithmetic by Tarski's theorem on the undefinability of truth.
:::
::::

::::exercise{#ex-no-computable-model difficulty=2 objective="Find a consistent computably axiomatized theory without computable models."}
Show that there is a consistent computably axiomatized theory with no computable model, and that it has a model whose elementary diagram is low.

:::solution
Take $T = \mathrm{PA} + \neg \mathrm{Con}(\mathrm{PA})$, which is computably axiomatized and consistent by Gödel's second incompleteness theorem. Every model of $T$ is non-standard, since $\neg\mathrm{Con}(\mathrm{PA})$ is false in $\nat$. By Tennenbaum's theorem (:ref{#thm-tennenbaum}), no non-standard model of $\mathrm{PA}$ has a computable addition, so $T$ has no computable model. By :ref{#cor-low-model}, it has a model with low elementary diagram.
:::
::::
:::::
