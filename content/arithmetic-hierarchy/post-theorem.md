---
title: Post's theorem
summary: The levels of the arithmetic hierarchy are the sets c.e. or computable in the iterated jumps; the iterated jumps are complete at each level; the hierarchy is strict.
duration: 40
prerequisites: [sigma-pi-sets]
---

The arithmetic hierarchy is defined by counting quantifiers; the iterated jumps $\emptyset, \emptyset', \emptyset'', \dots$ are defined by iterating the halting problem. Post's theorem shows that the two are the same scale. Each existential quantifier in front of a $\Pi^0_n$ relation corresponds to one jump: the $\Sigma^0_{n+1}$ sets are the sets c.e. in $\emptyset^{(n)}$, and the $\Delta^0_{n+1}$ sets are the sets computable in $\emptyset^{(n)}$. As a consequence, $\emptyset^{(n)}$ is complete at level $\Sigma^0_n$, and the hierarchy is strict.

## One jump for one quantifier

The whole theorem rests on the following lemma, which converts an oracle for the jump into one more quantifier, and back.

:::lemma{#lem-sigma2-jump}
For every $Y \in \cs$, a relation is $\Sigma^0_1(Y')$ if and only if it is $\Sigma^0_2(Y)$.
:::

:::proof{of=lem-sigma2-jump}
($\Leftarrow$) Let $A = \{ x : \exists y\ \forall z\ R(x, y, z) \}$ with $R$ $Y$-computable. The relation $P(x, y) \iff \forall z\ R(x, y, z)$ is $\Pi^0_1(Y)$, so its complement is $Y$-c.e., and by :ref{#thm-jump} there is a computable $f$ with $\neg P(x, y) \iff f(\langle x, y \rangle) \in Y'$. Hence $P$ is $Y'$-computable, and $A = \{ x : \exists y\ P(x, y) \}$ is $\Sigma^0_1(Y')$.

($\Rightarrow$) Let $A = W^{Y'}_e$. By :ref{#prop-oracle-stages}, $x \in A$ if and only if there are a string $\sigma$ and a stage $s$ with $\sigma \prec Y'$ and $\Phi^\sigma_e(x)[s]\converge$. The relation $\Phi^\sigma_e(x)[s]\converge$ is computable. The relation $\sigma \prec Y'$ is
$$
\forall k < |\sigma|\ \ \big( (\sigma(k) = 1 \wedge k \in Y') \vee (\sigma(k) = 0 \wedge k \notin Y') \big),
$$
where $k \in Y'$ is $\Sigma^0_1(Y)$ and $k \notin Y'$ is $\Pi^0_1(Y)$; both are $\Sigma^0_2(Y)$, so by :ref{#prop-hierarchy-closure} (relativized) the relation $\sigma \prec Y'$ is $\Sigma^0_2(Y)$. Then $A$ is the projection of the intersection of a $\Sigma^0_2(Y)$ relation and a computable relation, hence $\Sigma^0_2(Y)$.
:::

The two directions use the jump in opposite ways. In ($\Leftarrow$), one question to $Y'$ replaces a universal quantifier. In ($\Rightarrow$), a computation with oracle $Y'$ is guessed as a finite string, and the correctness of the guess costs one more quantifier: positive answers of the oracle are $\Sigma^0_1(Y)$ facts, negative answers are $\Pi^0_1(Y)$ facts.

:::quiz[one jump for one quantifier]
In the direction ($\Rightarrow$), why is the relation $\sigma \prec Y'$ not simply $\Sigma^0_1(Y)$?

- [x] Because it asserts both that some numbers are in $Y'$, which is $\Sigma^0_1(Y)$, and that others are not, which is $\Pi^0_1(Y)$.

  The negative information is what requires the second quantifier.
- [ ] Because $\sigma$ is a finite string.

  The finiteness of $\sigma$ is what keeps the quantifier over $k$ bounded.
- [ ] Because $Y'$ is not $Y$-c.e.

  $Y'$ is $Y$-c.e.; it is its complement that is not.

---

In the direction ($\Leftarrow$), where is the theorem on the jump used?

- [x] To decide the $\Pi^0_1(Y)$ relation $P(x, y)$ with the oracle $Y'$, through the reduction of its complement to $Y'$.
- [ ] To show that $A$ is $Y$-c.e.

  $A$ is in general not $Y$-c.e.
- [ ] To compute $Y$ from $Y'$.

  This is also true, but it is not what the proof needs.
:::

## Post's theorem

:::theorem[Post]{#thm-post}
For every $X \in \cs$ and $n \geq 0$:

1. a relation is $\Sigma^0_{n+1}(X)$ if and only if it is $X^{(n)}$-c.e.;
2. a set is $\Delta^0_{n+1}(X)$ if and only if it is computable in $X^{(n)}$;
3. for $n \geq 1$, the set $X^{(n)}$ is $\Sigma^0_n(X)$-complete, and in fact every $\Sigma^0_n(X)$ set is one-one reducible to it.

In particular, $\emptyset^{(n)}$ is $\Sigma^0_n$-complete, the $\Sigma^0_{n+1}$ sets are the $\emptyset^{(n)}$-c.e. sets, and the $\Delta^0_{n+1}$ sets are the sets computable in $\emptyset^{(n)}$.
:::

:::proof{of=thm-post}
1. By induction on $n$, simultaneously for all $X$. For $n = 0$, $X^{(0)} = X$, and the $\Sigma^0_1(X)$ relations are the $X$-c.e. relations. Suppose the statement holds for $n$ and all $X$. A relation $A$ is $\Sigma^0_{n+2}(X)$ if and only if $A = \{ \vec x : \exists y\ P(\vec x, y) \}$ with $P$ a $\Pi^0_{n+1}(X)$ relation. The complement of $P$ is $\Sigma^0_{n+1}(X)$, that is, $X^{(n)}$-c.e. by the induction hypothesis, so $P$ ranges exactly over the $\Pi^0_1(X^{(n)})$ relations. Hence the $\Sigma^0_{n+2}(X)$ relations are the projections of $\Pi^0_1(X^{(n)})$ relations, that is, the $\Sigma^0_2(X^{(n)})$ relations. By :ref{#lem-sigma2-jump} with $Y = X^{(n)}$, these are the $\Sigma^0_1(X^{(n+1)})$ relations.
2. A set is $\Delta^0_{n+1}(X)$ if and only if it and its complement are $\Sigma^0_{n+1}(X)$, that is, $X^{(n)}$-c.e. by item 1, that is, computable in $X^{(n)}$ by :ref{#prop-computable-iff-ce-coce} relativized.
3. $X^{(n)} = (X^{(n-1)})'$ is $X^{(n-1)}$-c.e., hence $\Sigma^0_n(X)$ by item 1. Every $\Sigma^0_n(X)$ set is $X^{(n-1)}$-c.e. by item 1, hence one-one reducible to $(X^{(n-1)})' = X^{(n)}$ by :ref{#thm-jump}.
:::

:::corollary{#cor-hierarchy-strict}
For every $n \geq 1$:

1. $\emptyset^{(n)}$ is $\Sigma^0_n$ and not $\Pi^0_n$, and its complement is $\Pi^0_n$ and not $\Sigma^0_n$;
2. the set $\emptyset^{(n)} \oplus (\nat \setminus \emptyset^{(n)})$ is $\Delta^0_{n+1}$, and neither $\Sigma^0_n$ nor $\Pi^0_n$.

So all the inclusions $\Delta^0_n \subsetneq \Sigma^0_n, \Pi^0_n \subsetneq \Delta^0_{n+1}$ are strict.
:::

:::proof{of=cor-hierarchy-strict}
1. $\emptyset^{(n)}$ is $\Sigma^0_n$ by the theorem. If it were $\Pi^0_n$, it would be $\Delta^0_n$, hence computable in $\emptyset^{(n-1)}$ by item 2, contradicting $\emptyset^{(n-1)} <_T \emptyset^{(n)}$ (:ref{#thm-jump}). The statement on the complement follows by complementation.
2. The set $J = \emptyset^{(n)} \oplus (\nat \setminus \emptyset^{(n)})$ is computable in $\emptyset^{(n)}$, hence $\Delta^0_{n+1}$. If $J$ were $\Sigma^0_n$, then $\nat \setminus \emptyset^{(n)} = \{ m : 2m + 1 \in J \}$ would be $\Sigma^0_n$, by substitution, contradicting item 1. If $J$ were $\Pi^0_n$, then $\emptyset^{(n)} = \{ m : 2m \in J \}$ would be $\Pi^0_n$.
:::

:::corollary{#cor-delta2-limit}
1. A set is $\Delta^0_2$ if and only if it is computable in $\emptyset'$, if and only if it is limit computable.
2. A set is arithmetic if and only if it is computable in $\emptyset^{(n)}$ for some $n$.
3. The class of $\Delta^0_n$ sets is closed under Turing reducibility, for every $n \geq 1$; the classes $\Sigma^0_n$ and $\Pi^0_n$ are not.
:::

:::proof{of=cor-delta2-limit}
1. Item 2 of the theorem for $n = 1$, and Shoenfield's limit lemma (:ref{#thm-limit-lemma}).
2. A $\Sigma^0_n$ set is $\Delta^0_{n+1}$, hence computable in $\emptyset^{(n)}$; conversely a set computable in $\emptyset^{(n)}$ is $\Delta^0_{n+1}$.
3. $\Delta^0_n$ is the class of sets computable in $\emptyset^{(n-1)}$, which is closed downward under $\leq_T$. The set $\nat \setminus \emptyset^{(n)}$ is Turing equivalent to the $\Sigma^0_n$ set $\emptyset^{(n)}$, but is not $\Sigma^0_n$.
:::

The name "$\Delta^0_2$ approximation" used in the course on Turing degrees is thus justified: the sets with such approximations are exactly the $\Delta^0_2$ sets.

:::quiz[Post's theorem]
Which statement is a consequence of Post's theorem?

- [x] A set is $\Pi^0_2$ if and only if its complement is c.e. relative to $\emptyset'$.

  The complement is $\Sigma^0_2$, which by item 1 means $\emptyset'$-c.e.
- [ ] A set is $\Pi^0_2$ if and only if it is computable in $\emptyset'$.

  The $\Pi^0_2$-complete sets, such as $\mathrm{Tot}$, are not computable in $\emptyset'$. The sets computable in $\emptyset'$ are the $\Delta^0_2$ sets.
- [ ] Every $\Sigma^0_2$ set is Turing equivalent to $\emptyset''$.

  Computable sets are $\Sigma^0_2$. Only the $\Sigma^0_2$-complete sets are equivalent to $\emptyset''$.

---

Which of these sets are $\Delta^0_2$?

- [x] $\emptyset'$.

  It is $\Sigma^0_1$, hence $\Delta^0_2$.
- [x] Every d.c.e. set $B \setminus C$, with $B$ and $C$ c.e.

  It is the intersection of a $\Sigma^0_1$ set and a $\Pi^0_1$ set, both $\Delta^0_2$.
- [ ] $\mathrm{Tot}$.

  It is $\Pi^0_2$-complete (next lesson), hence not $\Sigma^0_2$; equivalently, it is not computable in $\emptyset'$.
- [ ] $\nat \setminus \emptyset''$.

  It is $\Pi^0_2$ and not $\Sigma^0_2$, by :ref{#cor-hierarchy-strict}.
:::

## Exercises

::::exercise{difficulty=1}
Show that the set $\{ e : \Phi^{\emptyset'}_e \text{ is total} \}$ is $\Pi^0_3$.

:::solution
It is $\{ e : \forall x\ \exists s\ \Phi^{\emptyset'}_e(x)[s]\converge \}$, a $\Pi^0_2(\emptyset')$ set, since the relation $\Phi^{\emptyset'}_e(x)[s]\converge$ is $\emptyset'$-computable. Its complement is $\Sigma^0_2(\emptyset')$, that is, c.e. in $\emptyset'' = (\emptyset')'$ by :ref{#thm-post} relativized to $\emptyset'$, and hence $\Sigma^0_3$ by the theorem unrelativized. So the set is $\Pi^0_3$.
:::
::::

::::exercise{difficulty=2}
Show that $X \leq_T Y$ if and only if $X' \leq_m Y'$.

:::solution
If $X \leq_T Y$, then $X' \leq_1 Y'$ by :ref{#thm-jump}. Conversely, let $h$ be a many-one reduction of $X'$ to $Y'$. For $i \in \{0, 1\}$, let $a_i$ be an index such that $W^Z_{a_i} = \{ n : Z(n) = i \}$ for every oracle $Z$, and let $g_i$ be the computable function given by :ref{#thm-jump}, with $Z(n) = i \iff g_i(n) \in Z'$ for every $Z$. Then $X(n) = i \iff h(g_i(n)) \in Y'$. The two sets $\{ n : h(g_0(n)) \in Y' \}$ and $\{ n : h(g_1(n)) \in Y' \}$ are $Y$-c.e., and they are complementary, since they are $\{ n : X(n) = 0 \}$ and $\{ n : X(n) = 1 \}$. Hence $X$ is $Y$-computable.
:::
::::

::::exercise{difficulty=2}
Show that a set $A$ is $\Sigma^0_2$ if and only if $A = \{ x : \exists y\ \forall z \geq y\ \ g(x, z) = 1 \}$ for some total computable function $g : \nat^2 \to \{0, 1\}$.

:::solution
A set of this form is $\Sigma^0_2$. Conversely, let $A = \{ x : \exists y\ \forall z\ R(x, y, z) \}$ with $R$ computable. Define $g(x, s) = 1$ if there is $y < s$ such that $R(x, y, z)$ holds for all $z < s$, and in addition the least such $y$ is the same as at stage $s - 1$; and $g(x, s) = 0$ otherwise. If $x \in A$, let $y_0$ be the least $y$ with $\forall z\ R(x, y, z)$; every $y < y_0$ eventually fails at some $z$, so from some stage on the least candidate below $s$ is $y_0$, and $g(x, s) = 1$ for all large $s$. If $x \notin A$, every candidate $y$ eventually fails, so the least candidate changes infinitely often, or there is no candidate, and $g(x, s) = 0$ for infinitely many $s$.
:::
::::

## Notes and references

The theorem is due to Post, announced in 1948, and its proof is in Kleene's *Introduction to Metamathematics*. Its modern formulation in terms of the jump follows Kleene and Post (1954). The characterization of $\Sigma^0_2$ sets in the last exercise is the starting point of the use of "infinitely often" and "cofinitely often" conditions in constructions below $\emptyset''$.

- E. L. Post, *Degrees of recursive unsolvability (preliminary report)*, Bulletin of the American Mathematical Society 54 (1948), 641–642.
- S. C. Kleene, *Introduction to Metamathematics*, North-Holland, 1952.
- S. C. Kleene and E. L. Post, *The upper semi-lattice of degrees of recursive unsolvability*, Annals of Mathematics 59 (1954), 379–407.
