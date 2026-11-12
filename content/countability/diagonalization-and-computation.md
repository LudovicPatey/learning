---
title: Diagonalization and computation
summary: Counting arguments; effective diagonalization against uniformly computable sequences; partial functions and the halting set.
duration: 40
prerequisites: [continuum, models-of-computation/equivalence-of-models, models-of-computation/ackermann-function]
---

This lesson connects the previous ones with computation. Counting shows that almost all functions are not computable, but it exhibits none. Diagonalization does better: applied to an enumeration that is itself computable, it produces a function that is computable, and escapes the enumeration. Applied to the enumeration $\Phi_0, \Phi_1, \Phi_2, \dots$ of all partial computable functions, it does not produce a contradiction, but a point of divergence, and from there the undecidability of the halting problem. The next lesson presents diagonalization as the satisfaction of a list of requirements, the form in which it is used in the rest of computability theory.

We use the notation of the course on models of computation: $\Phi_e$ is the partial function computed by the program of code $e$, and $\Phi(e, x) \simeq \Phi_e(x)$ is partial computable (:ref{#cor-universal-function}). We write $\Phi_e(x)\converge$ when the computation halts and $\Phi_e(x)\diverge$ otherwise.

## Counting

:::proposition{#prop-countably-many-computable}
The set of partial computable functions $\nat \rightharpoonup \nat$, the set of total computable functions $\nat \to \nat$ and the set of computable subsets of $\nat$ are countably infinite.
:::

:::proof{of=prop-countably-many-computable}
By :ref{#cor-universal-function}, every partial computable function is $\Phi_e$ for some $e$, so $e \mapsto \Phi_e$ is a surjection from $\nat$ onto the partial computable functions, which are therefore countable (:ref{#prop-countable-characterizations}). The total computable functions form a subset, and the computable sets are the images of the computable characteristic functions under the bijection $X \mapsto \{ n : X(n) = 1 \}$, so both are countable by :ref{#cor-subset-countable}. All three sets are infinite: they contain the constant functions, or the finite sets $\underline n$.
:::

:::corollary{#cor-noncomputable-continuum}
The set of functions $\nat \to \nat$ that are not computable, and the set of subsets of $\nat$ that are not computable, have the cardinality of the continuum.
:::

:::proof{of=cor-noncomputable-continuum}
They are the complements of countable sets in $\nat^\nat$ and $\cs$, which have the cardinality of the continuum by :ref{#thm-continuum}. Conclude by :ref{#prop-cocountable}.
:::

The argument does not depend on the details of the model of computation. It uses only that every computable function has a **finite description**, so that there are countably many of them. For the same reason, there are only countably many subsets of $\nat$ definable by a formula of first-order arithmetic, so that most sets are not definable in arithmetic. The argument is not constructive: it does not exhibit any particular non-computable function.

:::quiz[the counting argument]
Which property of computable functions does the proof of :ref{#cor-noncomputable-continuum} actually use?

- [x] That there are countably many of them.

  Any countable class of functions misses all but countably many functions $\nat \to \nat$.
- [ ] That they are closed under composition.

  Closure properties play no role in a counting argument.
- [ ] That some of them are partial.

  The count would be the same for any countable class of total functions.

---

Does the corollary provide a non-computable set that one can describe?

- [ ] Yes: the diagonal set $Y(n) = 1 - X_n(n)$ for an enumeration $(X_n)$ of the computable sets.

  This set is described only relative to an enumeration of the computable sets, and nothing has been said about which enumerations exist or how complex they are. The next sections take up this question.
- [x] No: it shows that non-computable sets exist, and are the majority, without describing any.
:::

## Effective diagonalization

The diagonal function $g(n) = f_n(n) + 1$ of :ref{#ex-diagonal-instances} is defined from the whole sequence $(f_n)$. If this sequence is given by an algorithm, so is $g$.

:::definition{#def-uniformly-computable}
A sequence $(f_e)_{e \in \nat}$ of total functions $\nat \to \nat$ is **uniformly computable** if the function $(e, x) \mapsto f_e(x)$ is computable. A sequence of sets is uniformly computable if the sequence of their characteristic functions is.
:::

Each function of a uniformly computable sequence is computable, but the converse fails: being uniformly computable means that a single algorithm computes $f_e(x)$ from $e$ and $x$, not only that each $f_e$ has an algorithm of its own. For instance, let $f_e$ be the constant function with value $1$ if $e \in \emptyset'$ and $0$ otherwise, where $\emptyset'$ is the halting set of :ref{#cor-halting-diagonal} below. Each $f_e$ is constant, hence computable, but $e \mapsto f_e(0)$ is the characteristic function of $\emptyset'$, which is not computable.

:::theorem{#thm-effective-diagonal}
If $(f_e)$ is a uniformly computable sequence of total functions, then the function $g(n) = f_n(n) + 1$ is total computable and differs from every $f_e$. Consequently, there is no uniformly computable sequence containing all total computable functions.
:::

:::proof{of=thm-effective-diagonal}
The function $g$ is obtained by composing the computable function $(e, x) \mapsto f_e(x)$ with $n \mapsto (n, n)$ and with the successor, so it is computable; it is total since each $f_e$ is. It differs from every $f_e$ by :ref{#prop-diagonal-general}. If a uniformly computable sequence contained all total computable functions, it would contain $g$.
:::

The primitive recursive functions form a uniformly computable sequence $(f_e)$: enumerate the derivations and evaluate them. This is the argument of :ref{#thm-pr-diagonal}, which yields a total computable function that is not primitive recursive. The theorem shows that the total computable functions themselves cannot be enumerated in this way. The obstacle is identified by the following consequence.

:::corollary{#cor-tot-not-computable}
The set $\mathrm{Tot} = \{ e \in \nat : \Phi_e \text{ is total} \}$ is not computable.
:::

:::proof{of=cor-tot-not-computable}
The set $\mathrm{Tot}$ is infinite: the constant functions are total computable and pairwise distinct, and each of them is $\Phi_e$ for some $e$. Suppose $\mathrm{Tot}$ computable. Then its principal function $p$ (:ref{#lem-subsets-of-n}) is computable, by
$$
p(0) = \mu e\, [e \in \mathrm{Tot}], \qquad p(n+1) = \mu e\, [e > p(n) \wedge e \in \mathrm{Tot}],
$$
where each search terminates since $\mathrm{Tot}$ is infinite. Let $f_n(x) = \Phi(p(n), x)$. Since $\Phi$ is partial computable, $(n, x) \mapsto f_n(x)$ is partial computable; and it is total, since $p(n) \in \mathrm{Tot}$. So $(f_n)$ is a uniformly computable sequence of total functions. Every total computable function is $\Phi_e$ for some $e \in \mathrm{Tot}$, that is, $e = p(n)$ for some $n$, so it is $f_n$. This contradicts :ref{#thm-effective-diagonal}.
:::

:::quiz[effective diagonalization]
In the proof of :ref{#cor-tot-not-computable}, why is the principal function $p$ used rather than the sequence $f_e = \Phi_e$ for $e \in \mathrm{Tot}$ directly?

- [x] A uniformly computable sequence must be indexed by all of $\nat$, with every $f_n$ total; $p$ re-indexes the total programs by consecutive integers.

  Taking $f_e = \Phi_e$ for all $e$ would include partial functions, to which the theorem does not apply.
- [ ] Because $\Phi$ is not computable.

  $\Phi$ is partial computable by :ref{#cor-universal-function}.
- [ ] To make the sequence injective.

  Injectivity is not needed: the sequence $(f_n)$ may repeat functions.

---

Where does the proof use the hypothesis that $\mathrm{Tot}$ is computable?

- [x] To compute $p$, whose definition tests membership in $\mathrm{Tot}$ during the searches.

  Without it, $p$ is a well-defined function, but not necessarily a computable one, and the sequence $(f_n)$ is no longer uniformly computable.
- [ ] To show that $\mathrm{Tot}$ is infinite.

  This is shown independently.
- [ ] To show that $g$ differs from every $f_n$.

  This is the diagonal lemma, which uses no hypothesis on $\mathrm{Tot}$.
:::

## Partial functions

The previous section shows that three wishes are incompatible: a list $(f_e)$ (1) containing all computable functions, (2) uniformly computable, and (3) consisting of total functions. The diagonal function $g(n) = f_n(n) + 1$ would be computable by (2), total by (3), and missing from the list, against (1). The theory of computation keeps (1) and (2), which make a universal machine possible, and gives up (3). The enumeration $\Phi_0, \Phi_1, \dots$ of the partial computable functions is uniformly computable in the sense that $\Phi$ is partial computable. What happens when one diagonalizes against it?

:::proposition{#prop-diagonal-partial}
The partial function $d(e) \simeq \Phi_e(e) + 1$ is partial computable. If $c$ is a code of $d$, that is, $d = \Phi_c$, then $\Phi_c(c)\diverge$.
:::

:::proof{of=prop-diagonal-partial}
$d$ is obtained by composing $\Phi$, which is partial computable, with $e \mapsto (e, e)$ and with the successor; it is defined exactly when $\Phi_e(e)\converge$. If $d = \Phi_c$ and $\Phi_c(c)\converge$, then $\Phi_c(c) = d(c) = \Phi_c(c) + 1$, which is impossible. So $\Phi_c(c)\diverge$.
:::

:::figure[The values $\Phi_e(x)$ as an infinite table, with $\uparrow$ for divergence. The function $d$ adds $1$ to each diagonal entry and diverges where the diagonal diverges. It is itself a row, $\Phi_c$, and the only way for this row to escape the contradiction is the divergent entry at $(c, c)$.]
<svg class="fig" viewBox="0 0 400 290" width="400" role="img" aria-label="A table of values of partial computable functions, some undefined; the row of the diagonal function d has an undefined entry on the diagonal"><text x="107.0" y="24" text-anchor="middle" class="mrm muted" font-size="13">0</text><text x="141.0" y="24" text-anchor="middle" class="mrm muted" font-size="13">1</text><text x="175.0" y="24" text-anchor="middle" class="mrm muted" font-size="13">2</text><text x="209.0" y="24" text-anchor="middle" class="mrm muted" font-size="13">3</text><text x="243.0" y="24" text-anchor="middle" class="mrm muted" font-size="13">4</text><text x="277.0" y="24" text-anchor="middle" class="mrm muted" font-size="13">⋯</text><text x="311.0" y="24" text-anchor="middle" class="math muted" font-size="13">c</text><text x="50" y="56" text-anchor="middle" class="mrm" font-size="16">Φ<tspan class="mrm" font-size="10" dy="4">0</tspan></text><rect x="90" y="34" width="34" height="34" class="cell head-cell"/><text x="107.0" y="56" text-anchor="middle" class="mrm" font-size="15">2</text><rect x="124" y="34" width="34" height="34" class="cell"/><text x="141.0" y="56" text-anchor="middle" class="mrm muted" font-size="15">↑</text><rect x="158" y="34" width="34" height="34" class="cell"/><text x="175.0" y="56" text-anchor="middle" class="mrm muted" font-size="15">0</text><rect x="192" y="34" width="34" height="34" class="cell"/><text x="209.0" y="56" text-anchor="middle" class="mrm muted" font-size="15">5</text><rect x="226" y="34" width="34" height="34" class="cell"/><text x="243.0" y="56" text-anchor="middle" class="mrm muted" font-size="15">1</text><text x="277.0" y="56" text-anchor="middle" class="mrm muted" font-size="15">⋯</text><rect x="294" y="34" width="34" height="34" class="cell"/><text x="311.0" y="56" text-anchor="middle" class="mrm muted" font-size="15">3</text><text x="50" y="90" text-anchor="middle" class="mrm" font-size="16">Φ<tspan class="mrm" font-size="10" dy="4">1</tspan></text><rect x="90" y="68" width="34" height="34" class="cell"/><text x="107.0" y="90" text-anchor="middle" class="mrm muted" font-size="15">0</text><rect x="124" y="68" width="34" height="34" class="cell head-cell"/><text x="141.0" y="90" text-anchor="middle" class="mrm" font-size="15">↑</text><rect x="158" y="68" width="34" height="34" class="cell"/><text x="175.0" y="90" text-anchor="middle" class="mrm muted" font-size="15">4</text><rect x="192" y="68" width="34" height="34" class="cell"/><text x="209.0" y="90" text-anchor="middle" class="mrm muted" font-size="15">↑</text><rect x="226" y="68" width="34" height="34" class="cell"/><text x="243.0" y="90" text-anchor="middle" class="mrm muted" font-size="15">2</text><text x="277.0" y="90" text-anchor="middle" class="mrm muted" font-size="15">⋯</text><rect x="294" y="68" width="34" height="34" class="cell"/><text x="311.0" y="90" text-anchor="middle" class="mrm muted" font-size="15">↑</text><text x="50" y="124" text-anchor="middle" class="mrm" font-size="16">Φ<tspan class="mrm" font-size="10" dy="4">2</tspan></text><rect x="90" y="102" width="34" height="34" class="cell"/><text x="107.0" y="124" text-anchor="middle" class="mrm muted" font-size="15">1</text><rect x="124" y="102" width="34" height="34" class="cell"/><text x="141.0" y="124" text-anchor="middle" class="mrm muted" font-size="15">1</text><rect x="158" y="102" width="34" height="34" class="cell head-cell"/><text x="175.0" y="124" text-anchor="middle" class="mrm" font-size="15">7</text><rect x="192" y="102" width="34" height="34" class="cell"/><text x="209.0" y="124" text-anchor="middle" class="mrm muted" font-size="15">0</text><rect x="226" y="102" width="34" height="34" class="cell"/><text x="243.0" y="124" text-anchor="middle" class="mrm muted" font-size="15">0</text><text x="277.0" y="124" text-anchor="middle" class="mrm muted" font-size="15">⋯</text><rect x="294" y="102" width="34" height="34" class="cell"/><text x="311.0" y="124" text-anchor="middle" class="mrm muted" font-size="15">0</text><text x="50" y="158" text-anchor="middle" class="mrm" font-size="16">Φ<tspan class="mrm" font-size="10" dy="4">3</tspan></text><rect x="90" y="136" width="34" height="34" class="cell"/><text x="107.0" y="158" text-anchor="middle" class="mrm muted" font-size="15">↑</text><rect x="124" y="136" width="34" height="34" class="cell"/><text x="141.0" y="158" text-anchor="middle" class="mrm muted" font-size="15">6</text><rect x="158" y="136" width="34" height="34" class="cell"/><text x="175.0" y="158" text-anchor="middle" class="mrm muted" font-size="15">2</text><rect x="192" y="136" width="34" height="34" class="cell head-cell"/><text x="209.0" y="158" text-anchor="middle" class="mrm" font-size="15">↑</text><rect x="226" y="136" width="34" height="34" class="cell"/><text x="243.0" y="158" text-anchor="middle" class="mrm muted" font-size="15">3</text><text x="277.0" y="158" text-anchor="middle" class="mrm muted" font-size="15">⋯</text><rect x="294" y="136" width="34" height="34" class="cell"/><text x="311.0" y="158" text-anchor="middle" class="mrm muted" font-size="15">2</text><text x="50" y="192" text-anchor="middle" class="mrm" font-size="16">Φ<tspan class="mrm" font-size="10" dy="4">4</tspan></text><rect x="90" y="170" width="34" height="34" class="cell"/><text x="107.0" y="192" text-anchor="middle" class="mrm muted" font-size="15">4</text><rect x="124" y="170" width="34" height="34" class="cell"/><text x="141.0" y="192" text-anchor="middle" class="mrm muted" font-size="15">0</text><rect x="158" y="170" width="34" height="34" class="cell"/><text x="175.0" y="192" text-anchor="middle" class="mrm muted" font-size="15">0</text><rect x="192" y="170" width="34" height="34" class="cell"/><text x="209.0" y="192" text-anchor="middle" class="mrm muted" font-size="15">1</text><rect x="226" y="170" width="34" height="34" class="cell head-cell"/><text x="243.0" y="192" text-anchor="middle" class="mrm" font-size="15">0</text><text x="277.0" y="192" text-anchor="middle" class="mrm muted" font-size="15">⋯</text><rect x="294" y="170" width="34" height="34" class="cell"/><text x="311.0" y="192" text-anchor="middle" class="mrm muted" font-size="15">↑</text><text x="175.0" y="224" text-anchor="middle" class="mrm muted" font-size="15">⋮</text><text x="50" y="260" text-anchor="middle" class="mrm" font-size="16">Φ<tspan class="math" font-size="11" dy="4">c</tspan><tspan dy="-4"> = </tspan><tspan class="math">d</tspan></text><rect x="90" y="238" width="34" height="34" class="cell"/><text x="107.0" y="260" text-anchor="middle" class="mrm muted" font-size="15">3</text><rect x="124" y="238" width="34" height="34" class="cell"/><text x="141.0" y="260" text-anchor="middle" class="mrm muted" font-size="15">↑</text><rect x="158" y="238" width="34" height="34" class="cell"/><text x="175.0" y="260" text-anchor="middle" class="mrm muted" font-size="15">8</text><rect x="192" y="238" width="34" height="34" class="cell"/><text x="209.0" y="260" text-anchor="middle" class="mrm muted" font-size="15">↑</text><rect x="226" y="238" width="34" height="34" class="cell"/><text x="243.0" y="260" text-anchor="middle" class="mrm muted" font-size="15">1</text><text x="277.0" y="260" text-anchor="middle" class="mrm muted" font-size="15">⋯</text><rect x="294" y="238" width="34" height="34" class="cell head-cell"/><text x="311.0" y="260" text-anchor="middle" class="mrm" font-size="15">↑</text></svg>
:::

So the diagonal argument does not fail: it determines a point, $c$, where the enumerated function $d = \Phi_c$ must be undefined. The partial functions escape diagonalization by being undefined at the diagonal point. This is why an enumeration of all partial computable functions can be computable, while an enumeration of all total computable functions cannot.

:::theorem{#thm-no-total-extension}
The partial computable function $d(e) \simeq \Phi_e(e) + 1$ has no total computable extension: there is no total computable $h$ with $h(e) = d(e)$ whenever $d(e)\converge$.
:::

:::proof{of=thm-no-total-extension}
Suppose $h$ is such an extension, and let $c$ be a code of $h$, so that $\Phi_c = h$ is total. Then $\Phi_c(c)\converge$, so $d(c) = \Phi_c(c) + 1$ is defined, and $h(c) = d(c) = h(c) + 1$, a contradiction.
:::

:::corollary{#cor-halting-diagonal}
The halting set $\emptyset' = \{ e : \Phi_e(e)\converge \}$ is not computable.
:::

:::proof{of=cor-halting-diagonal}
If $\emptyset'$ were computable, the function $h$ defined by $h(e) = \Phi_e(e) + 1$ if $e \in \emptyset'$, and $h(e) = 0$ otherwise, would be total computable: to compute $h(e)$, decide whether $e \in \emptyset'$, and run the computation of $\Phi_e(e)$ only if it halts. It would extend $d$, contradicting :ref{#thm-no-total-extension}.
:::

This is the halting problem, which is the starting point of the course on fundamentals (:ref{#thm-halting}). Its proof there is the same diagonal argument, presented directly.

:::quiz[diagonalization against partial functions]
In the proof of :ref{#thm-no-total-extension}, where is the totality of $h$ used?

- [x] To get $\Phi_c(c)\converge$, so that $d(c)$ is defined and the extension property applies at $c$.

  For a partial $h = \Phi_c$, one could have $\Phi_c(c)\diverge$, and no contradiction arises; $d$ itself is such a function.
- [ ] To show that $h$ has a code $c$.

  Every partial computable function has a code.
- [ ] To show that $d$ is partial computable.

  This does not depend on $h$.

---

Why is the function $h$ of :ref{#cor-halting-diagonal} total, given that $\Phi_e(e)$ may diverge?

- [x] The computation of $\Phi_e(e)$ is started only when $e \in \emptyset'$, that is, when it is known to halt.

  A definition by cases evaluates only the branch that applies; here this is essential, unlike in the primitive recursive definition by cases.
- [ ] Because $\Phi_e(e)$ always converges.

  It does not: for some $e$, $\Phi_e(e)\diverge$.
- [ ] Because $h$ takes the value $0$ on all inputs.

  It takes the value $0$ only outside $\emptyset'$.
:::

## Exercises

::::exercise{difficulty=1}
A function $h$ **dominates** a function $f$ if $h(n) \geq f(n)$ for all sufficiently large $n$. Show that no total computable function dominates every total computable function.

:::solution
If $h$ is total computable and dominates every total computable function, it dominates $h + 1$, which is total computable: $h(n) \geq h(n) + 1$ for large $n$, a contradiction.
:::
::::

::::exercise{#ex-no-uniform-computable-sets difficulty=1}
Show that there is no uniformly computable sequence $(X_n)$ of sets containing every computable set.

:::solution
If $(X_n)$ is uniformly computable, then $Y(n) = 1 - X_n(n)$ is computable, as a composition of computable functions, and differs from every $X_n$. Alternatively, apply :ref{#thm-effective-diagonal} to the characteristic functions, replacing $f_n(n) + 1$ by $1 - f_n(n)$.
:::
::::

::::exercise{difficulty=2}
Let $A = \{ e : \Phi_e(e)\converge = 0 \}$ and $B = \{ e : \Phi_e(e)\converge = 1 \}$. Show that there is no computable set $S$ with $A \subseteq S$ and $S \cap B = \emptyset$. (The sets $A$ and $B$ are **computably inseparable**.)

:::solution
Let $S$ be computable, and let $c$ be a code of its characteristic function, so that $\Phi_c$ is total with values in $\{0, 1\}$. If $c \in S$, then $\Phi_c(c) = 1$, so $c \in B$, and $S \cap B \neq \emptyset$. If $c \notin S$, then $\Phi_c(c) = 0$, so $c \in A$, and $A \not\subseteq S$. This is a diagonal argument in which the program $c$ is defeated at its own index.
:::
::::

::::exercise{difficulty=2}
Using :ref{#prop-ce-range} of the course on fundamentals, where computably enumerable sets are defined, show that $\mathrm{Tot}$ is not even computably enumerable.

:::solution
$\mathrm{Tot}$ is infinite. If it were computably enumerable, there would be an injective total computable $f$ with $f(\nat) = \mathrm{Tot}$. Then $f_n(x) = \Phi(f(n), x)$ defines a uniformly computable sequence of total functions containing every total computable function, contradicting :ref{#thm-effective-diagonal}. The proof of :ref{#cor-tot-not-computable} is the special case where $f$ is the principal function.
:::
::::

## Notes and references

The undecidability of the halting problem is due to Turing (1936), in the form that no machine decides whether a given machine is circle-free, that is, prints infinitely many digits. The incompatibility of the three requirements on a list of computable functions, and the resulting need for partial functions, is explained in Soare's textbook (§1.1.2); Monin and Patey (chapter *Cantor's infinity*, section *Non-computable reals*) give the counting argument. Rogers' and Soare's textbooks present diagonalization as the basic method of computability theory; Odifreddi gives a historical account of the many forms of the argument.

- A. M. Turing, *On computable numbers, with an application to the Entscheidungsproblem*, Proceedings of the London Mathematical Society (2) 42 (1936), 230–265.
- H. Rogers, *Theory of Recursive Functions and Effective Computability*, McGraw-Hill, 1967.
- P. Odifreddi, *Classical Recursion Theory*, North-Holland, 1989.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, §1.1.2.
- B. Monin and L. Patey, *Computability theory*, chapter *Cantor's infinity*.
