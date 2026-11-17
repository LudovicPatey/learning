---
title: Random sequences and c.e. sets
summary: A c.e. set that computes a Martin-Löf random sequence is Turing complete (Kučera); a fixed-point free function computable in ∅′ computes a non-computable c.e. set (Kučera), which gives an injury-free solution to Post's problem.
duration: 35
prerequisites: [martin-lof-randomness/random-dnc, immunity-growth/arslanov, kolmogorov-complexity/kc-theorem, randomness-notions/weak-2-randomness]
---

Random sequences and c.e. sets interact in two opposite ways. On the one hand, a random sequence cannot be computed from a c.e. set unless the c.e. set is complete: the only c.e. degree above a random degree is $\mathbf 0'$. On the other hand, a random sequence computable in $\emptyset'$ computes a non-computable c.e. set, and if the random sequence is low, so is the c.e. set. With a low random sequence, which exists by the low basis theorem, this gives a solution to Post's problem without the priority method. Both theorems are due to Kučera.

The first theorem is proved with the KC theorem. If a random sequence $A = \Psi^B$ is computed from a c.e. set $B$, every number entering $\emptyset'$ is answered by a short description of the current approximation of $A$; since $A$ is random, the true $A$ must differ from this approximation, so $B$ must change below the use of the computation. Hence $B$ cannot settle before $\emptyset'$ does. The second theorem uses the fixed point theorem: a c.e. set is built that copies, at well-chosen moments, the c.e. sets whose indices are given by a fixed-point free function, and the fact that this function has no fixed point bounds the stages at which elements can enter the set, which makes the set computable from the function.

## A c.e. set above a random sequence is complete

