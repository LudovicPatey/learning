---
title: Spector's uniqueness theorem and the hyperarithmetic sets
summary: H-sets decide comparisons of notations; Spector's theorem that the Turing degree of an H-set depends only on the ordinal of the notation; the degrees 0^(α); the hyperarithmetic sets form a countable jump ideal.
duration: 45
prerequisites: [h-sets]
---

A constructive ordinal has many notations, and two notations of the same ordinal may lie on incomparable branches of $\mathcal O$; the H-sets along them are built from different sequences. Spector proved that their Turing degrees are nevertheless equal: if $|a| \leq |b|$, then $H_a \leq_T H_b$. This makes the iterated jump $\emptyset^{(\alpha)}$ well defined up to Turing degree for every computable ordinal $\alpha$, and gives the class of hyperarithmetic sets its robustness.

The idea of the proof is to compute $H_a$ from $H_b$ by effective transfinite recursion on $a$, following the construction of $H_a$. The obstacle appears when $a = 2^c$ and $b$ is a limit notation with fundamental sequence $(b_m)$: one needs some $b_m$ with $|c| \leq |b_m|$, to compute $H_c$ from $H_{b_m}$ and then $H_c'$ from $H_{b_m}'$, a column of $H_b$. Since $c$ and the $b_m$ lie on different branches, the relation $<_{\mathcal O}$ does not help. The first section shows that the H-sets can compare the ordinals of notations on different branches, which overcomes the obstacle.

## H-sets compare notations

For $x \in \mathcal O$, write $\mathcal O_{<x} = \{ y \in \mathcal O : |y| < |x| \}$: the notations, on all branches, of ordinals smaller than $|x|$. Recall that $x_m$ denotes the terms $\Phi_f(m)$ of the fundamental sequence of a limit notation $x = 3 \cdot 5^f$, and that, by the first exercise of :ref{to="h-sets"}, $2^{x_m} <_{\mathcal O} x$, so that $H_{2^{x_m}}$ is a column of $H_x$. We use Post's theorem relativized (:ref{#thm-post}): a $\Sigma^0_1(A)$ question is answered by $A'$, and a $\Pi^0_2(A)$ question by $A''$, uniformly in an index of the question.

