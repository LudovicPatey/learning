---
title: The Sacks splitting theorem
summary: Splitting a c.e. set into two c.e. sets that avoid the cone above a non-computable c.e. set; the length of agreement and Sacks' preservation strategy; consequences for the c.e. degrees.
duration: 45
prerequisites: [low-simple-set]
---

The requirements met so far were either diagonalization requirements, which act once, or preservation requirements for a single computation. To ensure that a set $A_i$ does **not** compute a given non-computable set $B$, neither suffices: there are infinitely many potential reductions $\Phi_e$, and for each of them the construction cannot know whether $\Phi^{A_i}_e = B$ will hold. Sacks found a strategy that turns the hypothesis "$B$ is not computable" into a tool: preserve the agreement between $\Phi^{A_i}_e$ and $B$ as far as it goes. If the agreement were total, the preserved computations would compute $B$. So it is not, and the restraints needed stay finite. This lesson applies the strategy to split a c.e. set into two parts that both avoid the cone above $B$.

:::theorem[Sacks splitting theorem]{#thm-sacks-splitting}
Let $A$ and $B$ be c.e. sets, with $B$ not computable. There are disjoint c.e. sets $A_0$ and $A_1$ with $A_0 \cup A_1 = A$, $A_0, A_1 \leq_T A$, and $B \not\leq_T A_0$, $B \not\leq_T A_1$.
:::

## Length of agreement

If $A$ is finite, take $A_0 = A$ and $A_1 = \emptyset$, which are computable, so that neither computes $B$. Assume from now on that $A$ is infinite, and fix a computable injective enumeration $a_0, a_1, a_2, \dots$ of $A$ (:ref{#prop-ce-range}) and a c.e. approximation $(B_s)$ of $B$. We build $A_0$ and $A_1$ by putting each $a_s$ into one of them at stage $s + 1$; so $A_{i,s}$ is the part of $A_i$ built at the end of stage $s$, and $A_0 \cup A_1 = A$, $A_0 \cap A_1 = \emptyset$. The requirements are, for every $e$ and $i \in \{0, 1\}$,
$$
\mathcal R_{e,i} : \Phi^{A_i}_e \neq B,
$$
ordered by priority according to the code $\langle e, i \rangle$: the smaller the code, the higher the priority.

:::definition{#def-length-agreement}
For $e$, $i$ and $s$:

1. the **length of agreement** $l(e, i, s)$ is the largest $y \leq s$ such that $\Phi^{A_{i,s}}_e(x)[s]\converge = B_s(x)$ for every $x < y$;
2. the **restraint** $r(e, i, s)$ is the largest use $\use^{A_{i,s}}_e(x)$ of a computation $\Phi^{A_{i,s}}_e(x)[s]$ that converges, for $x \leq l(e, i, s)$; it is $0$ if there is none.
:::

The restraint protects the computations below the length of agreement, **and** the computation at the length of agreement itself, if it converges. At that point the computation disagrees with $B_s$, or $B$ has just changed there. Protecting it is what makes the strategy work, as the proof of the main lemma shows.

## The construction

*Stage $s + 1$.* If there is a pair $\langle e, i \rangle \leq s$ with $a_s \leq r(e, i, s)$, take the one with the smallest code, and put $a_s$ into $A_{1-i}$. Otherwise, put $a_s$ into $A_0$.

In words: the new element is put on the side opposite to the most important restraint it would violate. We say that $\mathcal R_{e,i}$ is **injured** at stage $s + 1$ if $a_s \leq r(e, i, s)$ and $a_s$ is put into $A_i$.

The construction is computable, so $A_0$ and $A_1$ are c.e., disjoint, with union $A$. Each is computable in $A$: to decide whether $x \in A_i$, decide whether $x \in A$; if so, find the $s$ with $a_s = x$, and run the construction up to stage $s + 1$.

## Verification

:::lemma{#lem-sacks-main}
For every $e$ and $i$, writing $k = \langle e, i \rangle$:

1. $\mathcal R_{e,i}$ is injured only finitely often;
2. $\Phi^{A_i}_e \neq B$;
3. the restraint $r(e, i, s)$ is bounded, and in fact eventually constant.
:::

:::proof{of=lem-sacks-main}
By induction on $k$. Suppose the three statements hold for all codes smaller than $k$, and let $R$ bound the restraints of all requirements of higher priority, at all stages.

*Item 1.* Suppose $\mathcal R_{e,i}$ is injured at stage $s + 1$. Then $a_s \leq r(e, i, s)$, so the pair of smallest code whose restraint is at least $a_s$ has code at most $k$; since $a_s$ goes into $A_i$, this pair is some $\langle e', 1 - i \rangle$, of code smaller than $k$. So $a_s \leq r(e', 1 - i, s) \leq R$. Since the enumeration is injective, this happens for finitely many $s$. Let $s_0$ be a stage after the last injury, and after the last enumeration of a number at most $R$.

*Preservation.* For $s \geq s_0$, no number at most $r(e, i, s)$ enters $A_i$ at stage $s + 1$. So every computation $\Phi^{A_{i,s}}_e(x)[s]$ with $x \leq l(e, i, s)$ that converges also converges at stage $s + 1$, with the same value and use.

*Item 2.* Suppose, towards a contradiction, that $\Phi^{A_i}_e = B$. Then $l(e, i, s) \to \infty$: for each $y$, once $A_i$ has settled below the uses of the computations $\Phi^{A_i}_e(x)$ for $x < y$, and $B$ has settled below $y$, these computations converge with the correct values at all large stages. We show that $B$ is computable, by the following procedure: to compute $B(p)$, find a stage $s \geq s_0$ with $l(e, i, s) > p$, and output $B_s(p)$.

Suppose the output is wrong for some $p$. Since $B$ is c.e., $B_s(p) = 0$ and $p$ enters $B$ after stage $s$. Let $q \leq p$ be the least number that enters $B$ after stage $s$. We claim that for all $t \geq s$, the computations $\Phi^{A_{i,t}}_e(x)[t]$ for $x \leq q$ are the ones found at stage $s$, and $l(e, i, t) \geq q$. This holds at $t = s$. If it holds at $t$, then $q \leq l(e, i, t)$, so the restraint $r(e, i, t)$ covers the uses of these computations, which are preserved at stage $t + 1$. Their values at $x < q$ equal $B_s(x) = B_{t+1}(x)$, since no $x < q$ enters $B$ after stage $s$, so $l(e, i, t + 1) \geq q$. Hence $\Phi^{A_i}_e(q) = \Phi^{A_{i,s}}_e(q)[s] = B_s(q) = 0$, while $q \in B$: this contradicts $\Phi^{A_i}_e = B$. So the procedure computes $B$, contradicting the hypothesis on $B$.

*Item 3.* By item 2, let $p$ be the least number with $\Phi^{A_i}_e(p) \neq B(p)$, either because $\Phi^{A_i}_e(p)$ diverges or because it converges to another value. For $x < p$, the computation $\Phi^{A_i}_e(x)$ converges to $B(x)$; once $A_i$ has settled below its use and $B$ has settled below $p + 1$, the computation found at each large stage is this one, with a fixed use. So $l(e, i, s) \geq p$ for all large $s$.

We show that $l(e, i, s) \leq p$ for all large $s$. If $\Phi^{A_i}_e(p)$ converges to a value different from $B(p)$, then at large stages the computation at $p$ is the true one and disagrees with $B_s(p) = B(p)$. If $\Phi^{A_i}_e(p)$ diverges, suppose $l(e, i, s) > p$ for some $s \geq s_0$ at which $B$ has settled below $p + 1$. Then the computations at $x \leq p$ converge at stage $s$; by preservation and since $B$ no longer changes below $p + 1$, they converge at every later stage with $l(e, i, t) > p$, so $\Phi^{A_i}_e(p)$ converges, a contradiction.

So $l(e, i, s) = p$ for all large $s$. The restraint is then the maximum of the uses of the computations at $x < p$, which are eventually fixed, and of the use of the computation at $p$, if it converges. In the first case, the latter is eventually the true computation, with a fixed use. In the second case, a computation at $p$ converging at a stage $s \geq s_0$ with $l(e, i, s) = p$ would be preserved forever, so that $\Phi^{A_i}_e(p)$ would converge; hence the computation at $p$ eventually diverges at every stage. In both cases $r(e, i, s)$ is eventually constant.
:::

:::proof{of=thm-sacks-splitting}
The sets $A_0$ and $A_1$ are c.e., disjoint, with union $A$, and computable in $A$. By :ref{#lem-sacks-main}, $\Phi^{A_i}_e \neq B$ for every $e$ and $i$, so neither $A_0$ nor $A_1$ computes $B$.
:::

The procedure in item 2 is the heart of **Sacks' preservation strategy**. The requirement does not try to make $\Phi^{A_i}_e$ differ from $B$. It preserves the agreement as far as it goes, and lets the non-computability of $B$ guarantee that the agreement cannot be total. If it were, the preserved computations would compute $B$, since an element entering $B$ below the length of agreement would create a permanent disagreement.

:::quiz[the preservation strategy]
Why does the restraint protect the computation at $x = l(e, i, s)$, and not only those below the length of agreement?

- [x] When an element $q$ enters $B$ below a previous length of agreement, the length of agreement drops to $q$, and the computation at $q$, now a disagreement, must remain protected to become a permanent disagreement.

  Without this, the computation at $q$ could be destroyed and replaced by one that agrees with the new value of $B$, and the procedure of item 2 would not compute $B$.
- [ ] Because the computation at $l(e, i, s)$ agrees with $B_s$.

  By definition of the length of agreement, it does not agree, or does not converge.
- [ ] To make the restraint larger than the length of agreement.

  The restraint is a bound on uses, unrelated to the length of agreement as a number.

---

Where is the hypothesis that $B$ is c.e. used?

- [x] In item 2, to know that a wrong output $B_s(p)$ can only be $0$, with $p$ entering $B$ later; a set approximated with removals could also change from $1$ to $0$.

  The argument uses that the changes of $B$ below $p$ are enumerations, which happen at most once for each number.
- [ ] To make the construction computable.

  The construction uses the approximation $(B_s)$, which exists for every $\Delta^0_2$ set; but the argument uses that it is a c.e. approximation.
- [ ] To show that $A_0$ and $A_1$ are c.e.

  This only uses that $A$ is c.e. and the construction is computable.

---

In item 1, why does an injury of $\mathcal R_{e,i}$ involve a requirement of higher priority?

- [x] Because $a_s$ goes into $A_i$ only if the most important restraint it violates belongs to a requirement $\mathcal R_{e', 1-i}$ on the other side, and this requirement is more important than $\mathcal R_{e,i}$, whose restraint is also violated.
- [ ] Because requirements of lower priority never have a restraint.

  They do; they are injured instead.
- [ ] Because $A_i$ is computable in $A$.

  This property of the construction plays no role in the injuries.
:::

## Consequences

:::corollary{#cor-splitting-post}
1. The halting set $\emptyset'$ is the disjoint union of two c.e. sets, neither of which is computable or Turing complete. This gives a third solution to Post's problem.
2. Every non-computable c.e. set $A$ is the disjoint union of two c.e. sets $A_0$ and $A_1$ with $\emptyset <_T A_i <_T A$ and $A_0 \not\leq_T A_1$, $A_1 \not\leq_T A_0$.
:::

:::proof{of=cor-splitting-post}
2. Apply :ref{#thm-sacks-splitting} with $B = A$. Then $A_i \leq_T A$ and $A \not\leq_T A_i$. Since $x \in A$ if and only if $x \in A_0$ or $x \in A_1$, we have $A \leq_T A_0 \oplus A_1$. If $A_0 \leq_T A_1$, then $A \leq_T A_0 \oplus A_1 \leq_T A_1$, a contradiction; so $A_0 \not\leq_T A_1$, symmetrically $A_1 \not\leq_T A_0$, and in particular neither $A_i$ is computable.
1. Item 2 with $A = \emptyset'$.
:::

:::corollary{#cor-no-minimal-ce}
There is no minimal non-computable c.e. degree: below every non-computable c.e. degree $\abf$ there is a c.e. degree $\bbf$ with $\obf < \bbf < \abf$. Moreover, every non-computable c.e. degree is the join of two incomparable c.e. degrees below it.
:::

:::proof{of=cor-no-minimal-ce}
Let $A \in \abf$ be c.e., and $A_0, A_1$ as in :ref{#cor-splitting-post}. Then $\deg_T(A_0)$ is strictly between $\obf$ and $\abf$. Moreover $A_0 \oplus A_1 \equiv_T A$: one direction was shown above, and $A_0, A_1 \leq_T A$ gives the other.
:::

By contrast, Spector showed that there are **minimal** degrees, that is, non-zero degrees with only $\obf$ below them, but none of them is c.e., by the corollary. The structure of the c.e. degrees is much richer than these results show. Sacks proved in 1964 that the c.e. degrees are **dense**: between any two c.e. degrees $\abf < \bbf$ there is a third. Lachlan and Yates proved independently in 1966 that there are **minimal pairs**: non-computable c.e. degrees $\abf$ and $\bbf$ whose only common lower bound is $\obf$. Both proofs use the **infinite injury** method, in which some requirements act infinitely often and the construction is organized along a tree of strategies. We admit these results.

## Exercises

::::exercise{difficulty=1}
Let $B$ be a non-computable c.e. set. Show that there is a c.e. set $C$ that is neither computable nor computes $B$.

:::solution
Apply :ref{#thm-sacks-splitting} to $A = \emptyset'$ and $B$: $\emptyset' = A_0 \sqcup A_1$ with $B \not\leq_T A_i$. If both $A_i$ were computable, so would be $\emptyset' \leq_T A_0 \oplus A_1$. So one of them, $C$, is not computable, and $B \not\leq_T C$. In fact both are non-computable: if $A_0$ were computable, then $B \leq_T \emptyset' \leq_T A_0 \oplus A_1 \leq_T A_1$.
:::
::::

::::exercise{difficulty=2}
In the construction, replace the restraint by the largest use of the computations at $x < l(e, i, s)$ only. Identify the step of the proof of :ref{#lem-sacks-main} that fails.

:::solution
Item 2 fails. When the least number $q$ entering $B$ after stage $s$ enters, the length of agreement becomes at most $q$, and the computation at $q$ is no longer protected. A later element below its use may enter $A_i$ and destroy it, after which $\Phi^{A_i}_e(q)$ may converge to $1 = B(q)$, and the agreement may be restored. The claim that $\Phi^{A_i}_e(q) = B_s(q)$ no longer follows, so the procedure is not shown to compute $B$.
:::
::::

## Notes and references

The splitting theorem is due to Sacks (1963), who also introduced the preservation strategy. The density theorem is due to Sacks (1964); minimal pairs of c.e. degrees are due to Lachlan (1966) and Yates (1966); minimal degrees to Spector (1956). Soare's book of 1987 presents all these results, and the tree method for infinite injury arguments.

- G. E. Sacks, *On the degrees less than 0′*, Annals of Mathematics 77 (1963), 211–231.
- G. E. Sacks, *The recursively enumerable degrees are dense*, Annals of Mathematics 80 (1964), 300–312.
- A. H. Lachlan, *Lower bounds for pairs of recursively enumerable degrees*, Proceedings of the London Mathematical Society (3) 16 (1966), 537–569.
- C. E. M. Yates, *A minimal pair of recursively enumerable degrees*, Journal of Symbolic Logic 31 (1966), 159–168.
- R. I. Soare, *Recursively Enumerable Sets and Degrees*, Springer, 1987.
