---
title: Programs as numbers
summary: The enumeration Φₑ of the partial computable functions, its approximation by stages, and computable sets and relations.
duration: 50
prerequisites: [models-of-computation/equivalence-of-models]
---

The course on models of computation ends with an enumeration of all partial computable functions: machines are coded by integers, and the function computed by the machine of code $e$ is obtained from $e$ by a single unbounded search (:ref{#thm-kleene-normal-form-proof}). The whole of computability theory is built on this enumeration. This lesson fixes it once and for all, together with its approximation by stages, and sets up the notions of computable set and computable relation. From now on, algorithms are described in words or pseudo-code, following the practice explained in :ref{to="models-of-computation/church-turing-thesis"}.

## The enumeration

Recall that $T_k(e, \vec x, s)$ is the primitive recursive predicate "$s$ codes the complete computation of the machine of code $e$ on input $\vec x = (x_1, \dots, x_k)$", that for given $e$ and $\vec x$ at most one $s$ satisfies it, and that $U(s)$ is the primitive recursive function reading the output on the last configuration of the computation coded by $s$. Integers that do not code a machine are treated as coding a fixed machine that never halts, so that every integer is the code of a machine.

:::notation{#not-phi-e}
For $e \in \nat$ and $k \geq 1$, $\Phi^{(k)}_e$ is the $k$-ary partial function
$$
\Phi^{(k)}_e(\vec x) \simeq U\big(\mu s\ T_k(e, \vec x, s)\big),
$$
computed by the machine of code $e$. The integer $e$ is an **index** of $\Phi^{(k)}_e$. The superscript is omitted when the number of arguments is clear, and $\Phi_e$ stands for $\Phi^{(1)}_e$. For an input $\vec x$:

- $\Phi_e(\vec x)\converge$ means that the computation halts in a standard configuration, so that $\Phi_e(\vec x)$ is defined; $\Phi_e(\vec x)\diverge$ means that it is undefined;
- $\Phi_e(\vec x)\converge = y$ means that it is defined, with value $y$.
:::

By :ref{#cor-universal-function}, the sequence $\Phi_0, \Phi_1, \Phi_2, \dots$ contains every unary partial computable function, and the map $(e, \vec x) \mapsto \Phi_e(\vec x)$ is itself partial computable. These two facts — every partial computable function has an index, and the enumeration is computable — are the only properties of the enumeration used in most of the theory. The next lesson adds a third one, the SMN theorem.

The point of view of the whole course is that an index is at the same time a **program** and a **datum**. As a program, $e$ describes a computation; as a datum, it is an integer that other programs can receive as input, transform and output. The interplay of the two roles is the source of both the universal function and the undecidability results.

:::example{#ex-indices}
An integer that does not code a machine is, by convention, an index of the nowhere defined function; so is the code of any machine that never halts, for instance a machine whose only transition moves right forever. The nowhere defined function therefore has infinitely many indices. The next lesson shows that every partial computable function does (:ref{#cor-infinitely-many-indices}).
:::

:::notation{#not-kleene-equality}
As in the course on models of computation (:ref{#not-kleene-eq}), $\alpha \simeq \beta$ between two expressions denoting possibly undefined values means: either both are defined and equal, or both are undefined. For partial functions, $f = g$ means $f(\vec x) \simeq g(\vec x)$ for every $\vec x$: the two functions have the same domain and agree on it.
:::

The **domain** of a partial function $f$ is $\mathrm{dom}(f) = \{ \vec x : f(\vec x)\converge \}$, and its **graph** is $\{ (\vec x, y) : f(\vec x)\converge = y \}$. A partial function is **total** if its domain is the set of all inputs.

## Approximation by stages

The computation of $\Phi_e(x)$ can be followed for a while. The following definition makes this precise, with conventions that make the approximations finite objects.

:::definition{#def-stage}
For $e, x, s \in \nat$, let
$$
\Phi_e(x)[s] \simeq \begin{cases} U(t) & \text{if } e, x < s \text{ and } T_1(e, x, t) \text{ for some } t < s,\\ \text{undefined} & \text{otherwise.}\end{cases}
$$
We say that $\Phi_e(x)$ **converges at stage $s$** when $\Phi_e(x)[s]\converge$. The same notation is used for several arguments, with $T_k$ in place of $T_1$.
:::

Since a computation of $t$ steps has a code larger than $t$, convergence at stage $s$ implies that the computation halts in fewer than $s$ steps. The precise relation between stages and steps is irrelevant: what matters is the following.

:::proposition{#prop-stage-properties}
1. The relation $\Phi_e(x)[s]\converge = y$, of the variables $e, x, s, y$, is primitive recursive. In particular, given $e$, $x$ and $s$, one can decide whether $\Phi_e(x)[s]\converge$, and compute its value if so.
2. If $\Phi_e(x)[s]\converge = y$ and $s' \geq s$, then $\Phi_e(x)[s']\converge = y$.
3. $\Phi_e(x)\converge = y$ if and only if $\Phi_e(x)[s]\converge = y$ for some $s$.
:::

:::proof{of=prop-stage-properties}
1. $\Phi_e(x)[s]\converge = y$ holds if and only if $e < s \wedge x < s \wedge \exists t < s\, \big(T_1(e, x, t) \wedge U(t) = y\big)$. This is obtained from primitive recursive predicates by Boolean operations and a bounded quantifier, hence it is primitive recursive (:ref{#cor-pr-bounded-quantifiers}). The value, when defined, is $U(\mu t < s\ T_1(e, x, t))$, a bounded minimization.
2. The witness $t < s$ is also smaller than $s'$, and the conditions $e, x < s$ are preserved.
3. If $\Phi_e(x)\converge = y$, let $t$ be the code of the computation; then $T_1(e, x, t)$ and $U(t) = y$, so $\Phi_e(x)[s]\converge = y$ for $s = \max(e, x, t) + 1$. Conversely, if $\Phi_e(x)[s]\converge = y$ with witness $t$, then $t$ is the unique $t$ with $T_1(e, x, t)$, so $\mu u\, T_1(e, x, u) = t$ and $\Phi_e(x) = U(t) = y$.
:::

:::figure[A possible run of the approximation, for an index $e \leq 1$, so that the condition $e < s$ holds from stage $2$ on. The cell in column $x$ and row $s$ is shaded when $\Phi_e(x)[s]\converge$. Shaded cells lie below the staircase $x < s$, and a column remains shaded from the stage of convergence on (item 2). Row $8$ is the finite set $\{ x : \Phi_e(x)[8]\converge \}$, written $W_e[8]$ in the lesson on c.e. sets. The columns marked ? have not converged by stage $12$; no finite part of the table tells whether they ever will.]
<svg class="fig" viewBox="0 0 560 420" width="560" role="img" aria-label="A table of inputs x against stages s; the cells where the computation on x has converged by stage s are shaded; they form columns that start at the stage of convergence and never stop"><text x="220.0" y="14" text-anchor="middle" class="label">input x</text><text x="77.0" y="32" text-anchor="middle" class="mrm muted" font-size="12">0</text><text x="103.0" y="32" text-anchor="middle" class="mrm muted" font-size="12">1</text><text x="129.0" y="32" text-anchor="middle" class="mrm muted" font-size="12">2</text><text x="155.0" y="32" text-anchor="middle" class="mrm muted" font-size="12">3</text><text x="181.0" y="32" text-anchor="middle" class="mrm muted" font-size="12">4</text><text x="207.0" y="32" text-anchor="middle" class="mrm muted" font-size="12">5</text><text x="233.0" y="32" text-anchor="middle" class="mrm muted" font-size="12">6</text><text x="259.0" y="32" text-anchor="middle" class="mrm muted" font-size="12">7</text><text x="285.0" y="32" text-anchor="middle" class="mrm muted" font-size="12">8</text><text x="311.0" y="32" text-anchor="middle" class="mrm muted" font-size="12">9</text><text x="337.0" y="32" text-anchor="middle" class="mrm muted" font-size="12">10</text><text x="363.0" y="32" text-anchor="middle" class="mrm muted" font-size="12">11</text><text x="14" y="209.0" text-anchor="middle" class="label" transform="rotate(-90 14 209.0)">stage s</text><text x="54" y="57" text-anchor="end" class="mrm muted" font-size="12">0</text><text x="54" y="83" text-anchor="end" class="mrm muted" font-size="12">1</text><rect x="64" y="66" width="26" height="26" class="cell"/><text x="54" y="109" text-anchor="end" class="mrm muted" font-size="12">2</text><rect x="64" y="92" width="26" height="26" class="cell"/><rect x="90" y="92" width="26" height="26" class="cell head-cell"/><text x="54" y="135" text-anchor="end" class="mrm muted" font-size="12">3</text><rect x="64" y="118" width="26" height="26" class="cell head-cell"/><rect x="90" y="118" width="26" height="26" class="cell head-cell"/><rect x="116" y="118" width="26" height="26" class="cell"/><text x="54" y="161" text-anchor="end" class="mrm muted" font-size="12">4</text><rect x="64" y="144" width="26" height="26" class="cell head-cell"/><rect x="90" y="144" width="26" height="26" class="cell head-cell"/><rect x="116" y="144" width="26" height="26" class="cell"/><rect x="142" y="144" width="26" height="26" class="cell"/><text x="54" y="187" text-anchor="end" class="mrm muted" font-size="12">5</text><rect x="64" y="170" width="26" height="26" class="cell head-cell"/><rect x="90" y="170" width="26" height="26" class="cell head-cell"/><rect x="116" y="170" width="26" height="26" class="cell"/><rect x="142" y="170" width="26" height="26" class="cell"/><rect x="168" y="170" width="26" height="26" class="cell"/><text x="54" y="213" text-anchor="end" class="mrm muted" font-size="12">6</text><rect x="64" y="196" width="26" height="26" class="cell head-cell"/><rect x="90" y="196" width="26" height="26" class="cell head-cell"/><rect x="116" y="196" width="26" height="26" class="cell head-cell"/><rect x="142" y="196" width="26" height="26" class="cell"/><rect x="168" y="196" width="26" height="26" class="cell"/><rect x="194" y="196" width="26" height="26" class="cell"/><text x="54" y="239" text-anchor="end" class="mrm muted" font-size="12">7</text><rect x="64" y="222" width="26" height="26" class="cell head-cell"/><rect x="90" y="222" width="26" height="26" class="cell head-cell"/><rect x="116" y="222" width="26" height="26" class="cell head-cell"/><rect x="142" y="222" width="26" height="26" class="cell"/><rect x="168" y="222" width="26" height="26" class="cell"/><rect x="194" y="222" width="26" height="26" class="cell head-cell"/><rect x="220" y="222" width="26" height="26" class="cell"/><text x="54" y="265" text-anchor="end" class="mrm muted" font-size="12">8</text><rect x="64" y="248" width="26" height="26" class="cell head-cell"/><rect x="90" y="248" width="26" height="26" class="cell head-cell"/><rect x="116" y="248" width="26" height="26" class="cell head-cell"/><rect x="142" y="248" width="26" height="26" class="cell"/><rect x="168" y="248" width="26" height="26" class="cell"/><rect x="194" y="248" width="26" height="26" class="cell head-cell"/><rect x="220" y="248" width="26" height="26" class="cell"/><rect x="246" y="248" width="26" height="26" class="cell"/><text x="54" y="291" text-anchor="end" class="mrm muted" font-size="12">9</text><rect x="64" y="274" width="26" height="26" class="cell head-cell"/><rect x="90" y="274" width="26" height="26" class="cell head-cell"/><rect x="116" y="274" width="26" height="26" class="cell head-cell"/><rect x="142" y="274" width="26" height="26" class="cell"/><rect x="168" y="274" width="26" height="26" class="cell head-cell"/><rect x="194" y="274" width="26" height="26" class="cell head-cell"/><rect x="220" y="274" width="26" height="26" class="cell"/><rect x="246" y="274" width="26" height="26" class="cell"/><rect x="272" y="274" width="26" height="26" class="cell"/><text x="54" y="317" text-anchor="end" class="mrm muted" font-size="12">10</text><rect x="64" y="300" width="26" height="26" class="cell head-cell"/><rect x="90" y="300" width="26" height="26" class="cell head-cell"/><rect x="116" y="300" width="26" height="26" class="cell head-cell"/><rect x="142" y="300" width="26" height="26" class="cell"/><rect x="168" y="300" width="26" height="26" class="cell head-cell"/><rect x="194" y="300" width="26" height="26" class="cell head-cell"/><rect x="220" y="300" width="26" height="26" class="cell"/><rect x="246" y="300" width="26" height="26" class="cell"/><rect x="272" y="300" width="26" height="26" class="cell head-cell"/><rect x="298" y="300" width="26" height="26" class="cell"/><text x="54" y="343" text-anchor="end" class="mrm muted" font-size="12">11</text><rect x="64" y="326" width="26" height="26" class="cell head-cell"/><rect x="90" y="326" width="26" height="26" class="cell head-cell"/><rect x="116" y="326" width="26" height="26" class="cell head-cell"/><rect x="142" y="326" width="26" height="26" class="cell"/><rect x="168" y="326" width="26" height="26" class="cell head-cell"/><rect x="194" y="326" width="26" height="26" class="cell head-cell"/><rect x="220" y="326" width="26" height="26" class="cell"/><rect x="246" y="326" width="26" height="26" class="cell head-cell"/><rect x="272" y="326" width="26" height="26" class="cell head-cell"/><rect x="298" y="326" width="26" height="26" class="cell"/><rect x="324" y="326" width="26" height="26" class="cell"/><text x="54" y="369" text-anchor="end" class="mrm muted" font-size="12">12</text><rect x="64" y="352" width="26" height="26" class="cell head-cell"/><rect x="90" y="352" width="26" height="26" class="cell head-cell"/><rect x="116" y="352" width="26" height="26" class="cell head-cell"/><rect x="142" y="352" width="26" height="26" class="cell"/><rect x="168" y="352" width="26" height="26" class="cell head-cell"/><rect x="194" y="352" width="26" height="26" class="cell head-cell"/><rect x="220" y="352" width="26" height="26" class="cell"/><rect x="246" y="352" width="26" height="26" class="cell head-cell"/><rect x="272" y="352" width="26" height="26" class="cell head-cell"/><rect x="298" y="352" width="26" height="26" class="cell"/><rect x="324" y="352" width="26" height="26" class="cell head-cell"/><rect x="350" y="352" width="26" height="26" class="cell"/><path d="M64,40 L64,66 L90,66 L90,92 L116,92 L116,118 L142,118 L142,144 L168,144 L168,170 L194,170 L194,196 L220,196 L220,222 L246,222 L246,248 L272,248 L272,274 L298,274 L298,300 L324,300 L324,326 L350,326 L350,352 L376,352 L376,378 L376,352" class="ink-stroke" stroke-width="1.6"/><rect x="61" y="245" width="318" height="32" class="track-outline"/><text x="388" y="265" class="math" font-size="15">W<tspan class="mrm" font-size="10" dy="4">e</tspan><tspan class="mrm" dy="-4">[8] = {0, 1, 2, 5}</tspan></text><text x="388" y="80" class="label">only inputs x &lt; s</text><text x="388" y="96" class="label">can have converged</text><text x="155.0" y="400" text-anchor="middle" class="mrm muted" font-size="14">?</text><text x="233.0" y="400" text-anchor="middle" class="mrm muted" font-size="14">?</text><text x="311.0" y="400" text-anchor="middle" class="mrm muted" font-size="14">?</text><text x="363.0" y="400" text-anchor="middle" class="mrm muted" font-size="14">?</text><text x="388" y="400" class="label">no convergence yet: undecided</text></svg>
:::

The contrast between items 1 and 3 is the central phenomenon of the theory. Convergence at a given stage is decidable; convergence is the existence of a stage, a question with an unbounded quantifier, and it is not decidable, as the lesson on the halting problem shows. Divergence is never confirmed at a finite stage: $\Phi_e(x)\diverge$ means $\Phi_e(x)[s]\diverge$ for **every** $s$.

Replacing a computation that may not halt by its approximations at finite stages is the basic technique of the subject. It is used in this course to build reductions (in the lesson on the halting problem) and to enumerate sets (in the lesson on c.e. sets), and later in every construction by stages, from the finite extension method to the priority method.

:::quiz[approximation by stages]
Which statements hold for all $e$ and $x$?

- [x] If $\Phi_e(x)[100]\converge$, then $\Phi_e(x)[1000]\converge$, with the same value.

  This is item 2 of :ref{#prop-stage-properties}.
- [ ] If $\Phi_e(x)[s]\diverge$ for every $s \leq 10^9$, then $\Phi_e(x)\diverge$.

  The computation may converge at stage $10^9 + 1$. No finite amount of simulation establishes divergence.
- [x] $\Phi_e(x)\diverge$ if and only if $\Phi_e(x)[s]\diverge$ for every $s$.

  This is the negation of item 3.
- [ ] If $\Phi_e(x)\converge$, then $\Phi_e(x)[x + 1]\converge$.

  Nothing bounds the stage of convergence in terms of the input. For $x = 0$ and $e \geq 1$, already the condition $e < s$ fails at stage $1$; and in any case the computation may be arbitrarily long.

---

Why does the definition of $\Phi_e(x)[s]$ require $e, x < s$?

- [x] So that at stage $s$ only the pairs $(e, x)$ with $e, x < s$ can have converged: what has happened by stage $s$ is a finite amount of information, with an explicit bound.

  Without the condition, a bound on the inputs that have converged by stage $s$ would depend on the details of the coding of computations; with it, the bound is explicit. It is used constantly in constructions.
- [ ] To make the relation $\Phi_e(x)[s]\converge$ decidable.

  The relation $\exists t < s\ T_1(e, x, t)$ is already decidable without this condition.
- [ ] To ensure that $\Phi_e(x)[s]\converge$ implies $\Phi_e(x)\converge$.

  This holds with or without the condition.
:::

## Computable sets and relations

:::definition{#def-computable-set}
A relation $R \subseteq \nat^k$ is **computable** (or **decidable**) if its characteristic function, equal to $1$ on $R$ and $0$ outside, is computable: there is an $e$ such that $\Phi^{(k)}_e$ is total and $\Phi^{(k)}_e(\vec x) = 1$ if $\vec x \in R$, $\Phi^{(k)}_e(\vec x) = 0$ otherwise. For $k = 1$ one speaks of computable **sets**.
:::

Computable sets were called *recursive* in older texts, after the partial recursive functions, and the expressions *recursion theory* and *recursive set* are still used. We freely identify a relation $R \subseteq \nat^k$ with the set $\{ \langle x_1, \dots, x_k \rangle : \vec x \in R \}$, obtained through the pairing function; one is computable if and only if the other is.

:::proposition{#prop-computable-closure}
1. The computable relations are closed under complement, finite union and finite intersection, and under substitution of total computable functions: if $R \subseteq \nat^m$ is computable and $g_1, \dots, g_m : \nat^k \to \nat$ are total computable, then $\{ \vec x : (g_1(\vec x), \dots, g_m(\vec x)) \in R \}$ is computable.
2. They are closed under bounded quantification: if $R \subseteq \nat^{k+1}$ is computable, so are $\{ (\vec x, y) : \exists z < y\ R(\vec x, z) \}$ and $\{ (\vec x, y) : \forall z < y\ R(\vec x, z) \}$.
3. Definition by cases: if $R_1, \dots, R_n$ are computable relations partitioning $\nat^k$ and $g_1, \dots, g_n$ are partial computable, then $f(\vec x) \simeq g_i(\vec x)$ for $\vec x \in R_i$ defines a partial computable function.
4. Unbounded search: if $R \subseteq \nat^{k+1}$ is computable, then $f(\vec x) \simeq \mu y\, R(\vec x, y)$ is partial computable, and total if for every $\vec x$ there is some $y$ with $R(\vec x, y)$.
:::

:::proof{of=prop-computable-closure}
By :ref{#thm-equivalence-models}, the computable partial functions are the partial recursive functions, which contain the primitive recursive functions and are closed under composition, primitive recursion and minimization. Let $\chi_R$ denote the characteristic function of $R$.

1. $\chi_{\nat^k \setminus R} = 1 \dotminus \chi_R$, $\chi_{R \cap S} = \chi_R \cdot \chi_S$, and unions are complements of intersections of complements. Substitution is composition: the characteristic function of the new relation is $\chi_R(g_1(\vec x), \dots, g_m(\vec x))$, which is total.
2. The function $(\vec x, y) \mapsto \sum_{z < y} \chi_R(\vec x, z)$ is defined by primitive recursion from $\chi_R$, hence computable, and $\exists z < y\ R(\vec x, z)$ holds exactly when it is non-zero. The bounded universal quantifier is the complement of a bounded existential quantifier applied to the complement.
3. On input $\vec x$, compute $\chi_{R_1}(\vec x), \dots, \chi_{R_n}(\vec x)$, which are all defined, find the unique $i$ with $\vec x \in R_i$, and compute $g_i(\vec x)$. Only the branch that applies is evaluated, so the result is undefined exactly when $g_i(\vec x)$ is.
4. $f(\vec x) \simeq \mu y\, [1 \dotminus \chi_R(\vec x, y) = 0]$ is a minimization of a total computable function. It is defined exactly when some $y$ satisfies $R(\vec x, y)$.
:::

In item 3, the evaluation of only one branch matters: in the primitive recursive definition by cases of the course on models of computation, all branches are computed, which is harmless for total functions but not for partial ones.

The hypothesis that the conditions $R_i$ are computable is needed. With $R_1 = \emptyset'$ and $R_2 = \nat \setminus \emptyset'$, and the constant branches $g_1 = 1$ and $g_2 = 0$, the function defined by cases is the characteristic function of $\emptyset'$, which is not computable (:ref{#thm-halting}), although $\emptyset'$ is the domain of a partial computable function. In item 4, if the test "$R(\vec x, y)$?" could fail to terminate, the search could get stuck on some $y$ although a larger witness exists; the lesson on c.e. sets shows how to search in that case, by **dovetailing**.

:::quiz[closure properties]
Let $R \subseteq \nat^2$ be computable. Which of the following are computable relations?

- [x] $\{ (x, y) : \exists z < x + y\ R(x, z) \}$.

  A bounded quantifier, with a bound given by a total computable function of the variables: substitute $x + y$ for the bound.
- [ ] $\{ x : \exists z\ R(x, z) \}$, in general.

  The unbounded search $\mu z\, R(x, z)$ gives a program that halts exactly on this set, but no program that says "no". Sets of this form are the computably enumerable sets of a later lesson; some of them are not computable.
- [x] $\{ x : R(x, x) \text{ and not } R(x, 2x) \}$.

  Substitution and Boolean operations.

---

Let $e$ be an index of the following algorithm: on input $n$, try $r = 0, 1, 2, \dots$ and return the first $r$ with $r^2 = n$. Which statements are true?

- [x] The domain of $\Phi_e$ is the set of perfect squares.

  The search succeeds exactly when $n$ is a square.
- [x] $\Phi_e(49)\converge = 7$.
- [ ] $\Phi_e$ is total, since $\lfloor \sqrt n \rfloor$ is defined for every $n$.

  The function $n \mapsto \lfloor \sqrt n \rfloor$ is total computable, but it is computed by other programs. $\Phi_e(50)\diverge$: this program computes a different, partial, function.
:::

## Uniformity

A typical statement of computability theory asserts that some object is obtained **uniformly** from others: for instance, "the set $A_x$ is computable, uniformly in $x$" means that the relation $\{ (x, y) : y \in A_x \}$ is computable, and not only that each $A_x$ is computable. The difference is essential. Let $\emptyset' = \{ e : \Phi_e(e)\converge \}$ be the halting set, which is not computable (:ref{#thm-halting}, in the lesson on the halting problem). Each set $A_x = \{ 0 \}$ if $x \in \emptyset'$ and $A_x = \emptyset$ otherwise is finite, hence computable; but the relation $y \in A_x$ is not, since $x \in \emptyset'$ if and only if $0 \in A_x$. Similarly, an index $e$ "obtained uniformly in $x$" is the value of a total computable function of $x$.

## Exercises

::::exercise{difficulty=1}
Let $f : \nat \to \nat$ be total. Show that $f$ is computable if and only if its graph is computable.

:::solution
If $f$ is computable, $f(x) = y$ is decided by computing $f(x)$ and comparing with $y$. Conversely, if the graph $G$ is computable, then $f(x) = \mu y\ G(x, y)$, a search that terminates since $f$ is total; it is computable by :ref{#prop-computable-closure}.
:::
::::

::::exercise{difficulty=1}
Show that the set $\{ e : \Phi_e(0)[e]\converge \}$ is computable, and that the function $s \mapsto |\{ e < s : \Phi_e(e)[s]\converge \}|$ is total computable.

:::solution
Both follow from item 1 of :ref{#prop-stage-properties}. The first set is defined by substituting $(e, 0, e)$ in a primitive recursive relation. The function is $\sum_{e < s} \chi(e, s)$, where $\chi(e, s)$ is the characteristic function of the primitive recursive relation $\Phi_e(e)[s]\converge$; it is primitive recursive.
:::
::::

::::exercise{difficulty=2}
Show that a partial computable function with a computable domain has a total computable extension. Show by an example that a partial computable function may have a total computable extension and a non-computable domain.

:::solution
If $D = \mathrm{dom}(f)$ is computable, let $g(x) \simeq f(x)$ for $x \in D$ and $g(x) = 0$ for $x \notin D$, a definition by cases (:ref{#prop-computable-closure}); $g$ is total since $f(x)\converge$ for $x \in D$. For the converse, consider the partial function defined by $f(e) \simeq 0$ if $\Phi_e(e)\converge$, undefined otherwise. It is partial computable, its domain $\emptyset'$ is not computable (:ref{#thm-halting}), and the constant function $0$ is a total computable extension.
:::
::::

## Notes and references

The enumeration of the partial recursive functions by indices, and the normal form theorem on which it rests, are due to Kleene (1936, 1938). The notation $\Phi_e$ follows Soare's textbook; Rogers writes $\varphi_e$. The approximation by stages and its conventions are standard in modern texts, where they are the basis of all constructions by stages. Soare presents the numbering in Section 1.5 of his textbook and the approximation by stages in Section 1.6.4, where the convention also requires the output to be smaller than $s$.

- S. C. Kleene, *General recursive functions of natural numbers*, Mathematische Annalen 112 (1936), 727–742.
- S. C. Kleene, *On notation for ordinal numbers*, Journal of Symbolic Logic 3 (1938), 150–155.
- H. Rogers, *Theory of Recursive Functions and Effective Computability*, McGraw-Hill, 1967.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016.
- B. Monin and L. Patey, *Computability theory*, chapter *Foundations of computability*, sections *Computable functions* and *Computable sets*.
