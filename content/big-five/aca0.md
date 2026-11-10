---
title: Arithmetic comprehension
summary: The system ACA₀; it is equivalent to Σ⁰₁ comprehension, to the existence of Turing jumps, and to the existence of ranges of injections; its ω-models are the jump ideals; the monotone convergence theorem and König's lemma are equivalent to ACA₀.
duration: 40
prerequisites: [second-order-arithmetic/analysis-in-rca0, pi01-classes/finitely-branching-trees]
---

The system $\mathsf{ACA}_0$ adds to $\mathsf{RCA}_0$ the existence of every set defined by an arithmetic formula. It is the system of the Turing jump: its ω-models are the classes of sets closed under relative computability, join and jump. Many classical theorems are equivalent to it: sequential compactness, the existence of limits of monotone sequences, König's lemma for finitely branching trees, the existence of bases of vector spaces and of maximal ideals in countable rings. The proofs of the reversals share a pattern: the theorem, applied to a well-chosen computable instance, yields the range of an arbitrary injection.

## The system and its equivalent forms

:::definition{#def-aca0}
$\mathsf{ACA}_0$ consists of the axioms of $\mathsf{RCA}_0$ together with the comprehension scheme for arithmetic formulas.
:::

By :ref{#prop-induction-comprehension}, $\mathsf{ACA}_0$ proves the induction scheme for arithmetic formulas.

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

The proof of (2 ⇒ 1) uses $m$ applications of $\Sigma^0_1$ comprehension for a $\Sigma^0_m$ formula. Provability does not count applications: $\mathsf{ACA}_0$ does not distinguish the levels of the arithmetic hierarchy. Finer notions of reducibility between theorems, such as Weihrauch reducibility, do.

:::definition{#def-jump-ideal}
A **jump ideal** is a Turing ideal $\mathcal I$ such that $X' \in \mathcal I$ for every $X \in \mathcal I$.
:::

:::corollary{#cor-aca-jump-ideal}
An ω-model satisfies $\mathsf{ACA}_0$ if and only if it is a jump ideal. The class $\mathrm{ARITH}$ of arithmetic sets is the least ω-model of $\mathsf{ACA}_0$.
:::

:::proof{of=cor-aca-jump-ideal}
By :ref{#thm-rca-turing-ideal} and :ref{#thm-aca-equivalents} (3), using absoluteness: $Y$ is the jump of $X$ in the model if and only if $Y = X'$. A jump ideal contains $\emptyset^{(n)}$ for every $n$, hence every arithmetic set, and $\mathrm{ARITH}$ is a jump ideal by Post's theorem (:ref{#thm-post}).
:::

$\mathrm{REC}$ is not a jump ideal, so $\mathsf{RCA}_0$ does not prove $\mathsf{ACA}_0$. The ω-jump $\emptyset^{(\omega)} = \bigoplus_n \emptyset^{(n)}$ is not arithmetic, so $\mathsf{ACA}_0$ does not prove that it exists: the system of the next level, $\mathsf{ATR}_0$, does.

:::quiz[equivalents of ACA₀]
In (4 ⇒ 2) of :ref{#thm-aca-equivalents}, why are the values $2n + 1$ only taken at the least witness $k$?

- [x] To make $f$ injective: a number $n$ may have many witnesses $k$, and each would otherwise produce the value $2n + 1$.
- [ ] To make $f$ computable.

  Computability holds whether or not the least witness is used; the restriction ensures injectivity.
- [ ] Because only the least witness makes $\varphi(n)$ true.

  Every witness makes $\varphi(n)$ true; the choice of one is a matter of counting.

---

Why does $\mathsf{ACA}_0$ not prove that $\emptyset^{(\omega)}$ exists?

- [x] Because $\mathrm{ARITH}$ is an ω-model of $\mathsf{ACA}_0$ that does not contain $\emptyset^{(\omega)}$, which is not arithmetic.
- [ ] Because $\emptyset^{(\omega)}$ is not definable in $\mathcal L_2$.

  It is definable, by a formula quantifying over sets; the issue is that arithmetic comprehension does not apply to such formulas.
- [ ] Because $\mathsf{ACA}_0$ has only arithmetic induction.

  The failure is witnessed in an ω-model, where induction holds fully.
:::

## Monotone convergence

:::theorem{#thm-monotone-aca}
Over $\mathsf{RCA}_0$, $\mathsf{ACA}_0$ is equivalent to the monotone convergence theorem: every bounded non-decreasing sequence of reals has a limit.
:::

:::proof{of=thm-monotone-aca}
($\Rightarrow$) Rescaling, we may assume $0 \leq x_n \leq 1$. By arithmetic comprehension, the set $S$ of rationals $q$ such that $x_n > q$ for some $n$ exists. For each $k$, let $q_k$ be the largest number of the form $j 2^{-k}$, with $-1 \leq j \leq 2^k$, that belongs to $S$; it exists since $-2^{-k} < x_0$, and the sequence $(q_k)$ exists by $\Delta^0_1$ comprehension relative to $S$. Some $x_n$ exceeds $q_k$, and no $x_n$ exceeds $q_k + 2^{-k}$: either $q_k + 2^{-k} \notin S$, or $q_k = 1$. For $k \leq l$, $q_k \leq q_l$, since $q_k$ is also of the form $j 2^{-l}$, and $q_l < q_k + 2^{-k}$, since some $x_n$ exceeds $q_l$. So $x = (q_k)$ is a real, with $q_k \leq x \leq q_k + 2^{-k}$. It is the limit: every $x_n$ satisfies $x_n \leq q_k + 2^{-k} \leq x + 2^{-k}$ for all $k$, hence $x_n \leq x$; and for each $k$ some $x_n > q_k \geq x - 2^{-k}$, so $x - x_m < 2^{-k}$ for all $m \geq n$, since the sequence is non-decreasing.

($\Leftarrow$) We prove (4) of :ref{#thm-aca-equivalents}. Let $f$ be injective, and $x_n = \sum_{i \leq n} 2^{-f(i)-1}$, as in :ref{#prop-specker}. It is non-decreasing and bounded by $1$; let $x$ be its limit. For each $m$, there is $n$ with $x - x_n < 2^{-m-1}$, and then $m$ is in the range of $f$ if and only if $m = f(i)$ for some $i \leq n$: an $i > n$ with $f(i) = m$ would give $x - x_n \geq 2^{-m-1}$. The function $m \mapsto n_m$, the least such $n$, is defined by a search whose termination is guaranteed, and the condition $x - x_n < 2^{-m-1}$ is $\Sigma^0_1$ in $x$; so the range is $\Delta^0_1$ in $f$ and $x$: $m \in \mathrm{ran}(f)$ if and only if $\exists i \leq n_m\ f(i) = m$, if and only if $\forall i\ (f(i) = m \rightarrow i \leq n_m)$. It exists by $\Delta^0_1$ comprehension.
:::

## König's lemma

A tree $T \subseteq \nat^{<\nat}$ is **finitely branching** if every node has finitely many immediate successors. **König's lemma** states that every infinite finitely branching tree has an infinite path. Weak König's lemma, the restriction to binary trees, is the subject of the next lesson. The computability-theoretic content of König's lemma was established in :ref{#thm-konig-strength}; the reverse mathematics version is the following.

:::theorem{#thm-konig-aca}
Over $\mathsf{RCA}_0$, $\mathsf{ACA}_0$ is equivalent to König's lemma.
:::

:::proof{of=thm-konig-aca}
($\Rightarrow$) Let $T$ be infinite and finitely branching. By arithmetic comprehension, the set $E$ of nodes of $T$ with infinitely many extensions in $T$ exists. The root belongs to $E$. If $\sigma \in E$, one of its finitely many immediate successors belongs to $E$: otherwise each of them has finitely many extensions, and so would $\sigma$, by arithmetic induction on the number of successors. Define the path $P$ by $P \uh 0 = \varepsilon$ and $P \uh (n+1) = $ the first immediate successor of $P \uh n$ in $E$, in the order of codes; this is a search relative to $T \oplus E$ that terminates, so $P$ exists by $\Delta^0_1$ comprehension.

($\Leftarrow$) We prove (4) of :ref{#thm-aca-equivalents}. Let $f$ be injective. Let $T$ be the set of sequences $\sigma \in \nat^{<\nat}$ such that, for every $m < |\sigma|$, either $\sigma(m) = i + 1$ with $f(i) = m$, or $\sigma(m) = 0$ and $f(i) \neq m$ for every $i < |\sigma|$. It is a tree, defined by a bounded formula, and each node has at most two immediate successors, since $f$ is injective. It is infinite: for each $n$, the sequence $\sigma$ of length $n$ with $\sigma(m) = i + 1$ if $f(i) = m$ for some $i < n$, and $\sigma(m) = 0$ otherwise, belongs to $T$. Let $P$ be a path. If $P(m) = i + 1$, then $f(i) = m$. If $P(m) = 0$, then $f(i) \neq m$ for every $i$, since $P \uh n \in T$ for every $n > i$. So $\mathrm{ran}(f) = \{ m : P(m) \neq 0 \}$, which exists by $\Delta^0_1$ comprehension.
:::

The tree in the reversal is finitely branching, but the bound on the number of successors of a node, $\sigma(m) \leq i + 1$ with $f(i) = m$, is not computable. For trees with a computable bound, or binary trees, the strength drops to weak König's lemma.

:::quiz[König's lemma]
In the reversal of :ref{#thm-konig-aca}, why does a path $P$ with $P(m) = 0$ guarantee that $m$ is not in the range of $f$?

- [x] Because every prefix $P \uh n$ belongs to $T$, and membership in $T$ with $P(m) = 0$ requires $f(i) \neq m$ for all $i < n$; as $n$ is arbitrary, $f(i) \neq m$ for all $i$.
- [ ] Because $f$ is injective.

  Injectivity bounds the branching of $T$; the conclusion comes from the infinitely many prefixes of the path.
- [ ] Because $0$ is the leftmost choice.

  The path need not be leftmost; any path works.

---

In the forward direction, where is arithmetic comprehension used?

- [x] To form the set $E$ of nodes with infinitely many extensions, defined by a $\Pi^0_2$ formula relative to $T$.
- [ ] To show that $T$ is infinite.

  This is the hypothesis.
- [ ] To define the path by a search.

  Given $E$, the path is computed by a search, which only requires $\Delta^0_1$ comprehension.
:::

## Exercises

::::exercise{difficulty=1}
Show that $\mathsf{ACA}_0$ does not prove that there is a set $Y$ with $Y^{[0]} = \emptyset$ and $Y^{[n+1]} = (Y^{[n]})'$ for every $n$.

:::solution
The condition on $Y$ is expressed by the arithmetic formula $\forall e\, (e \notin Y^{[0]}) \wedge \forall n\, \forall e\, (e \in Y^{[n+1]} \leftrightarrow \Phi^{Y^{[n]}}_e(e)\converge)$. By absoluteness, a set $Y$ satisfying it in an ω-model has $Y^{[n]} = \emptyset^{(n)}$ for every $n$, so $Y$ computes every $\emptyset^{(n)}$ and is not arithmetic. So the statement fails in the ω-model $\mathrm{ARITH}$ of $\mathsf{ACA}_0$ (:ref{#cor-aca-jump-ideal}).
:::
::::

::::exercise{difficulty=2}
The Bolzano–Weierstrass theorem states that every sequence of reals in $[0, 1]$ has a subsequence converging to some real. Show that it is equivalent to $\mathsf{ACA}_0$ over $\mathsf{RCA}_0$.

:::solution
($\Rightarrow$) With arithmetic comprehension relative to the sequence, define nested closed dyadic intervals $J_0 = [0, 1] \supseteq J_1 \supseteq \cdots$, with $J_k$ of length $2^{-k}$ containing $x_n$ for infinitely many $n$: take the left half of $J_k$ if it contains infinitely many terms, an arithmetic property, and the right half otherwise. By a search, choose $n_0 < n_1 < \cdots$ such that $x_{n_k}$ lies within $2^{-k}$ of $J_k$, a $\Sigma^0_1$ condition satisfied by infinitely many indices. The left endpoints of the $J_k$ form a real $x$, and $|x_{n_k} - x| \leq 2^{-k+2}$, so the subsequence converges to $x$.

($\Leftarrow$) We prove the monotone convergence theorem and apply :ref{#thm-monotone-aca}. Let $(x_n)$ be non-decreasing, rescaled into $[0, 1]$, and let $(x_{n_k})$ converge to $x$. Every $x_m$ satisfies $x_m \leq x$: otherwise, all terms $x_{n_k}$ with $n_k \geq m$ would be at least $x_m > x$, and could not converge to $x$. Given $\varepsilon > 0$, choose $k$ with $x - x_{n_k} < \varepsilon$; then $0 \leq x - x_m < \varepsilon$ for every $m \geq n_k$. So $x$ is the limit of the whole sequence.
:::
::::

## Notes and references

The equivalences of this lesson are in Simpson's monograph, Chapter III, which also covers vector spaces, ideals in countable rings and the Bolzano–Weierstrass theorem. The arithmetic theorems of $\mathsf{ACA}_0$ are exactly those of Peano arithmetic: $\mathsf{ACA}_0$ is conservative over $\mathsf{PA}$, a result we admit (Simpson, Section IX.1).

- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009.
- H. Friedman, *Systems of second order arithmetic with restricted induction*, abstracts, Journal of Symbolic Logic 41 (1976), 557–559.
