---
title: A low simple set
summary: A c.e. set that is simple and low, built by finite injury; preservation of computations by restraints; a second solution to Post's problem.
duration: 40
prerequisites: [friedberg-muchnik, turing-degrees/low-and-high]
---

The Friedberg–Muchnik construction builds two sets and makes them incomparable. A single set solves Post's problem as well, if it is non-computable and **low**: a low set is never Turing complete (:ref{#prop-low-basic}). In the course on Turing degrees, a non-computable low set was obtained by finite extensions with the oracle $\emptyset'$. This lesson builds one that is c.e., and even simple, by a finite injury construction. The construction introduces the second basic ingredient of priority arguments: requirements that **preserve** computations by restraining the set, rather than diagonalizing.

:::theorem{#thm-low-simple}
There is a simple set $A$ that is low.
:::

:::corollary{#cor-low-simple-post}
There is a c.e. set $A$ with $\emptyset <_T A <_T \emptyset'$.
:::

:::proof{of=cor-low-simple-post}
A simple set is not computable, and a low set is not Turing complete, by :ref{#prop-low-basic}.
:::

## The requirements

We enumerate $A$ by stages $A_0 \subseteq A_1 \subseteq \cdots$, and satisfy, for every $e$:
$$
\begin{aligned}
\mathcal P_e &: \ W_e \text{ is infinite} \ \Rightarrow\ W_e \cap A \neq \emptyset, \\
\mathcal N_e &: \ \Phi^{A_s}_e(e)[s]\converge \text{ for infinitely many } s \ \Rightarrow\ \Phi^A_e(e)\converge.
\end{aligned}
$$
The **positive** requirements $\mathcal P_e$ make the complement of $A$ meet every infinite c.e. set; together with a counting argument that keeps the complement infinite, they make $A$ simple. The **negative** requirements $\mathcal N_e$ ensure lowness, as shown in the verification: they say that a computation $\Phi^A_e(e)$ that keeps appearing during the construction must eventually be preserved.

The priority order is $\mathcal N_0 > \mathcal P_0 > \mathcal N_1 > \mathcal P_1 > \cdots$: the requirement $\mathcal P_e$ must respect the restraints of $\mathcal N_0, \dots, \mathcal N_e$, and may ignore those of $\mathcal N_{e+1}, \mathcal N_{e+2}, \dots$.

:::definition{#def-restraint-function}
The **restraint** of $\mathcal N_e$ at stage $s$ is $r(e, s) = \use^{A_s}_e(e)$ if $\Phi^{A_s}_e(e)[s]\converge$, and $r(e, s) = 0$ otherwise.
:::

Since computations converging at stage $s$ have use at most $s$, the restraint is at most $s$, and it is computable from $e$ and $s$.

## The construction

*Stage $0$.* $A_0 = \emptyset$.

*Stage $s + 1$.* Say that $\mathcal P_e$ **requires attention** at stage $s + 1$ if $e \leq s$, $W_e[s] \cap A_s = \emptyset$, and there is $x \in W_e[s]$ with
$$
x > 2e \quad\text{and}\quad x > r(i, s) \text{ for every } i \leq e.
$$
If some $\mathcal P_e$ requires attention, take the least such $e$, and enumerate into $A$ the least $x$ satisfying the condition. We say that $\mathcal P_e$ **acts**. Otherwise, $A_{s+1} = A_s$.

The construction is computable, so $A$ is c.e. Once $\mathcal P_e$ has acted, $W_e \cap A \neq \emptyset$, so it never requires attention again: **each positive requirement acts at most once**.

## Verification

:::lemma{#lem-low-coinfinite}
The complement of $A$ is infinite.
:::

:::proof{of=lem-low-coinfinite}
Each $\mathcal P_e$ enumerates at most one number, and this number is greater than $2e$. So the numbers of $A$ below $2n + 1$ come from requirements $\mathcal P_e$ with $e < n$, and there are at most $n$ of them. At least $n + 1$ of the numbers $0, \dots, 2n$ are outside $A$, for every $n$.
:::

We say that $\mathcal N_e$ is **injured** at stage $s + 1$ if a number $x \leq r(e, s)$ is enumerated into $A$ at stage $s + 1$, while $r(e, s) > 0$.

:::lemma{#lem-low-negative}
For every $e$, the requirement $\mathcal N_e$ is injured at most $e$ times, the limit $r_e = \lim_s r(e, s)$ exists, and
$$
\lim_s g(e, s) = A'(e), \qquad\text{where } g(e, s) = 1 \text{ if } \Phi^{A_s}_e(e)[s]\converge, \text{ and } g(e, s) = 0 \text{ otherwise.}
$$
:::

:::proof{of=lem-low-negative}
A number enumerated by $\mathcal P_i$ with $i \geq e$ is greater than $r(e, s)$, so only the requirements $\mathcal P_i$ with $i < e$ can injure $\mathcal N_e$; each acts at most once, so $\mathcal N_e$ is injured at most $e$ times. Let $s_0$ be a stage after the last injury.

Suppose $\Phi^{A_s}_e(e)[s]\converge$ with use $u = r(e, s)$, for some $s \geq s_0$. The number enumerated at stage $s + 1$, if any, is greater than $u$, since $\mathcal N_e$ is not injured. So $A_{s+1} \uh u = A_s \uh u$, and by monotonicity of stages and the use principle $\Phi^{A_{s+1}}_e(e)[s + 1]\converge$ with the same use. By induction, the computation converges at every stage $t \geq s$ with use $u$, and $A \uh u = A_s \uh u$; hence $\Phi^A_e(e)\converge$, $g(e, t) = 1$ and $r(e, t) = u$ for all $t \geq s$.

If no such $s \geq s_0$ exists, then $g(e, t) = 0$ and $r(e, t) = 0$ for all $t \geq s_0$, and $\Phi^A_e(e)\diverge$: if it converged, with use $u$, then for large $t$ we would have $A_t \uh u = A \uh u$ and $\Phi^{A_t}_e(e)[t]\converge$. In both cases, $\lim_s g(e, s)$ exists and equals $A'(e)$, and $r(e, s)$ is eventually constant.
:::

:::lemma{#lem-low-positive}
Every requirement $\mathcal P_e$ is satisfied.
:::

:::proof{of=lem-low-positive}
Suppose $W_e$ is infinite. By :ref{#lem-low-negative} and since each $\mathcal P_i$ acts at most once, there is a stage $s_1$ after which no $\mathcal P_i$ with $i < e$ acts and $r(i, s) = r_i$ for all $i \leq e$. Let $m = \max(2e, r_0, \dots, r_e)$. Since $W_e$ is infinite, some $x > m$ belongs to $W_e[s]$ for some $s \geq \max(s_1, e)$. If $W_e[s] \cap A_s \neq \emptyset$ at that stage, $\mathcal P_e$ is satisfied. Otherwise $\mathcal P_e$ requires attention at stage $s + 1$. No $\mathcal P_i$ with $i < e$ requires attention, since it would act; so $\mathcal P_e$ acts, and $W_e \cap A \neq \emptyset$.
:::

:::proof{of=thm-low-simple}
$A$ is c.e., its complement is infinite by :ref{#lem-low-coinfinite}, and meets every infinite c.e. set by :ref{#lem-low-positive}; so $A$ is simple. By :ref{#lem-low-negative}, the computable function $g$ is a $\Delta^0_2$ approximation of $A'$. By the limit lemma (:ref{#thm-limit-lemma}), $A' \leq_T \emptyset'$, that is, $A$ is low.
:::

The two kinds of requirements have opposite needs. A positive requirement wants to put numbers into $A$; a negative one wants to keep numbers out of $A$, below its restraint. The negative requirement $\mathcal N_e$ only needs its restraint to be respected from some point on, and the positive requirements of lower priority, which respect it, still have room: the restraint is finite, and an infinite $W_e$ has elements beyond it. This balance — a finite restraint against an infinite supply of candidates — is the core of finite injury arguments.

:::quiz[the low simple set]
Why may a positive requirement $\mathcal P_i$ with $i < e$ ignore the restraint of $\mathcal N_e$?

- [x] Because it has higher priority; and since it acts at most once, the injuries it causes to $\mathcal N_e$ are finitely many, which $\mathcal N_e$ can tolerate.

  If every positive requirement had to respect every restraint, a positive requirement might wait forever behind the restraints of infinitely many negative requirements.
- [ ] Because $\mathcal N_e$ is already satisfied.

  Nothing guarantees this at the time $\mathcal P_i$ acts; the injury is harmless because it happens only finitely often.
- [ ] Because the restraint of $\mathcal N_e$ is $0$.

  The restraint may be positive; the point is that injuring it finitely often is harmless.

---

In :ref{#lem-low-negative}, why does a computation $\Phi^{A_s}_e(e)[s]$ found after the last injury remain convergent forever?

- [x] Because the numbers enumerated afterwards are all greater than its use, so the part of the oracle it reads never changes.
- [ ] Because $A$ is low.

  Lowness is what is being proved.
- [ ] Because computations with a c.e. oracle never change.

  A computation with oracle $A_s$ may disappear when a number below its use enters $A$; this is exactly what an injury is.

---

Why does $g$ provide a $\Delta^0_2$ approximation of $A'$?

- [x] Because for each $e$, the value $g(e, s)$ is eventually constant, and its final value is $1$ exactly when $\Phi^A_e(e)\converge$.

  Without the restraints, $g(e, s)$ could change infinitely often, as the computation appears and disappears.
- [ ] Because $g$ is computable.

  Computability is needed, but the essential point is the existence of the limit.
- [ ] Because $A'$ is c.e.

  $A'$ is $A$-c.e.; it is not c.e. in general.
:::

## Exercises

::::exercise{difficulty=1}
Show that for every $e$, the value $g(e, s)$ changes at most $2e + 1$ times as $s$ increases. Deduce that $A'$ has a $\Delta^0_2$ approximation whose number of changes at $e$ is bounded by a computable function of $e$.

:::solution
Between two consecutive injuries of $\mathcal N_e$, and after the last one, the argument of :ref{#lem-low-negative} shows that once $\Phi^{A_s}_e(e)[s]$ converges, it keeps converging until the next injury. So on each of these intervals, $g(e, \cdot)$ changes at most once from $0$ to $1$, and it can change from $1$ to $0$ only at an injury. There are at most $e$ injuries, hence at most $e + 1$ intervals, and at most $(e + 1) + e = 2e + 1$ changes. The function $g$ itself is such an approximation of $A'$.
:::
::::

::::exercise{difficulty=2}
Show that every c.e. set $C$ is the union of two disjoint low c.e. sets $C_0$ and $C_1$.

:::hint
Enumerate $C$ one element at a time, and put each element into one of the two sets, so as to injure the restraint of highest priority as rarely as possible.
:::

:::solution
If $C$ is finite, take $C_0 = C$ and $C_1 = \emptyset$. Otherwise, let $c_0, c_1, \dots$ be a computable injective enumeration of $C$. For $i \in \{0, 1\}$ and every $e$, let $\mathcal N_{e,i}$ be the requirement $\mathcal N_e$ for the set $C_i$, with restraint $r(e, i, s)$ defined as above with $C_{i,s}$ in place of $A_s$, and order them as $\mathcal N_{0,0} > \mathcal N_{0,1} > \mathcal N_{1,0} > \cdots$. At stage $s + 1$, consider $c_s$: if some $\mathcal N_{e,i}$ has $c_s \leq r(e, i, s)$, take the one of highest priority and put $c_s$ into $C_{1-i}$; otherwise put $c_s$ into $C_0$.

By induction along the priority order, each $\mathcal N_{e,i}$ is injured finitely often. Suppose the restraints of all requirements of higher priority converge, with maximum limit $R$, from stage $s_0$ on. After $s_0$, an injury of $\mathcal N_{e,i}$ puts $c_s \leq r(e, i, s)$ into $C_i$, which by the rule only happens if a requirement $\mathcal N_{e', 1-i}$ of higher priority has $c_s \leq r(e', 1-i, s) \leq R$. Only finitely many elements of $C$ are at most $R$, and each is enumerated once, so $\mathcal N_{e,i}$ is injured finitely often. Then, as in :ref{#lem-low-negative}, its restraint converges and $\lim_s g_i(e, s) = C_i'(e)$. So both sets are low, they are disjoint, and their union is $C$.
:::
::::

## Notes and references

The construction follows Soare's textbook, where low simple sets and the terminology of positive and negative requirements and restraints are developed systematically. The splitting of the second exercise is a weak form of the Sacks splitting theorem of the next lesson.

- R. I. Soare, *Recursively Enumerable Sets and Degrees*, Springer, 1987.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016.
