---
title: Martin-Löf tests
summary: Martin-Löf tests and Martin-Löf random sequences; why the definition requires uniformity and an effective rate; a universal test; random sequences form a conull Σ⁰₂ class, with low and computably dominated members.
duration: 40
prerequisites: [measure, pi01-classes/basis-theorems]
---

A sequence is random if it has no property that can be detected effectively and that only a null class of sequences shares. Martin-Löf (1966) made this precise by requiring the null class to be covered by open classes of measure at most $2^{-n}$, enumerated uniformly in $n$. The rate $2^{-n}$ allows all such tests to be combined into a single one, which is the main technical feature of the definition. This lesson introduces the tests, explains why each part of the definition is needed, and proves the existence of a universal test, from which the first properties of the class of random sequences follow.

## Tests

The definition follows the practice of statistics. A statistician who wants to reject the hypothesis that a sequence was produced by a fair coin chooses in advance a property of small probability, say at most $2^{-n}$, and rejects the hypothesis if the sequence has it; $2^{-n}$ is the **significance level**. A test in the sense of Martin-Löf is a family of such rejection regions, one for each level, given by a single algorithm. A sequence is random if no test rejects it at every level. The rejection regions are open classes, so that rejection is witnessed by a finite prefix of the sequence.

A sequence of classes $(\mathcal U_n)_{n \in \nat}$ is **uniformly $\Sigma^0_1$** if there is a c.e. set $W \subseteq \nat \times \bstr$ such that $\mathcal U_n = [W^{[n]}]^{\prec}$ for every $n$, where $W^{[n]} = \{ \sigma : (n, \sigma) \in W \}$. An index of $W$ is an **index** of the sequence.

