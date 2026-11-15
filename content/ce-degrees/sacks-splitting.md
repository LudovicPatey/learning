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

If $A$ is finite, take $A_0 = A$ and $A_1 = \emptyset$, which are computable, so that neither computes $B$. Assume from now on that $A$ is infinite, and fix a computable injective enumeration $a_0, a_1, a_2, \dots$ of $A$ (:ref{#prop-ce-range}) and a c.e. approximation $(B_s)$ of $B$. We build $A_0$ and $A_1$ by putting each $a_s$ into one of them at stage $s + 1$; so $A_{i,s}$ is the part of $A_i$ built at the end of stage $s$, with $A_{0,0} = A_{1,0} = \emptyset$, and $A_0 \cup A_1 = A$, $A_0 \cap A_1 = \emptyset$. The requirements are, for every $e$ and $i \in \{0, 1\}$,
$$
\mathcal R_{e,i} : \Phi^{A_i}_e \neq B,
$$
ordered by priority according to the code $\langle e, i \rangle$: the smaller the code, the higher the priority.

:::definition{#def-length-agreement}
For $e$, $i$ and $s$:

1. the **length of agreement** $l(e, i, s)$ is the largest $y \leq s$ such that $\Phi^{A_{i,s}}_e(x)[s]\converge = B_s(x)$ for every $x < y$;
2. the **restraint** $r(e, i, s)$ is the largest use $\use^{A_{i,s}}_e(x)$ of a computation $\Phi^{A_{i,s}}_e(x)[s]$ that converges, for $x \leq l(e, i, s)$; it is $0$ if there is none.
:::

The restraint protects the computations below the length of agreement, **and** the computation at the length of agreement itself, if it converges. At that point a convergent computation disagrees with $B_s$, typically because an element has just entered $B$ there. Protecting it is what makes the strategy work, as the proof of the main lemma shows.

:::figure[The length of agreement at two stages, with hypothetical values. At stage $s$, the computations at $x < 6$ converge and agree with $B_s$, and the computation at $6$ diverges: $l = 6$, and the restraint protects the uses at $x < 6$. Later, $3$ enters $B$. The protected computation at $3$ still gives $0$, so the length of agreement drops to $3$; the restraint still protects the computation at $3$, which is now a disagreement. If it is never destroyed, the requirement is satisfied at $3$.]
<svg class="fig" viewBox="0 0 590 200" width="590" role="img" aria-label="The length of agreement between the reduction and B at two stages; when a number enters B below the length of agreement, the computation there becomes a disagreement and remains protected"><text x="40" y="74" text-anchor="end" class="math" font-size="15">B<tspan class="mrm" font-size="10" dy="4">t</tspan></text><text x="40" y="104" text-anchor="end" class="mrm" font-size="15">Φ<tspan class="math" font-size="10" dy="-6">A</tspan><tspan class="mrm" font-size="8" dy="3">i,t</tspan></text><text x="160" y="20" text-anchor="middle" class="label">stage t = s</text><text x="69.0" y="44" text-anchor="middle" class="mrm muted" font-size="11">0</text><text x="95.0" y="44" text-anchor="middle" class="mrm muted" font-size="11">1</text><text x="121.0" y="44" text-anchor="middle" class="mrm muted" font-size="11">2</text><text x="147.0" y="44" text-anchor="middle" class="mrm muted" font-size="11">3</text><text x="173.0" y="44" text-anchor="middle" class="mrm muted" font-size="11">4</text><text x="199.0" y="44" text-anchor="middle" class="mrm muted" font-size="11">5</text><text x="225.0" y="44" text-anchor="middle" class="mrm muted" font-size="11">6</text><text x="251.0" y="44" text-anchor="middle" class="mrm muted" font-size="11">7</text><rect x="56" y="52" width="26" height="26" class="cell"/><text x="69.0" y="70" text-anchor="middle" class="mrm" font-size="14">0</text><rect x="82" y="52" width="26" height="26" class="cell"/><text x="95.0" y="70" text-anchor="middle" class="mrm" font-size="14">0</text><rect x="108" y="52" width="26" height="26" class="cell"/><text x="121.0" y="70" text-anchor="middle" class="mrm" font-size="14">1</text><rect x="134" y="52" width="26" height="26" class="cell"/><text x="147.0" y="70" text-anchor="middle" class="mrm" font-size="14">0</text><rect x="160" y="52" width="26" height="26" class="cell"/><text x="173.0" y="70" text-anchor="middle" class="mrm" font-size="14">0</text><rect x="186" y="52" width="26" height="26" class="cell"/><text x="199.0" y="70" text-anchor="middle" class="mrm" font-size="14">1</text><rect x="212" y="52" width="26" height="26" class="cell head-cell"/><text x="225.0" y="70" text-anchor="middle" class="mrm" font-size="14">0</text><rect x="238" y="52" width="26" height="26" class="cell"/><text x="251.0" y="70" text-anchor="middle" class="mrm" font-size="14">0</text><rect x="56" y="82" width="26" height="26" class="cell"/><text x="69.0" y="100" text-anchor="middle" class="mrm" font-size="14">0</text><rect x="82" y="82" width="26" height="26" class="cell"/><text x="95.0" y="100" text-anchor="middle" class="mrm" font-size="14">0</text><rect x="108" y="82" width="26" height="26" class="cell"/><text x="121.0" y="100" text-anchor="middle" class="mrm" font-size="14">1</text><rect x="134" y="82" width="26" height="26" class="cell"/><text x="147.0" y="100" text-anchor="middle" class="mrm" font-size="14">0</text><rect x="160" y="82" width="26" height="26" class="cell"/><text x="173.0" y="100" text-anchor="middle" class="mrm" font-size="14">0</text><rect x="186" y="82" width="26" height="26" class="cell"/><text x="199.0" y="100" text-anchor="middle" class="mrm" font-size="14">1</text><rect x="212" y="82" width="26" height="26" class="cell head-cell"/><text x="225.0" y="100" text-anchor="middle" class="mrm" font-size="14">↑</text><rect x="238" y="82" width="26" height="26" class="cell"/><text x="251.0" y="100" text-anchor="middle" class="mrm" font-size="14">0</text><path d="M58,116 L58,122 L210,122 L210,116" class="ink-stroke" stroke-width="1.3"/><text x="134.0" y="136" text-anchor="middle" class="label">agreement, l = 6</text><rect x="56" y="148" width="156" height="12" class="soft-fill accent-stroke" stroke-width="1"/><text x="56" y="176" class="label">protected: the uses at x &lt; 6</text><text x="442" y="20" text-anchor="middle" class="label">stage t > s, after 3 has entered B</text><text x="351.0" y="44" text-anchor="middle" class="mrm muted" font-size="11">0</text><text x="377.0" y="44" text-anchor="middle" class="mrm muted" font-size="11">1</text><text x="403.0" y="44" text-anchor="middle" class="mrm muted" font-size="11">2</text><text x="429.0" y="44" text-anchor="middle" class="mrm muted" font-size="11">3</text><text x="455.0" y="44" text-anchor="middle" class="mrm muted" font-size="11">4</text><text x="481.0" y="44" text-anchor="middle" class="mrm muted" font-size="11">5</text><text x="507.0" y="44" text-anchor="middle" class="mrm muted" font-size="11">6</text><text x="533.0" y="44" text-anchor="middle" class="mrm muted" font-size="11">7</text><rect x="338" y="52" width="26" height="26" class="cell"/><text x="351.0" y="70" text-anchor="middle" class="mrm" font-size="14">0</text><rect x="364" y="52" width="26" height="26" class="cell"/><text x="377.0" y="70" text-anchor="middle" class="mrm" font-size="14">0</text><rect x="390" y="52" width="26" height="26" class="cell"/><text x="403.0" y="70" text-anchor="middle" class="mrm" font-size="14">1</text><rect x="416" y="52" width="26" height="26" class="cell head-cell"/><text x="429.0" y="70" text-anchor="middle" class="mrm" font-size="14">1</text><rect x="442" y="52" width="26" height="26" class="cell"/><text x="455.0" y="70" text-anchor="middle" class="mrm" font-size="14">0</text><rect x="468" y="52" width="26" height="26" class="cell"/><text x="481.0" y="70" text-anchor="middle" class="mrm" font-size="14">1</text><rect x="494" y="52" width="26" height="26" class="cell"/><text x="507.0" y="70" text-anchor="middle" class="mrm" font-size="14">0</text><rect x="520" y="52" width="26" height="26" class="cell"/><text x="533.0" y="70" text-anchor="middle" class="mrm" font-size="14">0</text><rect x="338" y="82" width="26" height="26" class="cell"/><text x="351.0" y="100" text-anchor="middle" class="mrm" font-size="14">0</text><rect x="364" y="82" width="26" height="26" class="cell"/><text x="377.0" y="100" text-anchor="middle" class="mrm" font-size="14">0</text><rect x="390" y="82" width="26" height="26" class="cell"/><text x="403.0" y="100" text-anchor="middle" class="mrm" font-size="14">1</text><rect x="416" y="82" width="26" height="26" class="cell head-cell"/><text x="429.0" y="100" text-anchor="middle" class="mrm" font-size="14">0</text><rect x="442" y="82" width="26" height="26" class="cell"/><text x="455.0" y="100" text-anchor="middle" class="mrm" font-size="14">0</text><rect x="468" y="82" width="26" height="26" class="cell"/><text x="481.0" y="100" text-anchor="middle" class="mrm" font-size="14">1</text><rect x="494" y="82" width="26" height="26" class="cell"/><text x="507.0" y="100" text-anchor="middle" class="mrm" font-size="14">↑</text><rect x="520" y="82" width="26" height="26" class="cell"/><text x="533.0" y="100" text-anchor="middle" class="mrm" font-size="14">0</text><path d="M340,116 L340,122 L414,122 L414,116" class="ink-stroke" stroke-width="1.3"/><text x="377.0" y="136" text-anchor="middle" class="label">agreement, l = 3</text><rect x="338" y="148" width="104" height="12" class="soft-fill accent-stroke" stroke-width="1"/><text x="338" y="176" class="label">protected: the uses at x ≤ 3</text></svg>
:::

*The strategy and its two outcomes.* A requirement $\mathcal R_{e,i}$ keeps the restraint $r(e, i, s)$ out of $A_i$ as long as it is not injured. If $\Phi^{A_i}_e$ were equal to $B$, the length of agreement would tend to infinity and so would the restraint; the requirement would then injure the requirements of lower priority infinitely often. The proof shows that this outcome is impossible when $B$ is not computable: an agreement that is preserved can only be broken by a change of $B$, and that change is then preserved as a disagreement. So the only outcome is the finite one, in which the length of agreement and the restraint are eventually constant. This is **Sacks' preservation strategy**: the requirement is satisfied not by diagonalization, but because the hypothesis of non-computability rules out the infinite outcome.

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

*Item 1.* Suppose $\mathcal R_{e,i}$ is injured at stage $s + 1$, with $s \geq k$ (there are finitely many earlier stages). Then $a_s \leq r(e, i, s)$ and $k \leq s$, so the pair of smallest code at most $s$ whose restraint is at least $a_s$ has code at most $k$; since $a_s$ goes into $A_i$, this pair is some $\langle e', 1 - i \rangle$, of code smaller than $k$. So $a_s \leq r(e', 1 - i, s) \leq R$. Since the enumeration is injective, this happens for finitely many $s$. Let $s_0$ be a stage after the last injury, and after the last enumeration of a number at most $R$.

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

The procedure in item 2 is the heart of Sacks' preservation strategy. The requirement does not try to make $\Phi^{A_i}_e$ differ from $B$. It preserves the agreement as far as it goes, and lets the non-computability of $B$ guarantee that the agreement cannot be total. If it were, the preserved computations would compute $B$, since an element entering $B$ below the length of agreement would create a permanent disagreement.

*The hypotheses.* That $B$ is not computable is needed: a computable $B$ is computed by every set. That $B$ is c.e. is used in item 2, where an incorrect output $B_s(p) = 0$ can only be corrected by an enumeration into $B$. The theorem still holds for every non-computable $\Delta^0_2$ set $B$, but the strategy must then preserve the computations up to the largest length of agreement seen so far, rather than the current one (Soare 2016, Section 7.6).

*Unbounded injury.* In the Friedberg–Muchnik construction, $\mathcal R_i$ is injured at most $2^i - 1$ times, and in the low simple set $\mathcal N_e$ at most $e$ times. Here the injuries of $\mathcal R_{e,i}$ come from the elements of $A$ below the final restraints of higher priority, and in general no computable function of $\langle e, i \rangle$ bounds their number, a fact we admit (Soare 2016, remark after Lemma 7.5.7; Downey and Hirschfeldt, Section 2.12.1). The argument is a finite injury argument of **unbounded type**, and its induction must carry the finiteness of the restraints, item 3 of the lemma, and not only the finiteness of the actions.

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
We prove item 2 first. Apply :ref{#thm-sacks-splitting} with $B = A$. Then $A_i \leq_T A$ and $A \not\leq_T A_i$. Since $x \in A$ if and only if $x \in A_0$ or $x \in A_1$, we have $A \leq_T A_0 \oplus A_1$. If $A_0 \leq_T A_1$, then $A \leq_T A_0 \oplus A_1 \leq_T A_1$, a contradiction; so $A_0 \not\leq_T A_1$, symmetrically $A_1 \not\leq_T A_0$, and in particular neither $A_i$ is computable.

Item 1 is item 2 with $A = \emptyset'$.
:::

:::corollary{#cor-no-minimal-ce}
There is no minimal non-computable c.e. degree: below every non-computable c.e. degree $\abf$ there is a c.e. degree $\bbf$ with $\obf < \bbf < \abf$. Moreover, every non-computable c.e. degree is the join of two incomparable c.e. degrees below it.
:::

:::proof{of=cor-no-minimal-ce}
Let $A \in \abf$ be c.e., and $A_0, A_1$ as in :ref{#cor-splitting-post}. Then $\deg_T(A_0)$ is strictly between $\obf$ and $\abf$. Moreover $A_0 \oplus A_1 \equiv_T A$: one direction was shown above, and $A_0, A_1 \leq_T A$ gives the other.
:::

By contrast, Spector showed that there are **minimal** degrees, that is, non-zero degrees with only $\obf$ below them; by the corollary, none of them is c.e. The next lesson combines the preservation strategy with other requirements, and describes what lies beyond finite injury in the c.e. degrees.

## Exercises

::::exercise{#ex-sacks-restraint-at-l difficulty=2 objective="See why the restraint must protect the computation at the length of agreement."}
In the construction, replace the restraint by the largest use of the computations at $x < l(e, i, s)$ only. Identify the step of the proof of :ref{#lem-sacks-main} that fails.

:::solution
Item 2 fails. When the least number $q$ entering $B$ after stage $s$ enters, the length of agreement becomes at most $q$, and the computation at $q$ is no longer protected. A later element below its use may enter $A_i$ and destroy it, after which $\Phi^{A_i}_e(q)$ may converge to $1 = B(q)$, and the agreement may be restored. The claim that $\Phi^{A_i}_e(q) = B_s(q)$ no longer follows, so the procedure is not shown to compute $B$.
:::
::::

## Notes and references

The splitting theorem is due to Sacks (1963), who also introduced the preservation strategy. Soare's book of 2016 presents the preservation strategy for a single set in Section 7.4, the splitting theorem in Section 7.5 (Theorem 7.5.1 and its corollaries, including :ref{#cor-no-minimal-ce}), and the case of a $\Delta^0_2$ set $B$ in Section 7.6. Downey and Hirschfeldt present the splitting theorem as their example of a finite injury argument of unbounded type (Section 2.12.1). Monin and Patey prove a cone avoidance theorem with the preservation strategy and give the splitting theorem as an exercise, in their chapter on the priority method and c.e. degrees. Minimal degrees are due to Spector (1956).

- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010.
- B. Monin and L. Patey, *Computability theory*, chapter *Priority method and c.e. degrees*.
- G. E. Sacks, *On the degrees less than 0′*, Annals of Mathematics 77 (1963), 211–231.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016.
- C. Spector, *On degrees of recursive unsolvability*, Annals of Mathematics 64 (1956), 581–592.

:::::exercises
::::exercise{#ex-sacks-compute difficulty=1 objective="Compute a length of agreement and a restraint, and follow them through one stage."}
At a stage $s \geq 5$, suppose that for $x = 0, 1, 2, 3$ the computations $\Phi^{A_{i,s}}_e(x)[s]$ converge with values $0, 1, 0, 0$ and uses $3, 5, 9, 4$ respectively, that $\Phi^{A_{i,s}}_e(4)[s]$ diverges, and that $B_s \cap \{ 0, \dots, 4 \} = \{ 1 \}$.

1. Compute $l(e, i, s)$ and $r(e, i, s)$.
2. At stage $s + 1$, the number $2$ enters $B$, and $a_s = 7$. Suppose that $\mathcal R_{e,i}$ is the requirement of highest priority whose restraint is at least $7$. Where is $a_s$ placed? Compute $l(e, i, s + 1)$ and $r(e, i, s + 1)$.
3. What happens to $\mathcal R_{e,i}$ if it is never injured after stage $s$?

:::solution
1. For $x = 0, 1, 2, 3$, the values $0, 1, 0, 0$ agree with $B_s(x)$, and the computation at $4$ diverges. So $l(e, i, s) = 4$. The restraint is the largest use of a convergent computation at $x \leq 4$, that is, $\max(3, 5, 9, 4) = 9$.

2. Since $7 \leq r(e, i, s)$ and $\mathcal R_{e,i}$ is the requirement of highest priority with this property, $a_s$ goes into $A_{1-i}$. So $A_{i,s+1} = A_{i,s}$, and the computations at $x \leq 3$ converge at stage $s + 1$ with the same values and uses. Now $B_{s+1}(2) = 1 \neq 0$, while the values at $0$ and $1$ still agree with $B_{s+1}$. So $l(e, i, s + 1) = 2$, and $r(e, i, s + 1) = \max(3, 5, 9) = 9$: the restraint still covers the computation at $2$, which is now a disagreement.

3. If $\mathcal R_{e,i}$ is never injured after stage $s$, no number below $9$ ever enters $A_i$, so the computation at $2$ is preserved forever: $\Phi^{A_i}_e(2) = 0 \neq 1 = B(2)$, and the requirement is satisfied. This is the situation of the proof of item 2 of :ref{#lem-sacks-main}, with $q = 2$.
:::
::::

::::exercise{#ex-sacks-one-query difficulty=1 objective="Show that the halves of any c.e. splitting are computable in the set with one oracle question per input."}
Let $A_0$ and $A_1$ be disjoint c.e. sets, and $A = A_0 \cup A_1$. Show that $A_0 \leq_T A$ and $A_1 \leq_T A$, by a procedure that on input $x$ asks only whether $x \in A$. Deduce that $A \equiv_T A_0 \oplus A_1$.

:::solution
On input $x$, ask whether $x \in A$. If not, then $x \notin A_i$. If so, enumerate $A_0$ and $A_1$ simultaneously until $x$ appears in one of them; this happens, since $x \in A_0 \cup A_1$, and in exactly one of them, since they are disjoint. Answer that $x \in A_i$ if $x$ appeared in $A_i$. This computes $A_i$ from $A$, with use $x + 1$.

Conversely, $x \in A$ if and only if $x \in A_0$ or $x \in A_1$, so $A \leq_T A_0 \oplus A_1$; and $A_0 \oplus A_1 \leq_T A$ by the first part. The argument does not use the construction: it gives another proof that the halves built in :ref{#thm-sacks-splitting} are computable in $A$.
:::
::::

::::exercise{#ex-sacks-many-parts difficulty=1 objective="Iterate the splitting theorem to split a c.e. degree into finitely many parts."}
Let $A$ and $B$ be c.e. sets with $B$ not computable, and $n \geq 2$. Show that $A$ is the disjoint union of $n$ c.e. sets, each computable in $A$ and none computing $B$. Deduce that every non-computable c.e. degree is the join of $n$ c.e. degrees strictly below it.

:::solution
By induction on $n$. For $n = 2$, this is :ref{#thm-sacks-splitting}. If $A = A_1 \sqcup \cdots \sqcup A_n$ with the required properties, apply the theorem to the c.e. set $A_n$ and to $B$: $A_n = A'_n \sqcup A''_n$ with $A'_n, A''_n$ c.e., computable in $A_n$, hence in $A$, and not computing $B$. Then $A_1, \dots, A_{n-1}, A'_n, A''_n$ are $n + 1$ parts with the required properties.

Let $A$ be a non-computable c.e. set, and apply this with $B = A$. Each part $A_j$ is computable in $A$ and does not compute $A$, so its degree is strictly below that of $A$. Since $x \in A$ if and only if $x$ belongs to one of the parts, $A \leq_T A_1 \oplus \cdots \oplus A_n$, and the converse holds since each $A_j \leq_T A$. So $\deg_T(A)$ is the join of the degrees of the parts.
:::
::::

::::exercise{#ex-sacks-sequence difficulty=2 objective="Run the Sacks preservation strategy against a uniformly c.e. sequence of sets."}
Let $A$ be a c.e. set and $(C_j)_{j \in \nat}$ a uniformly c.e. sequence of non-computable sets. Show that there are disjoint c.e. sets $A_0$ and $A_1$ with $A_0 \cup A_1 = A$, $A_0, A_1 \leq_T A$, and $C_j \not\leq_T A_i$ for every $j$ and $i \in \{0, 1\}$.

:::solution
If $A$ is finite, take $A_0 = A$ and $A_1 = \emptyset$. Otherwise, fix an injective computable enumeration $(a_s)$ of $A$ and a computable approximation $(C_{j,s})$ of the sequence, with $C_{j,s} \subseteq C_{j,s+1}$ and $C_j = \bigcup_s C_{j,s}$, computable in $(j, s)$. The requirements are $\mathcal R_{e,j,i} : \Phi^{A_i}_e \neq C_j$, ordered by the code $\langle e, j, i \rangle$. Define the length of agreement $l(e, j, i, s)$ and the restraint $r(e, j, i, s)$ as in :ref{#def-length-agreement}, with $C_{j,s}$ in place of $B_s$; they are computable in $(e, j, i, s)$.

*Construction.* At stage $s + 1$, if some code $\langle e, j, i \rangle \leq s$ has $a_s \leq r(e, j, i, s)$, take the smallest one and put $a_s$ into $A_{1-i}$; otherwise put $a_s$ into $A_0$. The sets $A_0$ and $A_1$ are c.e., disjoint, with union $A$, and computable in $A$ as in the lesson (or by :ref{#ex-sacks-one-query}).

*Verification.* Prove the three items of :ref{#lem-sacks-main} for $\mathcal R_{e,j,i}$, by induction on the code $k = \langle e, j, i \rangle$. Item 1: an injury of $\mathcal R_{e,j,i}$ at a stage $s \geq k$ puts $a_s$ into $A_i$, so the smallest code at most $s$ whose restraint is at least $a_s$ belongs to a requirement $\mathcal R_{e',j',1-i}$ of smaller code; then $a_s$ is at most a bound $R$ on the restraints of higher priority, which exists by item 3 for smaller codes, and this happens for finitely many $s$. Items 2 and 3 use only the preservation property after the last injury, and the facts that $C_j$ is c.e. and not computable; their proofs apply verbatim with $C_j$ in place of $B$. So $\Phi^{A_i}_e \neq C_j$ for all $e$, $j$, $i$.

The case of $\Delta^0_2$ sets $C_j$ is Soare 2016, Exercise 7.6.3; it requires the variant of the strategy for $\Delta^0_2$ sets.
:::
::::
:::::