:::theorem[Kučera]{#thm-kucera-ce-random}
Let $A$ be a Martin-Löf random sequence and $B$ a c.e. set with $A \leq_T B$. Then $\emptyset' \leq_T B$. If moreover $A \leq_{wtt} B$, then $\emptyset' \leq_{wtt} B$.
:::

:::proof{of=thm-kucera-ce-random}
Let $\Psi$ be a Turing functional with $\Psi^B = A$, $(B_s)$ an enumeration of $B$, and $c$ a constant with $K(A \uh m) > m - c$ for every $m$, by the Levin–Schnorr theorem (:ref{#thm-levin-schnorr}). For a number $m$ and a stage $t$, write $A_t \uh m$ for the string $\Psi^{B_t} \uh m [t]$ when the computations $\Psi^{B_t}(i)[t]$, $i < m$, all converge, and $u_t(m)$ for the largest use of these computations.

*Request sets.* For each $d$, let $k_d = c + 2d + 1$, and let $R_d$ be the set of requests $(A_t \uh (n + k_d),\ n + 1 + d)$ for the pairs $(n, t)$ such that $n$ enters $\emptyset'$ at stage $t$ and $A_t \uh (n + k_d)$ is defined. Each $n$ contributes at most one request, so the weight of $R_d$ is at most $\sum_n 2^{-n-1-d} = 2^{-d}$. The sets $R_d$ are uniformly c.e. By :ref{#ex-request-weight}, there is a constant $b$ with
$$
K(\sigma) \leq \ell + b \quad \text{for every } d \text{ and every } (\sigma, \ell) \in R_d.
$$
Fix $d = b$ and $k = k_b = c + 2b + 1$.

*The reduction.* Given $n$, with oracle $B$, search for a stage $s \geq n$ such that $A_s \uh (n + k)$ is defined and $B_s \uh u_s(n + k) = B \uh u_s(n + k)$. Such a stage exists: the true computations $\Psi^B(i)$, $i < n + k$, have finite uses, and once $B_s$ agrees with $B$ below them, they appear at stage $s$, for $s$ large. Answer "$n \in \emptyset'$" if and only if $n \in \emptyset'_s$.

*Correctness.* Suppose that $n$ enters $\emptyset'$ at a stage $t > s$. Since $B$ is c.e. and $B_s$ already agrees with $B$ below $u = u_s(n + k)$, $B_t \uh u = B_s \uh u$, and the computations seen at stage $s$ are still present at stage $t$; so $A_t \uh (n + k) = A_s \uh (n + k) = A \uh (n + k)$. The request $(A \uh (n + k), n + 1 + b)$ is in $R_b$, so
$$
K(A \uh (n + k)) \leq n + 1 + 2b = (n + k) - c,
$$
which contradicts the choice of $c$. So $n \in \emptyset'$ if and only if $n \in \emptyset'_s$.

*Weak truth-table case.* If the use of $\Psi^X(i)$ is bounded by $\gamma(i)$ for a computable $\gamma$, the reduction only reads $B$ below $\max_{i < n + k} \gamma(i)$, a computable bound.
:::

:::quiz[Kučera's completeness theorem]
In the proof of :ref{#thm-kucera-ce-random}, why are the requests issued for every $d$, with $k_d$ depending on $d$, instead of a single request set?

- [x] The constant $b$ given by the KC theorem depends on the request set, which depends on $k$; running the construction for every $d$ with weights $2^{-d}$ gives one constant $b$ for all of them, and then $d = b$ can be chosen. This replaces an application of the fixed point theorem.
- [ ] Because $\emptyset'$ has infinitely many elements.

  Each request set already handles all elements of $\emptyset'$, with one request per element.
- [ ] To make the weight of each request set at most $1$.

  A single request set with lengths $n + 1$ already has weight at most $1$; the parameter $d$ is there to break the circularity between $k$ and $b$.

---

Where is it used that $B$ is c.e.?

- [x] Once $B_s$ agrees with $B$ below the use $u$, it never changes below $u$ again, so the computations seen at stage $s$ persist at every later stage $t$, and the request made at stage $t$ concerns the true $A \uh (n + k)$.
- [ ] To make the request sets c.e.

  They are c.e. for any computable approximation of $B$; the point is that the approximation does not return to old values.
- [ ] To compute the stage $s$ from $B$.

  Finding $s$ uses the oracle $B$, but this would work for any approximable $B$; the persistence of computations is what needs enumerability.
:::

So a random sequence is computable from a c.e. set only if the set is complete. In particular, a random sequence of c.e. degree is Turing equivalent to $\emptyset'$, which was obtained differently in :ref{#ex-random-ce-complete}, from Arslanov's completeness criterion; and a random left-c.e. real, being of c.e. degree, is Turing complete.

## Kučera's solution to Post's problem

The second theorem goes in the other direction: random sequences below $\emptyset'$ compute non-computable c.e. sets. It applies to every fixed-point free function computable in $\emptyset'$, and random sequences compute such functions (:ref{#cor-random-dnc}, :ref{#thm-dnc-fpf}). We use fixed-point free functions in the form given by :ref{#ex-fpf-ce-indices}: total functions $f$ with $W_{f(e)} \neq W_e$ for every $e$.

:::theorem[Kučera]{#thm-kucera-post}
Let $f \leq_T \emptyset'$ be a total function with $W_{f(e)} \neq W_e$ for every $e$. Then there is a simple c.e. set $B \leq_T f$. In particular, $B$ is not computable.
:::

The set $B$ must meet every infinite c.e. set $W_e$, and is built by putting into $B$ an element of $W_e$ at a stage when the approximation $f_s(i)$ of $f$ at a number $i$ looks stable. To compute $B$ from $f$, we need to know that elements entering late do not enter at all: if an element $x$ entered $B$ after the true value $f(i)$ is visible, the construction makes $W_i$ equal to $W_{f(i)}$, which is impossible. The number $i$ is chosen by the fixed point theorem so that the construction can define $W_i$ itself.

:::proof{of=thm-kucera-post}
Let $(f_s)$ be a computable approximation of $f$, by the limit lemma (:ref{#thm-limit-lemma}). For numbers $i$ and $e$, let $P(i, e)$ be the following search: find the least stage $s$ such that some $x > \max(2e, i)$ is enumerated into $W_e$ at stage $s$, that is $x \in W_{e, s} \setminus W_{e, s-1}$, and $f_t(i) = f_s(i)$ for every $t$ with $x \leq t \leq s$; take the least such $x$. If the search succeeds, $P(i, e)$ outputs the pair $(x, s)$.

By SMN, there is a total computable function $g$ such that $W_{g(i, e)} = W_{f_s(i)}$ if $P(i, e)$ outputs $(x, s)$, and $W_{g(i, e)} = \emptyset$ if the search fails: the c.e. set $W_{g(i, e)}$ waits for the search to succeed, then enumerates $W_{f_s(i)}$. By the fixed point theorem with parameters (:ref{#thm-fixed-point-parameters}), applied to $(e, n) \mapsto g(n, e)$, there is a total computable $h$ with $\Phi_{h(e)} = \Phi_{g(h(e), e)}$, hence $W_{h(e)} = W_{g(h(e), e)}$, for every $e$. Let
$$
B = \{ x : P(h(e), e) \text{ outputs } (x, s) \text{ for some } e \text{ and } s \}.
$$
It is c.e., since the searches $P(h(e), e)$ can be run in parallel.

*$B$ is coinfinite.* Each $e$ contributes at most one element, and it is larger than $2e$. So $B$ has at most $n$ elements below $2n$, and its complement is infinite.

*$B$ meets every infinite $W_e$.* Let $W_e$ be infinite, and let $u$ be a stage after which $f_t(h(e)) = f(h(e))$. Some $x > \max(2e, h(e), u)$ enters $W_e$ at some stage $s \geq x$, and then $f_t(h(e)) = f_s(h(e))$ for all $t \in [x, s]$, since $x > u$. So the search $P(h(e), e)$ succeeds, and puts an element of $W_e$ into $B$. So $B$ is simple, hence not computable.

*$B \leq_T f$.* Let $q(x)$ be the least stage $q > x$ with $f_q(y) = f(y)$ for every $y \leq x$; it is computable from $f$, by searching. We claim that $x \in B$ if and only if $x$ is put into $B$ by a search $P(h(e), e)$ ending at a stage $s \leq q(x)$. This is decidable once $q(x)$ is known: only the numbers $e < x/2$ are relevant, since an element put into $B$ by $P(h(e), e)$ is larger than $2e$, and their searches are run up to stage $q(x)$. Suppose that $P(h(e), e)$ outputs $(x, s)$ with $s > q(x)$. Then $x < q(x) < s$, so $f_{q(x)}(h(e)) = f_s(h(e))$ by the definition of the search, and $f_{q(x)}(h(e)) = f(h(e))$ since $h(e) < x$. So
$$
W_{h(e)} = W_{g(h(e), e)} = W_{f_s(h(e))} = W_{f(h(e))},
$$
contradicting the hypothesis on $f$. This proves the claim, and $B \leq_T f$.
:::

:::corollary[Kučera]{#cor-kucera-post}
1. Every Martin-Löf random sequence $A \leq_T \emptyset'$ computes a simple c.e. set.
2. There is a low simple c.e. set, obtained without the priority method: by the low basis theorem, there is a low random sequence, and the c.e. set it computes is low.
:::

:::proof{of=cor-kucera-post}
A random sequence computes a DNC function by :ref{#cor-random-dnc}, hence a function $f$ with $W_{f(e)} \neq W_e$ by :ref{#ex-fpf-ce-indices}. If $A \leq_T \emptyset'$, then $f \leq_T \emptyset'$, and :ref{#thm-kucera-post} gives a simple c.e. set $B \leq_T f \leq_T A$. For (2), the random sequences form a $\Sigma^0_2$ class containing a non-empty $\Pi^0_1$ class $\{ X : K(X \uh n) \geq n - c \text{ for all } n \}$, for $c$ large (:ref{#cor-mlr-structure}); a low member $A$ of this class exists by :ref{#thm-low-basis}, and $B' \leq_T A' \equiv_T \emptyset'$.
:::

The two theorems together say that the random sequences below $\emptyset'$ bound non-computable c.e. sets, but that no random sequence lies below an incomplete c.e. set. The c.e. sets below a low random sequence are thus far from it in the Turing degrees: they are below it, never above. In the course on K-trivial sets, these c.e. sets reappear as the K-trivial sets that are computable from incomplete random sequences.

::::exercise{#ex-two-random-no-minimal-pair difficulty=2 objective="Combine Kučera's theorem with the construction of a c.e. set below two sets at once."}
Let $A_0, A_1 \leq_T \emptyset'$ be random. Admit the theorem of Ambos-Spies, Jockusch, Shore and Soare that the c.e. set $B$ built in the proof of :ref{#thm-kucera-post} can be made promptly simple, and that a promptly simple c.e. set $B_0$ and a non-computable c.e. set $B_1$ always compute a common non-computable c.e. set. Deduce that the Turing degrees of $A_0$ and $A_1$ do not form a minimal pair: some non-computable set is computable from both.

:::solution
By :ref{#cor-kucera-post} and the admitted strengthening, $A_0$ computes a promptly simple c.e. set $B_0$, and $A_1$ computes a simple, hence non-computable, c.e. set $B_1$. By the admitted theorem, there is a non-computable c.e. set $C \leq_T B_0, B_1$, so $C \leq_T A_0$ and $C \leq_T A_1$. (Kučera; Downey–Hirschfeldt, Corollary 8.8.3.)
:::
::::

## Notes and references

Both theorems are from Kučera's papers of 1985 and 1986. Kučera's original proof of the completeness theorem used Arslanov's criterion; the direct proof with the KC theorem is from Downey and Hirschfeldt (Theorem 8.2.1), who use the recursion theorem where we use a uniform family of request sets. The solution to Post's problem is Theorem 2.22.5 of Downey and Hirschfeldt, who prove the stronger conclusion that $B$ is promptly simple; Nies (Section 4.2) presents it among injury-free constructions of c.e. sets.

- A. Kučera, *Measure, $\Pi^0_1$-classes and complete extensions of PA*, in: Recursion Theory Week, Lecture Notes in Mathematics 1141, Springer, 1985, 245–259.
- A. Kučera, *An alternative, priority-free, solution to Post's problem*, in: Mathematical Foundations of Computer Science 1986, Lecture Notes in Computer Science 233, Springer, 1986, 493–500.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Sections 2.22, 8.2 and 8.8.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Section 4.2.

:::::exercises
::::exercise{#ex-kucera-not-wtt-incomplete difficulty=1 objective="Apply Kučera's theorem in its weak truth-table form."}
Show that no c.e. set $B$ with $\emptyset' \not\leq_{wtt} B$ is weak truth-table above a random sequence. Deduce that a c.e. set that is Turing complete but not weak truth-table complete computes random sequences, but none by a weak truth-table reduction.

:::solution
The first statement is the contrapositive of the weak truth-table case of :ref{#thm-kucera-ce-random}. If $B$ is c.e. and Turing complete, then $B$ computes $\Omega$, which is random; if $B$ is not weak truth-table complete, the first statement says that no random sequence is weak truth-table reducible to $B$.
:::
::::

::::exercise{#ex-random-delta2-noncomputable-ce difficulty=1 objective="Check the hypotheses of Kučera's theorem on examples."}
Let $A$ be random. Show that if $A \leq_T \emptyset'$, then the sets computable from $A$ include a non-computable c.e. set; and that if $A$ is weakly 2-random, they include no non-computable c.e. set. Why does this not contradict :ref{#cor-kucera-post}?

:::solution
The first statement is :ref{#cor-kucera-post} (1). The second is the theorem of Downey, Nies, Weber and Yu and Hirschfeldt and Miller (:ref{#thm-dnwy}). There is no contradiction, because a weakly 2-random sequence is not computable in $\emptyset'$: the class $\{ X \}$ of a $\Delta^0_2$ sequence $X$ is a null $\Pi^0_2$ class, so weak 2-randomness excludes every $\Delta^0_2$ sequence.
:::
::::

:::::