:::definition[Martin-Löf]{#def-ml-test}
A **Martin-Löf test** is a uniformly $\Sigma^0_1$ sequence $(\mathcal U_n)$ with $\lambda(\mathcal U_n) \leq 2^{-n}$ for every $n$. A sequence $X$ is **captured** by the test if $X \in \bigcap_n \mathcal U_n$, and **passes** it otherwise. A sequence is **Martin-Löf random** if it passes every Martin-Löf test.
:::

The class $\bigcap_n \mathcal U_n$ captured by a test is a null $\Pi^0_2$ class, since its measure is at most $2^{-n}$ for every $n$. One may assume the test decreasing: the classes $\mathcal U_0 \cap \cdots \cap \mathcal U_n$ are uniformly $\Sigma^0_1$, decrease, satisfy the same bound, and have the same intersection. We write MLR for the class of Martin-Löf random sequences.

:::example{#ex-ml-tests}
1. A computable sequence $X$ is not random: $\mathcal U_n = [X \uh n]$ is a Martin-Löf test capturing $X$.
2. The covers of :ref{#ex-null-classes} are Martin-Löf tests. So a random sequence $X$ has $X(2i) \neq X(2i+1)$ for some $i$, is not a member of $\mathrm{DNC}_2$, and for every computable infinite set $A$, $X(a) = 1$ for some $a \in A$, hence for infinitely many, applying this to the tails of $A$.
:::

Each requirement of the definition is needed.

- **Uniformity.** If each $\mathcal U_n$ were only required to be $\Sigma^0_1$, with no single algorithm enumerating all of them, every sequence $X$ would be captured: the classes $\mathcal U_n = [X \uh n]$ are clopen, of measure $2^{-n}$, and contain $X$. The cover of a single sequence is always available; what the definition requires is that it be produced by an algorithm.
- **An effective rate.** If the measures were only required to tend to $0$, without a computable bound, the class captured would still be null, but more sequences would be captured. For example, a $\Delta^0_2$ sequence $X$ is captured by the classes $\mathcal U_n = \{ Y : Y \uh n = X_s \uh n \text{ for some } s \geq n \}$, where $(X_s)$ is a computable approximation of $X$: they are uniformly $\Sigma^0_1$, decrease to $\{ X \}$, and their measures tend to $0$, at a rate that is not computable in general. The resulting notion, **weak 2-randomness**, is strictly stronger than Martin-Löf randomness: Chaitin's $\Omega$ is $\Delta^0_2$, hence not weakly 2-random, and it is Martin-Löf random, as shown in the lesson on the Levin–Schnorr theorem (:ref{#cor-omega-random}). Weak 2-randomness is studied in the course on notions of randomness. With a computable bound, the rate itself does not matter, by :ref{#lem-test-bound} below.

The bound $2^{-n}$ can be replaced by any computable bound tending to $0$.

:::lemma{#lem-test-bound}
Let $(\mathcal V_m)$ be uniformly $\Sigma^0_1$, and let $(q_m)$ be a computable sequence of rationals with $\lambda(\mathcal V_m) \leq q_m$ and $\lim_m q_m = 0$. Then no Martin-Löf random sequence belongs to $\bigcap_m \mathcal V_m$.
:::

:::proof{of=lem-test-bound}
For each $n$, let $m_n$ be the least $m$ with $q_m \leq 2^{-n}$; it exists since $q_m$ tends to $0$, and is computable from $n$. The sequence $\mathcal U_n = \mathcal V_{m_n}$ is uniformly $\Sigma^0_1$, with $\lambda(\mathcal U_n) \leq 2^{-n}$, and $\bigcap_m \mathcal V_m \subseteq \bigcap_n \mathcal U_n$.
:::

## A universal test

There are countably many tests, and a countable union of null classes is null. The point of the next theorem is that the union can be taken effectively, and that it is again covered by a single test. Two obstacles must be overcome. One cannot decide which c.e. sets define tests, so every c.e. set is first trimmed into a test, in a way that leaves genuine tests unchanged; this is possible because the bound $2^{-n}$ is checked on finite approximations. Then the $e$-th test is used at a level shifted by $e + 1$, so that the measures add up to at most $2^{-n}$, as in the proof that a countable union of null classes is null.

:::theorem[Martin-Löf]{#thm-universal-test}
There is a Martin-Löf test $(\mathcal U_n)$ such that $\bigcap_n \mathcal U_n$ contains every class captured by a Martin-Löf test. So a sequence is Martin-Löf random if and only if it passes $(\mathcal U_n)$.
:::

:::proof{of=thm-universal-test}
Let $(W_e)$ be the standard enumeration of the c.e. subsets of $\nat \times \bstr$. Every Martin-Löf test is of the form $([W_e^{[n]}]^{\prec})_n$ for some $e$, but most indices $e$ do not define tests. We transform each $W_e$ into a test, without changing those that already are.

Fix $e$ and $n$, and let $\sigma_0, \sigma_1, \dots$ be the elements of $W_e^{[n]}$ in the order of their enumeration (the list may be finite). Define finite sets $F_0 = \emptyset$, and $F_{i+1} = F_i \cup \{ \sigma_i \}$ if $\lambda([F_i \cup \{ \sigma_i \}]^{\prec}) \leq 2^{-n}$, and $F_{i+1} = F_i$ otherwise. The measure of the open class generated by a finite set of strings is a rational computable from the set, so the sets $F_i$ are computable from $e$, $n$ and $i$. Let $\mathcal V^e_n = \bigcup_i [F_i]^{\prec}$. Then:

- $(\mathcal V^e_n)_n$ is uniformly $\Sigma^0_1$, uniformly in $e$;
- $\lambda(\mathcal V^e_n) \leq 2^{-n}$, as the supremum of the measures of the increasing classes $[F_i]^{\prec}$, each at most $2^{-n}$;
- if $\lambda([W_e^{[n]}]^{\prec}) \leq 2^{-n}$, then every $\sigma_i$ is accepted, since $[F_i \cup \{ \sigma_i \}]^{\prec} \subseteq [W_e^{[n]}]^{\prec}$; so $\mathcal V^e_n = [W_e^{[n]}]^{\prec}$.

So $(\mathcal V^e_n)_n$ is a Martin-Löf test for every $e$, and every Martin-Löf test is one of them. Let
$$
\mathcal U_n = \bigcup_e \mathcal V^e_{n + e + 1}.
$$
It is uniformly $\Sigma^0_1$, and $\lambda(\mathcal U_n) \leq \sum_e 2^{-n-e-1} = 2^{-n}$. If $X$ is captured by the test $(\mathcal V^e_m)_m$, then $X \in \mathcal V^e_{n+e+1} \subseteq \mathcal U_n$ for every $n$.
:::

:::quiz[the universal test]
In the proof of :ref{#thm-universal-test}, why is each $W_e$ trimmed into $(\mathcal V^e_n)$ before taking the union?

- [x] Because most c.e. sets do not define tests, and their classes may have large measure; trimming bounds every $\mathcal V^e_n$ by $2^{-n}$ while leaving genuine tests unchanged.
- [ ] Because the set of indices $e$ of Martin-Löf tests is c.e., and the trimming enumerates it.

  The trimming never decides whether $e$ defines a test; this set of indices is not c.e. Trimming makes every index define a test.
- [ ] Because $\bigcup_e [W_e^{[n]}]^{\prec}$ is not uniformly $\Sigma^0_1$.

  It is uniformly $\Sigma^0_1$; the problem is its measure, which is $1$ since some $W_e$ contains the empty string.

---

Why is the component $\mathcal V^e_{n+e+1}$, rather than $\mathcal V^e_n$, used in $\mathcal U_n$?

- [x] To make the measures summable: the $e$-th test contributes at most $2^{-n-e-1}$, and the total is at most $2^{-n}$.
- [ ] To make the classes decreasing.

  The tests need not be decreasing; the shift is for the measure bound.
- [ ] Because $\mathcal V^e_n$ is not defined for $n < e$.

  It is defined for every $n$ and $e$.
:::

## Consequences

:::corollary{#cor-mlr-structure}
Let $(\mathcal U_n)$ be a universal Martin-Löf test.

1. The class MLR is conull.
2. For every $n$, the complement $\mathcal P_n = \cs \setminus \mathcal U_n$ is a $\Pi^0_1$ class of measure at least $1 - 2^{-n}$ consisting of random sequences. So MLR $= \bigcup_n \mathcal P_n$ is a $\Sigma^0_2$ class.
3. There is a low Martin-Löf random sequence, and a computably dominated one.
:::

:::proof{of=cor-mlr-structure}
1. The complement of MLR is $\bigcap_n \mathcal U_n$, which is null.
2. The complement of a $\Sigma^0_1$ class is a $\Pi^0_1$ class (:ref{#prop-pi01-equivalent}). A sequence outside $\mathcal U_n$ is outside $\bigcap_m \mathcal U_m$, hence random by universality. A sequence is random if and only if it is outside $\bigcap_n \mathcal U_n$, that is, in some $\mathcal P_n$.
3. $\mathcal P_1$ is a non-empty $\Pi^0_1$ class, since its measure is at least $1/2$. Apply the low basis theorem (:ref{#thm-low-basis}) and the computably dominated basis theorem (:ref{#thm-dominated-basis}). Both theorems are proved by forcing with $\Pi^0_1$ classes.
:::

The two random sequences of (3) are very different. A computably dominated sequence that is not computable is not $\Delta^0_2$ (:ref{#def-computably-dominated}), whereas a low sequence is $\Delta^0_2$. The lesson on the Levin–Schnorr theorem shows that Chaitin's $\Omega$ is random, giving a random sequence of the degree of $\emptyset'$ (:ref{#cor-omega-random}).

## Exercises

::::exercise{difficulty=1}
Let $X$ be Martin-Löf random. Show that for every $k$, some block $X(ik) \cdots X(ik + k - 1)$ consists of zeros only. Deduce that $X$ contains arbitrarily long runs of zeros.

:::solution
Fix $k$, and let $\mathcal V_N$ be the clopen class of sequences none of whose first $N$ blocks of length $k$ is $0^k$. The blocks are independent: $\lambda(\mathcal V_N) = (1 - 2^{-k})^N$, which tends to $0$ and is a computable rational. The sequence $(\mathcal V_N)_N$ is uniformly $\Sigma^0_1$, so by :ref{#lem-test-bound} a random sequence is outside some $\mathcal V_N$: one of its first $N$ blocks is $0^k$.
:::
::::

::::exercise{#ex-tails difficulty=1}
Let $X$ be Martin-Löf random. Show that $\sigma X$ is random for every string $\sigma$, and that the tail $Y = X(1) X(2) \cdots$ is random.

:::solution
For an open class $\mathcal U = [W]^{\prec}$ and a string $\sigma$, write $\mathcal U_\sigma = \{ Z : \sigma Z \in \mathcal U \}$. Then $\mathcal U_\sigma = [\{ \tau : \text{some prefix of } \sigma\tau \text{ is in } W \}]^{\prec}$; this generating set is c.e., uniformly in an index of $W$ and in $\sigma$, when $W$ is c.e. (if some prefix of $\sigma$ is in $W$, it contains the empty string and $\mathcal U_\sigma = \cs$). So $\mathcal U_\sigma$ is $\Sigma^0_1$ uniformly in $\sigma$ and in an index of $\mathcal U$, and $\lambda(\mathcal U_\sigma) = 2^{|\sigma|} \lambda(\mathcal U \cap [\sigma])$, since $[\tau] \mapsto [\sigma\tau]$ divides measures by $2^{|\sigma|}$.

If $\sigma X$ is captured by $(\mathcal U_n)$, then $X$ belongs to every $(\mathcal U_n)_\sigma$, and $\lambda((\mathcal U_n)_\sigma) \leq 2^{|\sigma| - n}$; by :ref{#lem-test-bound}, $X$ is not random. For the tail, $X = iY$ with $i = X(0)$. If $Y$ is captured by $(\mathcal U_n)$, let $\mathcal V_n = \{ jZ : j \in \{0, 1\},\ Z \in \mathcal U_n \}$, a uniformly $\Sigma^0_1$ sequence with $\lambda(\mathcal V_n) = \lambda(\mathcal U_n)$; it captures $X$.
:::
::::

::::exercise{difficulty=1}
Show that no Martin-Löf random sequence, viewed as a set of numbers, is c.e. or co-c.e.

:::solution
A finite or cofinite set is computable, hence not random (:ref{#ex-ml-tests}). Let $X$ be infinite and c.e. It has an infinite computable subset $A$: enumerate $X$ and keep each element larger than all the elements kept before. Let $a_0 < a_1 < \cdots$ enumerate $A$, and let $\mathcal U_n$ be the clopen class of the sequences $Y$ with $Y(a_i) = 1$ for $i < n$. It has measure $2^{-n}$, is computable from $n$, and contains $X$; so $(\mathcal U_n)$ is a Martin-Löf test capturing $X$. If $X$ is co-c.e. and coinfinite, apply the same argument to its complement, with $Y(a_i) = 0$: the test obtained is the one of :ref{#ex-null-classes} (2).
:::
::::

## Notes and references

Martin-Löf (1966) introduced the tests and the universal test; the definition was meant to capture all effective statistical tests at once, the law of large numbers of :ref{to="martin-lof-randomness/solovay-tests"} being the first example. The existence of low and of computably dominated random sequences is an application of the basis theorems of Jockusch and Soare (1972). Weak 2-randomness, mentioned after :ref{#def-ml-test}, was introduced by Kurtz (1981). Downey and Hirschfeldt present Martin-Löf tests and the universal test in Section 6.2 (Definition 6.2.1, Theorem 6.2.5), and low random sets in Section 8.1; Nies does so in Section 3.2 (Definition 3.2.1, Fact 3.2.4, Proposition 3.2.5 for the $\Sigma^0_2$ class).

- P. Martin-Löf, *The definition of random sequences*, Information and Control 9 (1966), 602–619.
- C. G. Jockusch and R. I. Soare, *$\Pi^0_1$ classes and degrees of theories*, Transactions of the American Mathematical Society 173 (1972), 33–56.
- S. A. Kurtz, *Randomness and genericity in the degrees of unsolvability*, PhD thesis, University of Illinois at Urbana–Champaign, 1981.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Sections 6.2 and 8.1.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Section 3.2.
