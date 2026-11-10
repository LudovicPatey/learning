---
title: Iterating the jump along notations
summary: The H-sets, iterating the Turing jump along Kleene's notations; their basic reductions; Spector's uniqueness theorem; the hyperarithmetic sets and degrees.
duration: 35
prerequisites: [computable-ordinals/kleene-o]
---

The arithmetic sets are the sets computable in some finite jump $\emptyset^{(n)}$. To go further, one iterates the jump transfinitely: $\emptyset^{(\omega)} = \bigoplus_n \emptyset^{(n)}$, then $\emptyset^{(\omega + 1)} = (\emptyset^{(\omega)})'$, and so on. At limit stages, the iteration needs to know a sequence converging to the limit, which is exactly what a notation in $\mathcal O$ provides. The resulting sets $H_a$ are the **H-sets**, and the sets computable in some $H_a$ are the **hyperarithmetic** sets. Remarkably, the degree of $H_a$ depends only on the ordinal $|a|$, not on the notation.

## The H-sets

:::definition{#def-h-sets}
For $a \in \mathcal O$, the set $H_a$ is defined by transfinite recursion along $<_{\mathcal O}$:

1. $H_1 = \emptyset$;
2. $H_{2^b} = (H_b)'$;
3. $H_{3 \cdot 5^e} = \{ \langle u, v \rangle : u <_{\mathcal O} 3 \cdot 5^e \text{ and } v \in H_u \}$.
:::

At a limit notation $a = 3 \cdot 5^e$, the set $H_a$ gathers all the sets $H_u$ for $u <_{\mathcal O} a$, each in its own column. The definition is a recursion along the well-founded relation $<_{\mathcal O}$ restricted to $\{ u : u \leq_{\mathcal O} a \}$, so $H_a$ is well defined for every $a \in \mathcal O$.

:::proposition{#prop-h-sets-basic}
Let $a \in \mathcal O$.

1. If $b <_{\mathcal O} a$, then $H_b \leq_T H_a$, and even $H_b' \leq_T H_a$.
2. If $|a| = n$ is finite, then $H_a = \emptyset^{(n)}$. If $|a| = \omega$, then $H_a \equiv_T \emptyset^{(\omega)}$.
3. $H_a$ is not computable in any $H_b$ with $b <_{\mathcal O} a$.
:::

:::proof{of=prop-h-sets-basic}
1. By induction on $a$. If $a = 2^c$, then $b = c$ or $b <_{\mathcal O} c$; in the first case $H_b' = H_a$, in the second $H_b' \leq_T H_c \leq_T H_c' = H_a$ by the induction hypothesis. If $a = 3 \cdot 5^e$ and $b <_{\mathcal O} a$, then $b <_{\mathcal O} \Phi_e(n)$ for some $n$, so $2^b \leq_{\mathcal O} \Phi_e(n) <_{\mathcal O} a$: one checks by induction on $c \in \mathcal O$ that $b <_{\mathcal O} c$ implies $2^b \leq_{\mathcal O} c$. Then $H_b' = H_{2^b} = \{ v : \langle 2^b, v \rangle \in H_a \}$ is computable in $H_a$, as a column of $H_a$.
2. The only notation of $n$ is $2^{2^{\cdots^1}}$ with $n$ exponentiations, and the first case follows by induction. A notation of $\omega$ is $a = 3 \cdot 5^e$ with $|\Phi_e(m)| = k_m$ finite and increasing; the notations below $a$ are the notations of the finite ordinals, one for each $k$, and $H_a$ has columns $\emptyset^{(k)}$, indexed by these notations. The map from $k$ to the notation of $k$ is computable, so $H_a \equiv_T \emptyset^{(\omega)}$.
3. By (1), $H_b' \leq_T H_a$, so $H_a \leq_T H_b$ would give $H_b' \leq_T H_b$, contradicting :ref{#thm-jump}.
:::

The reductions in (1) are uniform: an index of a reduction of $H_b$ to $H_a$ can be computed from $a$ and $b$, by an effective version of the induction called **effective transfinite recursion**, which uses the recursion theorem as in :ref{#lem-notation-sum}.

:::quiz[H-sets]
Why does the definition of $H_{3 \cdot 5^e}$ use the c.e. relation $u <_{\mathcal O} 3 \cdot 5^e$ rather than only the sets $H_{\Phi_e(n)}$?

- [x] Both choices give the same Turing degree; gathering all $H_u$ below $a$ makes the reductions $H_u \leq_T H_a$ immediate, since each $H_u$ is a column.
- [ ] Because $\Phi_e(n)$ might not be in $\mathcal O$.

  For $3 \cdot 5^e \in \mathcal O$, every $\Phi_e(n)$ is a notation.
- [ ] Because the relation $<_{\mathcal O}$ is computable.

  It is only c.e. on initial segments, which suffices to describe the columns.

---

In :ref{#prop-h-sets-basic} (3), why can $H_a$ not be computed by $H_b$ for $b <_{\mathcal O} a$?

- [x] Because $H_a$ computes $H_b'$, and a set computing $H_b'$ cannot be computed by $H_b$.
- [ ] Because $|a| > |b|$.

  The comparison of ordinals alone does not give non-reducibility; the jump does.
- [ ] Because $H_a$ is not arithmetic.

  For finite $|a|$, $H_a$ is arithmetic; the argument is relative to $H_b$.
:::

## Spector's uniqueness theorem

A constructive ordinal has many notations, possibly incomparable for $<_{\mathcal O}$. Their H-sets nevertheless have the same Turing degree.

:::theorem[Spector]{#thm-spector-uniqueness}
If $a, b \in \mathcal O$ and $|a| \leq |b|$, then $H_a \leq_T H_b$. In particular, $|a| = |b|$ implies $H_a \equiv_T H_b$.
:::

The proof compares the two notations by effective transfinite recursion: one builds, computably in $H_b$, an embedding of the notations below $a$ into those below $b$, which requires deciding questions about $\mathcal O$ that are answered by the H-sets themselves. It is admitted here; see Sacks, *Higher Recursion Theory*, Section II.1, or Ash and Knight, *Computable Structures and the Hyperarithmetical Hierarchy*, Chapter 5.

By the theorem, for every computable ordinal $\alpha$, the degree $\obf^{(\alpha)} = \deg_T(H_a)$, for any $a$ with $|a| = \alpha$, is well defined. For finite $\alpha$ it is the degree of $\emptyset^{(\alpha)}$, and the map $\alpha \mapsto \obf^{(\alpha)}$ is strictly increasing on $\omega_1^{\mathrm{CK}}$.

## Hyperarithmetic sets

:::definition{#def-hyp}
A set is **hyperarithmetic** if it is computable in $H_a$ for some $a \in \mathcal O$. The class of hyperarithmetic sets is written $\mathrm{HYP}$.
:::

:::proposition{#prop-hyp-ideal}
$\mathrm{HYP}$ is a jump ideal containing every arithmetic set, and it is countable. For every hyperarithmetic set $X$, there is a hyperarithmetic set not computable in $X$.
:::

:::proof{of=prop-hyp-ideal}
If $X \leq_T H_a$ and $Y \leq_T H_b$, let $c$ be a notation for $\max(|a|, |b|)$, which is $a$ or $b$; by :ref{#thm-spector-uniqueness}, $X \oplus Y \leq_T H_c$. Closure under $\leq_T$ is clear, and $X' \leq_T H_a' = H_{2^a}$. The arithmetic sets are computable in the sets $H_a$ with $|a|$ finite. There are countably many notations. Finally $H_a' \not\leq_T H_a$.
:::

The jump ideal $\mathrm{HYP}$ is much larger than $\mathrm{ARITH}$, but it is not closed under all definable operations: $\mathcal O$ itself, which is $\Pi^1_1$, is not hyperarithmetic, since it computes every $H_a$, uniformly in $a$. The next lesson identifies the hyperarithmetic sets with the $\Delta^1_1$ sets.

## Exercises

::::exercise{difficulty=1}
Show that $\mathcal O$ computes every hyperarithmetic set, and that it is not hyperarithmetic.

:::solution
By the next lesson, each $H_a$ is $\Pi^1_1$, and every $\Pi^1_1$ set is many-one reducible to $\mathcal O$, which is $\Pi^1_1$-complete (a result admitted in :ref{to="computable-ordinals/trees-and-pi11"}); so $H_a \leq_T \mathcal O$, and every hyperarithmetic set is computable in $\mathcal O$. If $\mathcal O$ were hyperarithmetic, say $\mathcal O \leq_T H_a$, then $H_{2^a} \leq_T \mathcal O \leq_T H_a$, contradicting :ref{#prop-h-sets-basic} (3).
:::
::::

::::exercise{difficulty=2}
Let $a$ be a notation for $\omega \cdot 2$. Describe $H_a$ up to Turing equivalence in terms of $\emptyset^{(\omega)}$, and show that a set is computable in $H_a$ if and only if it is arithmetic in $\emptyset^{(\omega)}$.

:::solution
By :ref{#thm-spector-uniqueness}, $H_a \equiv_T \bigoplus_n (\emptyset^{(\omega)})^{(n)} = (\emptyset^{(\omega)})^{(\omega)}$, the ω-jump of $\emptyset^{(\omega)}$, using a notation for $\omega \cdot 2$ whose fundamental sequence is $\omega + n$. A set computable in it is computable in some $(\emptyset^{(\omega)})^{(n)}$, hence arithmetic in $\emptyset^{(\omega)}$, by Post's theorem relativized. Conversely, a set arithmetic in $\emptyset^{(\omega)}$ is computable in some finite jump of $\emptyset^{(\omega)}$, hence in $H_a$.
:::
::::

## Notes and references

Kleene (1955) introduced the hierarchy of H-sets; Davis and Mostowski had considered the iteration of the jump. Spector (1955) proved the uniqueness theorem. The theory is developed in Sacks's monograph and in Ash and Knight's book, which applies it to computable structures.

- S. C. Kleene, *Hierarchies of number-theoretic predicates*, Bulletin of the American Mathematical Society 61 (1955), 193–213.
- C. Spector, *Recursive well-orderings*, Journal of Symbolic Logic 20 (1955), 151–163.
- C. J. Ash and J. F. Knight, *Computable Structures and the Hyperarithmetical Hierarchy*, Elsevier, 2000.
