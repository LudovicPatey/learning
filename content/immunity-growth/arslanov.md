---
title: Arslanov's completeness criterion
summary: A c.e. set is Turing complete if and only if it computes a DNC function; effectively simple sets are complete, and the complement of a low simple set is not effectively immune.
duration: 30
prerequisites: [dnc-functions, ce-degrees/low-simple-set]
---

The halting set computes a DNC function. Among c.e. sets, it is the only one up to Turing equivalence: Arslanov showed that a c.e. set computing a DNC function is Turing complete. In terms of fixed points, every function computable from an incomplete c.e. set has a fixed point, as computable functions do by the fixed point theorem. The criterion explains why the c.e. degrees and the DNC degrees are almost disjoint, a fact used in the course on algorithmic randomness: a random sequence computes a DNC function, so its degree contains a c.e. set only if it is the degree of $\emptyset'$.

The proof combines two tools from earlier courses. The first is the fixed point theorem with parameters, used to build programs that would become fixed points if something happened. The second is the settling of c.e. approximations: once an approximation of a c.e. set is correct below a number, it stays correct, and the oracle can recognize when this happens.

## The criterion

Let $A$ be c.e. and $f = \Phi^A_i$ a fixed-point free function. For each $n$, a program $p(n)$ waits for $n$ to enter $\emptyset'$, and then copies the program that the current approximation of $f$ assigns to $p(n)$. If $n$ entered $\emptyset'$ after the approximation of $f(p(n))$ has reached its final value, $p(n)$ would compute the same function as the program $f(p(n))$, and would be a fixed point of $f$. So $n$ can only enter $\emptyset'$ before that stage, and $A$, which can compute the stage, decides whether $n \in \emptyset'$.

