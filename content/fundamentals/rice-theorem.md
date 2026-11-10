---
title: Rice's theorem
summary: Non-trivial index sets are not computable. A consequence of the fixed point theorem.
duration: 10
prerequisites: [fixed-point, halting-problem]
---

Rice's theorem (1951) generalizes the undecidability of the halting problem: no non-trivial property of the partial function computed by a program is decidable from its code. This applies, for instance, to totality, to finiteness of the domain, and to equality with a fixed function.

## Behavioral properties

We must distinguish properties of a program's *text* ("does the code contain a `while` loop?" — decidable by inspection) from properties of its *behavior*.

:::definition{#def-index-set}
A set $P \subseteq \nat$ is an **index set** if it respects behavior: whenever $\Phi_{e_1} = \Phi_{e_2}$, we have $e_1 \in P \iff e_2 \in P$. It is **non-trivial** if $P \neq \emptyset$ and $P \neq \nat$.
:::

For example, $\{e : \Phi_e \text{ is total}\}$ and $\{e : \Phi_e(0)\converge = 42\}$ are non-trivial index sets. The set $\{e : e \text{ is even}\}$ is not an index set: every function has both even and odd codes.

:::quiz
Which of these sets are index sets?

- [x] $\{e : \Phi_e(3)\converge\}$
- [x] $\{e : W_e \text{ is finite}\}$, where $W_e$ is the domain of $\Phi_e$.
- [ ] $\{e : \text{the program of code } e \text{ has fewer than } 100 \text{ instructions}\}$

  A property of the text, not of the behavior: padding a short program gives a long one computing the same function.
- [ ] $\{e : \Phi_e(e)\converge\}$

  No: one can construct $e_1 \neq e_2$ with $\Phi_{e_1} = \Phi_{e_2}$, $\Phi_{e_1}(e_1)\converge$ but $\Phi_{e_2}(e_2)\diverge$. The diagonal input depends on the code, not just the function.
:::

## The theorem

:::theorem[Rice]{#thm-rice}
No non-trivial index set is computable.
:::

:::proof{of=thm-rice}
Let $P$ be a non-trivial index set, and suppose it is computable. Fix $a \in P$ and $b \notin P$, and define
$$
f(x) = \begin{cases} b & \text{if } x \in P, \\ a & \text{if } x \notin P. \end{cases}
$$
Since $P$ is computable, $f$ is total computable. By :ref{#thm-fixed-point}, there is an $e$ with $\Phi_{f(e)} = \Phi_e$. As $P$ is an index set, $e \in P \iff f(e) \in P$. But by construction, $e \in P \iff f(e) = b \notin P$. Contradiction.
:::

:::quiz
The function $f$ maps codes in $P$ to $b \notin P$ and codes outside $P$ to $a \in P$. Which property of $f$ makes the fixed point lead to a contradiction?

- [x] $f$ always moves a code **across** the boundary of $P$, while a fixed point $e$ and its image $f(e)$ compute the same function, so must stay on the same side.
- [ ] $f$ is injective.

  $f$ takes only two values: it is far from injective.
- [ ] $f(e) = e$ for some $e$.

  The fixed point theorem gives $\Phi_{f(e)} = \Phi_e$, not $f(e) = e$; in fact $f(e) \neq e$ always here.

---

Where is the computability of $P$ used?

- [x] To make $f$ computable, which is required to apply the fixed point theorem.
- [ ] To choose $a \in P$ and $b \notin P$.

  This only uses non-triviality; no algorithm is needed to fix two numbers.
- [ ] To show that $P$ is an index set.

  That is a hypothesis about $P$, unrelated to its computability.
:::

## Consequences and limits

In particular, whether a program meets a behavioral specification is undecidable in general; this is the theoretical limitation underlying automated program verification.

Rice's theorem is about **decidability** only. Some index sets are c.e. — for instance $\{e : \Phi_e(0)\converge\}$ — while others, such as $\{e : \Phi_e \text{ is total}\}$, are not even c.e. Measuring exactly *how* undecidable they are is the purpose of the arithmetic hierarchy.

::::exercise{difficulty=1}
Deduce from Rice's theorem that there is no algorithm which, given two codes $e_1$ and $e_2$, decides whether $\Phi_{e_1} = \Phi_{e_2}$.

:::solution
Fix a code $z$ of the nowhere-defined function. If equality of programs were decidable, then $\{e : \Phi_e = \Phi_z\}$ would be computable. It is an index set, non-trivial since it contains $z$ and not a code of the constant function $0$. This contradicts :ref{#thm-rice}.
:::
::::
