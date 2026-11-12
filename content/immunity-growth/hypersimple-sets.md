---
title: Hypersimple sets and truth-table reducibility
summary: Dekker's deficiency sets give a hypersimple set in every non-zero c.e. degree; truth-table reductions are the Turing reductions that are total on every oracle; hypersimple sets can be Turing complete but not truth-table complete.
duration: 40
prerequisites: [immune-sets, pi01-classes/trees-and-classes]
---

Post tried to solve his problem, the existence of a c.e. set that is neither computable nor complete, by constructing c.e. sets with thinner and thinner complements: simple sets, then hypersimple sets. He showed that these thinness properties prevent completeness for reducibilities stronger than Turing reducibility, among them **truth-table reducibility**, which he introduced at the same time. This lesson shows that for Turing reducibility, thinness alone gives nothing: Dekker's construction finds a hypersimple set in every non-zero c.e. degree, including the degree of $\emptyset'$. It then studies truth-table reducibility, which reappears in :ref{to="immunity-growth/computably-dominated"}.

## Deficiency sets

Let $A$ be an infinite c.e. set, and let $a$ be a computable injective function with range $A$; $a(s)$ is the element enumerated at stage $s$. If $A$ is not computable, the enumeration cannot be increasing: small elements keep appearing late. Dekker's idea is to record the stages at which this happens. A stage $s$ is **deficient** if some element smaller than $a(s)$ is enumerated later:
$$
B = \{ s : \exists t > s\ \ a(t) < a(s) \}.
$$
The set $B$ is the **deficiency set** of the enumeration. A stage $s \notin B$ is **non-deficient**: every element enumerated after stage $s$ is larger than $a(s)$. At a non-deficient stage, the part of $A$ below $a(s)$ is already enumerated; for this reason Soare calls these stages **true stages**.

:::figure[An enumeration $a$ of a c.e. set, stage by stage. A stage is non-deficient when all later values are larger than its value (dashed lines). The values at the non-deficient stages increase, and below such a value the set is already enumerated.]
<svg class="fig" viewBox="0 0 600 322" width="600" role="img" aria-label="The values a(s) of an enumeration plotted against the stage s; the non-deficient stages, after which only larger values are enumerated, are highlighted and their values increase"><line x1="50" y1="276" x2="572" y2="276" class="axis"/><line x1="50" y1="276" x2="50" y2="36" class="axis"/><text x="578" y="280" class="math" font-size="14">s</text><text x="46" y="30" class="math" font-size="14">a<tspan class="mrm">(</tspan>s<tspan class="mrm">)</tspan></text><text x="60" y="292" text-anchor="middle" class="mrm muted" font-size="10">0</text><text x="92" y="292" text-anchor="middle" class="mrm muted" font-size="10">1</text><text x="124" y="292" text-anchor="middle" class="mrm muted" font-size="10">2</text><text x="156" y="292" text-anchor="middle" class="mrm muted" font-size="10">3</text><text x="188" y="292" text-anchor="middle" class="mrm muted" font-size="10">4</text><text x="220" y="292" text-anchor="middle" class="mrm muted" font-size="10">5</text><text x="252" y="292" text-anchor="middle" class="mrm muted" font-size="10">6</text><text x="284" y="292" text-anchor="middle" class="mrm muted" font-size="10">7</text><text x="316" y="292" text-anchor="middle" class="mrm muted" font-size="10">8</text><text x="348" y="292" text-anchor="middle" class="mrm muted" font-size="10">9</text><text x="380" y="292" text-anchor="middle" class="mrm muted" font-size="10">10</text><text x="412" y="292" text-anchor="middle" class="mrm muted" font-size="10">11</text><text x="444" y="292" text-anchor="middle" class="mrm muted" font-size="10">12</text><text x="476" y="292" text-anchor="middle" class="mrm muted" font-size="10">13</text><text x="508" y="292" text-anchor="middle" class="mrm muted" font-size="10">14</text><text x="540" y="292" text-anchor="middle" class="mrm muted" font-size="10">15</text><line x1="124" y1="256" x2="556.0" y2="256" class="accent-stroke" stroke-dasharray="3 3" stroke-width="1"/><line x1="220" y1="246" x2="556.0" y2="246" class="accent-stroke" stroke-dasharray="3 3" stroke-width="1"/><line x1="316" y1="196" x2="556.0" y2="196" class="accent-stroke" stroke-dasharray="3 3" stroke-width="1"/><line x1="380" y1="166" x2="556.0" y2="166" class="accent-stroke" stroke-dasharray="3 3" stroke-width="1"/><line x1="444" y1="136" x2="556.0" y2="136" class="accent-stroke" stroke-dasharray="3 3" stroke-width="1"/><line x1="476" y1="116" x2="556.0" y2="116" class="accent-stroke" stroke-dasharray="3 3" stroke-width="1"/><line x1="540" y1="86" x2="556.0" y2="86" class="accent-stroke" stroke-dasharray="3 3" stroke-width="1"/><polyline points="124,256 220,246 316,196 380,166 444,136 476,116 540,86" class="accent-stroke" stroke-width="1.6"/><circle cx="60" cy="226" r="4" class="node"/><circle cx="92" cy="186" r="4" class="node"/><circle cx="124" cy="256" r="5" class="accent-fill"/><circle cx="156" cy="156" r="4" class="node"/><circle cx="188" cy="206" r="4" class="node"/><circle cx="220" cy="246" r="5" class="accent-fill"/><circle cx="252" cy="126" r="4" class="node"/><circle cx="284" cy="176" r="4" class="node"/><circle cx="316" cy="196" r="5" class="accent-fill"/><circle cx="348" cy="96" r="4" class="node"/><circle cx="380" cy="166" r="5" class="accent-fill"/><circle cx="412" cy="76" r="4" class="node"/><circle cx="444" cy="136" r="5" class="accent-fill"/><circle cx="476" cy="116" r="5" class="accent-fill"/><circle cx="508" cy="56" r="4" class="node"/><circle cx="540" cy="86" r="5" class="accent-fill"/><circle cx="60" cy="312" r="5" class="accent-fill"/><text x="72" y="316" class="label">non-deficient stage: every later value is larger (dashed line)</text><circle cx="430" cy="312" r="4" class="node"/><text x="442" y="316" class="label">deficient stage</text></svg>
:::