:::figure[The stages in the proof of Arslanov's criterion, for one $n$. From the stage $s(n)$ on, computable from $A$, the approximation of $f(p(n))$ has its final value. If $n$ entered $\emptyset'$ after $s(n)$, the program $p(n)$ would copy the program $f(p(n))$; so whether $n \in \emptyset'$ is decided at stage $s(n)$.]
<svg class="fig" viewBox="0 0 600 200" width="600" role="img" aria-label="Two rows indexed by stages: the approximations f_t(p(n)), constant from the stage s(n) on, and the membership of n in the halting set at stage t, which can only change before s(n)"><text x="178.0" y="30" text-anchor="middle" class="mrm muted" font-size="11">0</text><text x="214.0" y="30" text-anchor="middle" class="mrm muted" font-size="11">1</text><text x="250.0" y="30" text-anchor="middle" class="mrm muted" font-size="11">2</text><text x="286.0" y="30" text-anchor="middle" class="mrm muted" font-size="11">3</text><text x="322.0" y="30" text-anchor="middle" class="mrm muted" font-size="11">4</text><text x="358.0" y="30" text-anchor="middle" class="mrm muted" font-size="11">5</text><text x="394.0" y="30" text-anchor="middle" class="mrm muted" font-size="11">6</text><text x="430.0" y="30" text-anchor="middle" class="mrm muted" font-size="11">7</text><text x="466.0" y="30" text-anchor="middle" class="mrm muted" font-size="11">8</text><text x="502.0" y="30" text-anchor="middle" class="mrm muted" font-size="11">9</text><text x="538.0" y="30" text-anchor="middle" class="mrm muted" font-size="11">10</text><text x="574.0" y="30" text-anchor="middle" class="mrm muted" font-size="11">11</text><text x="150" y="30" text-anchor="end" class="label">stage t</text><text x="150" y="63" text-anchor="end" class="math" font-size="14">f<tspan class="mrm" font-size="10" dy="4">t</tspan><tspan class="mrm" dy="-4">(</tspan>p<tspan class="mrm">(</tspan>n<tspan class="mrm">))</tspan></text><text x="150" y="99" text-anchor="end" class="label">is n in ∅′ at stage t?</text><rect x="160" y="40" width="36" height="36" class="cell"/><text x="178.0" y="63" text-anchor="middle" class="mrm" font-size="15">3</text><rect x="160" y="76" width="36" height="36" class="cell"/><text x="178.0" y="99" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="196" y="40" width="36" height="36" class="cell"/><text x="214.0" y="63" text-anchor="middle" class="mrm" font-size="15">3</text><rect x="196" y="76" width="36" height="36" class="cell"/><text x="214.0" y="99" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="232" y="40" width="36" height="36" class="cell"/><text x="250.0" y="63" text-anchor="middle" class="mrm" font-size="15">7</text><rect x="232" y="76" width="36" height="36" class="cell"/><text x="250.0" y="99" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="268" y="40" width="36" height="36" class="cell"/><text x="286.0" y="63" text-anchor="middle" class="mrm" font-size="15">7</text><rect x="268" y="76" width="36" height="36" class="cell"/><text x="286.0" y="99" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="304" y="40" width="36" height="36" class="cell"/><text x="322.0" y="63" text-anchor="middle" class="mrm" font-size="15">7</text><rect x="304" y="76" width="36" height="36" class="cell"/><text x="322.0" y="99" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="340" y="40" width="36" height="36" class="cell head-cell"/><text x="358.0" y="63" text-anchor="middle" class="mrm" font-size="15">4</text><rect x="340" y="76" width="36" height="36" class="cell"/><text x="358.0" y="99" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="376" y="40" width="36" height="36" class="cell head-cell"/><text x="394.0" y="63" text-anchor="middle" class="mrm" font-size="15">4</text><rect x="376" y="76" width="36" height="36" class="cell"/><text x="394.0" y="99" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="412" y="40" width="36" height="36" class="cell head-cell"/><text x="430.0" y="63" text-anchor="middle" class="mrm" font-size="15">4</text><rect x="412" y="76" width="36" height="36" class="cell"/><text x="430.0" y="99" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="448" y="40" width="36" height="36" class="cell head-cell"/><text x="466.0" y="63" text-anchor="middle" class="mrm" font-size="15">4</text><rect x="448" y="76" width="36" height="36" class="cell"/><text x="466.0" y="99" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="484" y="40" width="36" height="36" class="cell head-cell"/><text x="502.0" y="63" text-anchor="middle" class="mrm" font-size="15">4</text><rect x="484" y="76" width="36" height="36" class="cell"/><text x="502.0" y="99" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="520" y="40" width="36" height="36" class="cell head-cell"/><text x="538.0" y="63" text-anchor="middle" class="mrm" font-size="15">4</text><rect x="520" y="76" width="36" height="36" class="cell"/><text x="538.0" y="99" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="556" y="40" width="36" height="36" class="cell head-cell"/><text x="574.0" y="63" text-anchor="middle" class="mrm" font-size="15">4</text><rect x="556" y="76" width="36" height="36" class="cell"/><text x="574.0" y="99" text-anchor="middle" class="mrm" font-size="15">1</text><line x1="340" y1="36" x2="340" y2="138" class="accent-stroke" stroke-width="1.6" stroke-dasharray="4 3"/><text x="340" y="154" text-anchor="middle" class="math" font-size="14">s<tspan class="mrm">(</tspan>n<tspan class="mrm">)</tspan></text><text x="20" y="178" class="label">from s(n) on, the approximation equals f(p(n)); an entry of n into ∅′</text><text x="20" y="194" class="label">after s(n) would make p(n) a fixed point of f, so it does not happen</text></svg>
:::

:::theorem[Arslanov's completeness criterion]{#thm-arslanov}
A c.e. set $A$ is Turing complete if and only if it computes a DNC function.
:::

:::proof{of=thm-arslanov}
If $A \equiv_T \emptyset'$, it computes a DNC function (:ref{#def-dnc}). Conversely, let $A$ be c.e., with a c.e. approximation $(A_s)$, and suppose that $A$ computes a DNC function. By :ref{#thm-dnc-fpf}, there is a functional $\Phi_i$ such that $f = \Phi^A_i$ is total and fixed-point free. Let $f_s(x) = \Phi^{A_s}_i(x)[s]$ if this computation converges, and $f_s(x) = 0$ otherwise; the function $(s, x) \mapsto f_s(x)$ is computable. Let $\emptyset'_t$ be the set of $n \leq t$ with $\Phi_n(n)[t]\converge$.

By SMN, there is a total computable function $r$ such that the program $r(n, x)$, on input $m$, searches for the least $t$ with $n \in \emptyset'_t$ and, if it finds one, runs $\Phi_{f_t(x)}(m)$. By the fixed point theorem with parameters (:ref{#thm-fixed-point-parameters}), there is a total computable function $p$ with $\Phi_{p(n)} = \Phi_{r(n, p(n))}$ for every $n$.

With oracle $A$, compute for each $n$ the least stage $s(n)$ such that $\Phi^{A_s}_i(p(n))[s]$ converges, with use $u$, and $A_s \uh u = A \uh u$, for $s = s(n)$. Such a stage exists, since $f(p(n))$ is defined and $A_s \uh u$ eventually equals $A \uh u$; and the condition is decided by $A$. Since $A$ is c.e., $A_t \uh u = A \uh u$ for every $t \geq s(n)$, so the same computation gives $f_t(p(n)) = f(p(n))$ for every $t \geq s(n)$.

We claim that $n \in \emptyset'$ if and only if $n \in \emptyset'_{s(n)}$, which shows $\emptyset' \leq_T A$. Suppose that $n \in \emptyset'$, and let $t$ be the least stage with $n \in \emptyset'_t$. If $t > s(n)$, then the program $r(n, p(n))$ runs $\Phi_{f_t(p(n))} = \Phi_{f(p(n))}$, so $\Phi_{p(n)} = \Phi_{r(n, p(n))} = \Phi_{f(p(n))}$, contradicting the fact that $f$ is fixed-point free. So $t \leq s(n)$, and $n \in \emptyset'_{s(n)}$, since $\emptyset'_t \subseteq \emptyset'_{s(n)}$. Conversely, $\emptyset'_{s(n)} \subseteq \emptyset'$.
:::

The hypothesis that $A$ is c.e. is necessary. There are low PA sets (:ref{#cor-pa-basis}), which compute DNC functions without computing $\emptyset'$. In the proof, the hypothesis is used at one point: for a $\Delta^0_2$ approximation, $A_t \uh u$ may change again after being correct, and the stage $s(n)$ found by $A$ does not bound the entry of $n$ into $\emptyset'$.

:::quiz[Arslanov's completeness criterion]
Where is the hypothesis that $A$ is c.e. used in the proof of :ref{#thm-arslanov}?

- [x] To know that once $A_s \uh u$ agrees with $A \uh u$, it agrees at every later stage, so that $f_t(p(n)) = f(p(n))$ for all $t \geq s(n)$, and to recognize such a stage with oracle $A$.

  For a general $\Delta^0_2$ approximation, $A_t \uh u$ may change again after being correct.
- [ ] To apply the fixed point theorem with parameters.

  The fixed point theorem is applied to a computable function $r$, independently of $A$.
- [ ] To make $f$ total.

  $f = \Phi^A_i$ is total by hypothesis.

---

Why does the program $r(n, x)$ use the stage $t$ at which $n$ enters $\emptyset'$, rather than the true value $f(x)$?

- [x] Because a program cannot use the oracle $A$; it can only compute the approximation $f_t$ at a stage it finds by itself.
- [ ] Because $f(x)$ may be undefined.

  $f$ is total.
- [ ] Because the fixed point theorem requires the program to halt.

  The fixed point theorem applies to all programs, halting or not.
:::

## Consequences

:::corollary{#cor-arslanov}
1. A c.e. set of PA degree is Turing complete.
2. (Martin) Every effectively simple set is Turing complete.
3. The complement of a low simple set is immune but not effectively immune.
:::

:::proof{of=cor-arslanov}
1. A PA set computes a DNC function.
2. If $A$ is effectively simple, then $A$ computes its complement, which is effectively immune; by :ref{#thm-dnc-effectively-immune}, $A$ computes a DNC function, and :ref{#thm-arslanov} applies.
3. A low simple set exists (:ref{#thm-low-simple}). Its complement is immune; if it were effectively immune, the set would be complete by 2, hence not low.
:::

By :ref{#ex-post-effectively-simple}, Post's simple set is effectively simple, hence Turing complete. Post's construction, designed to produce a thin complement, produces a complete set; the incomplete simple set of :ref{#thm-low-simple} is built by a priority argument. Martin's theorem preceded Arslanov's criterion by fifteen years, and was the first indication that thinness of the complement gives no control over the Turing degree.

The criterion is sharp in another direction. A function computable in $\emptyset'$ and fixed-point free need not compute $\emptyset'$, by the low PA sets; but Kučera showed that it always computes a non-computable c.e. set (Downey and Hirschfeldt 2010, Theorem 2.22.5). This gives a solution of Post's problem without priority, and is admitted here.

## Exercises

::::exercise{difficulty=1}
Show that if $A$ is effectively immune, $B$ is c.e. and $A \leq_T B$, then $B \equiv_T \emptyset'$.

:::solution
By :ref{#thm-dnc-effectively-immune}, $A$ computes a DNC function, hence so does $B$. Since $B$ is c.e., :ref{#thm-arslanov} gives $\emptyset' \leq_T B$, and $B \leq_T \emptyset'$ since $B$ is c.e.
:::
::::

::::exercise{difficulty=1}
Show that there is a non-computable $\Delta^0_2$ set that computes no DNC function. Compare with the last exercise of :ref{to="immunity-growth/dnc-functions"}.

:::solution
Let $A$ be a low simple set (:ref{#thm-low-simple}). It is c.e., hence $\Delta^0_2$, and not computable. It is not complete, since $A' \equiv_T \emptyset' <_T \emptyset''$. By :ref{#thm-arslanov}, it computes no DNC function. The exercise of the previous lesson builds such a set computable in $\emptyset''$ by finite extensions, without priority.
:::
::::

::::exercise{difficulty=2}
Let $A$ be a c.e. set with $A <_T \emptyset'$. Show that for every $A$-computable total function $f$ there is $e$ with $\Phi_{f(e)} = \Phi_e$.

:::solution
Otherwise some $A$-computable function $f$ is fixed-point free, so $A$ computes a DNC function by :ref{#thm-dnc-fpf}, and $A$ is complete by :ref{#thm-arslanov}, a contradiction.
:::
::::

## Notes and references

Arslanov (1981) proved the completeness criterion, in the form of fixed-point free functions; it extends the theorem of Martin (1966) that effectively simple sets are complete, and Nies notes that it builds on work of Martin and of Lachlan. Jockusch, Lerman, Soare and Solovay (1989) gave several extensions of the criterion. The proof given here follows the common pattern of the textbook proofs: Soare (2016, Theorem 5.4.3), Downey and Hirschfeldt (2010, Theorem 2.22.3), Nies (2009, Theorem 4.1.11), and the section *Arslanov completeness criterion* of the chapter *Immunity and function growth* of Monin and Patey.

- M. M. Arslanov, *On some generalizations of the fixed-point theorem*, Soviet Mathematics (Izvestiya VUZ. Matematika) 25 (1981), 1–10.
- D. A. Martin, *Completeness, the recursion theorem and effectively simple sets*, Proceedings of the American Mathematical Society 17 (1966), 838–842.
- C. G. Jockusch, M. Lerman, R. I. Soare and R. M. Solovay, *Recursively enumerable sets modulo iterated jumps and extensions of Arslanov's completeness criterion*, Journal of Symbolic Logic 54 (1989), 1288–1323.
- A. Kučera, *An alternative priority-free solution to Post's problem*, in *Mathematical Foundations of Computer Science 1986*, Lecture Notes in Computer Science 233, Springer, 1986, 493–500.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, Section 5.4.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Section 2.22.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Section 4.1.
