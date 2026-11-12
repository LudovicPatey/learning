---
title: Relativization
summary: Computability and enumerability relative to an oracle; the relativized universal function and SMN theorem, uniform in the oracle; functions as oracles.
duration: 35
prerequisites: [oracle-computation]
---

The course on fundamentals proved its results about machines without any oracle. Almost all of these proofs describe algorithms, or constructions of algorithms, and never look inside the machines they simulate except through the universal function and the SMN theorem. Such proofs go through unchanged if every machine is given access to the same oracle $X$. This observation, **relativization**, gives at once a relative version of every result of that course. This lesson states the principle, proves the two results on which it rests, and isolates the property that distinguishes the relativized results from mere copies of the unrelativized ones: they are **uniform** in the oracle.

## Relative computability

:::definition{#def-relative-computability}
Let $X \in \cs$. A partial function is **$X$-computable**, or **computable in $X$**, if it is $\Phi^X_e$ for some $e$. A set is $X$-computable if its characteristic function is. A set is **$X$-computably enumerable**, or **$X$-c.e.**, if it is the domain of an $X$-computable partial function; we write $W^X_e = \dom(\Phi^X_e)$.
:::

:::example{#ex-relative-computability}
1. Every set $X$ is $X$-computable, and so are its complement, the set $\{ n : 2n \in X \}$, and every finite modification of $X$.
2. The set $\{ n : X \cap \{ m : m > n \} \neq \emptyset \}$ is $X$-c.e.: it is the domain of the second functional of :ref{#ex-functionals}. It is $X$-computable as well, since it is either $\nat$ (if $X$ is infinite) or $\{ n : n < \max X \}$, or empty; but no single oracle machine decides it for every $X$, since deciding whether $X$ has an element above $n$ depends on infinitely many bits of $X$, against the use principle.
3. If $X$ is computable, the $X$-computable functions are the partial computable functions (see the exercises). Relative computability is interesting only for non-computable oracles.
:::

Item 2 shows the difference between a set being $X$-computable for each $X$ and being computable *uniformly* in $X$, by a single machine for all oracles. This distinction is the subject of the rest of the lesson.

## The principle of relativization

Every argument of the course on fundamentals is an algorithm, or a construction of algorithms, and remains valid if all machines are given access to the same oracle $X$. This yields, for each theorem, a version relative to $X$, obtained by replacing *computable* with *$X$-computable* and $\Phi_e$ with $\Phi^X_e$ throughout. For instance, relative to $X$, the c.e. sets are characterized as in :ref{#thm-ce-characterizations}, and the fixed point theorem holds for $X$-computable transformations of indices.

:::example[Relativizing a proof]{#ex-relativized-complementation}
The relativization of :ref{#prop-computable-iff-ce-coce} reads: *a set $A$ is $X$-computable if and only if $A$ and $\nat \setminus A$ are $X$-c.e.* The proof is the same, word for word. If $A = W^X_a$ and $\nat \setminus A = W^X_b$, an oracle machine decides $A$ with oracle $X$: on input $x$, it searches for the least $s$ such that $\Phi^X_a(x)[s]\converge$ or $\Phi^X_b(x)[s]\converge$, and answers accordingly. The stages $\Phi^X_e(x)[s]$ are $X$-computable by :ref{#prop-oracle-stages}, which is the only new ingredient. Moreover, the machine is the same for all oracles, and its index is computed from $a$ and $b$ alone.
:::

Relativization replaces *every* machine by an oracle machine, including the machines hidden in the definitions of particular sets. The relativization of "the halting set is not computable" is "the set $\{ e : \Phi^X_e(e)\converge \}$ is not $X$-computable", not "the halting set is not $X$-computable", which is false for $X = \emptyset'$. The first statement is the starting point of the lesson on the Turing jump.

Two results deserve to be stated explicitly, because the relativized versions of all others rest on them, and because their relativized form is uniform: the objects they provide do not depend on $X$.

:::theorem[Relativized universal function]{#thm-relativized-universal}
There is an index $u$ such that $\Phi^X_u(e, x) \simeq \Phi^X_e(x)$ for every $X$, $e$ and $x$.
:::

:::proof{of=thm-relativized-universal}
By :ref{#prop-oracle-stages}, $\Phi^X_e(x) \simeq U\big(\mu t\ T(X \uh t, e, x, t)\big)$, where $T(\sigma, e, x, t)$ is the primitive recursive relation "$t$ codes a halting computation of $e$ on $x$ with oracle $\sigma$". An oracle machine computes this expression: on input $(e, x)$, for $t = 0, 1, 2, \dots$, it reads $X \uh t$ on its oracle tape, and tests the relation. The same machine works for every oracle.
:::

:::theorem[Relativized SMN theorem]{#thm-relativized-smn}
For all $m, n \geq 1$, the primitive recursive function $S^m_n$ of :ref{#thm-smn} satisfies, for every oracle $X$,
$$
\Phi^X_{S^m_n(e, \vec x)}(\vec y) \simeq \Phi^X_e(\vec x, \vec y).
$$
:::

:::proof{of=thm-relativized-smn}
The construction of :ref{#thm-smn} prepends to the machine $e$ a machine writing $\vec x$ on the work tape, without touching the oracle head. The resulting oracle machine first writes $\vec x$, then behaves as the machine $e$, with the same oracle; this does not depend on the oracle.
:::

The function $S^m_n$ is computable, not merely $X$-computable: it manipulates codes of machines and never consults the oracle. Uniformity of this kind is used repeatedly, for instance to show that the jump is monotone and to compare computations relative to different oracles. In proofs, we use the parameter form: if $f(X, x, \vec y)$ is computed by an oracle machine, there is a computable $s$ with $\Phi^X_{s(x)}(\vec y) \simeq f(X, x, \vec y)$ for every $X$.

:::remark[Relativization in complexity theory]{#rem-relativization}
Almost all proofs of computability theory relativize. In complexity theory, this is a limitation: Baker, Gill and Solovay constructed oracles $A$ and $B$ with $\mathrm{P}^A = \mathrm{NP}^A$ and $\mathrm{P}^B \neq \mathrm{NP}^B$, so no relativizing argument can settle the question $\mathrm P = \mathrm{NP}$. We admit this result.
:::

:::quiz[relativization]
What is the relativization to $X$ of the statement "the halting set $\emptyset'$ is not computable"?

- [x] The set $\{ e : \Phi^X_e(e)\converge \}$ is not $X$-computable.

  The definition of the halting set involves machines, and must itself be relativized.
- [ ] The set $\emptyset'$ is not $X$-computable.

  This is false for $X = \emptyset'$. Relativization replaces every machine by an oracle machine, including those in the definition of $\emptyset'$.
- [ ] The set $\emptyset'$ is not computable, for every $X$.

  This does not involve $X$ at all.

---

Why is it useful that $S^m_n$ is computable rather than only $X$-computable?

- [x] Because the same function then works for all oracles at once, which allows comparing computations relative to different oracles.

  For instance, a reduction between relativized halting sets $X'$ and $Y'$ must not depend on the oracle.
- [ ] Because $X$-computable functions are not total.

  An $X$-computable function may well be total.
- [ ] It makes no difference.

  It matters when computations relative to different oracles are compared, for instance to show that the jump is monotone.

---

In :ref{#ex-relativized-complementation}, which fact about oracle computations is used beyond the unrelativized proof?

- [x] That the relation $\Phi^X_e(x)[s]\converge$ is $X$-computable, uniformly in $e$, $x$ and $s$.

  This is item 1 of :ref{#prop-oracle-stages} combined with reading $X \uh s$ on the oracle tape.
- [ ] The use principle.

  The proof never compares computations with different oracles.
- [ ] That $X$ is c.e.

  $X$ is arbitrary.
:::

## Oracles that are functions

A function $f : \nat \to \nat$ can also serve as an oracle, through its graph: let $G_f = \{ \langle x, y \rangle : f(x) = y \}$, a subset of $\nat$. A machine with oracle $G_f$ can compute $f(x)$ by searching for the $y$ with $\langle x, y \rangle \in G_f$; conversely, a machine that can compute $f$ can decide $G_f$. We say that a set or a function is **$f$-computable** if it is $G_f$-computable. Computing with an oracle $f$ is therefore computing with the ability to evaluate $f$ at any point.

For example, if $X$ is infinite, its principal function $p_X$ and $X$ compute each other (an exercise of the next lesson). Function oracles are used throughout the course to express that fast-growing functions carry computational power, as in :ref{#ex-oracle-domination}.

## Exercises

::::exercise{difficulty=1}
Show that if $X$ is computable, then the $X$-computable partial functions are exactly the partial computable functions.

:::solution
A partial computable function is computed by a machine that ignores its oracle. Conversely, let $X = \Phi_c$ be computable and let $f = \Phi^X_e$. Replace each consultation of the oracle tape at cell $k$ by a computation of $\Phi_c(k)$; more precisely, $f(x) \simeq U(\mu t\ T(\sigma_t, e, x, t))$ where $\sigma_t = \Phi_c(0) \cdots \Phi_c(t-1)$ is computable from $t$. This expression is partial computable.
:::
::::

::::exercise{difficulty=1}
State and prove the relativized Rice theorem: if $P$ is a set of indices such that $\Phi^X_a = \Phi^X_b$ and $a \in P$ imply $b \in P$, and $P \neq \emptyset, \nat$, then $P$ is not $X$-computable.

:::solution
The fixed point theorem relativizes: for every total $X$-computable $f$ there is $e$ with $\Phi^X_{f(e)} = \Phi^X_e$, by the proof of :ref{#thm-fixed-point}, which only uses the universal function and the SMN theorem, now in their relativized forms. Then the proof of :ref{#thm-rice} applies verbatim: if $P$ were $X$-computable, fix $a \in P$ and $b \notin P$, and let $f(x) = b$ if $x \in P$ and $f(x) = a$ otherwise; $f$ is total and $X$-computable, and a fixed point $e$ gives $e \in P \iff f(e) \in P \iff e \notin P$.
:::
::::

::::exercise{difficulty=2}
Show that there is a computable function $g$ such that $W^X_{g(a, b)} = W^X_a \cup W^X_b$ for all $a$, $b$ and $X$. Show that, for the set $A_X = \{ n : X \cap \{ m : m > n \} \neq \emptyset \}$ of :ref{#ex-relative-computability}, there is no index $d$ with $\Phi^X_d = A_X$ for every $X$.

:::solution
Let $\Phi^X_{g(a, b)}(x)$ run $\Phi^X_a(x)$ and $\Phi^X_b(x)$ alternately, one step at a time, and halt as soon as one of them halts. This oracle machine does not depend on $X$, and its index is obtained computably from $a$ and $b$ by the relativized SMN theorem.

Suppose that $\Phi^X_d = A_X$ for every $X$. For $X = \emptyset$, $\Phi^\emptyset_d(0)\converge = 0$, with some use $u$. The set $Y = \{ u \}$ agrees with $\emptyset$ below $u$, so $\Phi^Y_d(0) = 0$ by the use principle; but $A_Y(0) = 1$ when $u > 0$, and $u \geq 1$ by definition of the use. This is a contradiction.
:::
::::

## Notes and references

Relativization was used systematically from Kleene and Post (1954) on; Soare states it as a general principle for the arithmetical hierarchy (Soare 2016, §4.4). The chapter on Turing degrees of Monin and Patey states the relativized SMN theorem with a computable function $S^m_n$, quantified after the oracle; the independence of $S^m_n$ from the oracle, which their proof gives, is made explicit here. The theorem of Baker, Gill and Solovay is the reason why the question $\mathrm{P} = \mathrm{NP}$ cannot be settled by the diagonal arguments of this course.

- S. C. Kleene and E. L. Post, *The upper semi-lattice of degrees of recursive unsolvability*, Annals of Mathematics 59 (1954), 379–407.
- T. Baker, J. Gill and R. Solovay, *Relativizations of the P =? NP question*, SIAM Journal on Computing 4 (1975), 431–442.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, §3.2 and §4.4.
