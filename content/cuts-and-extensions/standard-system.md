---
title: Coded subsets of cuts and the standard system
summary: The coded subsets of a cut and the standard system of a non-standard model; formulas with set parameters evaluated through codes; a separation lemma by overspill; the coded subsets of a cut closed under addition and multiplication are closed under Δ⁰₁ definability, and the standard system is a Turing ideal.
duration: 45
prerequisites: [fragments-of-arithmetic/definable-cuts, fragments-of-arithmetic/coding, second-order-arithmetic/rca0]
---

A non-standard model of arithmetic cannot define its standard part, nor any of its proper cuts if it satisfies enough induction (:ref{#prop-cuts-induction}). It can nevertheless say a great deal about a cut through the numbers that it codes. A number $c$ codes a finite set in the sense of the model, $\mathrm{Ack}(c)$, which may have non-standard elements; its trace on a cut $I$ is a subset of $I$ that need not be bounded in $I$. The traces on $\nat$ form the **standard system** of the model, a set of subsets of $\nat$ that measures what the model knows about the natural numbers. This lesson shows that coded subsets of a cut are closed under the definitions that a computation would allow; for the standard cut, this makes the standard system a Turing ideal.

The track assumes first-order logic: the completeness and compactness theorems are used without comment. Throughout the course, cuts are those of :ref{#def-cut}: nonempty initial segments closed under successor. A cut is **proper** if it is not the whole model.

## Coded subsets of a cut

:::definition{#def-coded-subsets}
Let $M$ be a model of $\mathrm I\Delta_0$ and $I$ a cut of $M$. For $c \in M$, the **subset of $I$ coded by $c$** is $\mathrm{Ack}(c) \cap I$, with $\mathrm{Ack}(c)$ as in :ref{#def-ack-membership}. The set of these sets is
$$
\mathrm{Cod}(M/I) = \{ \mathrm{Ack}(c) \cap I : c \in M \}.
$$
If $M$ is non-standard, the **standard system** of $M$ is $\mathrm{SSy}(M) = \mathrm{Cod}(M/\nat)$, a set of subsets of $\nat$.
:::

A coded set $\mathrm{Ack}(c)$ is bounded in $M$, by $c$ itself (:ref{#lem-ack-basic}); its trace on a proper cut need not be bounded in the cut. The definition only makes sense for proper cuts: for $I = M$, the coded subsets are the sets $\mathrm{Ack}(c)$, which are "finite" in $M$.

:::example{#ex-coded-subsets}
Let $M$ be a model of $\mathrm I\Delta_0 + \mathrm{exp}$ and $I$ a proper cut.

1. Every set $\{ x \in I : M \models \delta(x, \bar p) \}$, with $\delta$ a $\Delta_0$ formula and parameters $\bar p \in M$, belongs to $\mathrm{Cod}(M/I)$: take $a \in M \setminus I$, and a code of $\{ x < a : \delta(x, \bar p) \}$ given by :ref{#thm-delta0-comprehension}. In particular $I$ itself is the trace of a code of $[0, a)$, although $I$ is not definable in $M$ when $M \models \mathrm I\Delta_0$ (:ref{#prop-cuts-induction}).
2. If $M$ is non-standard, every finite set $F \subseteq \nat$ belongs to $\mathrm{SSy}(M)$, coded by the standard number $\sum_{k \in F} 2^k$.
3. For $M = \nat$ no proper cut exists. If $M$ is non-standard, $\mathrm{SSy}(M)$ is countable when $M$ is, and so it is a small part of $\mathcal P(\nat)$; which sets it contains depends on $M$.
:::

The rest of the lesson shows that $\mathrm{Cod}(M/I)$ is closed under definitions of a certain kind. To state this, we view the cut with its coded subsets as a structure for the language $\mathcal L_2$ of second-order arithmetic (:ref{#def-l2}): when $I$ is closed under addition and multiplication, it is a substructure of $M$, and $(I, \mathrm{Cod}(M/I))$ is an $\mathcal L_2$-structure (:ref{#def-l2-structure}) whose number variables range over $I$ and whose set variables range over $\mathrm{Cod}(M/I)$.

## Formulas with set parameters, evaluated through codes

A bounded formula of $\mathcal L_2$ may contain atomic formulas $t \in X$. If $X$ is the trace of a code $c$, such an atom can be read inside $M$ as the bounded formula $t \in c$ of :ref{#def-ack-membership}. For an $\mathcal L_2$ formula $\delta$ with set variables $X_1, \dots, X_k$ and numbers $c_1, \dots, c_k \in M$, let $\delta[\bar c]$ be the $\mathcal L_A$ formula, with parameters $\bar c$, obtained by replacing each atom $t \in X_j$ by $t \in c_j$. If $\delta$ is bounded, so is $\delta[\bar c]$.

:::lemma{#lem-delta00-absolute-cut}
Let $M$ be a model of $\mathrm{PA}^-$, $I$ a cut of $M$ closed under addition and multiplication, $c_1, \dots, c_k \in M$ and $X_j = \mathrm{Ack}(c_j) \cap I$. For every bounded $\mathcal L_2$ formula $\delta(\bar x, X_1, \dots, X_k)$ and every tuple $\bar a$ of elements of $I$,
$$
(I, \bar X) \models \delta(\bar a, \bar X) \iff M \models \delta[\bar c](\bar a).
$$
:::

:::proof{of=lem-delta00-absolute-cut}
By induction on $\delta$, as for :ref{#lem-delta0-absolute}. Since $I$ is a substructure of $M$, every term has the same value $t(\bar a) \in I$ in both structures, which settles the atoms $s = t$ and $s < t$. For an atom $t \in X_j$: $(I, \bar X) \models t(\bar a) \in X_j$ if and only if $t(\bar a) \in \mathrm{Ack}(c_j)$, since $t(\bar a) \in I$, that is, if and only if $M \models t(\bar a) \in c_j$. Connectives are immediate. For $\exists y < t(\bar a)$, the candidates $y < t(\bar a)$ are the same in $I$ and in $M$, since $I$ is an initial segment of $M$ containing $t(\bar a)$; the induction hypothesis applies to each of them.
:::

The lemma is the bridge used in the whole course: a bounded property of elements of the cut and of coded subsets of the cut can be checked in $M$, where coded sets are ordinary numbers and the induction of $M$ applies.

## A separation lemma

The main tool of the lesson is the following lemma. Two disjoint sets $A$ and $B$, each defined in the cut by a $\Sigma^0_1$ formula, are separated by a coded set. The idea is to look for a code of "the numbers that have a witness for $A$", with all witnesses bounded by a single element $k$. If $k$ is in $I$, the code misses elements of $A$ whose witnesses are large; if $k$ is too large, it may contain elements of $B$, because a witness for $A$ above $I$ need not mean anything. **Overspill** chooses $k$ just above $I$, so that the bad behavior, which never occurs below elements of $I$, does not occur below $k$ either.

:::lemma[Separation]{#lem-cut-separation}
Let $M$ be a model of $\mathrm I\Delta_0 + \mathrm{exp}$ and $I$ a proper cut of $M$ closed under addition and multiplication. Let $\bar X$ be a tuple of members of $\mathrm{Cod}(M/I)$, and let $A, B \subseteq I$ be disjoint sets defined in $(I, \bar X)$ by $\Sigma^0_1$ formulas $\exists \bar y\ \alpha(x, \bar y, \bar X)$ and $\exists \bar z\ \beta(x, \bar z, \bar X)$, with $\alpha$ and $\beta$ bounded and with number parameters from $I$. Then there is $C \in \mathrm{Cod}(M/I)$ with $A \subseteq C$ and $C \cap B = \emptyset$.
:::

:::proof{of=lem-cut-separation}
Let $\bar c$ be codes with $X_j = \mathrm{Ack}(c_j) \cap I$, and write $\alpha'$ and $\beta'$ for $\alpha[\bar c]$ and $\beta[\bar c]$. Consider the bounded formula, with parameters $\bar c$ and the number parameters of $\alpha$ and $\beta$,
$$
\chi(k) \equiv \forall x < k\ \forall \bar y < k\ \forall \bar z < k\ \neg \big( \alpha'(x, \bar y) \wedge \beta'(x, \bar z) \big).
$$
*$\chi$ holds on $I$.* If $k \in I$ and $\chi(k)$ fails, the witnesses $x, \bar y, \bar z$ are below $k$, hence in $I$, and by :ref{#lem-delta00-absolute-cut} they satisfy $\alpha$ and $\beta$ in $(I, \bar X)$; so $x \in A \cap B$, a contradiction.

*Overspill.* Since $M \models \mathrm I\Delta_0$ and $\chi$ is bounded, :ref{#cor-overspill} (with $n = 0$) gives $k \in M \setminus I$ with $M \models \chi(k)$.

*The code.* By :ref{#thm-delta0-comprehension}, some $d \in M$ satisfies $\forall x < k\ \big(x \in d \leftrightarrow \exists \bar y < k\ \alpha'(x, \bar y)\big)$. Let $C = \mathrm{Ack}(d) \cap I$. If $x \in A$, it has witnesses $\bar y \in I$, which satisfy $\alpha'(x, \bar y)$ in $M$ by :ref{#lem-delta00-absolute-cut}; since $x$ and $\bar y$ are in $I$, they are below $k$, so $x \in C$. If $x \in B \cap C$, there are $\bar y < k$ with $M \models \alpha'(x, \bar y)$, since $x \in d$, and $\bar z \in I$ with $M \models \beta'(x, \bar z)$, since $x \in B$; as $x, \bar z < k$, this contradicts $\chi(k)$.
:::

:::figure[The separation lemma. The elements of $A$ (discs) and $B$ (squares) have their witnesses in $I$. Overspill gives $k$ above $I$ such that no $x < k$ has witnesses of both kinds below $k$. The set coded by $d$ contains the $x < k$ with a witness for $A$ below $k$: all of $A$, and no element of $B$.]
<svg class="fig" viewBox="0 0 600 170" width="600" role="img" aria-label="The separation lemma: below the cut I the two disjoint sets A and B are defined by witnesses in I; overspill gives k above I below which no number has witnesses of both kinds; the set coded by d contains the numbers below k with an A-witness below k, hence all of A and nothing of B"><line x1="20.0" y1="80.0" x2="580.0" y2="80.0" class="ink-stroke" stroke-width="1.2"/><circle cx="24.0" cy="80.0" r="3.5" class="accent-fill"/><text x="24" y="66" text-anchor="middle" class="mrm" font-size="13">0</text><circle cx="60.0" cy="80.0" r="4" class="accent-fill"/><circle cx="110.0" cy="80.0" r="4" class="accent-fill"/><circle cx="170.0" cy="80.0" r="4" class="accent-fill"/><circle cx="230.0" cy="80.0" r="4" class="accent-fill"/><rect x="81" y="76" width="8" height="8" class="muted-fill"/><rect x="136" y="76" width="8" height="8" class="muted-fill"/><rect x="196" y="76" width="8" height="8" class="muted-fill"/><rect x="251" y="76" width="8" height="8" class="muted-fill"/><line x1="300.0" y1="58.0" x2="300.0" y2="102.0" class="accent-stroke" stroke-width="1.6" stroke-dasharray="4 3"/><text x="300.0" y="50.0" text-anchor="middle" class="math" font-size="14">I</text><circle cx="450.0" cy="80.0" r="3.5" class="ink-fill"/><text x="450.0" y="66.0" text-anchor="middle" class="math" font-size="14">k</text><path d="M22,96 L22,102 L294,102 L294,96" class="muted-stroke" stroke-width="1.2"/><text x="158.0" y="120" text-anchor="middle" class="label">A (discs) and B (squares): witnesses in I</text><path d="M22,130 L22,136 L446,136 L446,130" class="muted-stroke" stroke-width="1.2"/><text x="234.0" y="154" text-anchor="middle" class="label">d codes {x &lt; k : some A-witness below k}</text><text x="450" y="40" text-anchor="middle" class="label">overspill: no x &lt; k has witnesses</text><text x="450" y="54" text-anchor="middle" class="label">of both kinds below k</text></svg>
:::

:::quiz[the separation lemma]
Why does the code $d$ use witnesses bounded by the element $k$ given by overspill, rather than by an arbitrary element $e \in M \setminus I$?

- [x] Below an arbitrary $e$, an element $x \in B$ may have a witness $\bar y < e$ for $\alpha'$, with $\bar y$ above $I$; such a witness is invisible in the cut, and $x$ would wrongly be put in $C$. The choice of $k$ excludes witnesses of both kinds below $k$.
- [ ] Because the code of a set of numbers below $e$ might not exist.

  Codes exist below every element, by :ref{#thm-delta0-comprehension}, since $M \models \mathrm{exp}$; the problem is what the code contains.
- [ ] Because elements of $A$ may have their witnesses above $e$.

  The witnesses for elements of $A$ that matter are in $I$, below every element of $M \setminus I$.

---

Where is it used that $I$ is closed under addition and multiplication?

- [x] In :ref{#lem-delta00-absolute-cut}: the cut must be a substructure, so that the terms of $\alpha$ and $\beta$ have values in $I$ and the bounded quantifiers range over elements of $I$.
- [ ] In the overspill step.

  :ref{#cor-overspill} holds for every proper cut of a model of $\mathrm I\Delta_0$.
- [ ] To find the code $d$.

  Bounded comprehension in $M$ does not depend on $I$.
:::

## Consequences: Δ⁰₁ comprehension and Turing ideals

When $A$ and $B$ are complementary in $I$, the separating set is $A$ itself.

:::corollary{#cor-cod-delta1-ca}
Let $M$ be a model of $\mathrm I\Delta_0 + \mathrm{exp}$ and $I$ a proper cut of $M$ closed under addition and multiplication. Every subset of $I$ defined in $(I, \mathrm{Cod}(M/I))$ both by a $\Sigma^0_1$ formula and by a $\Pi^0_1$ formula, with parameters, belongs to $\mathrm{Cod}(M/I)$. In other words, $(I, \mathrm{Cod}(M/I))$ satisfies the $\Delta^0_1$ comprehension scheme of :ref{#def-rca0}.
:::

:::proof{of=cor-cod-delta1-ca}
Let $A$ be defined by the $\Sigma^0_1$ formula $\varphi$ and by the $\Pi^0_1$ formula $\psi$. Its complement $B = I \setminus A$ is defined by $\neg \psi$, which is logically equivalent to a $\Sigma^0_1$ formula. By :ref{#lem-cut-separation}, some $C \in \mathrm{Cod}(M/I)$ contains $A$ and is disjoint from $B$; then $C = A$.
:::

For the standard cut, the $\Sigma^0_1$ formulas with set parameters are understood through computability. With a set parameter $Z$, they define exactly the sets that are c.e. relative to $Z$ (the relativization of :ref{#cor-sigma1-ce}, recalled in :ref{to="second-order-arithmetic/language-and-models"}); and a set is computable in $Z$ if and only if it and its complement are c.e. in $Z$. Recall that a **Turing ideal** (:ref{#def-turing-ideal}) is a nonempty set of subsets of $\nat$ closed under joins $X \oplus Y$ and downward under Turing reducibility.

:::theorem{#thm-ssy-turing-ideal}
For every non-standard model $M$ of $\mathrm I\Delta_0 + \mathrm{exp}$, the standard system $\mathrm{SSy}(M)$ is a Turing ideal. It contains every computable set.
:::

:::proof{of=thm-ssy-turing-ideal}
The standard cut $\nat$ is proper and closed under addition and multiplication, and $(\nat, \mathrm{SSy}(M))$ is an ω-model. The set $\emptyset = \mathrm{Ack}(0) \cap \nat$ belongs to $\mathrm{SSy}(M)$. If $X, Y \in \mathrm{SSy}(M)$, the join $X \oplus Y$ is defined by the bounded formula $\exists y < n + 1\ \big((n = 2y \wedge y \in X) \vee (n = 2y + 1 \wedge y \in Y)\big)$, so it belongs to $\mathrm{SSy}(M)$ by :ref{#cor-cod-delta1-ca}. If $Y \leq_T X \in \mathrm{SSy}(M)$, then $Y$ and its complement are c.e. in $X$, hence defined by $\Sigma^0_1$ formulas with parameter $X$; so $Y$ is defined by a $\Sigma^0_1$ and by a $\Pi^0_1$ formula, and $Y \in \mathrm{SSy}(M)$ by the same corollary. Every computable set is computable in $\emptyset$.
:::

The theorem uses $\mathrm{exp}$ only to have codes for bounded sets. It says that the standard system is closed under computations; the next lesson shows that it is also closed under the compactness argument of weak König's lemma, and the one after it uses the separation lemma to prove that non-standard models are not computable.

## Exercises

::::exercise{#ex-ssy-end-extension difficulty=2}
Let $M \subseteq_e N$ be models of $\mathrm I\Delta_0 + \mathrm{exp}$, with $M$ non-standard. Show that $\mathrm{SSy}(M) = \mathrm{SSy}(N)$.

:::solution
Every element of $\nat$ is identified with the same numeral in $M$ and in $N$. If $c \in M$, then for $k \in \nat$, $M \models k \in c$ if and only if $N \models k \in c$, by :ref{#lem-delta0-absolute}; so $\mathrm{SSy}(M) \subseteq \mathrm{SSy}(N)$. Conversely, let $d \in N$ and $a \in M$ non-standard. By :ref{#thm-delta0-comprehension} in $N$, some $c < 2^a$ satisfies $\forall x < a\ (x \in c \leftrightarrow x \in d)$. The power $2^a$ exists in $M$, hence is the same element in $N$ by absoluteness of $\varepsilon$, so $c < 2^a \in M$ and $c \in M$, since $M$ is an initial segment of $N$. For $k \in \nat$, $k < a$, so $k \in \mathrm{Ack}(d)$ if and only if $N \models k \in c$, if and only if $M \models k \in c$. Hence $\mathrm{Ack}(d) \cap \nat = \mathrm{Ack}^M(c) \cap \nat \in \mathrm{SSy}(M)$.
:::
::::

## Notes and references

Coded subsets of cuts, under the names $\mathrm{SSy}_I(M)$ or $\mathrm{Cod}(M/I)$, are introduced in Wong's Lecture 3, and in Hájek and Pudlák (Definition IV.2.13) for short cuts in models of arithmetic with a top. The closure of the coded subsets of a cut under $\Delta_1$ definability relative to a coded set is Theorem IV.2.14 of Hájek and Pudlák, proved there with a Rosser-type argument similar to :ref{#lem-cut-separation}. The bibliographical remarks to Chapter IV of Hájek and Pudlák attribute the first study of standard systems of models of $\mathrm{PA}$ to Scott (1962) and the notion used here to Friedman (1973).

- T. L. Wong, *Model theory of arithmetic*, lecture notes, Lecture 3.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapter IV, Section 2(b), and the bibliographical remarks to Chapter IV.
- D. Scott, *Algebras of sets binumerable in complete extensions of arithmetic*, in Recursive Function Theory, Proceedings of Symposia in Pure Mathematics 5, American Mathematical Society, 1962, 117–121.
