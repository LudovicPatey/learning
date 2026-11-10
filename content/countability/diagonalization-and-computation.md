---
title: Diagonalization and computation
summary: Counting arguments; effective diagonalization against uniformly computable sequences; partial functions and the halting set; diagonalization by requirements.
duration: 40
prerequisites: [continuum, models-of-computation/equivalence-of-models]
---

This lesson connects the previous ones with computation. Counting shows that almost all functions are not computable, but it exhibits none. Diagonalization does better: applied to an enumeration that is itself computable, it produces a function that is computable, and escapes the enumeration. Applied to the enumeration $\Phi_0, \Phi_1, \Phi_2, \dots$ of all partial computable functions, it does not produce a contradiction, but a point of divergence, and from there the undecidability of the halting problem. The last section presents diagonalization as the satisfaction of a list of requirements, the form in which it is used in the rest of computability theory.

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

Each function of a uniformly computable sequence is computable, but the converse fails: being uniformly computable means that a single algorithm computes $f_e(x)$ from $e$ and $x$, not only that each $f_e$ has an algorithm of its own.

:::theorem{#thm-effective-diagonal}
If $(f_e)$ is a uniformly computable sequence of total functions, then the function $g(n) = f_n(n) + 1$ is total computable and differs from every $f_e$. Consequently, there is no uniformly computable sequence containing all total computable functions.
:::

:::proof{of=thm-effective-diagonal}
The function $g$ is obtained by composing the computable function $(e, x) \mapsto f_e(x)$ with $n \mapsto (n, n)$ and with the successor, so it is computable; it is total since each $f_e$ is. It differs from every $f_e$ by :ref{#prop-diagonal-general}. If a uniformly computable sequence contained all total computable functions, it would contain $g$.
:::

The primitive recursive functions form a uniformly computable sequence $(f_e)$: enumerate the derivations and evaluate them. This is the content of :ref{#thm-pr-diagonal}, which therefore yields a total computable function that is not primitive recursive. The theorem shows that the total computable functions themselves cannot be enumerated in this way. The obstacle is identified by the following consequence.

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

The enumeration $\Phi_0, \Phi_1, \dots$ of the partial computable functions is uniformly computable in the sense that $\Phi$ is partial computable. What happens when one diagonalizes against it?

:::proposition{#prop-diagonal-partial}
The partial function $d(e) \simeq \Phi_e(e) + 1$ is partial computable. If $c$ is a code of $d$, that is, $d = \Phi_c$, then $\Phi_c(c)\diverge$.
:::

:::proof{of=prop-diagonal-partial}
$d$ is obtained by composing $\Phi$, which is partial computable, with $e \mapsto (e, e)$ and with the successor; it is defined exactly when $\Phi_e(e)\converge$. If $d = \Phi_c$ and $\Phi_c(c)\converge$, then $\Phi_c(c) = d(c) = \Phi_c(c) + 1$, which is impossible. So $\Phi_c(c)\diverge$.
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

## Diagonalization by requirements

In the diagonal argument, the sequence $Y$ is built to satisfy infinitely many conditions, $Y \neq X_n$ for each $n$, each of which can be secured by fixing a single bit. Constructions in computability theory are usually organized in this way: one lists **requirements** $R_0, R_1, R_2, \dots$, and builds the desired object by finite approximations, ensuring each requirement at its turn.

For strings $\sigma, \tau \in 2^{<\nat}$, write $\sigma \preceq \tau$ if $\sigma$ is a prefix of $\tau$, and $\sigma \prec X$ if $\sigma$ is a prefix of $X \in \cs$. A requirement is a property of elements of $\cs$, that is, a subset $R \subseteq \cs$.

:::lemma[Finite extension]{#lem-finite-extension}
Let $(R_e)_{e \in \nat}$ be a sequence of requirements such that for every $e$ and every $\sigma \in 2^{<\nat}$, there is $\tau \succeq \sigma$ such that every $X \succ \tau$ satisfies $R_e$. Then there is $Y \in \cs$ satisfying every $R_e$.
:::

:::proof{of=lem-finite-extension}
Fix an enumeration $\rho_0, \rho_1, \dots$ of $2^{<\nat}$, given by :ref{#prop-strings-countable}. If $\tau$ is as in the hypothesis, so is every extension of $\tau$; in particular there is such a $\tau$ with $|\tau| > |\sigma|$. Define $\sigma_0$ as the empty string and $\sigma_{e+1}$ as the first $\rho_i$ such that $\rho_i \succeq \sigma_e$, $|\rho_i| > |\sigma_e|$, and every $X \succ \rho_i$ satisfies $R_e$. The strings $\sigma_0 \preceq \sigma_1 \preceq \cdots$ have strictly increasing lengths, so there is a unique $Y \in \cs$ with $\sigma_e \prec Y$ for every $e$: its $n$-th bit is the $n$-th bit of any $\sigma_e$ of length greater than $n$. Since $\sigma_{e+1} \prec Y$, $Y$ satisfies $R_e$.
:::

Choosing $\sigma_{e+1}$ as the first suitable string in a fixed enumeration avoids any use of the axiom of choice, and makes the construction explicit.

:::example{#ex-finite-extension-diagonal}
Let $(X_n)$ be a sequence in $\cs$, and $R_n = \{ Y : Y \neq X_n \}$. Given $\sigma$, the string $\tau = \sigma \, i$ with $i = 1 - X_n(|\sigma|)$ satisfies the hypothesis: every $Y \succ \tau$ differs from $X_n$ at position $|\sigma|$. This is the diagonal argument, except that the position at which $X_n$ is defeated is now chosen by the construction rather than fixed in advance.
:::

:::proposition{#prop-infinitely-different}
For every sequence $(X_n)$ in $\cs$, there is $Y \in \cs$ that differs from every $X_n$ at infinitely many positions. If $(X_n)$ is uniformly computable, $Y$ can be taken computable.
:::

:::proof{of=prop-infinitely-different}
For $e = \langle n, k \rangle$, let $R_e$ be the requirement "$Y(m) \neq X_n(m)$ for some $m \geq k$". Given $\sigma$, extend it by zeros to a string $\sigma'$ of length at least $k$, and let $\tau = \sigma' i$ with $i = 1 - X_n(|\sigma'|)$; every $Y \succ \tau$ differs from $X_n$ at the position $|\sigma'| \geq k$. By :ref{#lem-finite-extension}, some $Y$ satisfies all $R_{\langle n, k \rangle}$, that is, differs from each $X_n$ beyond every $k$.

If $(X_n)$ is uniformly computable, use the explicit extension above instead of a search in an enumeration: $\sigma_{e+1}$ is obtained from $\sigma_e$ by padding with zeros to length $k$ and appending one bit, all computable from $\sigma_e$ and $e = \langle n, k \rangle$. Then $e \mapsto \sigma_e$ is computable, and so is $Y$, since $Y(m)$ is the $m$-th bit of $\sigma_{m+1}$, which has length at least $m + 1$.
:::

The requirements of this proposition never interfere: once a requirement is satisfied, it remains satisfied whatever is done afterwards. Requirements of this kind can be handled one after the other, by finite extensions. The method was introduced by Kleene and Post to build Turing degrees with prescribed properties, and it is the elementary case of **forcing**. When requirements conflict, so that satisfying one may later injure another, one needs the **priority method**, which is the main technique of the theory of computably enumerable sets.

:::quiz[the finite extension lemma]
Why does the proof of :ref{#lem-finite-extension} require $|\sigma_{e+1}| > |\sigma_e|$?

- [x] To ensure that the lengths tend to infinity, so that the strings $\sigma_e$ determine a whole infinite sequence $Y$.

  Without it, the construction could stall on a single finite string, which determines no element of $\cs$.
- [ ] To ensure that $\sigma_{e+1}$ extends $\sigma_e$.

  This is required separately, by $\rho_i \succeq \sigma_e$.
- [ ] To ensure that $Y$ satisfies $R_e$.

  That is ensured by the choice of $\sigma_{e+1}$ among the strings all of whose extensions satisfy $R_e$.

---

In the computable part of :ref{#prop-infinitely-different}, why is the explicit extension used rather than the search of the lemma?

- [x] The search tests the condition "every $X \succ \rho_i$ satisfies $R_e$", a property of infinitely many sequences, which is not in general decidable.

  The explicit extension computes a suitable string directly, so the whole construction is an algorithm.
- [ ] Because the lemma uses the axiom of choice.

  It does not: it uses a fixed enumeration of strings.
- [ ] Because the search may not terminate.

  It always terminates, by the hypothesis of the lemma; the problem is that its steps may not be computable.
:::

## Exercises

::::exercise{difficulty=1}
A function $h$ **dominates** a function $f$ if $h(n) \geq f(n)$ for all sufficiently large $n$. Show that no total computable function dominates every total computable function.

:::solution
If $h$ is total computable and dominates every total computable function, it dominates $h + 1$, which is total computable: $h(n) \geq h(n) + 1$ for large $n$, a contradiction.
:::
::::

::::exercise{difficulty=1}
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
Using :ref{#prop-ce-range}, show that $\mathrm{Tot}$ is not even computably enumerable.

:::solution
$\mathrm{Tot}$ is infinite. If it were computably enumerable, there would be an injective total computable $f$ with $f(\nat) = \mathrm{Tot}$. Then $f_n(x) = \Phi(f(n), x)$ defines a uniformly computable sequence of total functions containing every total computable function, contradicting :ref{#thm-effective-diagonal}. The proof of :ref{#cor-tot-not-computable} is the special case where $f$ is the principal function.
:::
::::

::::exercise{difficulty=3}
Show that there is a set $Y$ such that neither $Y$ nor its complement contains an infinite computable set.

:::hint
For each $e$ such that $\Phi_e$ is the characteristic function of an infinite set $W$, the requirement is: $W \not\subseteq Y$ and $W \not\subseteq \nat \setminus Y$. Satisfy it by a finite extension.
:::

:::solution
The infinite computable sets form a countably infinite set, by :ref{#prop-countably-many-computable}; let $W_0, W_1, \dots$ be an enumeration of them. Requirement $R_{2n}$: $Y(m) = 0$ for some $m \in W_n$; requirement $R_{2n+1}$: $Y(m) = 1$ for some $m \in W_n$. Given $\sigma$, since $W_n$ is infinite there is $m \in W_n$ with $m \geq |\sigma|$; extend $\sigma$ by zeros to length $m$, then append the required bit. Every $Y$ extending the result satisfies the requirement. By :ref{#lem-finite-extension}, some $Y$ satisfies all requirements: each infinite computable set meets both $Y$ and its complement, so it is contained in neither. Such a set is called **bi-immune**.
:::
::::

## Notes and references

The undecidability of the halting problem is due to Turing (1936), in the form that no machine decides whether a given machine is circle-free, that is, prints infinitely many digits. The finite extension method is due to Kleene and Post (1954), and the priority method to Friedberg and Muchnik (1956–1957). Rogers' and Soare's textbooks present diagonalization as the basic method of computability theory; Odifreddi gives a historical account of the many forms of the argument.

- A. M. Turing, *On computable numbers, with an application to the Entscheidungsproblem*, Proceedings of the London Mathematical Society (2) 42 (1936), 230–265.
- S. C. Kleene and E. L. Post, *The upper semi-lattice of degrees of recursive unsolvability*, Annals of Mathematics 59 (1954), 379–407.
- H. Rogers, *Theory of Recursive Functions and Effective Computability*, McGraw-Hill, 1967.
- P. Odifreddi, *Classical Recursion Theory*, North-Holland, 1989.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016.
