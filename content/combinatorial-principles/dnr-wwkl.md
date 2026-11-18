---
title: DNC functions and weak weak König's lemma
summary: The principle DNR and weak weak König's lemma WWKL, for trees of positive measure; WKL₀ implies WWKL₀, which implies DNR (Giusto, Simpson); the ω-models of WWKL₀ are those containing, for each set, a set random relative to it; WWKL₀ does not imply WKL₀ (Yu, Simpson), by Stephan's theorem; where DNR, WWKL₀ and Ramsey's theorem for pairs stand with respect to each other.
duration: 35
prerequisites: [orders, immunity-growth/dnc-functions, randomness-degrees/stephan-theorem, randomness-degrees/almost-every-degree, randomness-notions/relative-randomness]
---

The principles of the previous lessons are combinatorial consequences of Ramsey's theorem. This lesson turns to two principles that come from weak König's lemma by weakening it: the existence of diagonally non-computable functions, and the existence of paths through trees that are large in the sense of measure. They are linked to algorithmic randomness: a random sequence computes a DNC function, and the ω-models of weak weak König's lemma are exactly those closed under taking relatively random sequences. Ramsey's theorem for pairs also implies the first principle and not the second, so these principles measure a part of the strength of $\mathsf{RT}^2_2$ that is common with $\mathsf{WKL}_0$.

## DNC functions in second-order arithmetic

