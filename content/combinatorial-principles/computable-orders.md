---
title: A computable order without computable solutions
summary: A computable linear order of type ω + ω* with no computable ascending or descending sequence (Tennenbaum, Denisov), by a finite injury construction with a moving cut; RCA₀ proves neither ADS nor CAC.
duration: 35
prerequisites: [orders, ce-degrees/friedberg-muchnik]
---

The previous lesson showed that the solutions of a stable linear order are the infinite subsets of its two parts. To build an order without computable solutions, it is therefore enough to make both parts free of infinite c.e. subsets. This lesson does it with a finite injury priority construction, in which the order of the numbers never changes, but the boundary between the two parts does.

## The construction

:::theorem[Tennenbaum; Denisov]{#thm-tennenbaum-denisov}
There is a computable linear order of $\nat$ of order type $\omega + \omega^*$ with no infinite computable ascending or descending sequence.
:::

**Intuition.** The order will be stable, with parts $A$ and $A^*$. By :ref{#prop-stable-order-solutions}, a computable solution would be an infinite computable subset of $A$ or of $A^*$. It suffices to meet, for every $e$, the requirement
$$
\mathcal R_e : \text{if } W_e \text{ is infinite, then } W_e \text{ meets both } A \text{ and } A^*.
$$
The order is built by inserting the number $s$ at stage $s$, and never changes the relative order of numbers already placed. What changes is a **cut**, a partition of the numbers placed so far into a left part, our current guess at $A$, and a right part, our guess at $A^*$; each new number is inserted at the cut. The requirement $\mathcal R_e$ waits for two elements $u <_L v$ of $W_e$ and moves the cut between them; from then on it **protects** $u$ on the left and $v$ on the right: the cut may not cross them again. Two requirements may conflict, and priority decides, as in the Friedberg–Muchnik theorem (:ref{#thm-friedberg-muchnik}): $\mathcal R_e$ chooses its elements strictly between those protected by stronger requirements, and when it acts, the weaker requirements lose their protected elements. Finally, the order type requires that every number changes side only finitely often. This is the job of a second family of requirements: $\mathcal P_z$ protects the number $z$ on whatever side it currently lies, without moving the cut.

:::proof{of=thm-tennenbaum-denisov}
*Construction.* The requirements are ordered by priority as $\mathcal R_0, \mathcal P_0, \mathcal R_1, \mathcal P_1, \ldots$. At stage $s$ we have a linear order $\leq_{L,s}$ of $\{ 0, \ldots, s - 1 \}$ and a partition of this set into a left part $\mathrm{Left}_s$ and a right part $\mathrm{Right}_s$, every element of the left part being $<_{L,s}$-below every element of the right part. A requirement $\mathcal R_e$ may have two **protected elements** $u_e \in \mathrm{Left}_s$ and $v_e \in \mathrm{Right}_s$; a requirement $\mathcal P_z$ may have the protected element $z$. For a requirement $\mathcal Q$, its **interval** $I_s(\mathcal Q)$ is the set of $x < s$ such that $a <_{L,s} x <_{L,s} b$ for all elements $a \in \mathrm{Left}_s$ and $b \in \mathrm{Right}_s$ protected by requirements of higher priority than $\mathcal Q$.

Initially, at stage $0$, the order and both parts are empty, and no element is protected. At stage $s$:

- $\mathcal R_e$, for $e < s$, **requires attention** if it has no protected elements and there are $u <_{L,s} v$ in $W_{e,s} \cap I_s(\mathcal R_e)$;
- $\mathcal P_z$, for $z < s$, requires attention if it has no protected element.

If some requirement requires attention, let $\mathcal Q$ be the one of highest priority. If $\mathcal Q = \mathcal R_e$, take the least pair $\langle u, v \rangle$ as above, let the new left part be $\{ x < s : x \leq_{L,s} u \}$ and the new right part the rest, and protect $u_e = u$ and $v_e = v$. If $\mathcal Q = \mathcal P_z$, protect $z$, and leave the cut unchanged. In both cases, the requirements of lower priority than $\mathcal Q$ lose their protected elements; we say they are **injured**. Finally insert $s$ as the largest element of the left part: $x <_{L,s+1} s$ for $x$ in the left part, $s <_{L,s+1} x$ for $x$ in the right part. This defines $\leq_{L,s+1}$, $\mathrm{Left}_{s+1}$, which contains $s$, and $\mathrm{Right}_{s+1}$.

The order $\leq_L = \bigcup_s \leq_{L,s}$ is computable: whether $x \leq_L y$ is decided at stage $\max(x, y) + 1$ and never changes.

*An invariant.* At every stage, every element protected on the left is in the left part, and every element protected on the right is in the right part. This is preserved by an action of $\mathcal R_e$: the elements protected by stronger requirements satisfy $a <_{L,s} u <_{L,s} v <_{L,s} b$, since $u, v \in I_s(\mathcal R_e)$, so $a$ stays on the left of the new cut and $b$ on its right; and the weaker requirements no longer protect anything. It is preserved by an action of $\mathcal P_z$ and by the insertion of $s$, which do not move the cut. Consequently, the cut always lies strictly between the elements protected on the left and those protected on the right, and so do all numbers inserted at the cut.

*Each requirement acts finitely often.* By induction along the priority order, let $s_0$ be a stage after which no requirement of higher priority than $\mathcal Q$ acts. Then $\mathcal Q$ is not injured after $s_0$, and the elements protected by stronger requirements are fixed after $s_0$. If $\mathcal Q = \mathcal P_z$, it acts at the first stage $s \geq \max(s_0, z + 1)$ at which it has no protected element, if there is one, and then keeps $z$ forever. If $\mathcal Q = \mathcal R_e$, it acts at most once after $s_0$, and then keeps its protected elements. Suppose that $W_e$ is infinite. Every number $s \geq s_0$ is inserted at the cut, hence strictly between the elements protected by stronger requirements, and stays there since these elements are fixed: $s \in I_t(\mathcal R_e)$ for all $t > s$. As $W_e$ is infinite, it has two elements $u, v \geq s_0$, and they belong to $W_{e,t} \cap I_t(\mathcal R_e)$ for large $t$. So either $\mathcal R_e$ already has protected elements, or it requires attention at a stage after $s_0$, at which it is the requirement of highest priority requiring attention, and acts. In both cases, it has permanent protected elements $u_e$ and $v_e$ in $W_e$.

*Each number changes side finitely often.* Only an action of some $\mathcal R_e$ moves the cut. By the previous step, there is a stage $s_1$ after which no requirement of higher priority than $\mathcal P_z$ acts and $\mathcal P_z$ keeps its protected element $z$ forever. A requirement $\mathcal R_e$ of lower priority acting at $t > s_1$ moves the cut to just after an element $u \in I_t(\mathcal R_e)$; if $z$ is on the left, $z <_{L,t} u$ by definition of the interval, and $z$ stays on the left; if $z$ is on the right, $u <_{L,t} v <_{L,t} z$ and $z$ stays on the right. So $z$ never changes side after $s_1$. Let $A$ be the set of numbers that are eventually in the left part, and $A^*$ the set of numbers eventually in the right part; they partition $\nat$.

*The order type.* Let $z \in A$, permanently on the left after stage $t$. Every $s \geq t$ is inserted as the largest element of the left part, so $z <_L s$; hence the predecessors of $z$ are smaller than $t$, and there are finitely many. Similarly, every $z \in A^*$ has only finitely many successors, since every $s$ inserted after $z$ is permanently on the right is placed on the left of the cut, hence before $z$. So the order is stable, with parts $A$ and $A^*$. There are infinitely many $e$ with $W_e$ infinite, for instance infinitely many indices of $\nat$. For each of them, $u_e \in A$, and the elements $u_e$ are pairwise distinct: $u_e$ is chosen strictly to the right of the elements protected on the left by stronger requirements, among which are the final $u_{e'}$ for $e' < e$. So $A$ is infinite, and similarly $A^*$. An infinite initial segment in which every element has finitely many predecessors has type $\omega$; so $L$ has type $\omega + \omega^*$.

*No computable solution.* Let $S$ be an infinite computable ascending sequence. Then $S = W_e$ for some $e$, and $S \subseteq A$ by :ref{#prop-stable-order-solutions}. But $v_e \in W_e \cap A^*$, a contradiction. The case of descending sequences is symmetric, with $u_e \in W_e \cap A$.
:::

:::figure[An action of $\mathcal R_e$ in the proof of :ref{#thm-tennenbaum-denisov}. The numbers placed so far are drawn in their $\leq_L$-order. The elements $a$ and $b$ are protected by stronger requirements, and bound the interval of $\mathcal R_e$. The requirement picks $u <_L v$ in $W_e$ inside this interval, and moves the cut to just after $u$: the elements between $u$ and the old cut, including $v$, now lie in the right part.]
<svg class="fig" viewBox="0 0 600 200" width="600" role="img" aria-label="The finite linear order at a stage, drawn from left to right, with a cut separating the left part from the right part. Two elements protected by stronger requirements bound an interval; the requirement R e picks two elements u and v of W e inside this interval and moves the cut to immediately after u"><defs><marker id="cc-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="accent-fill"/></marker></defs><rect x="150" y="70" width="306" height="44" rx="6" class="soft-fill"/><line x1="30" y1="92" x2="576" y2="92" class="muted-stroke" stroke-width="1"/><circle cx="50" cy="92" r="5" class="node"/><circle cx="96" cy="92" r="5" class="node"/><circle cx="142" cy="92" r="8" class="head-cell"/><text x="142" y="122" text-anchor="middle" class="math">a</text><circle cx="188" cy="92" r="5" class="node"/><circle cx="234" cy="92" r="8" class="node"/><circle cx="234" cy="92" r="3.5" class="ink-fill"/><text x="234" y="122" text-anchor="middle" class="math">u</text><circle cx="280" cy="92" r="5" class="node"/><circle cx="326" cy="92" r="5" class="node"/><circle cx="372" cy="92" r="8" class="node"/><circle cx="372" cy="92" r="3.5" class="ink-fill"/><text x="372" y="122" text-anchor="middle" class="math">v</text><circle cx="418" cy="92" r="5" class="node"/><circle cx="464" cy="92" r="8" class="head-cell"/><text x="464" y="122" text-anchor="middle" class="math">b</text><circle cx="510" cy="92" r="5" class="node"/><circle cx="556" cy="92" r="5" class="node"/><line x1="395.0" y1="52" x2="395.0" y2="132" class="muted-stroke" stroke-width="1.6" stroke-dasharray="5 4"/><text x="395.0" y="46" text-anchor="middle" class="label">old cut</text><line x1="257.0" y1="52" x2="257.0" y2="132" class="ink-stroke" stroke-width="1.8"/><text x="257.0" y="46" text-anchor="middle" class="label">new cut</text><path d="M389.0,138 Q326.0,158 263.0,138" class="accent-stroke" fill="none" stroke-width="1.3" marker-end="url(#cc-arrow)"/><text x="303.0" y="176" text-anchor="middle" class="label">the interval of R_e: strictly between the protected elements of stronger requirements</text><text x="30" y="24" class="label">left part: guessed in A</text><text x="576" y="24" text-anchor="end" class="label">right part: guessed in A*</text></svg>
:::

:::quiz[the construction of Tennenbaum and Denisov]
Why does $\mathcal R_e$ choose its two elements inside its interval $I_s(\mathcal R_e)$, rather than anywhere in $W_{e,s}$?

- [x] Because moving the cut between two arbitrary elements could carry an element protected by a stronger requirement to the wrong side, and undo the satisfaction of that requirement.
- [ ] Because elements outside the interval are not in $W_e$.

  The interval is defined by the order, not by $W_e$; $W_e$ may have elements anywhere.
- [ ] Because elements outside the interval are already in $A$.

  Elements to the right of the interval are on the right part. And the sides of elements are not settled until the construction is over.

---

What would go wrong without the requirements $\mathcal P_z$?

- [x] A number could be crossed by the cut infinitely often, by actions of weaker and weaker requirements; it would then have infinitely many predecessors and infinitely many successors, and the order would not be stable.
- [ ] Some $\mathcal R_e$ would act infinitely often.

  Each $\mathcal R_e$ still acts finitely often: the inductive argument does not use the requirements $\mathcal P_z$. They are needed for the order type, not for the requirements $\mathcal R_e$.
- [ ] The order would not be computable.

  The relative order of two numbers is still fixed when the larger of them is inserted.
:::

The proof is a finite injury argument: the action of a requirement can only be undone by stronger requirements, each of which acts finitely often. The verification is an induction along the priority order on the statement "the requirement eventually stops acting", a $\Sigma^0_2$ statement. This is why such constructions are not in general formalizable in $\mathsf{RCA}_0$, which has only $\Sigma^0_1$ induction (Hirschfeldt, Section 9.3, discusses this point and a way around it). Here, the theorem is used only through its consequence for ω-models.

:::corollary{#cor-rca-not-ads}
The ω-model $\mathrm{REC}$ of the computable sets does not satisfy $\mathsf{ADS}$, even restricted to stable linear orders. Consequently, $\mathsf{RCA}_0$ proves neither $\mathsf{ADS}$ nor $\mathsf{CAC}$.
:::

:::proof{of=cor-rca-not-ads}
The order of :ref{#thm-tennenbaum-denisov} is a stable linear order in $\mathrm{REC}$ with no ascending or descending sequence in $\mathrm{REC}$. $\mathrm{REC}$ is a model of $\mathsf{RCA}_0$ (:ref{#thm-rca-turing-ideal}). If $\mathsf{RCA}_0$ proved $\mathsf{CAC}$, it would prove $\mathsf{ADS}$ by :ref{#prop-rt22-cac-ads}.
:::

How far is $\mathsf{ADS}$ from computable? For stable orders, not far: every computable stable linear order has a low ascending or descending sequence (Hirschfeldt and Shore; the course on lowness, :ref{to="lowness/stable-linear-orders"}). For arbitrary orders, Hirschfeldt and Shore built a computable linear order with no low ascending or descending sequence, from a computable partial order of Herrmann (2001) with no infinite $\Delta^0_2$ chain or antichain. By comparison, some computable colorings of pairs have no $\Delta^0_2$ homogeneous set (:ref{#thm-jockusch-no-delta2}). We admit these two results; the next lessons show that $\mathsf{ADS}$ is nevertheless not weak: it implies cohesiveness.

::::exercise{#ex-omega-order-computable difficulty=1 objective="See that a computable linear order of type ω always has a computable solution, so that the order type ω + ω* is the first one where ADS is not computably true."}
Show that every computable linear order of order type $\omega$ has an infinite computable ascending sequence, and every computable linear order of type $\omega^*$ an infinite computable descending sequence.

:::solution
In an order of type $\omega$, every element has finitely many predecessors, so $A = \nat$, which is an infinite computable subset of $A$; by :ref{#prop-stable-order-solutions}, with $H = \nat$, the order computes an ascending sequence. The construction there is explicit: $h_0 = 0$ and $h_{k+1}$ is the least $y > h_k$ with $h_k <_L y$. The case of $\omega^*$ is symmetric.
:::
::::

## Notes and references

:ref{#thm-tennenbaum-denisov} is due independently to Tennenbaum (see Rosenstein's *Linear Orderings*) and Denisov (see Goncharov and Nurtazin, 1973). Hirschfeldt proves the version without the order type as Theorem 9.11, with the requirements $\mathcal R_e$ only, and leaves the order type $\omega + \omega^*$ as Exercise 9.12; the requirements $\mathcal P_z$ used here are one way to obtain it. Dzhafarov and Mummert state the theorem in Section 9.2.1. Herrmann's partial order is in Herrmann (2001), and the order with no low solution in Hirschfeldt and Shore (2007) (Hirschfeldt, Theorem 9.5 and Exercise 9.6).

- J. G. Rosenstein, *Linear Orderings*, Academic Press, 1982.
- S. S. Goncharov and A. T. Nurtazin, *Constructive models of complete solvable theories*, Algebra and Logic 12 (1973), 67–77.
- E. Herrmann, *Infinite chains and antichains in computable partial orderings*, Journal of Symbolic Logic 66 (2001), 923–934.
- D. R. Hirschfeldt and R. A. Shore, *Combinatorial principles weaker than Ramsey's theorem for pairs*, Journal of Symbolic Logic 72 (2007), 171–206.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2014, Section 9.1.

:::::exercises
::::exercise{#ex-stable-order-immune difficulty=2 objective="Relate computable solutions of a stable order to c.e. subsets of its parts, and see why the requirements were stated with c.e. sets."}
Let $L$ be a computable stable linear order with parts $A$ and $A^*$.

1. Show that $L$ has an infinite computable ascending sequence if and only if $A$ has an infinite c.e. subset.
2. Show that if $A$ and $A^*$ are both infinite and neither has an infinite c.e. subset, then $A$ is not $\Sigma^0_1$ and not $\Pi^0_1$.

:::solution
1. A computable ascending sequence is an infinite computable, hence c.e., subset of $A$ by :ref{#prop-stable-order-solutions}. Conversely, an infinite c.e. set has an infinite computable subset, obtained by listing the elements enumerated after a larger element (the elements $x_0 < x_1 < \cdots$ with $x_{k+1}$ the first element enumerated larger than $x_k$); this subset of $A$ computes an ascending sequence by :ref{#prop-stable-order-solutions}, with the computable oracle $L$.
2. If $A$ were $\Sigma^0_1$, it would be an infinite c.e. subset of itself. If $A$ were $\Pi^0_1$, its complement $A^*$ would be an infinite c.e. set.
:::
::::
:::::
