---
title: The intermediate value theorem
summary: The intermediate value theorem has computable solutions for computable instances but not uniformly; the trisection method; the theorem lies between LLPO and weak König's lemma, its parallelization is equivalent to weak König's lemma, and it is equivalent to the Brouwer fixed point theorem in dimension one.
duration: 40
prerequisites: [closed-sets-and-choice, reducibilities/weihrauch, pi01-classes/computable-members]
---

A theorem of the form "for every $x$ there is $y$ such that ..." becomes a problem: given $x$, find $y$. The previous lesson classified closed choice as equivalent to weak König's lemma. This lesson treats the intermediate value theorem. It is non-uniformly computable: every computable instance has a computable solution, but no algorithm finds solutions uniformly. Its Weihrauch degree lies strictly between $\mathsf{LLPO}$ and $\mathsf{WKL}$, its parallelization is equivalent to $\mathsf{WKL}$, and it is shared by the Brouwer fixed point theorem in dimension one. The proofs combine the two methods of the course: continuity arguments for the negative results, and reductions to closed choice for the upper bounds.

All problems below are problems on represented spaces (:ref{#def-problem-represented}): reals are represented by $\rho$, and continuous functions on $[0, 1]$ by $\delta_C$, or equivalently by rectangle names.

## The intermediate value theorem

:::definition{#def-ivt-problem}
The problem $\mathsf{IVT}$ has as instances the functions $f \in C[0, 1]$ with $f(0) < 0 < f(1)$, and as solutions to $f$ the points $x \in [0, 1]$ with $f(x) = 0$.
:::

The proof by bisection in :ref{#thm-ivt-rca} is effective except for one decision: whether $f$ vanishes at the midpoint, a question that no algorithm answers. The **trisection method** avoids the decision when $f$ has no interval of zeros: instead of the midpoint, it looks for a point of the middle third where $f$ is certainly not zero.

:::theorem{#thm-trisection}
The restriction of $\mathsf{IVT}$ to the functions whose zero set has empty interior is computable.
:::

:::proof{of=thm-trisection}
We compute rationals $a_n < b_n$ in $[0, 1]$ with $f(a_n) < 0 < f(b_n)$ and $b_n - a_n \leq (2/3)^n$. Let $a_0 = 0$ and $b_0 = 1$. Given $a_n$ and $b_n$, search for a rational $c$ in the open middle third $(a_n + (b_n - a_n)/3,\ a_n + 2(b_n - a_n)/3)$ such that $f(c) < 0$ or $f(c) > 0$, by dovetailing the semi-decision procedures of :ref{#prop-order-undecidable}, applied to the values $f(c)$ computed by evaluation (:ref{#thm-rectangle-computable}). Such a $c$ exists: the middle third is an open interval, so it is not included in the zero set, and $f$ is non-zero on an open subinterval by continuity, which contains rationals. If $f(c) < 0$, let $(a_{n+1}, b_{n+1}) = (c, b_n)$; otherwise $(a_{n+1}, b_{n+1}) = (a_n, c)$. In both cases $b_{n+1} - a_{n+1} \leq \frac23 (b_n - a_n)$.

The intervals $[a_n, b_n]$ are nested and their lengths tend to $0$, so they shrink to a point $x$, and $|a_n - x| \leq (2/3)^n$. By continuity, $f(x) = \lim f(a_n) \leq 0$ and $f(x) = \lim f(b_n) \geq 0$, so $f(x) = 0$. Since $(2/3)^{2k} \leq 2^{-k}$, the rationals $a_{2k}$ form a Cauchy name of $x$ by :ref{#lem-cauchy-variants}.
:::

:::corollary{#cor-ivt-computable-instances}
Every computable instance of $\mathsf{IVT}$ has a computable solution.
:::

:::proof{of=cor-ivt-computable-instances}
Let $f$ be a computable instance. If $f(q) = 0$ for some rational $q$, then $q$ is a computable solution. Otherwise the zero set of $f$ contains no rational, so it has empty interior, and the algorithm of :ref{#thm-trisection}, applied to a computable name of $f$, outputs a computable name of a zero.
:::

This is the computable reading of :ref{#thm-ivt-rca}, whose proof makes the same case distinction; the distinction is not effective, and the next theorem shows that it cannot be avoided. The counterexample consists of the polygons $g_a$ with vertices $(0, -1)$, $(1/3, a)$, $(2/3, a)$ and $(1, 1)$, for $a \in \mathbb R$ (:ref{#fig-ivt-polygons}). For $a > 0$, $g_a$ has a single zero, in $(0, 1/3)$; for $a < 0$, a single zero, in $(2/3, 1)$; and the zeros of $g_0$ form the interval $[1/3, 2/3]$. The uniform distance between $g_a$ and $g_b$ is $|a - b|$.

:::figure[The polygons $g_a$. A small change of $a$ around $0$ moves every zero from one side of $1/2$ to the other.]{#fig-ivt-polygons}
<svg class="fig" viewBox="0 0 640 250" width="640" role="img" aria-label="The polygon g_a through (0, -1), (1/3, a), (2/3, a) and (1, 1): for a = 0 its zeros form the interval [1/3, 2/3], for positive a there is a single zero below 1/3, for negative a a single zero above 2/3"><line x1="34" y1="110.0" x2="210" y2="110.0" class="axis"/><line x1="40" y1="33.0" x2="40" y2="187.0" class="axis"/><line x1="93.3" y1="107.0" x2="93.3" y2="113.0" class="ink-stroke" stroke-width="1"/><text x="93.3" y="201.0" text-anchor="middle" class="mrm" font-size="11">1/3</text><line x1="146.7" y1="107.0" x2="146.7" y2="113.0" class="ink-stroke" stroke-width="1"/><text x="146.7" y="201.0" text-anchor="middle" class="mrm" font-size="11">2/3</text><line x1="200.0" y1="107.0" x2="200.0" y2="113.0" class="ink-stroke" stroke-width="1"/><text x="200.0" y="201.0" text-anchor="middle" class="mrm" font-size="11">1</text><polyline points="40.0,180.0 93.3,110.0 146.7,110.0 200.0,40.0" class="ink-stroke" stroke-width="1.8"/><line x1="93.3" y1="110.0" x2="146.7" y2="110.0" class="accent-stroke" stroke-width="4"/><text x="120.0" y="228.0" text-anchor="middle" class="label">a = 0: zeros [1/3, 2/3]</text><line x1="244" y1="110.0" x2="420" y2="110.0" class="axis"/><line x1="250" y1="33.0" x2="250" y2="187.0" class="axis"/><line x1="303.3" y1="107.0" x2="303.3" y2="113.0" class="ink-stroke" stroke-width="1"/><text x="303.3" y="201.0" text-anchor="middle" class="mrm" font-size="11">1/3</text><line x1="356.7" y1="107.0" x2="356.7" y2="113.0" class="ink-stroke" stroke-width="1"/><text x="356.7" y="201.0" text-anchor="middle" class="mrm" font-size="11">2/3</text><line x1="410.0" y1="107.0" x2="410.0" y2="113.0" class="ink-stroke" stroke-width="1"/><text x="410.0" y="201.0" text-anchor="middle" class="mrm" font-size="11">1</text><polyline points="250.0,180.0 303.3,92.5 356.7,92.5 410.0,40.0" class="ink-stroke" stroke-width="1.8"/><circle cx="292.7" cy="110.0" r="4" class="accent-fill"/><text x="330.0" y="228.0" text-anchor="middle" class="label">a > 0: one zero below 1/3</text><line x1="454" y1="110.0" x2="630" y2="110.0" class="axis"/><line x1="460" y1="33.0" x2="460" y2="187.0" class="axis"/><line x1="513.3" y1="107.0" x2="513.3" y2="113.0" class="ink-stroke" stroke-width="1"/><text x="513.3" y="201.0" text-anchor="middle" class="mrm" font-size="11">1/3</text><line x1="566.7" y1="107.0" x2="566.7" y2="113.0" class="ink-stroke" stroke-width="1"/><text x="566.7" y="201.0" text-anchor="middle" class="mrm" font-size="11">2/3</text><line x1="620.0" y1="107.0" x2="620.0" y2="113.0" class="ink-stroke" stroke-width="1"/><text x="620.0" y="201.0" text-anchor="middle" class="mrm" font-size="11">1</text><polyline points="460.0,180.0 513.3,127.5 566.7,127.5 620.0,40.0" class="ink-stroke" stroke-width="1.8"/><circle cx="577.3" cy="110.0" r="4" class="accent-fill"/><text x="540.0" y="228.0" text-anchor="middle" class="label">a &lt; 0: one zero above 2/3</text></svg>
:::

:::theorem{#thm-ivt-not-computable}
$\mathsf{IVT}$ has no continuous realizer. In particular, it is not computable.
:::

:::proof{of=thm-ivt-not-computable}
Suppose that $F$ is a continuous realizer. The constant sequence $p = (g_0, g_0, \dots)$ is a $\delta_C$-name of $g_0$, so $F(p)$ is a Cauchy name of a zero $x \in [1/3, 2/3]$ of $g_0$; let $r$ be its term of index $3$, so that $|r - x| \leq 1/8$. By continuity, there is $m$ such that the term of index $3$ of $F(q)$ is $r$ for every name $q \in [p \uh m]$ of an instance. If $r \leq 1/2$, let $a = -2^{-m}$; otherwise let $a = 2^{-m}$. The sequence $q$ of polygons $g_0, \dots, g_0, g_a, g_a, \dots$, with $m$ terms $g_0$, is a $\delta_C$-name of $g_a$, since $d(g_0, g_a) = 2^{-m} \leq 2^{-k}$ for $k < m$; and $g_a$ is an instance. So $F(q)$ is a name of the unique zero $z$ of $g_a$, and its term of index $3$ is $r$, whence $|r - z| \leq 1/8$. But if $r \leq 1/2$, then $z > 2/3$ and $z - r > 1/6$; if $r > 1/2$, then $z < 1/3$ and $r - z > 1/6$.
:::

:::quiz[the intermediate value theorem is not computable]
Why can the proof of :ref{#thm-ivt-not-computable} not be adapted to instances with a unique zero?

- [x] Because the argument needs an instance, $g_0$, whose zeros spread over an interval: near it, instances have zeros far apart. When all instances near $f$ have their zero near the zero of $f$, no contradiction arises, and indeed :ref{#thm-trisection} computes the zero.
- [ ] Because a function with a unique zero has a rational zero.

  The unique zero may be irrational, as for $x^2 - 1/2$.
- [ ] Because the realizer is then computable.

  The proof assumes only a continuous realizer; computability is the conclusion it refutes.

---

Why is the term of index $3$ of the output used?

- [x] Because it locates the zero within $1/8$, which is enough to tell the two sides apart: the zeros of $g_a$ for $a \neq 0$ are below $1/3$ or above $2/3$, at distance more than $1/6$ from any $r$ on the other side of $1/2$.
- [ ] Because the first terms of a Cauchy name are arbitrary.

  They are not arbitrary; they are only less precise, and the term of index $0$ only locates the zero within $1$.
- [ ] Because $m$ must be at least $3$.

  The value of $m$ is given by continuity; it plays no role in the choice of the index.
:::

::::exercise{#ex-inverse-increasing difficulty=2 objective="Compute inverse functions by unique choice, avoiding the boundary cases of the intermediate value theorem." lessons="closed-sets-and-choice"}
Let $f \in C[0, 1]$ be computable and strictly increasing. Show that its inverse $f^{-1} : [f(0), f(1)] \to [0, 1]$ is computable.

:::solution
Given a name of $y \in [f(0), f(1)]$, the function $g = f - y$ is computable from the name of $y$, uniformly, and has exactly one zero $x = f^{-1}(y)$. Its zero set $\{ x \}$ has empty interior, but $g(0) < 0 < g(1)$ may fail, when $y$ is $f(0)$ or $f(1)$. Use instead the singleton $\{ x \}$: a $\psi_>$-name of the zero set of $g$ is computed by :ref{#thm-zero-sets}, and the algorithm of :ref{#ex-unique-choice} computes $x$ from it. Both steps are uniform in the name of $y$.
:::
::::

## Between LLPO and weak König's lemma

The polygons $g_a$ also show that a solution to $\mathsf{IVT}$ answers a question of $\mathsf{LLPO}$ (:ref{#def-lpo-llpo}): the side of $1/2$ on which a zero lies determines the sign of $a$, when $a \neq 0$.

:::theorem{#thm-ivt-llpo-wkl}
$\mathsf{LLPO} \leq_{sW} \mathsf{IVT} \leq_{sW} \mathsf{WKL}$.
:::

:::proof{of=thm-ivt-llpo-wkl}
($\mathsf{LLPO} \leq_{sW} \mathsf{IVT}$) Given an instance $p$ of $\mathsf{LLPO}$, let $a = 2^{-n}$ if $p(n) = 1$ with $n$ even, $a = -2^{-n}$ if $p(n) = 1$ with $n$ odd, and $a = 0$ if $p$ has no $1$. Let $a_k$ be the value of the same definition applied to $p \uh (k+1)$, that is, with $a_k = 0$ if no $1$ occurs at positions $n \leq k$. Then $|a_k - a_l| \leq 2^{-k}$ for $k \leq l$, since they differ only if the $1$ of $p$ is at a position $n$ with $k < n \leq l$, and then by $2^{-n}$. So $(g_{a_k})_k$ is a $\delta_C$-name of $g_a$, computed from $p$. Given a zero $x$ of $g_a$, compute a rational $r$ with $|r - x| \leq 1/12$. If $r < 1/2$, then $x < 2/3$, so $a \geq 0$ and $p$ has no $1$ at an odd position: output $1$. If $r \geq 1/2$, then $x > 1/3$, so $a \leq 0$ and $p$ has no $1$ at an even position: output $0$. The output is a solution, and is computed from $x$ alone.

($\mathsf{IVT} \leq_{sW} \mathsf{WKL}$) The zero set of an instance $f$ is non-empty, and a $\psi_>$-name of it is computed from $f$ (:ref{#thm-zero-sets}). Every point of it is a solution, so $\mathsf{IVT} \leq_{sW} \mathsf C_{[0,1]}$, and :ref{#thm-closed-choice-wkl} concludes.
:::

:::corollary{#cor-ivt-parallel}
$\widehat{\mathsf{IVT}} \equiv_W \mathsf{WKL}$. Consequently, there is a computable sequence $(f_n)$ of instances of $\mathsf{IVT}$ such that no computable sequence $(x_n)$ satisfies $f_n(x_n) = 0$ for every $n$.
:::

:::proof{of=cor-ivt-parallel}
Parallelization preserves Weihrauch reducibility (:ref{to="reducibilities/parallelization"}), and the argument applies to problems on represented spaces. So $\widehat{\mathsf{LLPO}} \leq_W \widehat{\mathsf{IVT}} \leq_W \widehat{\mathsf{WKL}}$. By :ref{#thm-wkl-llpo}, $\widehat{\mathsf{LLPO}} \equiv_W \mathsf{WKL}$ and $\widehat{\mathsf{WKL}} \equiv_W \widehat{\widehat{\mathsf{LLPO}}}$. A sequence of sequences of instances is a sequence of instances, re-indexed by the pairing function, so $\widehat{\widehat{\mathsf{LLPO}}} \equiv_W \widehat{\mathsf{LLPO}} \equiv_W \mathsf{WKL}$.

For the second statement, let $T$ be an infinite computable binary tree without computable path (:ref{#thm-dnc2-no-computable}), and let $\Phi$ and $\Psi$ witness $\mathsf{WKL} \leq_W \widehat{\mathsf{IVT}}$. Then $\Phi(T)$ is a computable sequence of instances of $\mathsf{IVT}$. If a computable sequence of solutions $s$ existed, $\Psi(\langle T, s \rangle)$ would be a computable path through $T$.
:::

Each $f_n$ has a computable zero, by :ref{#cor-ivt-computable-instances}; what fails is the uniformity. This is the typical effect of parallelization: a non-uniformity that is invisible on a single computable instance becomes visible on a computable sequence of instances. The two reductions of :ref{#thm-ivt-llpo-wkl} are strict, and the exact degree of $\mathsf{IVT}$ is known; we admit these results.

:::fact[Brattka, Gherardi; Brattka, Le Roux, Miller, Pauly]{#fact-ivt-connected-choice}
1. $\mathsf{IVT} \equiv_{sW} \mathsf{CC}_{[0,1]}$, where **connected choice** $\mathsf{CC}_{[0,1]}$ is the restriction of closed choice to the non-empty closed intervals $[a, b] \subseteq [0, 1]$, possibly reduced to a point.
2. $\mathsf{LLPO} <_W \mathsf{IVT} <_W \mathsf{WKL}$. More precisely, $\mathsf{IVT} \times \mathsf{IVT} \not\leq_W \mathsf{IVT}$, while $\mathsf{WKL} \times \mathsf{WKL} \leq_W \mathsf{WKL}$.
:::

The first item says that the content of the intermediate value theorem is to choose a point in a closed interval known only through its complement: the difficulty is that the complement is revealed piece by piece, and a piece may lie on either side of the interval. The product statement in the second item implies $\mathsf{IVT} <_W \mathsf{WKL}$, since $\mathsf{WKL} \times \mathsf{WKL} \leq_W \mathsf{WKL}$: a pair of infinite binary trees is turned into a single tree whose paths code pairs of paths.

## The Brouwer fixed point theorem in dimension one

:::definition{#def-brouwer-one}
The problem $\mathsf{BFT}_1$ has as instances the functions $f \in C[0, 1]$ with values in $[0, 1]$, and as solutions to $f$ the points $x$ with $f(x) = x$.
:::

The Brouwer fixed point theorem in dimension one follows from the intermediate value theorem applied to $x - f(x)$, which is $\leq 0$ at $0$ and $\geq 0$ at $1$. The inequalities are not strict, and the reduction shifts the problem to a larger interval where they become strict. We write $\kappa(u) = \min(1, \max(0, u))$ for the projection of $\mathbb R$ onto $[0, 1]$. In both directions, the new function is obtained from $f$ by composition with computable functions; its values at rationals are computed by :ref{#thm-rectangle-computable}, a modulus of uniform continuity is computed from one of $f$ (:ref{#thm-modulus-max}), and the proof of :ref{#thm-cauchy-rectangle} computes a $\delta_C$-name from these two.

:::theorem[Brattka, Le Roux, Miller, Pauly]{#thm-brouwer-one}
$\mathsf{BFT}_1 \equiv_{sW} \mathsf{IVT}$.
:::

:::proof{of=thm-brouwer-one}
($\mathsf{BFT}_1 \leq_{sW} \mathsf{IVT}$) Given $f$, let $g(t) = (3t - 1) - f(\kappa(3t - 1))$ for $t \in [0, 1]$. Then $g(0) = -1 - f(0) < 0$ and $g(1) = 2 - f(1) > 0$. Let $g(t) = 0$ and $u = 3t - 1 \in [-1, 2]$. If $u < 0$, then $g(t) = u - f(0) < 0$; if $u > 1$, then $g(t) = u - f(1) > 0$ since $f(1) \leq 1$. So $u \in [0, 1]$ and $u - f(u) = 0$: $u$ is a fixed point of $f$, computed from $t$ alone.

($\mathsf{IVT} \leq_{sW} \mathsf{BFT}_1$) Given an instance $f$ of $\mathsf{IVT}$, let $g(x) = \kappa(x - f(x))$, with values in $[0, 1]$. Let $g(x) = x$. If $x = 0$, then $x - f(x) \leq 0$, that is, $f(0) \geq 0$, which is false; if $x = 1$, then $1 - f(1) \geq 1$, that is, $f(1) \leq 0$, which is false. So $0 < x < 1$, and then $g(x) = x$ forces $x - f(x) = x$, since $\kappa$ maps the values outside $(0, 1)$ to $0$ or $1$. So $f(x) = 0$, and the backward functional is the identity.
:::

In higher dimensions, the picture changes: for $n \geq 2$, the Brouwer fixed point theorem for $[0, 1]^n$ is equivalent to $\mathsf{WKL}$ (Brattka, Le Roux, Miller and Pauly), and there are computable functions $[0, 1]^2 \to [0, 1]^2$ without computable fixed points (Orevkov, 1963; Baigger, 1985). In dimension one, every computable instance has a computable fixed point, by :ref{#cor-ivt-computable-instances}.

## Notes and references

Zero-finding is Weihrauch, Section 6.3: the non-computability of $\mathsf{IVT}$ with the polygons $g_a$ is his Theorem 6.3.2, the trisection method Theorem 6.3.7, computable zeros of computable functions Theorem 6.3.8, isolated zeros Corollary 6.3.9 and inverse functions Theorem 6.3.11. Dzhafarov and Mummert prove that $\mathsf{IVT}$ does not uniformly admit computable solutions (Proposition 3.7.4) and present its equivalence with choice for nested intervals (Theorem 10.4.3). The Weihrauch degree of $\mathsf{IVT}$ was determined by Brattka and Gherardi (2011, Theorem 6.2), and connected choice and the Brouwer fixed point theorem were studied by Brattka, Le Roux, Miller and Pauly (2019), who prove $\mathsf{BFT}_1 \equiv_{sW} \mathsf{IVT}$, the equivalence of $\mathsf{BFT}_n$ with $\mathsf{WKL}$ for $n \geq 2$, and the non-idempotency of connected choice; see Brattka, Gherardi and Pauly, Theorems 7.34, 7.35 and 8.3, Corollary 8.4 and Figure 2. The computable sequence of instances without computable sequence of solutions of :ref{#cor-ivt-parallel} is due to Pour-El and Richards (1989; see Brattka, Gherardi and Pauly, Corollary 8.4). In reverse mathematics, the intermediate value theorem is provable in $\mathsf{RCA}_0$ (Simpson, Theorem II.6.6), and the Brouwer fixed point theorem in dimension two is equivalent to $\mathsf{WKL}_0$ (Simpson, Theorem IV.7.7).

- K. Weihrauch, *Computable Analysis: An Introduction*, Springer, 2000, Section 6.3.
- V. Brattka and G. Gherardi, *Effective choice and boundedness principles in computable analysis*, Bulletin of Symbolic Logic 17 (2011), 73–117.
- V. Brattka, S. Le Roux, J. S. Miller and A. Pauly, *Connected choice and the Brouwer fixed point theorem*, Journal of Mathematical Logic 19 (2019), 1950004.
- V. Brattka, G. Gherardi and A. Pauly, *Weihrauch complexity in computable analysis*, in *Handbook of Computability and Complexity in Analysis*, Springer, 2021, 367–417.
- M. B. Pour-El and J. I. Richards, *Computability in Analysis and Physics*, Springer, 1989.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Sections 3.7 and 10.4.
- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009, Sections II.6 and IV.7.

:::::exercises
::::exercise{#ex-ivt-sign difficulty=1 objective="Remove the sign convention of the intermediate value theorem by a semi-decision of the sign of $f(0)$."}
Let $\mathsf{IVT}^\pm$ be the version of $\mathsf{IVT}$ with instances the $f \in C[0, 1]$ such that $f(0) \cdot f(1) < 0$. Show that $\mathsf{IVT}^\pm \equiv_{sW} \mathsf{IVT}$.

:::solution
$\mathsf{IVT}$ is a restriction of $\mathsf{IVT}^\pm$, so the identity functionals reduce it. Conversely, given $f$ with $f(0) f(1) < 0$, the value $f(0)$ is non-zero, and its sign is found by dovetailing the two semi-decision procedures of :ref{#prop-order-undecidable}. If $f(0) < 0$, pass $f$; otherwise pass $-f$, which has the same zeros. The backward functional is the identity.
:::
::::

::::exercise{#ex-ivt-nonstrict difficulty=1 objective="Remove the strict inequalities from the intermediate value theorem by extending the function linearly beyond the interval."}
Let $\mathsf{IVT}_{\leq}$ be the version of $\mathsf{IVT}$ with instances the $f \in C[0, 1]$ such that $f(0) \leq 0 \leq f(1)$. Show that $\mathsf{IVT}_{\leq} \equiv_{sW} \mathsf{IVT}$.

:::solution
$\mathsf{IVT}$ is a restriction of $\mathsf{IVT}_{\leq}$, so the identity functionals reduce it. Conversely, with $\kappa(u) = \min(1, \max(0, u))$, let
$$
g(t) = f(\kappa(3t - 1)) + \min(3t - 1, 0) + \max(3t - 2, 0), \qquad t \in [0, 1].
$$
Then $g(0) = f(0) - 1 < 0$ and $g(1) = f(1) + 1 > 0$. Let $u = 3t - 1 \in [-1, 2]$. If $u < 0$, then $g(t) = f(0) + u < 0$; if $u > 1$, then $g(t) = f(1) + u - 1 > 0$; if $u \in [0, 1]$, then $g(t) = f(u)$. So the zeros of $g$ are the points $t = (u + 1)/3$ with $f(u) = 0$, and the backward functional computes $u = 3t - 1$ from $t$ alone. If $(P_k)$ is a $\delta_C$-name of $f$, the functions obtained by replacing $f$ by $P_k$ in the definition of $g$ are rational polygons, with breakpoints at $1/3$, $2/3$ and the points $(b + 1)/3$ for the breakpoints $b$ of $P_k$, and they are at uniform distance at most $d(P_k, f)$ from $g$: they form a $\delta_C$-name of $g$. The same device is used in :ref{#thm-brouwer-one}.
:::
::::

::::exercise{#ex-ivt-polynomial difficulty=1 objective="Apply the trisection method to polynomials given by their coefficients."}
Show that there is an algorithm which, given $d$ and Cauchy names of reals $a_0, \dots, a_d$ such that the polynomial $f(x) = \sum_{i \leq d} a_i x^i$ satisfies $f(0) < 0 < f(1)$, computes a zero of $f$ in $[0, 1]$.

:::solution
The polynomial $f$ is not the zero polynomial, since $f(0) = a_0 < 0$, so it has at most $d$ zeros, and its zero set has empty interior. The algorithm of :ref{#thm-trisection} uses the instance only through its values $f(c)$ at rationals $c$, on which it runs the semi-decision procedures of :ref{#prop-order-undecidable} (2), and through the continuity of $f$ in the correctness proof. The values $f(c) = \sum_{i \leq d} a_i c^i$ are computed from the names of the coefficients by :ref{#thm-arithmetic-computable}, uniformly in $c$. Running the trisection with these values gives a Cauchy name of a zero of $f$.
:::
::::

::::exercise{#ex-ivt-monotone difficulty=1 objective="See that monotonicity alone does not make the intermediate value theorem computable, while strict monotonicity does."}
Show that the restriction of $\mathsf{IVT}$ to the non-decreasing functions has no continuous realizer, and that $\mathsf{LLPO}$ is strongly Weihrauch reducible to it. Compare with :ref{#ex-inverse-increasing}.

:::solution
The polygon $g_a$ has slopes $3(a + 1)$, $0$ and $3(1 - a)$ on its three pieces, so it is non-decreasing for $|a| \leq 1$. The proof of :ref{#thm-ivt-not-computable} only uses the functions $g_0$ and $g_a$ with $a = \pm 2^{-m}$, and names made of these polygons; the proof that $\mathsf{LLPO} \leq_{sW} \mathsf{IVT}$ in :ref{#thm-ivt-llpo-wkl} uses $g_a$ with $a \in \{ 0 \} \cup \{ \pm 2^{-n} : n \in \nat \}$, and names made of polygons $g_{a_k}$ with $|a_k| \leq 1$. All these functions are non-decreasing instances, so both proofs apply to the restriction without change. For strictly increasing functions, the zero is unique and is computed by :ref{#ex-inverse-increasing}, as $f^{-1}(0)$: the obstruction is the interval of zeros of $g_0$.
:::
::::

::::exercise{#ex-lpo-not-ivt difficulty=1 objective="Transfer a separation of weak König's lemma to the intermediate value theorem and to closed choice." lessons="closed-sets-and-choice"}
Show that $\mathsf{LPO} \not\leq_W \mathsf{IVT}$ and $\mathsf{LPO} \not\leq_W \mathsf C_{[0,1]}$.

:::solution
By :ref{#thm-ivt-llpo-wkl} and :ref{#thm-closed-choice-wkl}, $\mathsf{IVT} \leq_W \mathsf{WKL}$ and $\mathsf C_{[0,1]} \leq_W \mathsf{WKL}$. If $\mathsf{LPO} \leq_W \mathsf{IVT}$ or $\mathsf{LPO} \leq_W \mathsf C_{[0,1]}$, then $\mathsf{LPO} \leq_W \mathsf{WKL}$ by transitivity (:ref{#ex-w-transitive}, whose proof applies to problems on represented spaces, since they are problems on names). This contradicts :ref{#ex-lpo-not-wkl}. In words: a zero of a function, or a point of a closed set, never answers uniformly a $\Sigma^0_1$ question about the instance.
:::
::::

::::exercise[Connected choice reduces to the intermediate value theorem]{#ex-cc-ivt difficulty=3 objective="Build an instance of the intermediate value theorem whose zero set is a closed interval given by negative information." lessons="closed-sets-and-choice"}
Show that $\mathsf{CC}_{[0,1]} \leq_{sW} \mathsf{IVT}$, where $\mathsf{CC}_{[0,1]}$ is the restriction of $\mathsf C_{[0,1]}$ to the non-empty closed intervals $[a, b] \subseteq [0, 1]$. Proceed as follows: given a $\psi_>$-name $(c_i, d_i)_i$ of $A = [a, b]$, compute the side of $A$ on which each interval $(c_i, d_i)$ lies, and modify the function of :ref{#thm-zero-sets} (2) so that it is negative to the left of $A$ and positive to the right.

:::solution
Call $i$ *relevant* if $c_i < d_i$, $c_i < 1$ and $d_i > 0$, which is decidable; exactly the relevant intervals meet $[0, 1]$. For relevant $i$, the rational $e_i = (\max(c_i, 0) + \min(d_i, 1))/2$ lies in $(c_i, d_i) \cap [0, 1]$, hence not in $A$. Since $(c_i, d_i)$ is an interval disjoint from the interval $A$, it lies entirely to the left of $a$ or entirely to the right of $b$, on the same side as $e_i$.

*The side is computable.* If $e_i < a$, then $[0, e_i]$ is a compact set disjoint from $A$, so it is covered by finitely many intervals of the name; if $e_i > b$, the same holds for $[e_i, 1]$. Search, by :ref{#lem-effective-heine-borel} (1), for $n$ such that the first $n$ intervals cover $[0, e_i]$ or cover $[e_i, 1]$; the search terminates. If $[0, e_i]$ is covered, then $[0, e_i] \cap A = \emptyset$ and $e_i < a$, since $A \neq \emptyset$; let $s_i = -1$. Otherwise $[e_i, 1]$ is covered, $e_i > b$, and let $s_i = 1$. For $i$ not relevant, let $s_i = 0$.

*The function.* Let $h_i$ be the tent function of :ref{#thm-zero-sets} (2), positive exactly on $(c_i, d_i)$, with values in $[0, 1]$, and $f = \sum_i s_i\, 2^{-i-1} h_i$ on $[0, 1]$. The partial sums $F_n = \sum_{i < n} s_i\, 2^{-i-1} h_i$ are rational polygons, computed once $s_0, \dots, s_{n-1}$ are found, and $d(F_n, f) \leq 2^{-n}$; so $(F_n)$ is a $\delta_C$-name of $f$. If $x \in A$, then $h_i(x) = 0$ for every $i$, and $f(x) = 0$. If $x \in [0, a)$, then $x \notin A$, so $x$ lies in some $(c_i, d_i)$, and every interval of the name that contains $x$ lies to the left of $A$; so every non-zero term $s_i 2^{-i-1} h_i(x)$ is negative, at least one is non-zero, and $f(x) < 0$. Symmetrically, $f(x) > 0$ for $x \in (b, 1]$. So $f(0) \leq 0 \leq f(1)$, and the zero set of $f$ is $A$.

*Conclusion.* The function $f$ is an instance of $\mathsf{IVT}_{\leq}$ whose zeros are the points of $A$, so $\mathsf{CC}_{[0,1]} \leq_{sW} \mathsf{IVT}_{\leq}$, with the identity as backward functional, and $\mathsf{IVT}_{\leq} \equiv_{sW} \mathsf{IVT}$ by :ref{#ex-ivt-nonstrict}. This is the easier half of :ref{#fact-ivt-connected-choice} (1); the converse reduction, $\mathsf{IVT} \leq_{sW} \mathsf{CC}_{[0,1]}$, is the one admitted in the lesson.
:::
::::
:::::