The complement of $B$ is co-c.e. and computes $A$; the proof shows that a computable bound on its elements would make $A$ computable. This is how hyperimmunity of $\nat \setminus B$ is obtained.

:::theorem[Dekker]{#thm-deficiency-set}
Let $A$ be an infinite c.e. set, enumerated without repetition by a computable function $a$, and let $B$ be its deficiency set. Then $B$ is c.e., $B \equiv_T A$, and if $A$ is not computable, $B$ is hypersimple.
:::

:::proof{of=thm-deficiency-set}
The set $B$ is c.e.: $s \in B$ as soon as a later stage $t$ with $a(t) < a(s)$ is found.

*Non-deficient stages.* If $s_0 < s_1 < \cdots$ are the non-deficient stages, then $a(s_0) < a(s_1) < \cdots$, since $s_{i+1}$ comes after $s_i$ and $s_i$ is non-deficient. A strictly increasing sequence of natural numbers satisfies $a(s_n) \geq n$. The complement of $B$ is infinite: for every $s$, the minimum of $\{ a(t) : t \geq s \}$ is attained at a unique stage $t_0 \geq s$, which is non-deficient.

*Key property.* If $s$ is non-deficient and $x \leq a(s)$, then $x \in A$ if and only if $x = a(t)$ for some $t \leq s$. Indeed, an element enumerated after $s$ is larger than $a(s)$.

*$B \leq_T A$.* To decide $s \in B$ with oracle $A$, determine the finitely many elements of $A$ smaller than $a(s)$ and the stages at which they are enumerated; $s \in B$ if and only if one of these stages is larger than $s$.

*$A \leq_T B$.* To decide $x \in A$ with oracle $B$, list the non-deficient stages $s_0 < s_1 < \cdots$ up to $s_x$. Since $a(s_x) \geq x$, the key property gives $x \in A$ if and only if $x \in \{ a(t) : t \leq s_x \}$.

*Hyperimmunity.* Suppose that the principal function of $\nat \setminus B$ is dominated by a computable function $g$, so that $s_n \leq g(n)$ for every $n$. Then $x \in A$ if and only if $x = a(t)$ for some $t \leq g(x)$: if $x = a(t)$ with $t > g(x) \geq s_x$, then $x$ is enumerated after the non-deficient stage $s_x$, so $x > a(s_x) \geq x$, which is absurd. This decides $A$ computably, contradicting the hypothesis. So the principal function of $\nat \setminus B$ is hyperimmune, and $\nat \setminus B$ is hyperimmune by :ref{#thm-hyperimmune-principal}.
:::

:::corollary{#cor-ce-hyperimmune}
Every non-computable c.e. set is Turing equivalent to a hypersimple set. In particular, every non-zero c.e. degree is hyperimmune.
:::

A non-computable c.e. set is infinite, so the theorem applies. The second statement also follows from :ref{#thm-computation-function}, since c.e. sets are $\Delta^0_2$. Applied to $A = \emptyset'$, the corollary gives a hypersimple set that is Turing complete: the thinness of the complement does not prevent Turing completeness.

The non-deficient stages are an instance of a technique used throughout the theory of c.e. sets. A computation with oracle $A_s$ that is performed at a non-deficient stage $s$, and whose use is at most $a(s)$, is a true computation with oracle $A$, since $A$ does not change below $a(s)$ after stage $s$. True stages of this kind are a standard tool of infinite injury arguments.

:::quiz[deficiency sets]
Why are the values $a(s_0) < a(s_1) < \cdots$ of the non-deficient stages strictly increasing?

- [x] Because $s_{i+1} > s_i$, and every element enumerated after a non-deficient stage $s_i$ is larger than $a(s_i)$.
- [ ] Because $a$ is increasing.

  An enumeration of a non-computable c.e. set is never increasing, otherwise the set would be computable.
- [ ] Because $B$ is c.e.

  The enumerability of $B$ plays no role in this property.

---

Where is the non-computability of $A$ used in :ref{#thm-deficiency-set}?

- [x] Only in the hyperimmunity of the complement: a computable bound on the non-deficient stages would decide $A$.
- [ ] To show that the complement of $B$ is infinite.

  This holds for every infinite c.e. set: the stage of the minimum of a tail of the enumeration is non-deficient.
- [ ] To show that $A \leq_T B$.

  The reduction works for every infinite c.e. set.
:::

## Truth-table reducibility

In a Turing reduction $\Phi^X = Y$, the procedure may diverge with oracles other than $X$, and the amount of the oracle it reads is not known in advance. A truth-table reduction fixes in advance, for each input, which bits of the oracle are read and how the answer depends on them.

:::definition{#def-tt}
A set $Y$ is **truth-table reducible** to $X$, written $Y \leq_{tt} X$, if there are total computable functions $\ell$ and $\theta$, where $\theta(n)$ is (a code of) a function from $\{0, 1\}^{\ell(n)}$ to $\{0, 1\}$, such that $Y(n) = \theta(n)(X \uh \ell(n))$ for every $n$.
:::

The function $\theta(n)$ is the **truth table** for the input $n$. Clearly $Y \leq_{tt} X$ implies $Y \leq_T X$.

:::example{#ex-tt-reductions}
1. If $Y \leq_m X$ via $f$ (:ref{#def-many-one}), then $Y \leq_{tt} X$ with $\ell(n) = f(n) + 1$ and the table that reads the last bit.
2. The complement of $\emptyset'$ is truth-table reducible to $\emptyset'$, with $\ell(n) = n + 1$ and the table that negates the last bit. It is not many-one reducible to $\emptyset'$, since a set many-one reducible to a c.e. set is c.e. So $\leq_{tt}$ is strictly weaker than $\leq_m$.
3. The reduction $B \leq_T A$ of :ref{#thm-deficiency-set} is a truth-table reduction in disguise; see the exercises.
:::

The definition asks for the tables explicitly. The next proposition shows that it is enough that the reduction never diverges, whatever the oracle. The argument is a compactness argument: the oracles form a compact space, so a procedure that halts on every oracle halts within a bounded time on all of them.

:::proposition{#prop-tt-total}
$Y \leq_{tt} X$ if and only if there is a functional $\Phi_e$ such that $\Phi^Z_e$ is total for every oracle $Z$, and $\Phi^X_e = Y$.
:::

:::proof{of=prop-tt-total}
($\Rightarrow$) The functional that, on input $n$ and with any oracle $Z$, computes $\ell(n)$ and $\theta(n)$, reads $Z \uh \ell(n)$ and outputs $\theta(n)(Z \uh \ell(n))$, is total on every oracle.

($\Leftarrow$) Fix $n$. The set $T_n = \{ \sigma : \Phi^\sigma_e(n)[|\sigma|]\diverge \}$ is a computable tree. A path $Z$ of $T_n$ would satisfy $\Phi^Z_e(n)\diverge$ by :ref{#prop-oracle-stages}, which is excluded. By :ref{#lem-weak-konig}, $T_n$ is finite, so there is a length $\ell$ such that every string $\sigma$ of length $\ell$ has $\Phi^\sigma_e(n)[\ell]\converge$. Let $\ell(n)$ be the least such $\ell$, found by a computable search, and let $\theta(n)(\sigma) = \Phi^\sigma_e(n)[\ell(n)]$ for $|\sigma| = \ell(n)$, with value replaced by $0$ if it is not in $\{0, 1\}$. Then $Y(n) = \Phi^X_e(n) = \theta(n)(X \uh \ell(n))$.
:::

:::quiz[total functionals]
In the proof of ($\Leftarrow$) in :ref{#prop-tt-total}, where is the totality of $\Phi_e$ on **every** oracle used?

- [x] To show that the tree of strings on which the computation at $n$ has not yet converged has no path, hence is finite by König's lemma.
- [ ] To show that $\Phi^X_e = Y$.

  This is a hypothesis, independent of the behavior on other oracles.
- [ ] To make each step of the search for $\ell(n)$ effective.

  Each step checks finitely many strings and is effective in any case; totality on every oracle is what makes the search terminate.
:::

## Post's theorem on hypersimple sets

Post proved that hypersimple sets are not truth-table complete: if $A$ is hypersimple, then $\emptyset' \not\leq_{tt} A$. Friedberg and Rogers strengthened this to weak truth-table reducibility, in which the use of a Turing reduction is bounded by a computable function. These results are admitted here; the version for weak truth-table reducibility is Exercise 4.1.15 in Nies (2009).

Combined with :ref{#cor-ce-hyperimmune}, Post's theorem separates the two reducibilities on c.e. sets. The deficiency set of an enumeration of $\emptyset'$ is a c.e. set $B$ with $\emptyset' \leq_T B$, but $\emptyset' \not\leq_{tt} B$, since $B$ is hypersimple. So the converse of the implication $\leq_{tt} \Rightarrow \leq_T$ fails. A second, self-contained separation follows from the characterization of computably dominated sets in :ref{to="immunity-growth/computably-dominated"}.

Post's program failed for Turing reducibility: Dekker's theorem gives Turing complete hypersimple sets, and Yates later constructed Turing complete maximal sets, whose complements are as thin as possible among co-infinite c.e. sets.

## Exercises

::::exercise{difficulty=1}
Let $B$ be the deficiency set of an enumeration $a$ of an infinite c.e. set $A$. Show that $B \leq_{tt} A$.

:::solution
For a stage $s$, let $F_s$ be the finite set of numbers $x < a(s)$ that are not in $\{ a(0), \dots, a(s) \}$; it is computable from $s$. Then $s \in B$ if and only if $F_s \cap A \neq \emptyset$: an element $x < a(s)$ of $A$ that is not among $a(0), \dots, a(s)$ is enumerated at a stage $t > s$, which makes $s$ deficient, and conversely. Let $\ell(s) = a(s)$, and let $\theta(s)$ be the table that outputs $1$ on $\sigma$ of length $a(s)$ if and only if $\sigma(x) = 1$ for some $x \in F_s$.
:::
::::

::::exercise{difficulty=1}
Show that $\leq_{tt}$ is transitive.

:::solution
Let $Z \leq_{tt} Y$ and $Y \leq_{tt} X$, via functionals $\Psi$ and $\Phi$ that are total on every oracle (:ref{#prop-tt-total}). Modify $\Phi$ so that it outputs $0$ instead of any value outside $\{0, 1\}$; it is still total on every oracle, and still computes $Y$ from $X$. For every oracle $V$, $\Phi^V$ is then the characteristic function of a set, so $\Psi^{\Phi^V}$ is total. The functional $V \mapsto \Psi^{\Phi^V}$ is total on every oracle and computes $Z$ from $X$, so $Z \leq_{tt} X$ by :ref{#prop-tt-total}.
:::
::::

## Notes and references

Post (1944) introduced hypersimple sets and truth-table reducibility, and proved that hypersimple sets are not truth-table complete. Dekker (1954) introduced deficiency sets and proved :ref{#thm-deficiency-set}; Soare states it with the additional fact $B \leq_{tt} A$ (Soare 2016, Theorem 5.3.6). Friedberg and Rogers (1959) introduced weak truth-table reducibility and showed that hypersimple sets are not wtt-complete. Soare attributes the characterization of truth-table reductions as total functionals to Nerode (Soare 2016, Theorem 3.8.5). Yates constructed a complete maximal set in 1965 (Soare 2016, Section 5.7).

- E. L. Post, *Recursively enumerable sets of positive integers and their decision problems*, Bulletin of the American Mathematical Society 50 (1944), 284–316.
- J. C. E. Dekker, *A theorem on hypersimple sets*, Proceedings of the American Mathematical Society 5 (1954), 791–796.
- R. M. Friedberg and H. Rogers, *Reducibility and completeness for sets of integers*, Zeitschrift für mathematische Logik und Grundlagen der Mathematik 5 (1959), 117–125.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, Sections 3.8, 5.3 and 5.7.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Section 4.1.
