---
title: Iterating the jump along notations
summary: The H-sets, iterating the Turing jump along Kleene's notations; their basic reductions; effective transfinite recursion, and the uniformity of the reductions between H-sets.
duration: 40
prerequisites: [computable-ordinals/kleene-o]
---

The arithmetic sets are the sets computable in some finite jump $\emptyset^{(n)}$. To go further, one iterates the jump transfinitely: $\emptyset^{(\omega)} = \bigoplus_n \emptyset^{(n)}$, then $\emptyset^{(\omega + 1)} = (\emptyset^{(\omega)})'$, and so on. Successor steps are clear: take the jump. Limit steps are the obstacle: to form the join of the sets built below a limit ordinal $\lambda$, one must know how to enumerate the stages below $\lambda$, and an ordinal by itself gives no such enumeration. A notation in $\mathcal O$ provides exactly this information: a notation $3 \cdot 5^e$ of $\lambda$ comes with the program $e$ of a sequence converging to $\lambda$. Iterating the jump along notations gives the **H-sets** $H_a$, $a \in \mathcal O$.

This lesson defines the H-sets, proves their basic properties, and introduces the technique used for all the uniformity arguments of the course, **effective transfinite recursion**. The next lesson shows that the Turing degree of $H_a$ depends only on the ordinal $|a|$ (Spector's theorem) and defines the hyperarithmetic sets.

## The H-sets

:::definition{#def-h-sets}
For $a \in \mathcal O$, the set $H_a$ is defined by transfinite recursion along $<_{\mathcal O}$:

1. $H_1 = \emptyset$;
2. $H_{2^b} = (H_b)'$;
3. $H_{3 \cdot 5^e} = \{ \langle u, v \rangle : u <_{\mathcal O} 3 \cdot 5^e \text{ and } v \in H_u \}$.
:::

At a limit notation $a = 3 \cdot 5^e$, the set $H_a$ gathers all the sets $H_u$ for $u <_{\mathcal O} a$, each in its own column $H_a^{[u]} = \{ v : \langle u, v \rangle \in H_a \}$; the columns indexed by numbers that are not below $a$ are empty. The definition is a recursion along the well-founded relation $<_{\mathcal O}$ restricted to $\{ u : u \leq_{\mathcal O} a \}$ (:ref{#prop-kleene-o-basic} (1)), so $H_a$ is well defined for every $a \in \mathcal O$. For numbers $a \notin \mathcal O$, the set $H_a$ is not defined.

:::example{#ex-h-sets-small}
The notation of $n$ is $n_{\mathcal O} = 2^{2^{\cdots^{1}}}$, with $n$ exponentiations. By induction, $H_{n_{\mathcal O}} = \emptyset^{(n)}$. Let $e$ be an index of the computable function $n \mapsto n_{\mathcal O}$, and $u = 3 \cdot 5^e$, a notation of $\omega$. The notations below $u$ are the $n_{\mathcal O}$, and $H_u = \{ \langle n_{\mathcal O}, v \rangle : v \in \emptyset^{(n)} \}$: up to the computable renaming $n \mapsto n_{\mathcal O}$ of the columns, it is $\emptyset^{(\omega)}$. Then $H_{2^u} = H_u'$ and $H_{2^{2^u}} = H_u''$ are the next two stages (:ref{#fig-h-chain}).
:::

:::figure[The H-sets along the notations below $2^{2^u}$, where $u$ is the notation of $\omega$ of :ref{#ex-h-sets-small}. The H-sets of the finite notations are the finite jumps of $\emptyset$; they are gathered as columns in $H_u$; the successor notations take jumps.]{#fig-h-chain}
<svg class="fig" viewBox="0 0 600 226" width="600" role="img" aria-label="The notations below a notation of omega plus 2, in a row, with the H-set of each notation below it; the limit notation gathers the H-sets of the finite notations as columns"><defs><marker id="ah-hchain" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="muted-fill"/></marker></defs><line x1="40" y1="80" x2="220" y2="80" class="ink-stroke" stroke-width="1.3"/><line x1="220" y1="80" x2="270" y2="80" class="ink-stroke" stroke-width="1.3" stroke-dasharray="3 4"/><text x="305" y="85" text-anchor="middle" class="mrm" font-size="15">⋯</text><line x1="400" y1="80" x2="540" y2="80" class="ink-stroke" stroke-width="1.3"/><circle cx="40" cy="80" r="5" class="ink-fill"/><text x="40" y="64" text-anchor="middle" class="mrm" font-size="14">0</text><circle cx="100" cy="80" r="5" class="ink-fill"/><text x="100" y="64" text-anchor="middle" class="mrm" font-size="14">1</text><circle cx="160" cy="80" r="5" class="ink-fill"/><text x="160" y="64" text-anchor="middle" class="mrm" font-size="14">2</text><circle cx="220" cy="80" r="5" class="ink-fill"/><text x="220" y="64" text-anchor="middle" class="mrm" font-size="14">3</text><circle cx="400" cy="80" r="5" class="accent-fill"/><text x="400" y="64" text-anchor="middle" class="mrm" font-size="14">ω</text><circle cx="470" cy="80" r="5" class="ink-fill"/><text x="470" y="64" text-anchor="middle" class="mrm" font-size="14">ω+1</text><circle cx="540" cy="80" r="5" class="ink-fill"/><text x="540" y="64" text-anchor="middle" class="mrm" font-size="14">ω+2</text><text x="40" y="114" text-anchor="middle" class="mrm" font-size="15">∅</text><text x="100" y="114" text-anchor="middle" class="mrm" font-size="15">∅′</text><text x="160" y="114" text-anchor="middle" class="mrm" font-size="15">∅″</text><text x="220" y="114" text-anchor="middle" class="mrm" font-size="15">∅‴</text><text x="400" y="114" text-anchor="middle" class="math" font-size="15">H<tspan class="mrm" font-size="10" dy="4">u</tspan></text><text x="470" y="114" text-anchor="middle" class="math" font-size="15">H<tspan class="mrm" font-size="10" dy="4">u</tspan><tspan class="mrm" font-size="12" dy="-10">′</tspan></text><text x="540" y="114" text-anchor="middle" class="math" font-size="15">H<tspan class="mrm" font-size="10" dy="4">u</tspan><tspan class="mrm" font-size="12" dy="-10">″</tspan></text><path d="M40,124 Q220.0,205 394,126" fill="none" class="muted-stroke" stroke-width="1" stroke-dasharray="3 3" marker-end="url(#ah-hchain)"/><path d="M100,124 Q250.0,197 394,126" fill="none" class="muted-stroke" stroke-width="1" stroke-dasharray="3 3" marker-end="url(#ah-hchain)"/><path d="M160,124 Q280.0,189 394,126" fill="none" class="muted-stroke" stroke-width="1" stroke-dasharray="3 3" marker-end="url(#ah-hchain)"/><path d="M220,124 Q310.0,181 394,126" fill="none" class="muted-stroke" stroke-width="1" stroke-dasharray="3 3" marker-end="url(#ah-hchain)"/><text x="300" y="212" text-anchor="middle" class="label">the H-set of the notation of <tspan class="math" font-size="14">k</tspan> is a column of <tspan class="math" font-size="14">H</tspan><tspan class="mrm" font-size="10" dy="4">u</tspan></text><text x="400" y="40" text-anchor="middle" class="label">limit: columns</text><text x="505" y="40" text-anchor="middle" class="label">successors: jumps</text><text x="130" y="40" text-anchor="middle" class="label">finite ordinals: finite jumps</text></svg>
:::

The proofs below use the following fact about notations: if $b <_{\mathcal O} c$, then $2^b \leq_{\mathcal O} c$. It is proved by induction on $c \in \mathcal O$ (first exercise). In particular, if $b <_{\mathcal O} a$ with $a$ a limit notation, then $2^b <_{\mathcal O} a$: the successor of a notation below a limit is still below it, and $H_{2^b} = H_b'$ is a column of $H_a$.

:::proposition{#prop-h-sets-basic}
Let $a \in \mathcal O$.

1. If $b <_{\mathcal O} a$, then $H_b \leq_T H_a$, and even $H_b' \leq_T H_a$.
2. If $|a| = n$ is finite, then $H_a = \emptyset^{(n)}$. If $|a| = \omega$, then $H_a \equiv_T \emptyset^{(\omega)}$.
3. $H_a$ is not computable in any $H_b$ with $b <_{\mathcal O} a$.
:::

:::proof{of=prop-h-sets-basic}
1. By induction on $a$. If $a = 2^c$, then $b = c$ or $b <_{\mathcal O} c$; in the first case $H_b' = H_a$, in the second $H_b' \leq_T H_c \leq_T H_c' = H_a$ by the induction hypothesis. If $a = 3 \cdot 5^e$ and $b <_{\mathcal O} a$, then $2^b <_{\mathcal O} a$, and $H_b' = H_{2^b} = \{ v : \langle 2^b, v \rangle \in H_a \}$ is computable in $H_a$, as a column of $H_a$. In both cases $H_b \leq_T H_b'$.
2. The only notation of $n$ is $n_{\mathcal O}$, and the first case follows by induction. A notation of $\omega$ is $a = 3 \cdot 5^e$ with $|\Phi_e(m)| = k_m$ finite and increasing; the notations below $a$ are the notations $k_{\mathcal O}$ of the finite ordinals, and $H_a$ has columns $\emptyset^{(k)}$, indexed by these notations. The map $k \mapsto k_{\mathcal O}$ is computable and injective, and its range is decidable; so the column of $H_a$ indexed by $k_{\mathcal O}$ is $\emptyset^{(k)}$, and each of $H_a$ and $\emptyset^{(\omega)}$ computes the other.
3. By (1), $H_b' \leq_T H_a$, so $H_a \leq_T H_b$ would give $H_b' \leq_T H_b$, contradicting :ref{#thm-jump}.
:::

:::quiz[H-sets]
Why does the definition of $H_{3 \cdot 5^e}$ use the c.e. relation $u <_{\mathcal O} 3 \cdot 5^e$ rather than only the sets $H_{\Phi_e(n)}$?

- [x] Both choices give the same Turing degree; gathering all $H_u$ below $a$ makes the reductions $H_u \leq_T H_a$ immediate, since each $H_u$ is a column.
- [ ] Because $\Phi_e(n)$ might not be in $\mathcal O$.

  For $3 \cdot 5^e \in \mathcal O$, every $\Phi_e(n)$ is a notation.
- [ ] Because the relation $<_{\mathcal O}$ is computable.

  It is only c.e. on initial segments, which suffices to describe the columns.

---

In :ref{#prop-h-sets-basic} (3), why can $H_a$ not be computed by $H_b$ for $b <_{\mathcal O} a$?

- [x] Because $H_a$ computes $H_b'$, and a set computing $H_b'$ cannot be computed by $H_b$.
- [ ] Because $|a| > |b|$.

  The comparison of ordinals alone does not give non-reducibility; the jump does.
- [ ] Because $H_a$ is not arithmetic.

  For finite $|a|$, $H_a$ is arithmetic; the argument is relative to $H_b$.
:::

## Effective transfinite recursion

The proof of :ref{#prop-h-sets-basic} (1) is an induction along $<_{\mathcal O}$, and at each step the reduction is obtained from the previous ones by an explicit procedure. Later arguments need more: an index of the reduction of $H_b$ to $H_a$ computed from $a$ and $b$. The method that gives it is **effective transfinite recursion**, which was already used for the addition of notations (:ref{#lem-notation-sum}).

1. One describes a partial computable function, or an oracle procedure, $\psi(a, \dots)$ by cases on the form of $a$ ($1$, $2^c$ or $3 \cdot 5^e$, which is decidable), where the computation at $a$ may call $\psi$ itself at notations $c <_{\mathcal O} a$, possibly with another oracle computed from the current one.
2. By the recursion theorem (:ref{#cor-self-reference}), a procedure that may use its own index exists; this step uses no property of $\mathcal O$.
3. One proves by induction along $<_{\mathcal O}$ that, for every $a \in \mathcal O$, the procedure halts and returns what it should, assuming this for all $c <_{\mathcal O} a$. On numbers $a \notin \mathcal O$, nothing is claimed: the procedure may diverge or return meaningless values.

The recursion is legitimate because $<_{\mathcal O}$ is well-founded below each notation, and the recursion theorem replaces the appeal to a previously defined function by an appeal to an index. The induction in step 3 is an ordinary transfinite induction in the metatheory.

:::proposition{#prop-h-sets-uniform}
There is a partial computable function $j$ such that for all $a \in \mathcal O$ and $b <_{\mathcal O} a$, $j(b, a)$ is defined and $\Phi^{H_a}_{j(b, a)}$ is the characteristic function of $H_b'$. In particular, $H_b \leq_T H_a$ and, for $a \in \mathcal O \setminus \{ 1 \}$, $\emptyset' \leq_T H_a$, uniformly in $a$ and $b$.
:::

:::proof{of=prop-h-sets-uniform}
Fix an index $i_0$ such that $\Phi^{X'}_{i_0} = X$ for every set $X$: on input $n$, compute an index $g(n)$ of the oracle program that, on every input, halts if and only if $n$ belongs to its oracle, and answer whether $g(n) \in X'$. Fix also, for indices $p$ and $q$, a computable index $p \ast q$ of the composition: if $\Phi^Y_q = Z$ and $\Phi^Z_p$ is total, then $\Phi^Y_{p \ast q} = \Phi^Z_p$. By the recursion theorem, there is a partial computable function $j$ such that:

- if $a = 2^c$ with $c \geq 1$ and $b = c$, then $j(b, a)$ is an index of the identity reduction, $\Phi^X_{j(b,a)} = X$;
- if $a = 2^c$ with $c \geq 1$ and $b \neq c$, then $j(b, a) = j(b, c) \ast i_0$;
- if $a = 3 \cdot 5^e$, then $j(b, a)$ is an index of the procedure that, with oracle $X$ and input $v$, answers whether $\langle 2^b, v \rangle \in X$;
- otherwise, $j(b, a)$ is undefined.

We prove the statement by induction on $a \in \mathcal O$. There is nothing to prove for $a = 1$. If $a = 2^c$ and $b = c$, then $H_b' = H_a$. If $a = 2^c$ and $b \neq c$, then $b <_{\mathcal O} c$, and by the induction hypothesis $j(b, c)$ is defined and computes $H_b'$ from $H_c$; the index $i_0$ computes $H_c$ from $H_c' = H_a$, so $j(b, c) \ast i_0$ computes $H_b'$ from $H_a$. If $a = 3 \cdot 5^e$, then $2^b <_{\mathcal O} a$, so $H_b' = H_{2^b}$ is the column $2^b$ of $H_a$. Finally, $H_b \leq_T H_b'$ uniformly, and for $a \in \mathcal O \setminus \{ 1 \}$, one has $1 <_{\mathcal O} a$ (by induction on $a$), so $\emptyset' = H_1' \leq_T H_a$ via $j(1, a)$.
:::

The next two lessons apply the same pattern to harder recursions: deciding, with an H-set as oracle, whether a notation denotes a smaller ordinal than another, and whether a tree has rank below a given ordinal.

:::quiz[effective transfinite recursion]
In the proof of :ref{#prop-h-sets-uniform}, the value $j(b, a)$ for $a = 2^c$ and $b \neq c$ calls $j(b, c)$. What guarantees that this call returns a correct index?

- [x] The induction hypothesis at $c <_{\mathcal O} a$, together with $b <_{\mathcal O} c$, which follows from $b <_{\mathcal O} 2^c$ and $b \neq c$.
- [ ] The recursion theorem.

  The recursion theorem only gives a function $j$ satisfying the equations; whether its values are correct is proved by induction along $<_{\mathcal O}$.
- [ ] The computability of $<_{\mathcal O}$.

  The relation $<_{\mathcal O}$ is not decidable; the procedure only tests whether $b = c$, which is decidable.
:::

## Exercises

::::exercise{difficulty=1}
Show that for all $c \in \mathcal O$ and every $b$, if $b <_{\mathcal O} c$, then $2^b \leq_{\mathcal O} c$. Deduce that if $a$ is a limit notation and $b <_{\mathcal O} a$, then $2^b <_{\mathcal O} a$.

:::solution
By induction on $c \in \mathcal O$. For $c = 1$, there is no $b <_{\mathcal O} 1$. For $c = 2^d$, $b <_{\mathcal O} c$ means $b = d$, in which case $2^b = c$, or $b <_{\mathcal O} d$, in which case $2^b \leq_{\mathcal O} d <_{\mathcal O} c$ by the induction hypothesis. For $c = 3 \cdot 5^e$, $b <_{\mathcal O} c$ means $b <_{\mathcal O} \Phi_e(n)$ for some $n$; by the induction hypothesis $2^b \leq_{\mathcal O} \Phi_e(n) <_{\mathcal O} c$.

If $a$ is a limit notation and $b <_{\mathcal O} a$, then $2^b \leq_{\mathcal O} a$, and $2^b \neq a$ since $a$ is not a power of $2$; so $2^b <_{\mathcal O} a$.
:::
::::

::::exercise{difficulty=1}
Give two notations $u$ and $w$ of $\omega$ such that neither $u \leq_{\mathcal O} w$ nor $w \leq_{\mathcal O} u$, and show directly that $H_{2^u} \equiv_T H_{2^w}$.

:::solution
Let $u = 3 \cdot 5^e$ and $w = 3 \cdot 5^{e'}$, where $\Phi_e(n) = n_{\mathcal O}$ and $\Phi_{e'}(n) = (2n)_{\mathcal O}$, with $e \neq e'$. Both are notations of $\omega$. The notations below each of them are the notations of finite ordinals, so neither is below the other, and they are different. By :ref{#prop-h-sets-basic} (2), $H_u \equiv_T \emptyset^{(\omega)} \equiv_T H_w$. The jump preserves Turing equivalence, so $H_{2^u} = H_u' \equiv_T H_w' = H_{2^w}$.
:::
::::

## Notes and references

Kleene (1955) introduced the hierarchy of H-sets; Davis and Mostowski had considered the iteration of the jump (Simpson, notes to Section VIII.3). The method of effective transfinite recursion goes back to Kleene's work on notations and is used throughout Sacks's monograph. The definition of the H-sets with all the columns below a limit notation follows Monin and Patey; Simpson (Section VIII.3) iterates the jump along computable linear orders instead of notations.

- S. C. Kleene, *Hierarchies of number-theoretic predicates*, Bulletin of the American Mathematical Society 61 (1955), 193–213.
- G. E. Sacks, *Higher Recursion Theory*, Springer, 1990.
- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009, Section VIII.3.
- B. Monin and L. Patey, *Computability theory*, chapter "Hyperarithmetic sets".
