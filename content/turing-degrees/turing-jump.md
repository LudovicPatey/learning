---
title: The Turing jump
summary: The jump of a set, its completeness for relatively c.e. sets, its strict increase and monotonicity, the iterated jumps, and the position of totality and finiteness below the double jump.
duration: 40
prerequisites: [turing-reducibility, fundamentals/complete-sets]
---

Relativizing the halting set to an oracle $X$ gives the **jump** $X'$ of $X$: the halting problem for machines with oracle $X$. It is strictly more powerful than $X$, and it depends only on the degree of $X$. Iterating it gives a strictly increasing sequence of degrees $\obf < \obf' < \obf'' < \cdots$, along which many natural problems can be located: the halting problem is at the first level, totality and finiteness of domains at the second. The jump is the main tool for measuring the complexity of sets, and the arithmetic hierarchy is its definability counterpart.

The proofs of this lesson are relativizations of the proofs about the halting set: diagonalization shows that $X'$ is not $X$-computable, and the SMN theorem shows that every $X$-c.e. set reduces to $X'$. What is new is that the relativized proofs are uniform in the oracle, and uniformity is what allows one to compare the jumps of different sets.

## Definition

:::definition{#def-jump}
The **jump** of $X \in \cs$ is
$$
X' = \{ e \in \nat : \Phi^X_e(e)\converge \}.
$$
We write $X'' = (X')'$, and in general $X^{(0)} = X$ and $X^{(n+1)} = (X^{(n)})'$.
:::

In particular $\emptyset' = \{ e : \Phi^\emptyset_e(e)\converge \}$, defined with oracle machines. The halting set of the course on fundamentals, defined with ordinary machines, is many-one equivalent to it, since both are m-complete among the c.e. sets (:ref{#thm-halting-complete} and the theorem below). From now on $\emptyset'$ denotes the jump of $\emptyset$.

:::example{#ex-jumps}
1. If $X$ is computable, then $X' \equiv_T \emptyset'$: this is a special case of item 5 of the theorem below, and can be seen directly, since a machine with a computable oracle can be replaced by an ordinary machine.
2. The relativized halting problem $K^X = \{ \langle e, x \rangle : \Phi^X_e(x)\converge \}$ is $X$-c.e., and $X' = \{ e : \langle e, e \rangle \in K^X \}$; conversely, $K^X$ reduces to $X'$ by item 2 of the theorem below. So $X' \equiv_1 K^X$, and either set may serve as the jump.
3. $\emptyset''$ is the halting problem for machines with oracle $\emptyset'$: it answers questions of the form "does this computation, which may itself consult the halting problem, terminate?".
:::

## Properties of the jump

:::theorem{#thm-jump}
For all $X, Y \in \cs$:

1. $X'$ is $X$-c.e.;
2. every $X$-c.e. set is one-one reducible to $X'$; more precisely, for every $a$ there is a computable injective function $f$ such that $x \in W^X_a \iff f(x) \in X'$ for every $X$;
3. $X \leq_1 X'$, in particular $X \leq_T X'$;
4. $X' \not\leq_T X$;
5. if $X \leq_T Y$, then $X' \leq_1 Y'$.
:::

:::proof{of=thm-jump}
1. $X' = \{ e : \exists s\ \Phi^X_e(e)[s]\converge \}$, and the relation $\Phi^X_e(e)[s]\converge$ is $X$-computable by :ref{#prop-oracle-stages}.
2. By the parameter form of the relativized SMN theorem (:ref{#thm-relativized-smn}), there is a computable $f$ such that $\Phi^Z_{f(x)}(y) \simeq \Phi^Z_a(x)$ for every $Z$, $x$ and $y$: the machine $f(x)$ ignores its input and runs $\Phi_a$ on $x$, with the same oracle. By the padding lemma (:ref{#lem-padding}), whose proof applies to oracle machines without change, $f$ can be taken injective, as in the exercises of :ref{to="fundamentals/universal-program-smn"}. Then $x \in W^X_a \iff \Phi^X_a(x)\converge \iff \Phi^X_{f(x)}(f(x))\converge \iff f(x) \in X'$.
3. $X$ is $X$-c.e., since it is $X$-computable; apply item 2.
4. This is the relativization of :ref{#thm-halting}. Suppose $X' = \Phi^X_c$. The oracle machine which, on input $x$, computes $\Phi^X_c(x)$ and enters an infinite loop if the result is $1$, and halts otherwise, has an index $d$, and $\Phi^X_d(x)\converge \iff x \notin X'$ for every $x$. For $x = d$, this gives $\Phi^X_d(d)\converge \iff \Phi^X_d(d)\diverge$.
5. Let $X = \Phi^Y_b$. The set $X'$ is $Y$-c.e.: $e \in X'$ if and only if $\Phi^X_e(e)\converge$, and by item 2 of :ref{#prop-turing-preorder} there is a computable $c$ with $\Phi^Y_{c(b, e)} = \Phi^X_e$ as partial functions, since $\Phi^Y_b = X$; so $e \in X' \iff \Phi^Y_{c(b, e)}(e)\converge$, and $X'$ is the domain of the $Y$-computable partial function $e \mapsto \Phi^Y_{c(b, e)}(e)$. By item 2 relative to $Y$, $X' \leq_1 Y'$.
:::

:::corollary{#cor-jump-degrees}
The jump induces an operation $\dbf \mapsto \dbf'$ on degrees, with $\dbf < \dbf'$ and $\abf \leq \bbf \Rightarrow \abf' \leq \bbf'$. In particular
$$
\obf < \obf' < \obf'' < \cdots < \obf^{(n)} < \cdots,
$$
where $\obf^{(n)} = \deg_T(\emptyset^{(n)})$, and $\emptyset^{(n)} \leq_T X^{(n)}$ for every $X$ and $n$.
:::

:::proof{of=cor-jump-degrees}
By item 5, $X \equiv_T Y$ implies $X' \equiv_T Y'$, so the jump is well defined on degrees and monotone. By items 3 and 4, $\dbf < \dbf'$. Finally $\emptyset \leq_T X$ for every $X$, and monotonicity gives $\emptyset^{(n)} \leq_T X^{(n)}$ by induction.
:::

The jump is not injective on degrees: the lesson on low and high sets constructs a non-computable set $A$ with $A' \equiv_T \emptyset'$. In particular the converse of item 5 fails for Turing reducibility: $A' \leq_T \emptyset'$ while $A \not\leq_T \emptyset$. For one-one reducibility the converse holds (see the exercises): $X \leq_T Y$ if and only if $X' \leq_1 Y'$. A one-one reduction between jumps carries more information than a Turing reduction, because it preserves the distinction between the sets that are c.e. relative to an oracle and their complements.

:::quiz[the properties of the jump]
In item 2, why must the function $f$ be computable, and not only $X$-computable?

- [x] So that the same reduction works for every oracle, which is used in item 5 to compare jumps relative to different oracles; and a computable injective function gives a one-one reduction.

  The relativized SMN theorem provides such an $f$, since it never consults the oracle.
- [ ] Because $X$-computable functions are not total.

  An $X$-computable function may well be total; the point is uniformity in $X$ and the one-one reduction.
- [ ] It does not matter: an $X$-computable reduction would give the same results.

  An $X$-computable reduction would show $W^X_a \leq_T X'$, but not $W^X_a \leq_1 X'$, and the uniformity in $X$ would be lost.

---

In item 5, which set is shown to be $Y$-c.e.?

- [x] $X'$, by simulating the computations $\Phi^X_e(e)$ with the oracle $X$ computed from $Y$.
- [ ] $Y'$.

  $Y'$ is $Y$-c.e. by item 1; the point is to place $X'$ among the $Y$-c.e. sets, all of which reduce to $Y'$.
- [ ] $X$.

  $X$ is $Y$-computable by hypothesis, but this alone does not give $X' \leq_1 Y'$.

---

Is $\emptyset'' $ c.e.?

- [ ] Yes, since it is the halting set of an oracle machine.

  It is $\emptyset'$-c.e., not c.e.
- [x] No: every c.e. set is computable in $\emptyset'$, while $\emptyset'' \not\leq_T \emptyset'$.

  So the relation "is c.e. relative to" is not transitive: $\emptyset''$ is $\emptyset'$-c.e. and $\emptyset'$ is c.e., but $\emptyset''$ is not c.e.
:::

## Complete sets

:::definition{#def-turing-complete}
A set $A$ is **Turing complete** if $\emptyset' \leq_T A$, and a degree $\dbf$ is complete if $\obf' \leq \dbf$.
:::

The halting set is the archetype of a complete set, but not all complete sets look like it. By :ref{#ex-oracle-domination}, every set whose principal function grows fast enough to bound the halting times of the computations $\Phi_e(e)$ is complete. The lesson on limit computability characterizes the sets computable in $\emptyset'$, and the course on Post's problem studies the c.e. sets that are not complete.

## Totality and finiteness

The double jump locates some of the undecidable index sets of the course on fundamentals.

:::proposition{#prop-tot-double-jump}
The sets $\mathrm{Tot} = \{ e : \Phi_e \text{ is total} \}$, $\mathrm{Inf} = \{ e : W_e \text{ is infinite} \}$ and $\mathrm{Fin} = \nat \setminus \mathrm{Inf}$ are computable in $\emptyset''$. The complements of $\mathrm{Tot}$ and $\mathrm{Inf}$ are $\emptyset'$-c.e.
:::

:::proof{of=prop-tot-double-jump}
The set $H = \{ \langle e, x \rangle : \Phi_e(x)\converge \}$ is c.e., hence computable in $\emptyset'$ (:ref{#prop-ce-below-jump}). Then
$$
e \notin \mathrm{Tot} \iff \exists x\ \langle e, x \rangle \notin H,
\qquad
e \notin \mathrm{Inf} \iff \exists n\ \forall x > n\ \ x \notin W_e.
$$
The first is the projection of an $\emptyset'$-computable relation, hence $\emptyset'$-c.e. For the second, the relation $\forall x > n\ x \notin W_e$ is the complement of the c.e. relation $\exists x > n\ x \in W_e$, hence $\emptyset'$-computable, and its projection is $\emptyset'$-c.e. A set whose complement is $\emptyset'$-c.e. is reducible to $\emptyset''$ (by item 2 of :ref{#thm-jump} relative to $\emptyset'$ and closure of $\leq_T$ under complements), and $\mathrm{Fin}$ is the complement of $\mathrm{Inf}$.
:::

In fact $\mathrm{Tot}$, $\mathrm{Inf}$ and $\mathrm{Fin}$ are all Turing equivalent to $\emptyset''$; this is proved in the course on the arithmetic hierarchy, where these sets are shown to be complete at the second level. Since none of them is computable in $\emptyset'$, they are strictly harder than the halting problem.

:::figure[The first jumps. Each degree $\obf^{(n+1)}$ is strictly above $\obf^{(n)}$. The sets computable in $\emptyset'$ include the c.e. sets; the lesson on finite extensions builds sets strictly between $\obf$ and $\obf'$ that are not c.e.]
<svg class="fig" viewBox="0 0 600 300" width="600" role="img" aria-label="The degrees 0, 0 prime, 0 double prime and 0 triple prime on a vertical axis, with the sets located at each level"><line x1="120" y1="12" x2="120" y2="280" class="axis"/><circle cx="120" cy="270" r="5" class="node"/><text x="106" y="276" text-anchor="end" class="mrm" font-size="17" font-weight="700">0<tspan font-weight="400"></tspan></text><text x="136" y="274" class="label">computable sets</text><circle cx="120" cy="180" r="5" class="node"/><text x="106" y="186" text-anchor="end" class="mrm" font-size="17" font-weight="700">0<tspan font-weight="400">′</tspan></text><text x="136" y="184" class="label">∅′ and the Turing complete c.e. sets</text><circle cx="120" cy="90" r="5" class="node"/><text x="106" y="96" text-anchor="end" class="mrm" font-size="17" font-weight="700">0<tspan font-weight="400">″</tspan></text><text x="136" y="94" class="label">Tot, Inf, Fin</text><circle cx="120" cy="20" r="5" class="node"/><text x="106" y="26" text-anchor="end" class="mrm" font-size="17" font-weight="700">0<tspan font-weight="400">‴</tspan></text><text x="136" y="24" class="label">⋯</text><path d="M430,272 L438,272 L438,178 L430,178" class="accent-stroke" stroke-width="1.3"/><text x="444" y="222" class="label">computable</text><text x="444" y="238" class="label">in ∅′</text><path d="M510,272 L518,272 L518,88 L510,88" class="accent-stroke" stroke-width="1.3"/><text x="524" y="126" class="label">computable</text><text x="524" y="142" class="label">in ∅″</text><text x="136" y="220" class="label">strictly between: the Kleene–Post sets,</text><text x="136" y="236" class="label">the non-computable low sets</text></svg>
:::

:::quiz[locating index sets]
Why is the relation "$\forall x > n\ \ x \notin W_e$" computable in $\emptyset'$?

- [x] It is the complement of the c.e. relation "$\exists x > n\ \ x \in W_e$", and every c.e. relation is computable in $\emptyset'$.

  A single question to the oracle settles a whole unbounded quantifier.
- [ ] Because it is a bounded quantification.

  The quantifier over $x > n$ is unbounded.
- [ ] Because $W_e$ is computable.

  $W_e$ is c.e., and not computable in general.
:::

## Exercises

::::exercise{difficulty=1}
Show that there is an index $e$ such that $\Phi^{X'}_e = X$ for every $X$.

:::solution
By item 2 of :ref{#thm-jump} applied to an index $a$ with $W^X_a = X$ for every $X$ (the machine that halts if and only if the oracle bit at its input is $1$), there is a computable $f$ with $x \in X \iff f(x) \in X'$ for every $X$. The machine which, on input $x$, computes $f(x)$ and outputs the bit of its oracle at $f(x)$ computes $X$ from $X'$, whatever $X$ is.
:::
::::

::::exercise{difficulty=1}
Show that $X' \oplus Y' \leq_T (X \oplus Y)'$ for all $X$ and $Y$. Admitting that there are sets $X$ and $Y$ with $X' \equiv_T Y' \equiv_T \emptyset'$ and $X \oplus Y \equiv_T \emptyset'$ (a consequence of Sacks' splitting theorem), show that the reverse reduction fails in general.

:::solution
Since $X, Y \leq_T X \oplus Y$, monotonicity gives $X', Y' \leq_T (X \oplus Y)'$, hence $X' \oplus Y' \leq_T (X \oplus Y)'$. With the given sets, $X' \oplus Y' \equiv_T \emptyset'$ while $(X \oplus Y)' \equiv_T \emptyset''$, which is not computable in $\emptyset'$.
:::
::::

::::exercise{difficulty=2}
Show that $X \leq_T Y$ if and only if $X' \leq_1 Y'$.

:::solution
One direction is item 5 of :ref{#thm-jump}. Conversely, suppose $X' \leq_1 Y'$ via $h$. By item 2 of :ref{#thm-jump}, applied to $X$ and to its complement, which are both $X$-c.e., there are computable injective $f_0$, $f_1$ with $x \in X \iff f_0(x) \in X'$ and $x \notin X \iff f_1(x) \in X'$. Then $x \in X \iff h(f_0(x)) \in Y'$ and $x \notin X \iff h(f_1(x)) \in Y'$, so $X$ and its complement are many-one reducible to the $Y$-c.e. set $Y'$, hence $Y$-c.e., and $X$ is $Y$-computable by :ref{#ex-relativized-complementation}.
:::
::::

::::exercise{difficulty=2}
Show that $\{ e : W_e = \emptyset \}$ and $\{ e : W_e \text{ is finite} \}$ are computable in $\emptyset'$ and in $\emptyset''$ respectively, and that the first is not computable.

:::solution
$W_e \neq \emptyset$ if and only if $\exists x \exists s\ \Phi_e(x)[s]\converge$, a c.e. condition, so the first set is the complement of a c.e. set, computable in $\emptyset'$. It is not computable, by :ref{#thm-rice}. The second set is $\mathrm{Fin}$, computable in $\emptyset''$ by :ref{#prop-tot-double-jump}.
:::
::::

## Notes and references

The jump operator was introduced by Kleene and Post (1954), who proved its basic properties. The theorem of this lesson, with the converse of item 5 for one-one reducibility, is the Jump Theorem 3.4.3 of Soare (2016); see also Downey and Hirschfeldt (2010, §2.4), Nies (2009, §1.2), and the section on the Turing jump of Monin and Patey. Soare's textbooks present the jump together with the arithmetic hierarchy.

The jump is degree invariant: $X \equiv_T Y$ implies $X' \equiv_T Y'$. **Martin's conjecture**, formulated in set theory with the axiom of determinacy, says that the jump and its transfinite iterates are the canonical examples of such operations: every degree-invariant function $f$ is either constant on a cone of degrees or satisfies $X \leq_T f(X)$ on a cone, and the functions of the second kind are prewellordered by the relation "$f(X) \leq_T g(X)$ on a cone", the successor of $f$ being $X \mapsto f(X)'$. The conjecture is open in general. Steel (1982) and Slaman and Steel (1988) proved it for uniformly degree-invariant functions, and Lutz and Siskind (preprint, 2023) proved its first part for order-preserving functions. These results place the jump, rather than any other operator, at the center of the theory of degrees.

- S. C. Kleene and E. L. Post, *The upper semi-lattice of degrees of recursive unsolvability*, Annals of Mathematics 59 (1954), 379–407.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, §3.4.
- J. R. Steel, *A classification of jump operators*, Journal of Symbolic Logic 47 (1982), 347–358.
- T. A. Slaman and J. R. Steel, *Definable functions on degrees*, in *Cabal Seminar 81–85*, Lecture Notes in Mathematics 1333, Springer, 1988, 37–55.
- P. Lutz and B. Siskind, *Part 1 of Martin's conjecture for order-preserving and measure-preserving functions*, arXiv:2305.19646, 2023.
