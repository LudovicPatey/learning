---
title: Relativization
summary: Computability and enumerability relative to an oracle; the relativized universal function and SMN theorem, uniform in the oracle; functions as oracles.
duration: 25
prerequisites: [oracle-computation, fundamentals/rice-theorem]
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

::::exercise{#ex-relativized-rice difficulty=1 objective="Relativize Rice's theorem through the relativized fixed point theorem."}
State and prove the relativized Rice theorem: if $P$ is a set of indices such that $\Phi^X_a = \Phi^X_b$ and $a \in P$ imply $b \in P$, and $P \neq \emptyset, \nat$, then $P$ is not $X$-computable.

:::solution
The fixed point theorem relativizes: for every total $X$-computable $f$ there is $e$ with $\Phi^X_{f(e)} = \Phi^X_e$, by the proof of :ref{#thm-fixed-point}, which only uses the universal function and the SMN theorem, now in their relativized forms. Then the proof of :ref{#thm-rice} applies verbatim: if $P$ were $X$-computable, fix $a \in P$ and $b \notin P$, and let $f(x) = b$ if $x \in P$ and $f(x) = a$ otherwise; $f$ is total and $X$-computable, and a fixed point $e$ gives $e \in P \iff f(e) \in P \iff e \notin P$.
:::
::::

::::exercise{#ex-union-uniform difficulty=2 objective="Distinguish a construction that is uniform in the oracle from a set that is computable in each oracle separately."}
Show that there is a computable function $g$ such that $W^X_{g(a, b)} = W^X_a \cup W^X_b$ for all $a$, $b$ and $X$. Show that, for the set $A_X = \{ n : X \cap \{ m : m > n \} \neq \emptyset \}$ of :ref{#ex-relative-computability}, there is no index $d$ with $\Phi^X_d = A_X$ for every $X$.

:::solution
Let $\Phi^X_{g(a, b)}(x)$ run $\Phi^X_a(x)$ and $\Phi^X_b(x)$ alternately, one step at a time, and halt as soon as one of them halts. This oracle machine does not depend on $X$, and its index is obtained computably from $a$ and $b$ by the relativized SMN theorem.

Suppose that $\Phi^X_d = A_X$ for every $X$. For $X = \emptyset$, $\Phi^\emptyset_d(0)\converge = 0$, with some use $u$. The set $Y = \{ u \}$ agrees with $\emptyset$ below $u$, so $\Phi^Y_d(0) = 0$ by the use principle; but $A_Y(0) = 1$ when $u > 0$, and $u \geq 1$ by definition of the use. This is a contradiction.
:::
::::

## Oracles that are functions

A function $f : \nat \to \nat$ can also serve as an oracle, through its graph: let $G_f = \{ \langle x, y \rangle : f(x) = y \}$, a subset of $\nat$. A machine with oracle $G_f$ can compute $f(x)$ by searching for the $y$ with $\langle x, y \rangle \in G_f$; conversely, a machine that can compute $f$ can decide $G_f$. We say that a set or a function is **$f$-computable** if it is $G_f$-computable. Computing with an oracle $f$ is therefore computing with the ability to evaluate $f$ at any point.

For example, if $X$ is infinite, its principal function $p_X$ and $X$ compute each other (an exercise of the next lesson). Function oracles are used throughout the course to express that fast-growing functions carry computational power, as in :ref{#ex-oracle-domination}.

## Notes and references

Relativization was used systematically from Kleene and Post (1954) on; Soare states it as a general principle for the arithmetical hierarchy (Soare 2016, §4.4). The chapter on Turing degrees of Monin and Patey states the relativized SMN theorem with a computable function $S^m_n$, quantified after the oracle; the independence of $S^m_n$ from the oracle, which their proof gives, is made explicit here. The theorem of Baker, Gill and Solovay is the reason why the question $\mathrm{P} = \mathrm{NP}$ cannot be settled by the diagonal arguments of this course.

- S. C. Kleene and E. L. Post, *The upper semi-lattice of degrees of recursive unsolvability*, Annals of Mathematics 59 (1954), 379–407.
- T. Baker, J. Gill and R. Solovay, *Relativizations of the P =? NP question*, SIAM Journal on Computing 4 (1975), 431–442.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, §3.2 and §4.4.

:::::exercises
::::exercise{#ex-computable-oracle difficulty=1 objective="Check that a computable oracle adds no computational power."}
Show that if $X$ is computable, then the $X$-computable partial functions are exactly the partial computable functions.

:::solution
A partial computable function is computed by a machine that ignores its oracle. Conversely, let $X = \Phi_c$ be computable and let $f = \Phi^X_e$. Replace each consultation of the oracle tape at cell $k$ by a computation of $\Phi_c(k)$; more precisely, $f(x) \simeq U(\mu t\ T(\sigma_t, e, x, t))$ where $\sigma_t = \Phi_c(0) \cdots \Phi_c(t-1)$ is computable from $t$. This expression is partial computable.
:::
::::

::::exercise{#ex-relativized-diagonal difficulty=1 objective="Relativize the diagonal argument against enumerations of total functions."}
Let $X \in \cs$. Show that there is no total $X$-computable function $F : \nat^2 \to \nat$ such that every total $X$-computable function is $x \mapsto F(e, x)$ for some $e$. Explain why the $X$-computable partial function $(e, x) \mapsto \Phi^X_e(x)$ of :ref{#thm-relativized-universal}, which lists all partial $X$-computable functions, does not lead to the same contradiction.

:::solution
Suppose that $F$ exists, and let $g(x) = F(x, x) + 1$. An oracle machine computes $g$ with oracle $X$: on input $x$, it computes $F(x, x)$ with the machine computing $F$, and adds $1$. So $g$ is total and $X$-computable, and $g = F(e, \cdot)$ for some $e$; then $F(e, e) = g(e) = F(e, e) + 1$, a contradiction.

For the partial function, the diagonal $d(x) \simeq \Phi^X_x(x) + 1$ is $X$-computable, so $d = \Phi^X_e$ for some $e$, and $\Phi^X_e(e) \simeq \Phi^X_e(e) + 1$. This only shows that $\Phi^X_e(e)\diverge$: both sides are undefined. This is the relativization of the argument of the course on fundamentals, word for word.
:::
::::

::::exercise{#ex-uniform-enumeration difficulty=1 objective="Make a relativized characterization of c.e. sets uniform in the oracle by replacing a fixed element with a search."}
Show that there is a computable function $g$ such that, for every $X$ and every $e$ with $W^X_e \neq \emptyset$, the function $\Phi^X_{g(e)}$ is total and its range is $W^X_e$.

:::solution
The usual proof that a non-empty c.e. set is the range of a total computable function fixes an element $a$ of the set; relative to $X$, such an element depends on $X$. A search replaces it. Consider the oracle machine which, on input $(e, n)$ with oracle $X$:

1. searches for the least pair $\langle y_0, t_0 \rangle$ such that $\Phi^X_e(y_0)[t_0]\converge$;
2. writes $n = \langle y, t \rangle$, and outputs $y$ if $\Phi^X_e(y)[t]\converge$, and $y_0$ otherwise.

The relation $\Phi^X_e(y)[t]\converge$ is $X$-computable, uniformly in $e$, $y$ and $t$ (:ref{#prop-oracle-stages}). If $W^X_e \neq \emptyset$, the search of step 1 terminates, by item 3 of :ref{#prop-oracle-stages}, so the machine is total on every input $(e, n)$. Every output belongs to $W^X_e$, and every $y \in W^X_e$ is output on $n = \langle y, t \rangle$ for a stage $t$ at which $\Phi^X_e(y)[t]\converge$. By the parameter form of :ref{#thm-relativized-smn}, there is a computable $g$ such that, for every $X$, $\Phi^X_{g(e)}(n)$ is the output of this machine on $(e, n)$ with oracle $X$.
:::
::::

::::exercise{#ex-relativized-selection difficulty=1 objective="See that relativized results provide in general objects computable in the oracle, and not computable ones."}
Give a set $X$ and an $X$-computable relation $R \subseteq \nat^2$ such that for every $x$ there is $y$ with $R(x, y)$, but no partial computable function $\psi$ satisfies $R(x, \psi(x))$ for every $x$. Compare with :ref{#thm-relativized-smn}, where the function provided by the relativized theorem is computable.

:::solution
Let $X$ be any non-computable set, and $R(x, y) \iff y = X(x)$. It is $X$-computable, and for every $x$ the value $y = X(x)$ satisfies $R(x, y)$. If $\psi$ is partial computable and $R(x, \psi(x))$ holds for every $x$, then $\psi$ is total and equal to the characteristic function of $X$, so $X$ is computable, a contradiction. The relativization of the selection theorem of the course on fundamentals provides an $X$-computable function choosing such a $y$, here $X$ itself, and nothing better. The SMN theorem is different because the function it provides manipulates indices without consulting the oracle.

Adapted from Soare 2016, Exercise 3.3.21.
:::
::::

::::exercise{#ex-graph-oracle difficulty=1 objective="Compare two ways of presenting a function as an oracle: its graph and the region below its graph."}
For a total function $f : \nat \to \nat$, let $L_f = \{ \langle x, y \rangle : y < f(x) \}$. Show that there are indices $a$ and $b$ such that $\Phi^{G_f}_a = L_f$ and $\Phi^{L_f}_b = G_f$ for every total $f$.

:::solution
Let the machine $a$, on input $z = \langle x, y \rangle$ (the pairing is a bijection, so every $z$ is of this form), search for $y'$ with $\langle x, y' \rangle$ in its oracle, and output $1$ if $y < y'$ and $0$ otherwise. With oracle $G_f$, the search finds $y' = f(x)$, so the output is $L_f(z)$.

Let the machine $b$, on input $z = \langle x, y \rangle$, search for the least $y'$ with $\langle x, y' \rangle$ not in its oracle, and output $1$ if $y = y'$ and $0$ otherwise. With oracle $L_f$, the pairs $\langle x, y' \rangle$ with $y' < f(x)$ are in the oracle and $\langle x, f(x) \rangle$ is not, so the search finds $y' = f(x)$, and the output is $G_f(z)$. Neither machine depends on $f$.
:::
::::
:::::
