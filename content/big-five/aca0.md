---
title: Arithmetic comprehension
summary: The system ACA₀; it is equivalent to Σ⁰₁ comprehension, to the existence of Turing jumps, and to the existence of ranges of injections; its ω-models are the jump ideals, and ARITH is the least one.
duration: 35
prerequisites: [second-order-arithmetic/rca0]
---

The system $\mathsf{ACA}_0$ adds to $\mathsf{RCA}_0$ the existence of every set defined by an arithmetic formula. It is the system of the Turing jump: a single application of comprehension to a $\Sigma^0_1$ formula already yields the halting problem relative to any set, and iterating it yields every arithmetic set. Its ω-models are the classes of sets closed under relative computability, join and jump. This lesson proves the equivalent forms of arithmetic comprehension that are used in reversals; the next lesson applies them to theorems of analysis and algebra and to König's lemma.

## The system and its equivalent forms

:::definition{#def-aca0}
$\mathsf{ACA}_0$ consists of the axioms of $\mathsf{RCA}_0$ together with the comprehension scheme for arithmetic formulas, possibly with set and number parameters.
:::

By :ref{#prop-induction-comprehension}, $\mathsf{ACA}_0$ proves the induction scheme for arithmetic formulas.

**Examples.** Each of the following sets exists in $\mathsf{ACA}_0$, by comprehension for the formula given; none of them is computable from the parameters in general.

- The jump $X' = \{ e : \Phi^X_e(e)\converge \}$ of a set $X$: a $\Sigma^0_1$ formula with parameter $X$.
- The set of nodes of a tree $T \subseteq \nat^{<\nat}$ that have infinitely many extensions in $T$: a $\Pi^0_2$ formula with parameter $T$.
- The set of indices $e$ such that $\Phi^X_e$ is total: a $\Pi^0_2$ formula.
- For a sequence of reals $(x_n)$, the set of rationals $q$ such that $q < x_n$ for some $n$: a $\Sigma^0_1$ formula, used to define suprema.

**Intuition for the equivalent forms.** In $\mathsf{RCA}_0$ a $\Sigma^0_1$ formula $\exists k\, \theta(n, k)$ cannot in general be turned into a set, since nothing bounds the search for a witness $k$. Three kinds of objects solve this problem uniformly: a set that answers all such questions at once (the jump), a comprehension axiom for these formulas, and a set that lists the numbers having a witness (the range of a function that enumerates them). The last form is the one used in reversals: it asks only for the range of a single injective function, a very simple object to encode into an instance of a theorem.

:::theorem{#thm-aca-equivalents}
The following are equivalent over $\mathsf{RCA}_0$:

1. $\mathsf{ACA}_0$;
2. $\Sigma^0_1$ comprehension;
3. for every set $X$, the jump $X' = \{ e : \Phi^X_e(e)\converge \}$ exists;
4. for every injective function $f : \nat \to \nat$, the range of $f$ exists.
:::

:::proof{of=thm-aca-equivalents}
(1 ⇒ 2), (2 ⇒ 3) and (2 ⇒ 4) are instances of comprehension: the jump and the range $\{ m : \exists i\ f(i) = m \}$ are defined by $\Sigma^0_1$ formulas.

(4 ⇒ 2) Let $\varphi(n) \equiv \exists k\, \theta(n, k)$ with $\theta$ bounded, possibly with parameters. Let $f(\langle n, k \rangle) = 2n + 1$ if $\theta(n, k)$ holds and no $k' < k$ satisfies $\theta(n, k')$, and $f(\langle n, k \rangle) = 2 \langle n, k \rangle$ otherwise. The function $f$ exists by $\Delta^0_1$ comprehension, and it is injective: an odd value $2n+1$ is taken at most once, at the least witness $k$, and an even value $2\langle n, k \rangle$ at most once. Its range $R$ exists by (4), and $\{ n : \varphi(n) \} = \{ n : 2n + 1 \in R \}$ exists by $\Delta^0_1$ comprehension.

(3 ⇒ 2) Let $\varphi(n)$ be $\Sigma^0_1$ with set parameters $A_1, \dots, A_k$, and $A = A_1 \oplus \cdots \oplus A_k$. By the formalized $s$-$m$-$n$ theorem, there is a primitive recursive $h$ such that $\Phi^A_{h(n)}(h(n))\converge$ if and only if $\varphi(n)$; so $\{ n : \varphi(n) \} = \{ n : h(n) \in A' \}$, which exists by $\Delta^0_1$ comprehension relative to $A'$.

(2 ⇒ 1) We show by induction on $m$ in the metatheory that $\Sigma^0_1$ comprehension proves $\Sigma^0_m$ comprehension. Let $\varphi(n) \equiv \exists k\, \psi(n, k)$ with $\psi$ a $\Pi^0_{m}$ formula. By $\Sigma^0_m$ comprehension applied to $\neg \psi$, which is equivalent to a $\Sigma^0_m$ formula, the set $Y = \{ \langle n, k \rangle : \neg \psi(n, k) \}$ exists. Then $\{ n : \varphi(n) \} = \{ n : \exists k\, \langle n, k \rangle \notin Y \}$ exists by $\Sigma^0_1$ comprehension with parameter $Y$. Every arithmetic formula is equivalent to a $\Sigma^0_m$ formula for some $m$, by the prenex normal form.
:::

The proof of (2 ⇒ 1) uses $m$ applications of $\Sigma^0_1$ comprehension for a $\Sigma^0_m$ formula, each with the set produced by the previous one as a parameter. This is the formal counterpart of the fact that a $\Sigma^0_m$ set is computable from $\emptyset^{(m)}$, the $m$-th iterate of the jump. Provability does not count applications: $\mathsf{ACA}_0$ does not distinguish the levels of the arithmetic hierarchy. Finer notions of reducibility between theorems, such as Weihrauch reducibility, do.

The coding of (4 ⇒ 2) replaces a set with many witnesses by one with a single witness: only the least witness $k$ of $n$ produces the value $2n + 1$, and the other pairs are sent to even numbers, out of the way. The same device, an enumeration without repetitions, is the starting point of every reversal of the next lesson.

:::quiz[equivalents of ACA₀]
In (4 ⇒ 2) of :ref{#thm-aca-equivalents}, why are the values $2n + 1$ only taken at the least witness $k$?

- [x] To make $f$ injective: a number $n$ may have many witnesses $k$, and each would otherwise produce the value $2n + 1$.
- [ ] To make $f$ computable.

  Computability holds whether or not the least witness is used; the restriction ensures injectivity.
- [ ] Because only the least witness makes $\varphi(n)$ true.

  Every witness makes $\varphi(n)$ true; using only the least one ensures that the value $2n + 1$ is taken once.

---

In (3 ⇒ 2), why is the jump of the join $A = A_1 \oplus \cdots \oplus A_k$ used, rather than the jumps of the $A_i$ separately?

- [x] Because a $\Sigma^0_1$ formula may query several parameters in one search, so it defines a set that is c.e. relative to their join, and this set need not be computable from the separate jumps $A_1', \dots, A_k'$.
- [ ] Because the jump of a join is the join of the jumps.

  This is false in general: by the Sacks splitting theorem there are low sets $A_1, A_2$ whose join computes $\emptyset'$, so that $(A_1 \oplus A_2)'$ computes $\emptyset''$, while $A_1' \oplus A_2'$ is computable in $\emptyset'$.
- [ ] Because $\Delta^0_1$ comprehension accepts only one parameter.

  $\Delta^0_1$ comprehension accepts any finite number of parameters; the join is needed for the jump, not for comprehension.
:::

## ω-models

:::definition{#def-jump-ideal}
A **jump ideal** is a Turing ideal $\mathcal I$ such that $X' \in \mathcal I$ for every $X \in \mathcal I$.
:::

**Examples.** For every set $A$, the class $\{ X : X \leq_T A^{(n)} \text{ for some } n \}$ of sets arithmetic in $A$ is a jump ideal. The class $\{ X : X \leq_T \emptyset' \}$ is a Turing ideal, closed under join and Turing reducibility, but not a jump ideal: it contains $\emptyset'$ and not $\emptyset''$. More generally, a jump ideal is never of the form $\{ X : X \leq_T A \}$, since $A' \not\leq_T A$.

:::corollary{#cor-aca-jump-ideal}
An ω-model satisfies $\mathsf{ACA}_0$ if and only if it is a jump ideal. The class $\mathrm{ARITH}$ of arithmetic sets is the least ω-model of $\mathsf{ACA}_0$.
:::

:::proof{of=cor-aca-jump-ideal}
By :ref{#thm-rca-turing-ideal} and :ref{#thm-aca-equivalents} (3), using absoluteness (:ref{#prop-omega-absolute}): $Y$ is the jump of $X$ in the model if and only if $Y = X'$. A jump ideal contains $\emptyset^{(n)}$ for every $n$, hence every arithmetic set, and $\mathrm{ARITH}$ is a jump ideal by Post's theorem (:ref{#thm-post}).
:::

$\mathrm{REC}$ is not a jump ideal, so $\mathsf{RCA}_0$ does not prove $\mathsf{ACA}_0$. The ω-jump $\emptyset^{(\omega)} = \bigoplus_n \emptyset^{(n)}$ is not arithmetic, so $\mathsf{ACA}_0$ does not prove that it exists: the system of the next level, $\mathsf{ATR}_0$, does. The method of these two separations is the basic one of reverse mathematics: to show that a system does not prove a statement, exhibit an ω-model of the system in which the statement fails, and verify the failure by absoluteness.

:::quiz[ω-models of ACA₀]
Why does $\mathsf{ACA}_0$ not prove that $\emptyset^{(\omega)}$ exists?

- [x] Because $\mathrm{ARITH}$ is an ω-model of $\mathsf{ACA}_0$ that does not contain $\emptyset^{(\omega)}$, which is not arithmetic.
- [ ] Because $\emptyset^{(\omega)}$ is not definable in $\mathcal L_2$.

  It is definable, by a formula quantifying over sets; the issue is that arithmetic comprehension does not apply to such formulas.
- [ ] Because $\mathsf{ACA}_0$ has only arithmetic induction.

  The failure is witnessed in an ω-model, where induction holds fully.

---

Why is a jump ideal never of the form $\{ X : X \leq_T A \}$?

- [x] Because $A$ would belong to it, hence $A'$ as well, while $A' \not\leq_T A$.
- [ ] Because a jump ideal is uncountable.

  $\mathrm{ARITH}$ is a countable jump ideal.
- [ ] Because $\{ X : X \leq_T A \}$ is not closed under join.

  It is closed under join: $X, Y \leq_T A$ implies $X \oplus Y \leq_T A$. It fails to be closed under the jump.
:::

## Exercises

::::exercise{difficulty=1}
Show that $\mathsf{ACA}_0$ does not prove that there is a set $Y$ with $Y^{[0]} = \emptyset$ and $Y^{[n+1]} = (Y^{[n]})'$ for every $n$.

:::solution
The condition on $Y$ is expressed by the arithmetic formula $\forall e\, (e \notin Y^{[0]}) \wedge \forall n\, \forall e\, (e \in Y^{[n+1]} \leftrightarrow \Phi^{Y^{[n]}}_e(e)\converge)$. By absoluteness, a set $Y$ satisfying it in an ω-model has $Y^{[n]} = \emptyset^{(n)}$ for every $n$, so $Y$ computes every $\emptyset^{(n)}$ and is not arithmetic. So the statement fails in the ω-model $\mathrm{ARITH}$ of $\mathsf{ACA}_0$ (:ref{#cor-aca-jump-ideal}).
:::
::::

::::exercise{difficulty=1}
Show that for every set $A$, the class $\mathrm{ARITH}(A)$ of sets arithmetic in $A$, that is, Turing reducible to $A^{(n)}$ for some $n$, is the least ω-model of $\mathsf{ACA}_0$ containing $A$.

:::solution
$\mathrm{ARITH}(A)$ contains $A$. It is a Turing ideal: if $X \leq_T A^{(m)}$ and $Y \leq_T A^{(n)}$, then $X \oplus Y \leq_T A^{(\max(m, n))}$, and it is closed downwards under $\leq_T$. It is a jump ideal: if $X \leq_T A^{(n)}$, then $X' \leq_T A^{(n+1)}$, since the jump is monotone with respect to $\leq_T$. By :ref{#cor-aca-jump-ideal}, it is an ω-model of $\mathsf{ACA}_0$. Conversely, a jump ideal containing $A$ contains every $A^{(n)}$, by induction on $n$, and every set computable from one of them.
:::
::::

## Notes and references

The equivalence of (1), (2) and (4) is Simpson, Lemma III.1.3; the characterization of the ω-models and the minimality of $\mathrm{ARITH}$ are in Section VIII.1 (Corollary VIII.1.11). The arithmetic theorems of $\mathsf{ACA}_0$ are exactly those of Peano arithmetic: $\mathsf{ACA}_0$ is conservative over $\mathsf{PA}$, a result we admit (Simpson, Section IX.1, after Friedman 1976); it is discussed in the course on induction and conservation. Dzhafarov and Mummert, Section 5.6.1, and Hirschfeldt, Section 4.3, give the same equivalences.

- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009, Sections III.1, VIII.1 and IX.1.
- H. Friedman, *Systems of second order arithmetic with restricted induction, I, II*, abstracts, Journal of Symbolic Logic 41 (1976), 557–559.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Section 5.6.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2014, Sections 4.3 and 4.5.