Recall that a function $f$ is DNC relative to $X$ if $f(e) \neq \Phi^X_e(e)$ for every $e$ such that $\Phi^X_e(e)\converge$ (:ref{#def-dnc}). In $\mathsf{RCA}_0$, the relation $\Phi^X_e(e)\converge = m$ is expressed by a $\Sigma^0_1$ formula (:ref{to="second-order-arithmetic/rca0"}).

:::definition{#def-dnr}
$\mathsf{DNR}$ is the statement: for every set $X$, there is a function $f$ that is DNC relative to $X$.
:::

An ω-model satisfies $\mathsf{DNR}$ if and only if each of its members $X$ is accompanied by a function DNC relative to $X$. So $\mathrm{REC}$ is not a model, since no computable function is DNC, and $\mathsf{RCA}_0$ does not prove $\mathsf{DNR}$. In the other direction, $\mathsf{WKL}_0$ proves $\mathsf{DNR}$: the binary tree of strings $\sigma$ such that $\sigma(e) \neq \Phi^X_e(e)[|\sigma|]$ for every $e < |\sigma|$ at which the computation has converged by stage $|\sigma|$ is $X$-computable and infinite, and its paths are $\{0, 1\}$-valued DNC functions relative to $X$. The point of $\mathsf{DNR}$ is that it asks for much less: a DNC function need not compute a $\{0,1\}$-valued one. For instance, a low random sequence computes a DNC function (:ref{#cor-random-dnc}) but no PA set, by Stephan's theorem (:ref{#thm-stephan}), since it does not compute $\emptyset'$.

## Trees of positive measure

The measure of the class of paths of a binary tree $T$ is the limit of the proportions $|T \cap 2^n| / 2^n$, which are non-increasing. In second-order arithmetic, one avoids the limit.

:::definition{#def-wwkl}
A tree $T \subseteq \bstr$ has **positive measure** if there is a rational $q > 0$ such that $|T \cap 2^n| \geq q \cdot 2^n$ for every $n$. **Weak weak König's lemma** $\mathsf{WWKL}$ states that every tree of positive measure has an infinite path. $\mathsf{WWKL}_0$ is $\mathsf{RCA}_0 + \mathsf{WWKL}$.
:::

A tree of positive measure is infinite, so $\mathsf{WKL}_0$ proves $\mathsf{WWKL}_0$. In ω-models, the instances of $\mathsf{WWKL}$ are the $\Pi^0_1$ classes of positive measure, relative to the members of the model: a $\Pi^0_1(X)$ class $\mathcal P$ of positive measure is the class of paths of an $X$-computable tree $T$, and then $|T \cap 2^n| / 2^n \geq \lambda(\mathcal P) > 0$ for every $n$.

:::example{#ex-wwkl-instances}
1. Let $(\mathcal U_n)$ be a universal Martin-Löf test. The complement of $\mathcal U_1$ is a $\Pi^0_1$ class of measure at least $\frac12$ consisting of random sequences (:ref{#cor-mlr-structure}). It is the class of paths of the computable tree $T$ of the strings $\sigma$ none of whose prefixes is enumerated into a generator of $\mathcal U_1$ by stage $|\sigma|$, and $|T \cap 2^n| \geq \frac12 2^n$. No random sequence is computable, so $T$ has no computable path, and $\mathrm{REC} \not\models \mathsf{WWKL}$.
2. The tree of strings $\sigma$ with $\sigma(2k) = 0$ for all $2k < |\sigma|$ has measure $0$: $|T \cap 2^n| = 2^{\lfloor n/2 \rfloor}$. It is an instance of $\mathsf{WKL}$, not of $\mathsf{WWKL}$.
:::

:::theorem[Giusto, Simpson]{#thm-wwkl-dnr}
Over $\mathsf{RCA}_0$, $\mathsf{WWKL}$ implies $\mathsf{DNR}$.
:::

**Intuition.** A random sequence computes a DNC function (:ref{#cor-random-dnc}). Here a crude version suffices: the value $f(e)$ is a block of $e + 2$ bits of a path, and the computation $\Phi^X_e(e)$, read as a string of length $e + 2$, can be avoided by removing one block, a proportion $2^{-e-2}$ of the space. All the removed proportions add up to at most $\frac12$.

:::proof{of=thm-wwkl-dnr}
We argue in $\mathsf{RCA}_0$. Fix a coding of binary strings by numbers. Let $X$ be a set, and let $T$ be the set of strings $\sigma$ such that for every $e$ with $e + 2 \leq |\sigma|$: if $\Phi^X_e(e)[|\sigma|]\converge$ and its value codes a string $\tau$ of length $e + 2$, then $\sigma \uh (e + 2) \neq \tau$. It exists by $\Delta^0_1$ comprehension, and it is a tree: the conditions imposed on a prefix of $\sigma$ are among those imposed on $\sigma$, since a computation that has converged by stage $|\sigma'|$ has converged by stage $|\sigma|$.

*Positive measure.* A string $\sigma$ of length $n$ is outside $T$ only if $\sigma \uh (e + 2) = \tau_e$ for some $e$ with $e + 2 \leq n$, where $\tau_e$ is the string of length $e + 2$ given by the computation $\Phi^X_e(e)$, if it has converged by stage $n$. For each $e$, at most $2^{n - e - 2}$ strings of length $n$ extend $\tau_e$. So at most $\sum_{e + 2 \leq n} 2^{n - e - 2} < 2^{n-1}$ strings of length $n$ are outside $T$, and $|T \cap 2^n| \geq \frac12 2^n$. This count is a bounded computation, carried out in $\mathsf{RCA}_0$ by $\Sigma^0_0$ induction on $n$.

*The DNC function.* By $\mathsf{WWKL}$, $T$ has a path $P$. Let $f(e)$ be the code of $P \uh (e + 2)$. Suppose $\Phi^X_e(e)\converge = m$. If $m$ codes a string $\tau$ of length $e + 2$, the computation has converged by some stage $s \geq e + 2$, and $P \uh s \in T$ gives $P \uh (e + 2) \neq \tau$, so $f(e) \neq m$. If $m$ does not code a string of length $e + 2$, then $f(e) \neq m$ trivially. So $f$ is DNC relative to $X$.
:::

:::quiz[the proof that WWKL implies DNR]
Why is $f(e)$ a block of $e + 2$ bits, rather than the single bit $P(e)$?

- [x] Because avoiding a prescribed value of a single bit removes half of the space for each $e$, and the tree would have measure $0$; avoiding a prescribed block of $e + 2$ bits removes a proportion $2^{-e-2}$, and these proportions add up to at most $\frac12$.
- [ ] Because a single bit cannot be compared with $\Phi^X_e(e)$.

  It can be: the tree of $\{0,1\}$-valued DNC functions does it, but that tree has measure $0$.
- [ ] Because $P$ is not $X$-computable.

  $P$ is not $X$-computable in general, but this does not explain the choice of blocks: $f$ is computed from $P$, and the issue is the measure of the tree.

---

In the proof, where would the argument fail if $T$ were defined with the full computation $\Phi^X_e(e)\converge$ instead of $\Phi^X_e(e)[|\sigma|]\converge$?

- [x] $T$ would be defined by a $\Pi^0_1$ condition on each string, not a bounded one, and would not exist by $\Delta^0_1$ comprehension.
- [ ] $T$ would not be a tree.

  It would still be closed under prefixes. The problem is its existence in $\mathsf{RCA}_0$.
- [ ] $T$ would have measure $0$.

  The count of removed strings would be the same, and even smaller at each length.
:::

## ω-models of WWKL₀ and randomness

:::theorem{#thm-wwkl-random}
An ω-model $\mathcal M$ satisfies $\mathsf{WWKL}_0$ if and only if for every $A \in \mathcal M$, some $X \in \mathcal M$ is Martin-Löf random relative to $A$.
:::

:::proof{of=thm-wwkl-random}
($\Rightarrow$) Let $A \in \mathcal M$, and let $\mathcal U$ be the first level of a universal Martin-Löf test relative to $A$. As in :ref{#ex-wwkl-instances} (1), relativized to $A$, its complement is the class of paths of an $A$-computable tree of positive measure, which belongs to $\mathcal M$. A path in $\mathcal M$ is random relative to $A$.

($\Leftarrow$) Let $T \in \mathcal M$ be a tree with $|T \cap 2^n| \geq q 2^n$ for all $n$. Its class of paths $\mathcal P$ is $\Pi^0_1(T)$ and has measure at least $q > 0$. Let $X \in \mathcal M$ be random relative to $T$. By Kučera's lemma relativized to $T$ (:ref{#lem-kucera-translate}), some translate of $X$, a sequence $n \mapsto X(n + k)$, belongs to $\mathcal P$. It is computable in $X$, hence in $\mathcal M$, and it is a path of $T$.
:::

:::corollary[Yu, Simpson]{#cor-wwkl-not-wkl}
There is an ω-model of $\mathsf{WWKL}_0$ that is not a model of $\mathsf{WKL}_0$. Consequently, $\mathsf{WWKL}_0$ does not prove $\mathsf{WKL}_0$.
:::

**Intuition.** Take the sets computable from the finite joins of the columns of a low random sequence. Each new column is random relative to the previous ones, so the model satisfies $\mathsf{WWKL}_0$. All the sets of the model are computable from a random sequence that does not compute $\emptyset'$, and such a sequence computes no PA set, by Stephan's theorem.

:::proof{of=cor-wwkl-not-wkl}
Let $Z$ be a low Martin-Löf random sequence (:ref{#cor-mlr-structure} (3)), with columns $Z^{[i]}$, and $Y_n = Z^{[0]} \oplus \cdots \oplus Z^{[n]}$. Let $\mathcal M$ be the class of sets computable in some $Y_n$. Since $Y_n \leq_T Y_{n+1}$, it is a Turing ideal, hence an ω-model of $\mathsf{RCA}_0$.

*$\mathcal M$ satisfies $\mathsf{WWKL}_0$.* By the proof of :ref{#ex-vl-columns} (2), the column $Z^{[n+1]}$ is random relative to a sequence that computes all the other columns, in particular $Y_n$; so it is random relative to $Y_n$, and relative to every $A \leq_T Y_n$, since a test relative to $A$ is a test relative to $Y_n$. Every $A \in \mathcal M$ is computable in some $Y_n$, and $Z^{[n+1]} \in \mathcal M$. By :ref{#thm-wwkl-random}, $\mathcal M \models \mathsf{WWKL}_0$.

*$\mathcal M$ does not satisfy $\mathsf{WKL}_0$.* Every ω-model of $\mathsf{WKL}_0$ contains a PA set (:ref{#prop-wkl-scott} (2)). Suppose $P \in \mathcal M$ is PA. Then $P \leq_T Y_n \leq_T Z$, so $Z$ is of PA degree and random, and $\emptyset' \leq_T Z$ by Stephan's theorem (:ref{#thm-stephan}). But $Z$ is low, so $\emptyset'' \leq_T Z' \leq_T \emptyset'$, which is false.
:::

So $\mathsf{WWKL}_0$ lies strictly between $\mathsf{RCA}_0$ and $\mathsf{WKL}_0$, and implies $\mathsf{DNR}$. Ambos-Spies, Kjos-Hanssen, Lempp and Slaman (2004) built an ω-model of $\mathsf{DNR}$ that is not a model of $\mathsf{WWKL}_0$, by a DNC function that computes no random sequence; we admit this. The chain
$$
\mathsf{WKL}_0 \;\Longrightarrow\; \mathsf{WWKL}_0 \;\Longrightarrow\; \mathsf{DNR}
$$
is thus strict, and corresponds to the chain of degrees: PA, computing a random sequence, computing a DNC function.

::::exercise{#ex-wwkl-dnr-models difficulty=1 objective="Recover the ω-model version of the Giusto–Simpson theorem from the characterization by randomness."}
Using :ref{#thm-wwkl-random} and :ref{#cor-random-dnc}, show directly that every ω-model of $\mathsf{WWKL}_0$ satisfies $\mathsf{DNR}$.

:::solution
Let $\mathcal M \models \mathsf{WWKL}_0$ and $A \in \mathcal M$. By :ref{#thm-wwkl-random}, some $X \in \mathcal M$ is random relative to $A$. By :ref{#cor-random-dnc} relativized to $A$, $X$ computes, together with $A$, a function DNC relative to $A$: the proof gives the function $n \mapsto X \uh (n + c)$, whose values have prefix-free complexity relative to $A$ at least $n$, and :ref{#thm-dnc-complexity} relativized to $A$ turns it into a DNC function relative to $A$, computably in $A \oplus X$. Since $A \oplus X \in \mathcal M$, the function is in $\mathcal M$.
:::
::::

## Ramsey's theorem for pairs, DNC functions and measure

Where does $\mathsf{RT}^2_2$ stand with respect to this chain? It implies $\mathsf{DNR}$: there is a computable coloring of pairs all of whose infinite homogeneous sets compute a DNC function (:ref{#cor-rt22-dnc}), a theorem of Hirschfeldt, Jockusch, Kjos-Hanssen, Lempp and Slaman (2008), who proved it over $\mathsf{RCA}_0$ even for $\mathsf{SRT}^2_2$. But it does not imply $\mathsf{WWKL}_0$, by Liu's theorem (:ref{#cor-rt22-not-wwkl}). Since $\mathsf{WKL}_0$ does not imply $\mathsf{RT}^2_2$ (:ref{#cor-wkl-not-rt22}), neither does $\mathsf{WWKL}_0$, and the two are incomparable. So $\mathsf{DNR}$ is a common consequence of $\mathsf{WKL}_0$ and $\mathsf{RT}^2_2$. The weaker principles $\mathsf{ADS}$ and $\mathsf{CAC}$ have no compactness at all: they do not imply $\mathsf{DNR}$, which is the subject of the next lesson.

## Notes and references

$\mathsf{WWKL}_0$ was introduced by Yu and Simpson (1990), who proved :ref{#cor-wwkl-not-wkl} by a different argument, and developed by Brown, Giusto and Simpson (2002) for measure theory; Giusto and Simpson (2000) proved :ref{#thm-wwkl-dnr}. The proofs follow Dzhafarov and Mummert, Section 9.11 (Theorem 9.11.2 and Corollaries 9.11.3, 9.11.6 and 9.11.9), and Hirschfeldt, Section 9.1 and Exercise 9.7. In the proof of :ref{#cor-wwkl-not-wkl}, the absence of PA sets is derived from the fact that all sets of the model are computable from a single low random sequence. The separation of $\mathsf{DNR}$ from $\mathsf{WWKL}_0$ is due to Ambos-Spies, Kjos-Hanssen, Lempp and Slaman (2004).

- X. Yu and S. G. Simpson, *Measure theory and weak König's lemma*, Archive for Mathematical Logic 30 (1990), 171–180.
- M. Giusto and S. G. Simpson, *Located sets and reverse mathematics*, Journal of Symbolic Logic 65 (2000), 1451–1480.
- K. Ambos-Spies, B. Kjos-Hanssen, S. Lempp and T. A. Slaman, *Comparing DNR and WWKL*, Journal of Symbolic Logic 69 (2004), 1089–1104.
- D. R. Hirschfeldt, C. G. Jockusch, B. Kjos-Hanssen, S. Lempp and T. A. Slaman, *The strength of some combinatorial principles related to Ramsey's theorem for pairs*, in *Computational Prospects of Infinity, Part II*, World Scientific, 2008, 143–161.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Section 9.11.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2014, Section 9.1.

:::::exercises
::::exercise{#ex-wwkl-threshold difficulty=2 objective="Use Kučera's lemma to show that the measure bound in WWKL can be fixed in advance in ω-models."}
For a rational $0 < q < 1$, let $q$-$\mathsf{WWKL}$ be the restriction of $\mathsf{WWKL}$ to trees with $|T \cap 2^n| \geq q 2^n$ for every $n$. Show that an ω-model satisfies $q$-$\mathsf{WWKL}$ if and only if it satisfies $\mathsf{WWKL}$.

:::solution
$\mathsf{WWKL}$ implies its restriction. Conversely, suppose $\mathcal M \models q$-$\mathsf{WWKL}$, and let $A \in \mathcal M$. Choose $k$ with $2^{-k} \leq 1 - q$, and let $\mathcal U_k$ be the $k$-th level of a universal Martin-Löf test relative to $A$. Its complement has measure at least $1 - 2^{-k} \geq q$, and it is the class of paths of the $A$-computable tree $T$ of strings with no prefix enumerated into a generator of $\mathcal U_k$ by stage $|\sigma|$; at each length $n$, the strings outside $T$ have total measure at most $\lambda(\mathcal U_k) \leq 2^{-k}$, so $|T \cap 2^n| \geq q 2^n$. A path of $T$ in $\mathcal M$ is random relative to $A$. By :ref{#thm-wwkl-random}, $\mathcal M \models \mathsf{WWKL}$. Dorais, Dzhafarov, Hirst, Mileti and Shafer proved the equivalence over $\mathsf{RCA}_0$ (Dzhafarov–Mummert, Theorem 9.11.12).
:::
::::

::::exercise{#ex-wwkl-low-model difficulty=1 objective="Build a model of WWKL₀ of low sets, and compare it with the low Scott ideal."}
Show that the ω-model $\mathcal M$ of the proof of :ref{#cor-wwkl-not-wkl} consists of low sets. Is it a Turing ideal of the form $\{ A : A \leq_T B \}$ for a single set $B$?

:::solution
Every $A \in \mathcal M$ is computable in the low set $Z$, so $A' \leq_T Z' \leq_T \emptyset'$, and $A$ is low. If $\mathcal M = \{ A : A \leq_T B \}$, then $B \in \mathcal M$, so $B \leq_T Y_n$ for some $n$, and $Z^{[n+1]} \leq_T B \leq_T Y_n$. But $Z^{[n+1]}$ is random relative to $Y_n$, and a sequence random relative to $Y_n$ is not computable in $Y_n$. So $\mathcal M$ is not principal.
:::
::::

::::exercise{#ex-wwkl-cone difficulty=2 objective="Show that WWKL admits cone avoidance, using Sacks's theorem on the measure of cones."}
Let $C$ be a non-computable set. Show that there is an ω-model of $\mathsf{WWKL}_0$ none of whose members computes $C$.

:::solution
By Sacks's theorem relativized (:ref{#thm-sacks}), for every $A \not\geq_T C$, the class of $X$ with $C \leq_T A \oplus X$ is null. The class of $X$ random relative to $A$ is conull. So some $X$, random relative to $A$, satisfies $C \not\leq_T A \oplus X$. Starting from $A_0 = \emptyset$, choose $X_n$ random relative to $A_n$ with $C \not\leq_T A_n \oplus X_n$, and let $A_{n+1} = A_n \oplus X_n$. The class $\mathcal M$ of sets computable in some $A_n$ is a Turing ideal avoiding $C$. For $A \leq_T A_n$, the set $X_n \in \mathcal M$ is random relative to $A_n$, hence relative to $A$. By :ref{#thm-wwkl-random}, $\mathcal M \models \mathsf{WWKL}_0$.
:::
::::

::::exercise{#ex-wkl-dnr difficulty=1 objective="Complete the proof that WKL₀ proves DNR by checking that the tree of the text is infinite in RCA₀."}
Let $X$ be a set, and $T$ the tree of strings $\sigma$ such that $\sigma(e) \neq \Phi^X_e(e)[|\sigma|]$ for every $e < |\sigma|$ at which the computation has converged by stage $|\sigma|$. Show in $\mathsf{RCA}_0$ that $T$ exists, is a tree, and has a string of every length. Deduce that $\mathsf{WKL}_0$ proves $\mathsf{DNR}$.

:::solution
The condition on $\sigma$ is bounded, with parameter $X$, so $T$ exists by $\Delta^0_1$ comprehension. If $\sigma' \preceq \sigma$ and $\sigma \in T$, every computation converged by stage $|\sigma'|$ has converged by stage $|\sigma|$, with the same value, so $\sigma' \in T$. For a length $n$, define $\sigma$ of length $n$ by $\sigma(e) = 1$ if $\Phi^X_e(e)[n]\converge = 0$, and $\sigma(e) = 0$ otherwise; it is in $T$, since $\sigma(e)$ differs from every value in $\{0, 1\}$ that the computation may have, and from any larger value trivially. So $T$ is an infinite binary tree. By $\mathsf{WKL}$, it has a path $P$. If $\Phi^X_e(e)\converge = m$, the computation has converged by some stage $s > e$, and $P \uh s \in T$ gives $P(e) \neq m$. So $P$ is DNC relative to $X$.
:::
::::
:::::
