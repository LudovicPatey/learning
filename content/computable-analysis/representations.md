---
title: Representations and the real numbers
summary: Represented spaces, realizers and reductions between representations; the Cauchy representation of the reals; the decimal representation has the same computable points but not the same computable functions; left and right representations, and left-c.e. reals.
duration: 45
prerequisites: [type-two-computability, second-order-arithmetic/real-numbers]
---

An algorithm cannot handle a real number directly, only a description of it. In computable analysis, the description is an element of Baire space, called a **name**, and a **representation** says which real each name denotes. The choice of the representation matters: two representations may have the same computable reals and still define different computable functions. The **Cauchy representation**, by sequences of rationals converging at a fixed rate, is the one used in the rest of the course; the decimal representation, the most familiar one, is inadequate, and the left and right representations capture one-sided information.

## Represented spaces

:::definition{#def-representation}
1. A **representation** of a set $X$ is a surjective partial function $\delta :\subseteq \bs \to X$. If $\delta(p) = x$, then $p$ is a **$\delta$-name** of $x$. The pair $(X, \delta)$ is a **represented space**.
2. A point $x \in X$ is **$\delta$-computable** if it has a computable $\delta$-name.
3. Let $(X, \delta_X)$ and $(Y, \delta_Y)$ be represented spaces and $f :\subseteq X \to Y$. A function $F :\subseteq \bs \to \bs$ **realizes** $f$ if $\delta_Y(F(p)) = f(\delta_X(p))$ for every $\delta_X$-name $p$ of a point of $\dom f$. The function $f$ is **$(\delta_X, \delta_Y)$-computable**, respectively **$(\delta_X, \delta_Y)$-continuous**, if it has a computable, respectively continuous, realizer.
:::

A realizer works on names, and must give a correct answer for every name of every point of the domain: two names of the same point may receive different outputs, provided that the outputs name the same point. Functions with values in $\nat$ are realized in the same way, $\nat$ being represented by $\delta_\nat(p) = p(0)$. Computable functions between represented spaces are closed under composition, since realizers compose (:ref{to="computable-analysis/type-two-computability"}).

Some represented spaces used throughout:

- $\bs$ and $\cs$, represented by the identity: computability is that of the previous lesson.
- $\mathbb Q$, represented by $\delta_{\mathbb Q}(p) = \nu(p(0))$, for a fixed computable bijection $\nu : \nat \to \mathbb Q$; we identify a rational with its code.
- Products: if $\delta_1$ and $\delta_2$ represent $X_1$ and $X_2$, then $[\delta_1, \delta_2](\langle p, q \rangle) = (\delta_1(p), \delta_2(q))$ represents $X_1 \times X_2$, and $\delta^\omega(\langle p_0, p_1, \dots \rangle) = (\delta(p_i))_i$ represents the sequences of elements of $X$.

:::definition{#def-representation-reduction}
Let $\delta$ and $\delta'$ be representations of a set $X$. We write $\delta \leq \delta'$, and say that $\delta$ **reduces** to $\delta'$, if the identity of $X$ is $(\delta, \delta')$-computable: some computable $F$ satisfies $\delta'(F(p)) = \delta(p)$ for every $p \in \dom \delta$. We write $\delta \leq_t \delta'$ if some continuous $F$ does, and $\delta \equiv \delta'$ if $\delta \leq \delta'$ and $\delta' \leq \delta$.
:::

If $\delta \leq \delta'$, a $\delta$-name carries at least as much information as a $\delta'$-name, uniformly. Equivalent representations have the same computable points and define the same computable functions: if $\delta_X \equiv \delta'_X$ and $\delta_Y \equiv \delta'_Y$, compose the realizers with the translations.

## The Cauchy representation

:::definition{#def-cauchy-representation}
The **Cauchy representation** $\rho :\subseteq \bs \to \mathbb R$ is defined by $\rho(p) = x$ if the rationals $q_k = \nu(p(k))$ satisfy $|q_k - q_l| \leq 2^{-k}$ for all $k \leq l$, and $x = \lim_k q_k$. For $n \geq 1$, $\mathbb R^n$ is represented by $\rho^n = [\rho, \dots, \rho]$.
:::

The names of $\rho$ are the real numbers of $\mathsf{RCA}_0$ (:ref{#def-real-rca}). There, a real is a name, and equality is an equivalence relation between names; here, a real is a point of $\mathbb R$, and a name denotes it. Letting $l \to \infty$ in the definition gives $|q_k - x| \leq 2^{-k}$ for every $k$. A real number is **computable** if it is $\rho$-computable: it is the limit of a computable sequence of rationals $(q_k)$ with $|q_k - x| \leq 2^{-k}$ for every $k$, by the following lemma.

:::lemma{#lem-cauchy-variants}
Let $\rho'(p) = x$ if $|\nu(p(k)) - x| \leq 2^{-k}$ for every $k$. Then $\rho \equiv \rho'$.
:::

:::proof{of=lem-cauchy-variants}
A $\rho$-name is a $\rho'$-name, as just observed, so the identity translates $\rho$ to $\rho'$. Conversely, if $|q_k - x| \leq 2^{-k}$ for every $k$, let $F(p)(k) = p(k+1)$. For $k \leq l$, $|q_{k+1} - q_{l+1}| \leq 2^{-k-1} + 2^{-l-1} \leq 2^{-k}$, and the limit is still $x$. So $F$ translates $\rho'$ to $\rho$.
:::

The lemma is used constantly: to compute a $\rho$-name of $y$, it suffices to compute rationals $r_k$ with $|r_k - y| \leq 2^{-k}$.

:::example{#ex-computable-reals}
1. Every rational $q$ is computable, with the constant name $q, q, q, \dots$
2. $\sqrt 2$ is computable: let $r_k$ be the largest multiple of $2^{-k}$ with $r_k^2 \leq 2$, found by a finite search; then $|r_k - \sqrt 2| \leq 2^{-k}$.
3. For $A \subseteq \nat$, the real $x_A = \sum_{n \in A} 2 \cdot 3^{-n-1}$ is computable if and only if $A$ is computable. If $A$ is computable, the partial sums over $n < k$ are within $3^{-k} \leq 2^{-k}$ of $x_A$. Conversely, $n \in A$ is decided from an approximation of $x_A$ within $3^{-n-2}$, once $A \cap \{0, \dots, n-1\}$ is known: the sum of the remaining terms lies in $[0, 3^{-n-1}]$ if $n \notin A$, and in $[2 \cdot 3^{-n-1}, 3^{-n}]$ if $n \in A$.
:::

Item 3 gives explicit non-computable reals, such as $x_{\emptyset'}$. The ternary digits $0$ and $2$ in item 3 leave gaps between the possible values, which makes the decoding possible.

## The decimal representation

:::definition{#def-decimal-representation}
The **decimal representation** $\rho_{10}$ of $[0, \infty)$ is defined on the sequences $p$ with $p(i) \leq 9$ for every $i \geq 1$, by $\rho_{10}(p) = p(0) + \sum_{i \geq 1} p(i)\, 10^{-i}$.
:::

The first value is the integer part, and the following ones are the digits. A real has one decimal name, or two when it is a decimal fraction $k/10^j$ with $k > 0$: $1 = \rho_{10}(1, 0, 0, \dots) = \rho_{10}(0, 9, 9, \dots)$. The difficulty with decimal names is not the double names, but the fact that a digit is a final commitment about an interval, which an algorithm reading approximations may be unable to make (:ref{#fig-decimal-one}).

:::figure[Every interval around $1$ contains reals below $1$, whose decimal names have integer part $0$, and reals above $1$, whose decimal names have integer part $1$. A finite part of a Cauchy name of $1$ is shared by names of reals on both sides.]{#fig-decimal-one}
<svg class="fig" viewBox="0 0 640 200" width="640" role="img" aria-label="Around the real 1, every neighborhood contains reals below 1, whose decimal expansions begin with 0, and reals above 1, whose decimal expansions begin with 1"><line x1="50" y1="90" x2="590" y2="90" class="axis"/><line x1="125.0" y1="86" x2="125.0" y2="94" class="ink-stroke" stroke-width="1"/><text x="125.0" y="110.0" text-anchor="middle" class="mrm" font-size="12">0.97</text><line x1="190.0" y1="86" x2="190.0" y2="94" class="ink-stroke" stroke-width="1"/><text x="190.0" y="110.0" text-anchor="middle" class="mrm" font-size="12">0.98</text><line x1="255.0" y1="86" x2="255.0" y2="94" class="ink-stroke" stroke-width="1"/><text x="255.0" y="110.0" text-anchor="middle" class="mrm" font-size="12">0.99</text><line x1="320.0" y1="86" x2="320.0" y2="94" class="ink-stroke" stroke-width="1"/><text x="320.0" y="110.0" text-anchor="middle" class="mrm" font-size="12">1.00</text><line x1="385.0" y1="86" x2="385.0" y2="94" class="ink-stroke" stroke-width="1"/><text x="385.0" y="110.0" text-anchor="middle" class="mrm" font-size="12">1.01</text><line x1="450.0" y1="86" x2="450.0" y2="94" class="ink-stroke" stroke-width="1"/><text x="450.0" y="110.0" text-anchor="middle" class="mrm" font-size="12">1.02</text><line x1="515.0" y1="86" x2="515.0" y2="94" class="ink-stroke" stroke-width="1"/><text x="515.0" y="110.0" text-anchor="middle" class="mrm" font-size="12">1.03</text><rect x="242.0" y="60" width="156.0" height="18" class="cell head-cell"/><text x="320.0" y="52.0" text-anchor="middle" class="label">reals with a name extending the prefix</text><circle cx="320.0" cy="90" r="4" class="accent-fill"/><line x1="73.0" y1="130" x2="317.0" y2="130" class="muted-stroke" stroke-width="3"/><line x1="323.0" y1="130" x2="567.0" y2="130" class="accent-stroke" stroke-width="3"/><text x="190.0" y="150.0" text-anchor="middle" class="label">y &lt; 1: integer part 0</text><text x="450.0" y="150.0" text-anchor="middle" class="label">y &gt; 1: integer part 1</text><text x="320.0" y="178.0" text-anchor="middle" class="label">1 has the two decimal names 0.999… and 1.000…</text></svg>
:::

:::proposition{#prop-decimal-cauchy}
1. $\rho_{10} \leq \rho$ on $[0, \infty)$.
2. $\rho \not\leq_t \rho_{10}$ on $[0, \infty)$: no continuous function translates Cauchy names of non-negative reals into decimal names.
3. The function $x \mapsto 3x$ on $[0, \infty)$ is not $(\rho_{10}, \rho_{10})$-continuous, although it is $(\rho, \rho)$-computable.
:::

:::proof{of=prop-decimal-cauchy}
1. From a decimal name $p$ of $x$, compute $r_k = p(0) + \sum_{1 \leq i \leq k} p(i)\, 10^{-i}$. Then $0 \leq x - r_k \leq 10^{-k} \leq 2^{-k}$, and :ref{#lem-cauchy-variants} gives a Cauchy name.

2. Suppose that a continuous $F$ translates $\rho$ to $\rho_{10}$. Let $p$ be the name of $1$ with $q_k = 1$ for every $k$. The integer part $F(p)(0)$ is $0$ or $1$, and by continuity there is $m$ such that $F(q)(0) = F(p)(0)$ for every Cauchy name $q \in [p \uh m]$. Let $y = 1 - 2^{-m-1}$ if $F(p)(0) = 1$, and $y = 1 + 2^{-m-1}$ if $F(p)(0) = 0$. The sequence $q$ of rationals $1, \dots, 1, y, y, \dots$, with $m$ terms equal to $1$, is a Cauchy name of $y$: for $k < m \leq l$, $|q_k - q_l| = 2^{-m-1} \leq 2^{-k}$. It extends $p \uh m$, so $F(q)(0) = F(p)(0)$. But the integer part of every decimal name of $y$ is $0$ if $y < 1$, and $1$ if $1 < y < 2$; in both cases it differs from $F(p)(0)$.

3. Let $p = (0, 3, 3, 3, \dots)$, the decimal name of $1/3$, and suppose that $F$ is a continuous realizer of $x \mapsto 3x$. The integer part $F(p)(0)$ of a name of $1$ is $0$ or $1$. By continuity, there is $m \geq 1$ such that $F(q)(0) = F(p)(0)$ for all decimal names $q \in [p \uh m]$. The names $(0, 3, \dots, 3, 0, 0, \dots)$ and $(0, 3, \dots, 3, 4, 0, \dots)$, with $m$ values before the last block, extend $p \uh m$ and denote reals $y_0 < 1/3 < y_1 < 2/3$. The integer part of $3 y_0$ is $0$ and that of $3 y_1$ is $1$, so one of them is not $F(q)(0)$. For the Cauchy representation, $(q_k) \mapsto (3 q_{k+2})$ realizes $x \mapsto 3x$, since $|3 q_{k+2} - 3x| \leq 3 \cdot 2^{-k-2} \leq 2^{-k}$, and :ref{#lem-cauchy-variants} applies.
:::

Both proofs are continuity arguments, and the failure is not about which reals are computable.

:::proposition{#prop-decimal-points}
A real $x \geq 0$ is $\rho$-computable if and only if it is $\rho_{10}$-computable.
:::

:::proof{of=prop-decimal-points}
If $x$ has a computable decimal name, it has a computable Cauchy name by :ref{#prop-decimal-cauchy} (1). Conversely, let $(q_k)$ be a computable Cauchy name of $x$. If $x = k/10^j$ for some $k, j$, then $x$ has a finite decimal expansion, padded with zeros, which is computable. Otherwise, for each $j$, there is a unique integer $k_j$ with $k_j/10^j < x < (k_j + 1)/10^j$, and it is found by searching for $k$ and $l$ with $k/10^j < q_l - 2^{-l}$ and $q_l + 2^{-l} < (k+1)/10^j$: since $x$ lies strictly inside the interval, such an $l$ exists. The decimal name $p(0) = k_0$, $p(j) = k_j - 10\, k_{j-1}$ for $j \geq 1$, is computable.
:::

The proof distinguishes two cases, and the case distinction cannot be made by an algorithm: whether $x$ is a decimal fraction is not decided by any finite part of a name. Each computable real has a computable decimal name, but no algorithm converts Cauchy names into decimal names. The representations have the same computable points and different computable functions; the course always uses $\rho$. Weihrauch shows that $\rho$ is **admissible**, a topological property that the decimal representation lacks (Section 3.2 and Theorem 4.1.13).

:::quiz[the decimal representation]
In the proof of :ref{#prop-decimal-cauchy} (2), why is the special name $q_k = 1$ used, rather than an arbitrary name of $1$?

- [x] Because its prefix of length $m$ must extend to a name of $y$; with $q_k = 1$ for $k < m$, the condition $|q_k - y| \leq 2^{-k}$ is satisfied for $y$ close to $1$ on both sides.
- [ ] Because $F$ is defined only on that name.

  $F$ is defined on all Cauchy names of non-negative reals.
- [ ] Because $1$ has two decimal names.

  The two decimal names of $1$ explain why $F(p)(0)$ may be $0$ or $1$; the choice of the Cauchy name serves the extension to names of $y$.

---

Why does :ref{#prop-decimal-points} not contradict :ref{#prop-decimal-cauchy}?

- [x] Because the proof of :ref{#prop-decimal-points} uses a different algorithm depending on whether $x$ is a decimal fraction, and no single algorithm works for all names.
- [ ] Because the computable reals are all rational.

  $\sqrt 2$ is computable and irrational.
- [ ] Because decimal fractions have no computable decimal names.

  They do: their finite expansions padded with zeros.
:::

## Left and right representations

Some reals arise with approximations from one side only, such as the limit of a computable non-decreasing sequence (:ref{#prop-specker}).

:::definition{#def-left-right}
The **left representation** $\rho_<$ of $\mathbb R$ is defined by $\rho_<(p) = x$ if $\{ \nu(p(n)) : n \in \nat \} = \{ q \in \mathbb Q : q < x \}$: a name lists the rationals below $x$. The **right representation** $\rho_>$ is defined symmetrically, with the rationals above $x$. A real is **left-c.e.** if it is $\rho_<$-computable, and **right-c.e.** if it is $\rho_>$-computable.
:::

A real is left-c.e. if and only if the set of rationals below it is c.e., if and only if it is the limit of a computable non-decreasing sequence of rationals (exercise of :ref{to="second-order-arithmetic/real-numbers"}). Chaitin's $\Omega$ and the limits of Specker sequences are left-c.e. and not computable.

:::proposition{#prop-left-right}
1. $\rho \leq \rho_<$ and $\rho \leq \rho_>$.
2. $\rho \equiv \rho_< \wedge \rho_>$, where $(\rho_< \wedge \rho_>)(\langle p, q \rangle) = x$ if $\rho_<(p) = x$ and $\rho_>(q) = x$.
3. $\rho_< \not\leq_t \rho$. In particular a real is computable if and only if it is left-c.e. and right-c.e., but no continuous function computes a Cauchy name from a left name.
:::

:::proof{of=prop-left-right}
1. Given a Cauchy name $(q_k)$ of $x$, list every rational $q$ such that $q < q_k - 2^{-k}$ for some $k$, by a dovetailed search over the pairs $(q, k)$, starting with $q_0 - 2$. Each listed $q$ is below $x$, since $q_k - 2^{-k} \leq x$. Conversely, if $q < x$, choose $k$ with $2^{-k+1} < x - q$; then $q_k - 2^{-k} \geq x - 2^{-k+1} > q$, so $q$ is listed. The right representation is symmetric.

2. By (1), a Cauchy name computes a pair of left and right names. Conversely, given a left name and a right name of $x$, compute for each $k$ the first pair $(a, b)$, with $a$ listed in the left name and $b$ in the right name, such that $b - a \leq 2^{-k}$, and output $a$. Such pairs exist, since there are rationals below and above $x$ arbitrarily close to it; and $a < x < b$ gives $|a - x| \leq 2^{-k}$. Conclude with :ref{#lem-cauchy-variants}.

3. Suppose that a continuous $F$ translates $\rho_<$ to $\rho$. Let $p$ be a left name of $0$, a list of the negative rationals. The term of index $2$ of $F(p)$ is a rational $r$ with $|r| \leq 1/4$, and by continuity there is $m$ such that the term of index $2$ of $F(q)$ is $r$ for every left name $q \in [p \uh m]$. The finitely many rationals listed in $p \uh m$ are negative, so below $1$; let $q$ be $p \uh m$ followed by a list of all rationals below $1$. Then $q$ is a left name of $1$ extending $p \uh m$, so $F(q)$ is a Cauchy name of $1$ whose term of index $2$ is $r$, and $|r - 1| \leq 1/4$, which contradicts $|r| \leq 1/4$. The first statement of (3) follows from (2).
:::

A finite part of a left name gives lower bounds only. Specker's theorem (:ref{#prop-specker}) shows more than item 3: some left-c.e. real is not computable, so the two representations differ already on computable points.

:::quiz[left and right representations]
In the proof of :ref{#prop-left-right} (3), why can $p \uh m$ be extended to a left name of $1$?

- [x] Because a left name lists rationals below the real in any order, and the finitely many rationals of $p \uh m$, all negative, are also below $1$.
- [ ] Because $0$ and $1$ have the same left names.

  A left name of $0$ lists only negative rationals, a left name of $1$ lists all rationals below $1$; they share prefixes, not whole names.
- [ ] Because $F$ is defined on all sequences.

  $F$ is defined on the left names; the point is that $q$ is one.

:::

## Exercises

::::exercise{difficulty=2}
The **signed-digit representation** $\rho_{sd}$ of $[-1, 1]$ names $x$ by sequences $p \in \{-1, 0, 1\}^\nat$ with $x = \sum_i p(i)\, 2^{-i-1}$ (the digits $-1, 0, 1$ are coded by $0, 1, 2$). Show that $\rho_{sd} \equiv \rho$ on $[-1, 1]$, and compare with :ref{#prop-decimal-cauchy}.

:::solution
From a signed-digit name, $r_k = \sum_{i < k} p(i)\, 2^{-i-1}$ satisfies $|x - r_k| \leq \sum_{i \geq k} 2^{-i-1} = 2^{-k}$; so $\rho_{sd} \leq \rho$ by :ref{#lem-cauchy-variants}. Conversely, from a Cauchy name of $x \in [-1, 1]$, compute digits $d_0, d_1, \dots$ such that the partial sums $s_n = \sum_{i < n} d_i\, 2^{-i-1}$ satisfy $|x - s_n| \leq 2^{-n}$. This holds for $s_0 = 0$. Given $s_n$, take a rational $r$ with $|r - x| \leq 2^{-n-3}$ and let $t = r - s_n$; choose $d_n = 1$ if $t \geq 2^{-n-2}$, $d_n = -1$ if $t \leq -2^{-n-2}$, and $d_n = 0$ otherwise. If $d_n = 1$, then $x - s_n \geq 2^{-n-2} - 2^{-n-3} > 0$ and $x - s_n \leq 2^{-n}$, so $x - s_{n+1} = x - s_n - 2^{-n-1}$ lies in $[-2^{-n-1}, 2^{-n-1}]$. The case $d_n = -1$ is symmetric. If $d_n = 0$, $|x - s_n| < 2^{-n-2} + 2^{-n-3} < 2^{-n-1}$. The digit $0$ gives the algorithm room: unlike a binary or decimal digit, a signed digit never has to decide on which side of a point $x$ lies, since the intervals of consecutive choices overlap.
:::
::::

## Notes and references

Representations, realizers and reductions between representations are Weihrauch, Sections 2.3 and 3.1; the Cauchy representation, its variants and the left and right representations are Section 4.1 (Definitions 4.1.3 and 4.1.5, Lemma 4.1.6, and Lemma 4.1.9 for $\rho \equiv \rho_< \wedge \rho_>$), and computable reals are Section 4.2. The properties of the base-$n$ representations, including :ref{#prop-decimal-cauchy} (1)–(2) and :ref{#prop-decimal-points}, are collected in Theorem 4.1.13; the failure of multiplication by $3$ for decimal names is Weihrauch's Example 2.1.4 (7). Turing noticed in his correction of 1937 that decimal expansions are not suitable names for computable reals, and replaced them by a representation through rational approximations. The signed-digit representation is his Definition 7.2.4, studied in Section 7.2. Brattka, Hertling and Weihrauch give a short presentation of the same material in Sections 2–3 of their tutorial.

- K. Weihrauch, *Computable Analysis: An Introduction*, Springer, 2000, Sections 2.1, 2.3, 3.1, 4.1, 4.2 and 7.2.
- V. Brattka, P. Hertling and K. Weihrauch, *A tutorial on computable analysis*, in *New Computational Paradigms*, Springer, 2008, 425–491.
- A. M. Turing, *On computable numbers, with an application to the Entscheidungsproblem. A correction*, Proceedings of the London Mathematical Society 43 (1937), 544–546.