:::lemma[Spector]{#lem-notations-below}
There is an oracle procedure $\Psi$ such that for every $x \in \mathcal O$ and every $y$, the computation $\Psi^{H_{2^x}}(x, y)$ halts, with output $1$ if $y \in \mathcal O_{<x}$ and $0$ otherwise. In other words, $\mathcal O_{<x} \leq_T H_{2^x}$, uniformly in $x$.
:::

:::proof{of=lem-notations-below}
We define $\Psi$ by effective transfinite recursion (:ref{to="h-sets"}), by cases on $x$, the oracle $X$ being $H_{2^x}$ when $x \in \mathcal O$. In each case, $H_x$, and if $x = 2^b$ also $H_{2^b}$ and $H_b$, are computed from $X = H_x'$ by :ref{#prop-h-sets-uniform}; the recursive calls are made with these sets or their columns as oracles.

1. $x = 1$. Output $0$: $\mathcal O_{<1}$ is empty.
2. $x = 2^b$ with $b \geq 1$. Then $|y| < |x|$ means $|y| \leq |b|$, and $X = H_b''$.
   - If $y = 1$, output $1$.
   - If $y = 2^z$ with $z \geq 1$, then $y \in \mathcal O_{<x}$ if and only if $z \in \mathcal O_{<b}$; output $\Psi^{H_{2^b}}(b, z)$.
   - If $y = 3 \cdot 5^e$ and $b = 1$, output $0$, since $|y|$ would be a limit ordinal, not $\leq 0$.
   - If $y = 3 \cdot 5^e$ and $b = 2^c$ with $c \geq 1$, then for $y \in \mathcal O$, $|y|$ is a limit and $|b|$ a successor, so $|y| \leq |b|$ if and only if $|y| < |b|$; output $\Psi^{H_{2^b}}(b, y)$.
   - If $y = 3 \cdot 5^e$ and $b = 3 \cdot 5^f$, then $y \in \mathcal O_{<x}$ if and only if
     $$
     \forall n\ \big[\Phi_e(n)\converge \wedge \exists m\ \Phi_e(n) \in \mathcal O_{<b_m} \wedge R(\Phi_e(n), \Phi_e(n+1))\big],
     $$
     with $R$ the c.e. relation of :ref{#prop-kleene-o-basic} (2). Indeed, if $y \in \mathcal O$ and $|y| \leq |b|$, then $\Phi_e$ is total, $\Phi_e(n) <_{\mathcal O} \Phi_e(n+1)$, and $|\Phi_e(n)| < |y| \leq |b| = \sup_m |b_m|$. Conversely, the condition gives $\Phi_e(n) \in \mathcal O$ for all $n$, hence $\Phi_e(n) <_{\mathcal O} \Phi_e(n+1)$ by the property of $R$, so $y \in \mathcal O$ and $|y| = \sup_n |\Phi_e(n)| \leq |b|$. The relation $\Phi_e(n) \in \mathcal O_{<b_m}$ is decided by $\Psi$ with oracle $H_{2^{b_m}}$, a column of $H_b$. So the bracket is $\Sigma^0_1(H_b)$ and the whole condition is $\Pi^0_2(H_b)$, answered by $H_b'' = X$.
   - Otherwise $y \notin \mathcal O$; output $0$.
3. $x = 3 \cdot 5^f$. Then $y \in \mathcal O_{<x}$ if and only if $y \in \mathcal O_{<x_m}$ for some $m$, since $|x| = \sup_m |x_m|$. Each of these relations is decided by $\Psi$ with oracle $H_{2^{x_m}}$, a column of $H_x$; so the condition is $\Sigma^0_1(H_x)$, answered by $H_x' = X$.

By induction on $x \in \mathcal O$, the computation halts with the correct output: the recursive calls are made at $b$, at the $b_m <_{\mathcal O} b$, and at the $x_m$, all below $x$, with the correct oracles.
:::

Comparing ordinals costs jumps: the comparison below $x$ is answered by $H_{2^x}$, not by $H_x$. This is why, in the next proof, the comparisons are made with columns of the oracle that lie strictly below it. Monin and Patey prove the lemma together with its analogue for ranks of trees, which is the main lemma of the next lesson.

:::quiz[comparing notations]
In case 2 of the proof of :ref{#lem-notations-below}, with $b = 3 \cdot 5^f$ and $y = 3 \cdot 5^e$, why is the question asked to $H_b''$ rather than to $H_b'$?

- [x] Because the condition has the form $\forall n\, \exists m\, (\dots)$ with a matrix decidable in $H_b$, a $\Pi^0_2(H_b)$ condition: totality of $\Phi_e$ and the bound on every term both require an alternation of quantifiers.
- [ ] Because $\Phi_e(n) \in \mathcal O_{<b_m}$ is only decidable in $H_b''$.

  It is decided by $H_{2^{b_m}}$, a column of $H_b$.
- [ ] Because $R$ is a $\Pi^0_2$ relation.

  $R$ is c.e., a $\Sigma^0_1$ relation.
:::

## Spector's theorem

:::theorem[Spector]{#thm-spector-uniqueness}
If $a, b \in \mathcal O$ and $|a| \leq |b|$, then $H_a \leq_T H_b$, uniformly in $a$ and $b$. In particular, $|a| = |b|$ implies $H_a \equiv_T H_b$.
:::

:::figure[The case $a = 2^c$, $b = 3 \cdot 5^f$ of the proof of :ref{#thm-spector-uniqueness}. The notations $c$ and $b_m$ lie on different branches of $\mathcal O$; the oracle $H_b$ finds $m$ by :ref{#lem-notations-below}, and computes $H_a = H_c'$ from its column $H_{2^{b_m}} = H_{b_m}'$.]{#fig-spector-matching}
<svg class="fig" viewBox="0 0 600 200" width="600" role="img" aria-label="Two branches of O: above, the notation a equal to 2 to the c; below, the fundamental sequence of the limit notation b; the notation c is matched with a term b_m of larger ordinal"><defs><marker id="ah-match" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><line x1="40" y1="50" x2="250" y2="50" class="ink-stroke" stroke-width="1.3" stroke-dasharray="3 4"/><line x1="250" y1="50" x2="330" y2="50" class="ink-stroke" stroke-width="1.3"/><circle cx="250" cy="50" r="5" class="ink-fill"/><circle cx="330" cy="50" r="5" class="accent-fill"/><text x="250" y="36" text-anchor="middle" class="math" font-size="15">c</text><text x="330" y="36" text-anchor="middle" class="math" font-size="15">a<tspan class="mrm"> = 2</tspan><tspan class="math" font-size="11" dy="-7">c</tspan></text><line x1="40" y1="140" x2="400" y2="140" class="ink-stroke" stroke-width="1.3"/><line x1="400" y1="140" x2="480" y2="140" class="ink-stroke" stroke-width="1.3" stroke-dasharray="3 4"/><circle cx="60" cy="140" r="4.5" class="ink-fill"/><text x="60" y="164" text-anchor="middle" class="math" font-size="15">b<tspan class="mrm" font-size="10" dy="4">0</tspan></text><circle cx="150" cy="140" r="4.5" class="ink-fill"/><text x="150" y="164" text-anchor="middle" class="math" font-size="15">b<tspan class="mrm" font-size="10" dy="4">1</tspan></text><circle cx="240" cy="140" r="4.5" class="ink-fill"/><text x="240" y="164" text-anchor="middle" class="math" font-size="15">b<tspan class="mrm" font-size="10" dy="4">2</tspan></text><circle cx="330" cy="140" r="4.5" class="ink-fill"/><text x="330" y="164" text-anchor="middle" class="math" font-size="15">b<tspan class="mrm" font-size="10" dy="4">m</tspan></text><text x="365" y="164" text-anchor="middle" class="mrm" font-size="15">⋯</text><circle cx="540" cy="140" r="5" class="accent-fill"/><text x="540" y="164" text-anchor="middle" class="math" font-size="15">b<tspan class="mrm"> = 3·5</tspan><tspan class="math" font-size="11" dy="-7">f</tspan></text><text x="508" y="145" text-anchor="middle" class="mrm" font-size="15">⋯</text><line x1="252" y1="58" x2="328" y2="131" class="ink-stroke" stroke-width="1.2" stroke-dasharray="4 3" marker-end="url(#ah-match)"/><text x="306" y="99.0" text-anchor="start" class="label">least <tspan class="math" font-size="14">m</tspan> with <tspan class="mrm" font-size="14">|</tspan><tspan class="math" font-size="14">c</tspan><tspan class="mrm" font-size="14">| &lt; |</tspan><tspan class="math" font-size="14">b</tspan><tspan class="math" font-size="10" dy="4">m</tspan><tspan class="mrm" font-size="14" dy="-4">|</tspan>, found by <tspan class="math" font-size="14">H</tspan><tspan class="math" font-size="10" dy="4">b</tspan></text><text x="40" y="28" class="label">branch of a</text><text x="40" y="126" class="label">branch of b</text></svg>
:::

:::proof{of=thm-spector-uniqueness}
We define, by effective transfinite recursion on $a$, an oracle procedure $\Theta$ such that for all $a, b \in \mathcal O$ with $|a| \leq |b|$, the procedure $\Theta^{H_b}(a, b, \cdot)$ is the characteristic function of $H_a$. Two uniform facts are used: if $\Phi^A_p$ is the characteristic function of $B$, then $B' \leq_T A'$ via an index computed from $p$, since "$\Phi^B_n(n)\converge$" becomes a $\Sigma^0_1(A)$ question; and $\emptyset' \leq_T H_b$ uniformly for $b \neq 1$ (:ref{#prop-h-sets-uniform}). The cases are the following.

1. $a = 1$. Output $0$, since $H_1 = \emptyset$.
2. $a = 2^c$ with $c \geq 1$. Then $|b| \geq 1$, so $b \neq 1$, and $|c| < |b|$.
   - If $b = 2^d$, then $|c| \leq |d|$, and $\Theta^{H_d}(c, d, \cdot)$ computes $H_c$; so $H_a = H_c'$ is computed from $H_d' = H_b$.
   - If $b = 3 \cdot 5^f$, search for the least $m$ with $c \in \mathcal O_{<b_m}$, using :ref{#lem-notations-below} with oracle $H_{2^{b_m}}$, a column of $H_b$. Such an $m$ exists, since $|c| < |b| = \sup_m |b_m|$ (:ref{#fig-spector-matching}). Then $|c| < |b_m|$, so $\Theta^{H_{b_m}}(c, b_m, \cdot)$ computes $H_c$, and $H_a = H_c'$ is computed from $H_{b_m}' = H_{2^{b_m}}$, again a column of $H_b$.
3. $a = 3 \cdot 5^e$. Then $|a| \geq \omega$, so $b \neq 1$. On input $\langle u, v \rangle$, decide whether $R(u, a)$ holds, using $\emptyset' \leq_T H_b$. If not, output $0$. If so, then $u <_{\mathcal O} a$, so $|u| < |a| \leq |b|$, and output $\Theta^{H_b}(u, b, v)$, which tells whether $v \in H_u$.

By induction on $a \in \mathcal O$, for every $b \in \mathcal O$ with $|a| \leq |b|$, the procedure computes $H_a$ from $H_b$: the recursive calls are made at $c <_{\mathcal O} a$ and at $u <_{\mathcal O} a$, with notations $d$, $b_m$ or $b$ of ordinals at least as large.
:::

:::quiz[Spector's theorem]
In case 2 of the proof of :ref{#thm-spector-uniqueness}, with $b$ a limit notation, why can the procedure not simply look for $m$ with $c <_{\mathcal O} b_m$?

- [x] Because $c$ need not be comparable with any $b_m$ under $<_{\mathcal O}$: the two notations may lie on different branches of $\mathcal O$, and only the ordinals can be compared, by :ref{#lem-notations-below}.
- [ ] Because $<_{\mathcal O}$ is not c.e.

  It is c.e. on the initial segment below a notation (:ref{#prop-kleene-o-basic} (2)); the problem is that $c$ may not be below any $b_m$.
- [ ] Because the sequence $(b_m)$ is not computable.

  It is computable: $b = 3 \cdot 5^f$ with $\Phi_f$ total.

---

In case 3, where is the hypothesis $|a| \leq |b|$ used?

- [x] To apply the induction hypothesis at the pair $(u, b)$: from $u <_{\mathcal O} a$ one gets $|u| < |a| \leq |b|$.
- [ ] To decide $R(u, a)$.

  This only requires $\emptyset' \leq_T H_b$, that is $b \neq 1$, which follows from $|a| \geq \omega$.
- [ ] It is not used in this case.

  Without it, $H_u$ might not be computable in $H_b$.
:::

By the theorem, for every computable ordinal $\alpha$, the degree $\obf^{(\alpha)} = \deg_T(H_a)$, for any $a$ with $|a| = \alpha$, is well defined. For finite $\alpha$ it is the degree of $\emptyset^{(\alpha)}$, and the map $\alpha \mapsto \obf^{(\alpha)}$ is strictly increasing on $\omega_1^{\mathrm{CK}}$: if $\alpha < \beta = |b|$, some $c <_{\mathcal O} b$ has $|c| = \alpha$, by :ref{#prop-kleene-o-basic} (1), and $H_b \not\leq_T H_c$ by :ref{#prop-h-sets-basic} (3). One also writes $\emptyset^{(\alpha)}$ for any set $H_a$ with $|a| = \alpha$, when only its Turing degree matters.

The theorem cannot be strengthened to many-one reducibility in general. For $|a| \geq \omega$, the set $H_{2^a}$ is complete, for many-one reductions, for the $\Sigma^0_{|a|}$ level of the effective transfinite extension of the arithmetic hierarchy, so the sets $H_{2^a}$ with $|a|$ fixed are many-one equivalent (Monin and Patey, chapter "Hyperarithmetic sets"). For limit notations, the many-one degrees of the sets $H_a$ were studied by Moschovakis (1966): the sets $H_a$ with $|a|$ fixed are many-one equivalent when $|a|$ has the form $\beta + \omega$, and the situation is more complicated for limits of limit ordinals.

## Hyperarithmetic sets

:::definition{#def-hyp}
A set is **hyperarithmetic** if it is computable in $H_a$ for some $a \in \mathcal O$. The class of hyperarithmetic sets is written $\mathrm{HYP}$.
:::

Equivalently, a set is hyperarithmetic if it is computable in $\emptyset^{(\alpha)}$ for some computable ordinal $\alpha$. Examples are the arithmetic sets, $\emptyset^{(\omega)}$, $\emptyset^{(\omega \cdot 2)}$, and $\emptyset^{(\varepsilon_0)}$, since $\varepsilon_0$ is computable (exercise of :ref{to="computable-ordinals/kleene-o"}).

:::proposition{#prop-hyp-ideal}
$\mathrm{HYP}$ is a **jump ideal**: it is closed under $\oplus$, under the jump, and downward under $\leq_T$. It contains every arithmetic set, and it is countable. For every hyperarithmetic set $X$, there is a hyperarithmetic set not computable in $X$.
:::

:::proof{of=prop-hyp-ideal}
If $X \leq_T H_a$ and $Y \leq_T H_b$, let $c$ be a notation for $\max(|a|, |b|)$, which is $a$ or $b$; by :ref{#thm-spector-uniqueness}, $X \oplus Y \leq_T H_c$. Closure under $\leq_T$ is clear, and $X' \leq_T H_a' = H_{2^a}$. Every arithmetic set is computable in some $\emptyset^{(n)}$, by Post's theorem (:ref{#thm-post}), hence in $H_a$ for the notation $a$ of $n$. There are countably many notations, and each $H_a$ computes countably many sets. Finally, if $X \leq_T H_a$, then $H_{2^a} = H_a'$ is not computable in $X$, since $H_a' \not\leq_T H_a$.
:::

Closure under $\oplus$ is where Spector's theorem is needed: two notations on different branches have no common upper bound in $<_{\mathcal O}$ given in advance, and the theorem replaces it by a comparison of ordinals.

The jump ideal $\mathrm{HYP}$ contains $\emptyset^{(\omega)}$ and many other sets that are not arithmetic, but it does not contain every set definable with a quantifier over sets: $\mathcal O$ itself, which is $\Pi^1_1$, is not hyperarithmetic, since it computes every $H_a$ (first exercise below). The next lesson identifies the hyperarithmetic sets with the $\Delta^1_1$ sets.

## Exercises

::::exercise{difficulty=1}
Show that $\mathcal O$ computes every hyperarithmetic set, and that it is not hyperarithmetic.

:::solution
By the next lesson, each $H_a$ is $\Pi^1_1$, and every $\Pi^1_1$ set is many-one reducible to $\mathcal O$, which is $\Pi^1_1$-complete (:ref{#thm-o-complete}); so $H_a \leq_T \mathcal O$, and every hyperarithmetic set is computable in $\mathcal O$. If $\mathcal O$ were hyperarithmetic, say $\mathcal O \leq_T H_a$, then $H_{2^a} \leq_T \mathcal O \leq_T H_a$, contradicting :ref{#prop-h-sets-basic} (3).
:::
::::

::::exercise{difficulty=2}
Let $a$ be a notation for $\omega \cdot 2$. Describe $H_a$ up to Turing equivalence in terms of $\emptyset^{(\omega)}$. Show that a set is arithmetic in $\emptyset^{(\omega)}$ if and only if it is computable in $H_b$ for some $b \in \mathcal O$ with $|b| < \omega \cdot 2$, and that $H_a$ is not arithmetic in $\emptyset^{(\omega)}$.

:::solution
Write $X^{(\omega)} = \bigoplus_n X^{(n)}$. Let $c$ be a notation for $\omega$, and $c_n$ the notation for $\omega + n$ obtained from $c$ by $n$ applications of $x \mapsto 2^x$; then $H_{c_n} = (H_c)^{(n)}$. Let $d = 3 \cdot 5^e$ with $\Phi_e(n) = c_{n+1}$, a notation for $\omega \cdot 2$. The notations below $d$ are the notations of the finite ordinals, $c$, and the $c_n$; this set is decidable, the columns of $H_d$ indexed by finite notations are computable in $H_c$ uniformly, and the column indexed by $c_n$ is $(H_c)^{(n)}$. Since $H_c \equiv_T \emptyset^{(\omega)}$ by :ref{#prop-h-sets-basic} (2), and the jump preserves Turing equivalence uniformly, $H_d \equiv_T \bigoplus_n (\emptyset^{(\omega)})^{(n)} = (\emptyset^{(\omega)})^{(\omega)}$. By :ref{#thm-spector-uniqueness}, $H_a \equiv_T H_d$.

By Post's theorem relativized, a set is arithmetic in $\emptyset^{(\omega)}$ if and only if it is computable in $(\emptyset^{(\omega)})^{(n)} \equiv_T H_{c_n}$ for some $n$. The notations $b$ with $|b| < \omega \cdot 2$ are those of the ordinals $k$ and $\omega + n$, and by :ref{#thm-spector-uniqueness} each $H_b$ is Turing equivalent to some $H_{c_n}$ or computable in $H_c$. Finally $H_a \geq_T (H_{c_n})'$ for every $n$, so $H_a$ is computable in no $(\emptyset^{(\omega)})^{(n)}$: it is not arithmetic in $\emptyset^{(\omega)}$.
:::
::::

::::exercise{difficulty=2}
Show that for every $x \in \mathcal O$, the set $\{ y \in \mathcal O : |y| = |x| \}$ is computable in $H_{2^{2^x}}$, uniformly in $x$.

:::solution
It is $\mathcal O_{<2^x} \setminus \mathcal O_{<x}$. By :ref{#lem-notations-below}, the first set is computable in $H_{2^{2^x}}$ and the second in $H_{2^x}$, both uniformly; and $H_{2^x} \leq_T H_{2^{2^x}}$ uniformly by :ref{#prop-h-sets-uniform}.
:::
::::

## Notes and references

Spector (1955) proved the uniqueness theorem. The proof given here, through the comparison of notations by H-sets (:ref{#lem-notations-below}), follows the presentation of Monin and Patey; Sacks's monograph and Ash and Knight's book give other presentations, the latter with applications to computable structures. Simpson (Section VIII.3) works with jump hierarchies along computable linear orders and proves the analogue of the theorem for isomorphic well-orderings (Lemma VIII.3.13) without the recursion theorem, by a definability argument (Lemma VIII.3.10) in place of the computation of indices of reductions.

- C. Spector, *Recursive well-orderings*, Journal of Symbolic Logic 20 (1955), 151–163.
- Y. N. Moschovakis, *Many-one degrees of the predicates $H_a(x)$*, Pacific Journal of Mathematics 18 (1966), 329–342.
- B. Monin and L. Patey, *Computability theory*, chapter "Hyperarithmetic sets".
- G. E. Sacks, *Higher Recursion Theory*, Springer, 1990.
- C. J. Ash and J. F. Knight, *Computable Structures and the Hyperarithmetical Hierarchy*, Elsevier, 2000.
- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009, Section VIII.3.
