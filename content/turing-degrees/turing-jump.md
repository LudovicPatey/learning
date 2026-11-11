---
title: The Turing jump
summary: The jump of a set, its completeness for relatively c.e. sets, its strict increase and monotonicity, the iterated jumps, and the position of totality and finiteness below the double jump.
duration: 35
prerequisites: [turing-reducibility]
---

Relativizing the halting set to an oracle $X$ gives the **jump** $X'$ of $X$: the halting problem for machines with oracle $X$. It is strictly more powerful than $X$, and it depends only on the degree of $X$. Iterating it gives a strictly increasing sequence of degrees $\obf < \obf' < \obf'' < \cdots$, along which many natural problems can be located: the halting problem is at the first level, totality and finiteness of domains at the second. The jump is the main tool for measuring the complexity of sets, and the arithmetic hierarchy is its definability counterpart.

## Definition

:::definition{#def-jump}
The **jump** of $X \in \cs$ is
$$
X' = \{ e \in \nat : \Phi^X_e(e)\converge \}.
$$
We write $X'' = (X')'$, and in general $X^{(0)} = X$ and $X^{(n+1)} = (X^{(n)})'$.
:::

In particular $\emptyset' = \{ e : \Phi^\emptyset_e(e)\converge \}$, defined with oracle machines. The halting set of the course on fundamentals, defined with ordinary machines, is many-one equivalent to it, since both are m-complete among the c.e. sets (:ref{#thm-halting-complete} and the theorem below). From now on $\emptyset'$ denotes the jump of $\emptyset$.

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

The jump is not injective on degrees: the lesson on low and high sets constructs a non-computable set $A$ with $A' \equiv_T \emptyset'$.

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
Show that $\{ e : W_e = \emptyset \}$ and $\{ e : W_e \text{ is finite} \}$ are computable in $\emptyset'$ and in $\emptyset''$ respectively, and that the first is not computable.

:::solution
$W_e \neq \emptyset$ if and only if $\exists x \exists s\ \Phi_e(x)[s]\converge$, a c.e. condition, so the first set is the complement of a c.e. set, computable in $\emptyset'$. It is not computable, by :ref{#thm-rice}. The second set is $\mathrm{Fin}$, computable in $\emptyset''$ by :ref{#prop-tot-double-jump}.
:::
::::

## Notes and references

The jump operator was introduced by Kleene and Post (1954), who proved its basic properties. Soare's textbooks present the jump together with the arithmetic hierarchy.

- S. C. Kleene and E. L. Post, *The upper semi-lattice of degrees of recursive unsolvability*, Annals of Mathematics 59 (1954), 379–407.
- R. I. Soare, *Recursively Enumerable Sets and Degrees*, Springer, 1987.
