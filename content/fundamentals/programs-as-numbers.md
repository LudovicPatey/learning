---
title: Programs as numbers
summary: Coding of programs by integers, the notation Φₑ, and computable sets.
duration: 15
prerequisites: [models-of-computation/church-turing-thesis]
---

Thanks to the Church–Turing thesis, we can stop writing Turing machines. From now on an algorithm is described in pseudo-code, and a function is **computable** if some such algorithm computes it. But we keep one essential feature of the formal models: programs are finite objects, so they can be **numbered**.

## Numbering programs

Fix a programming language. A program is a finite string of characters; read in binary, this string is a natural number. We say that $e$ is the **code** (or **index**) of the program. Numbers that do not encode a syntactically valid program are declared to code the program that loops forever on every input, so every $e \in \nat$ is the code of some program.

:::notation{#not-phi-e}
$\Phi_e$ denotes the partial function computed by the program of code $e$. For an input $x$:

- $\Phi_e(x)\converge$ means the computation halts; $\Phi_e(x)\diverge$ means it runs forever;
- $\Phi_e(x)\converge = y$ means it halts with output $y$;
- $\Phi_e(x)[t]\converge$ means it halts **within $t$ steps**.
:::

The list $\Phi_0, \Phi_1, \Phi_2, \dots$ contains every partial computable function — in fact each one infinitely often, since adding useless instructions changes the code but not the function.

:::notation{#not-kleene-equality}
For partial functions, $f(x) = g(x)$ means: either both sides are defined and equal, or both are undefined.
:::

## Running a program for a while

Two facts about the step-bounded notation are used constantly:

$$
\Phi_e(x)\converge \iff \exists t\ \ \Phi_e(x)[t]\converge, \qquad \Phi_e(x)[t]\converge \implies \Phi_e(x)[s]\converge \text{ for every } s \geq t.
$$

The key point: for fixed $e$, $x$ and $t$, whether $\Phi_e(x)[t]\converge$ is **decidable** — just run the program for $t$ steps. What is not decidable, as we will soon prove, is whether $\Phi_e(x)\converge$, because no bound on $t$ is known in advance.

:::quiz
Which statements hold for all $e$ and $x$?

- [x] If $\Phi_e(x)[100]\converge$ then $\Phi_e(x)[1000]\converge$.
- [ ] If $\Phi_e(x)[t]\diverge$ for every $t \leq 10^9$, then $\Phi_e(x)\diverge$.

  The program might halt at step $10^9 + 1$. No finite simulation can certify divergence.
- [x] $\Phi_e(x)\diverge$ if and only if $\Phi_e(x)[t]\diverge$ for every $t$.
- [ ] If $\Phi_e(x)\converge$ then $\Phi_e(x)[x]\converge$.

  Nothing bounds the running time in terms of the input.

---

Let $e$ be the code of: *on input $n$, try $r = 0, 1, 2, \dots$ and return the first $r$ with $r \cdot r = n$*. Which statements are true?

- [x] The domain of $\Phi_e$ is the set of perfect squares.
- [x] $\Phi_e(49)\converge = 7$.
- [ ] $\Phi_e$ is total, since $\lfloor \sqrt n \rfloor$ is defined for every $n$.

  $\lfloor\sqrt n\rfloor$ is computable, but by a **different** program. $\Phi_e(50)\diverge$.
:::

## Computable sets

:::definition{#def-computable-set}
A set $A \subseteq \nat$ is **computable** (or *decidable*) if its characteristic function is computable: there is an $e$ such that $\Phi_e$ is total, $\Phi_e(x) = 1$ for $x \in A$, and $\Phi_e(x) = 0$ for $x \notin A$.
:::

The same definition applies to subsets of $\nat^k$, which are often called **predicates**. Computable sets are closed under complement, finite union and intersection, and **bounded** quantification: if $A \subseteq \nat^2$ is computable, so is $\{(x, y) : \exists z < y\ (x, z) \in A\}$, by a `for` loop over $z < y$. Unbounded quantification $\exists z$ would require an unbounded search, which may never stop — this asymmetry will lead us to c.e. sets.

:::quiz
A program halts with output $1$ when $x \in A$, and **runs forever** when $x \notin A$. What can we conclude?

- [ ] $A$ is computable.

  The program never answers "no", so it does not decide $A$.
- [x] Nothing yet about whether $A$ is computable.

  Such sets are called *computably enumerable*. Some are computable, some are not.
- [ ] $A$ is not computable.

  Some other program might decide $A$.
:::

Historically, computable sets were called *recursive*, after the partial recursive functions; the expressions *recursion theory* and *recursive set* are still in use.
