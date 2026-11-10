---
title: Computably enumerable sets
summary: Computably enumerable sets, their characterizations, and their relation to computable sets.
duration: 20
prerequisites: [halting-problem]
---

Although the halting problem is not computable, membership in it can be confirmed: if $\Phi_e(e)\converge$, simulating the computation eventually establishes it. Sets with this property are called computably enumerable. Examples include the set of theorems of a computably axiomatized theory, the set of Diophantine equations having a solution, and the word problem of a finitely presented group.

:::definition{#def-ce}
A set $A \subseteq \nat$ is **computably enumerable** (c.e.) if there is a code $e$ such that for every $n$,
$$
n \in A \iff \Phi_e(n)\converge.
$$
We write $W_e = \{n : \Phi_e(n)\converge\}$, so the c.e. sets are exactly the sets $W_0, W_1, W_2, \dots$
:::

Older texts say *recursively enumerable* (r.e.).

## Dovetailing

The definition looks far from "listing the elements". To list $W_e$, we cannot simply run $\Phi_e(0)$, then $\Phi_e(1)$, and so on: if $\Phi_e(0)$ never halts, we would wait forever. Instead we interleave the computations, performing finitely many steps at each stage:

1. test whether $\Phi_e(0)[0]\converge$;
2. test whether $\Phi_e(0)[1]\converge$ or $\Phi_e(1)[1]\converge$;
3. test whether $\Phi_e(0)[2]\converge$, $\Phi_e(1)[2]\converge$ or $\Phi_e(2)[2]\converge$;
4. …

and we list $n$ the first time we find a $t$ with $\Phi_e(n)[t]\converge$. This technique is called **dovetailing**.

:::proposition{#prop-ce-range}
An infinite set $A$ is computably enumerable if and only if there is an injective total computable function $f : \nat \to \nat$ with $f(\nat) = A$.
:::

:::proof{of=prop-ce-range}
Suppose $A = W_e$ is infinite. Define $f$ as follows.

- $f(0)$: find the smallest $t$ such that $\Phi_e(s)[t]\converge$ for some $s \leq t$, and return the smallest such $s$.
- $f(n+1)$: compute $f(0), \dots, f(n)$, then find the smallest $t$ such that $\Phi_e(s)[t]\converge$ for some $s \leq t$ different from all $f(i)$, $i \leq n$, and return the smallest such $s$.

Each search terminates because $A$ is infinite, so $f$ is total; it is injective by construction, and $f(\nat) = A$.

Conversely, if $f(\nat) = A$ with $f$ total computable, let $g$ be the program which on input $n$ searches for a $t$ with $f(t) = n$, and halts when it finds one. Then $g(n)\converge$ if and only if $n \in A$.
:::

:::quiz
Why does the search for $f(n+1)$ always terminate?

- [x] $A$ is infinite, so some $s \in A$ differs from $f(0), \dots, f(n)$; then $\Phi_e(s)[t]\converge$ for some $t$, and the condition holds at stage $\max(s, t)$.

  Both bounds matter: the stage must be large enough for $s \leq t$ and for the computation to have halted.
- [ ] Because $\Phi_e$ is total.

  $\Phi_e$ diverges outside $A$, and $A$ may be very sparse.
- [ ] Because $f(0), \dots, f(n)$ are distinct.

  Distinctness gives injectivity, not termination.

---

Why does the proof search over pairs ($t$, $s \leq t$) instead of running $\Phi_e(0), \Phi_e(1), \dots$ one after the other?

- [x] Because a single divergent computation, say $\Phi_e(0)\diverge$, would block the whole enumeration.
- [ ] To make sure that $f$ enumerates $A$ in increasing order.

  The enumeration is in order of halting time, not in increasing order. (Sets that can be enumerated in increasing order are computable — see the exercises of the next lesson.)
- [ ] Because $\Phi_e(s)[t]\converge$ is not decidable otherwise.

  It is decidable for every $s, t$; the issue is only the order in which we look.

---

In the converse direction, what does $g$ do on an input $n \notin A$?

- [x] It runs forever.

  Exactly what the definition of c.e. requires: halting on $A$, diverging outside.
- [ ] It halts with output $0$.

  That would make $A$ computable. The search for $t$ with $f(t) = n$ has no reason to stop.
- [ ] It halts once $t > n$.

  $f$ is not increasing, so $n$ could still appear later.
:::

::::exercise
Show that every computable set is computably enumerable.

:::solution
If $A$ is computable, consider the program which, on input $x$, decides whether $x \in A$; if so it halts, otherwise it enters an infinite loop. It halts exactly on $A$.
:::
::::

## Computable versus c.e.

:::proposition{#prop-computable-iff-ce-coce}
A set $A$ is computable if and only if both $A$ and $\nat \setminus A$ are computably enumerable.
:::

:::proof{of=prop-computable-iff-ce-coce}
If $A$ is computable, so is $\nat \setminus A$, and both are c.e. by the previous exercise.

Conversely, let $e_1, e_2$ be such that $\Phi_{e_1}(n)\converge \iff n \in A$ and $\Phi_{e_2}(n)\converge \iff n \notin A$. Let $f(n)$ search for the smallest $t$ such that $\Phi_{e_1}(n)[t]\converge$ or $\Phi_{e_2}(n)[t]\converge$, and return $1$ in the first case and $0$ in the second. Then $f$ computes $A$.
:::

:::quiz
Why is the function $f$ in this proof **total**?

- [x] Every $n$ is either in $A$ or in $\nat \setminus A$, so one of the two computations halts at some step $t$.
- [ ] Because both $\Phi_{e_1}$ and $\Phi_{e_2}$ are total.

  Neither is: each diverges on the other set.
- [ ] Because $f$ runs $\Phi_{e_1}(n)$ to completion and then $\Phi_{e_2}(n)$.

  That would fail whenever $n \notin A$. The two computations are run *in parallel*, step by step.

---

Can the search find $t$ such that **both** $\Phi_{e_1}(n)[t]\converge$ and $\Phi_{e_2}(n)[t]\converge$?

- [ ] Yes, and then $f$ must make an arbitrary choice.
- [x] No: the two computations halt on disjoint sets of inputs.

  The two cases of the definition of $f$ never overlap.
:::

## c.e. approximations

A sequence of sets $A_0, A_1, \dots$ is **uniformly computable** if there is a computable $f : \nat^2 \to \{0, 1\}$ with $f(x, n) = 1 \iff x \in A_n$.

:::definition{#def-ce-approx}
A **c.e. approximation** of a set $A$ is a uniformly computable sequence $A_0 \subseteq A_1 \subseteq A_2 \subseteq \cdots$ with $\bigcup_n A_n = A$.
:::

:::proposition{#prop-ce-approx}
A set is computably enumerable if and only if it has a c.e. approximation.
:::

:::proof{of=prop-ce-approx}
If $A = W_e$, let $A_n = \{x : \Phi_e(x)[n]\converge\}$. This is uniformly computable, increasing since halting within $n$ steps implies halting within $n+1$ steps, and its union is $A$.

Conversely, given a c.e. approximation, let $\Phi_e$ compute $A_0(x)$, $A_1(x)$, $A_2(x)$, … until it finds $n$ with $A_n(x) = 1$, and halt then. It halts exactly on $\bigcup_n A_n = A$.
:::

:::notation
Given a c.e. set $A$, we fix a c.e. approximation and write $A[s]$ (or $A_s$) for the approximation of $A$ **at stage $s$**. By convention $A[s]$ is finite and, when non-empty, $\max A[s] < s$.
:::

## The halting problem, revisited

:::theorem{#thm-halting-ce}
The halting problem $\emptyset'$ is computably enumerable, but its complement $\nat \setminus \emptyset'$ is not.
:::

:::proof{of=thm-halting-ce}
The program "on input $e$, run $\Phi_e(e)$ and halt if it does" — available through the universal program — halts exactly on $\emptyset'$. If $\nat \setminus \emptyset'$ were also c.e., then $\emptyset'$ would be computable by :ref{#prop-computable-iff-ce-coce}, contradicting :ref{#thm-halting}.
:::

So the computable sets sit strictly inside the c.e. sets, and the c.e. sets are not closed under complement.

:::quiz
Which statements are correct?

- [x] Every computable set is c.e., but not conversely.
- [x] If $A$ is c.e. and not computable, then $\nat \setminus A$ is not c.e.
- [ ] The complement of a c.e. set is never c.e.

  It is c.e. exactly when the set is computable.
- [ ] Every subset of a c.e. set is c.e.

  $\nat$ is c.e., and has non-c.e. subsets such as $\nat \setminus \emptyset'$.
:::

## Exercises

::::exercise{difficulty=1}
An infinite set $A$ is **enumerable in increasing order** if $A = f(\nat)$ for some total computable $f$ with $f(n) < f(n+1)$ for all $n$. Show that such a set is computable.

:::solution
On input $x$, compute $f(0), f(1), \dots$ until some value exceeds $x$; this happens because $A$ is infinite. Then $x \in A$ iff $x$ appeared among the values computed so far, since all later values are even larger.
:::
::::

::::exercise{difficulty=1}
Show that every infinite c.e. set contains an infinite computable subset.

:::solution
Enumerate $A$ and keep an element only if it is larger than every element kept so far. Since $A$ is infinite, infinitely many elements are kept, and they are kept in increasing order. By the previous exercise, the set of kept elements is computable.
:::
::::

::::exercise{difficulty=2}
Disjoint sets $A$ and $B$ are **computably inseparable** if no computable set $C$ satisfies $A \subseteq C$ and $C \cap B = \emptyset$. Show that $A = \{e : \Phi_e(e)\converge = 0\}$ and $B = \{e : \Phi_e(e)\converge = 1\}$ are c.e. and computably inseparable.

:::solution
Both are c.e.: run $\Phi_e(e)$ and check its output. Suppose $C$ separates them, and let $\Phi_c$ be its (total, $\{0,1\}$-valued) characteristic function. If $\Phi_c(c) = 1$, then $c \in B$ and $c \in C$, contradicting $C \cap B = \emptyset$. If $\Phi_c(c) = 0$, then $c \in A \subseteq C$, so $\Phi_c(c) = 1$ — contradiction.
:::
::::
