---
title: Computable real functions
summary: Computable real functions are continuous, and continuous functions are those computable relative to an oracle; equality and order of reals are not decidable, only the strict order is semi-decidable; the arithmetic operations and effective limits are computable.
duration: 40
prerequisites: [representations, second-order-arithmetic/analysis-in-rca0]
---

A real function is computable if some algorithm transforms Cauchy names of the argument into Cauchy names of the value. The main theorem of this lesson is that such a function is continuous; conversely, every continuous function is computable relative to an oracle. Continuity is thus a necessary condition for computability, and discontinuity is the simplest obstruction: the sign function, the floor function and the test for equality are not computable. The arithmetic operations, the maximum and the limits of sequences with a known rate of convergence are computable, and with them most functions of elementary analysis.

## Computable real functions

:::definition{#def-computable-real-function}
A function $f :\subseteq \mathbb R^n \to \mathbb R$ is **computable** if it is $(\rho^n, \rho)$-computable, where $\rho$ is the Cauchy representation (:ref{#def-cauchy-representation}). A sequence $(x_i)_{i \in \nat}$ of reals is **computable** if it is a $\rho^\omega$-computable point: some computable function $i \mapsto p_i$ gives a Cauchy name $p_i$ of $x_i$, uniformly in $i$.
:::

A computable sequence of reals is more than a sequence of computable reals: the names must be computed by a single algorithm. The sequence $(x_e)$ of :ref{#ex-real-equality} is computable, while the set of $e$ with $x_e = 0$ is not: each real $x_e$ is either $0$ or a power of $2$, hence computable, but the information which is which is not available uniformly.

A realizer sees a real only through a finite part of a name at any time, and a finite part of a name says that the real lies in an interval (:ref{#fig-prefix-interval}). A string $\sigma = (q_0, \dots, q_{m-1})$ of rationals is a **valid prefix** if $|q_k - q_l| \leq 2^{-k}$ for all $k \leq l < m$; this is decidable. We write
$$
U_\sigma = \bigcap_{k < m} \left( q_k - 2^{-k},\ q_k + 2^{-k} \right),
$$
an open interval with rational endpoints computed from $\sigma$, possibly empty.

:::figure[A valid prefix $\sigma = (1, \tfrac12, \tfrac34, \tfrac58)$ and the open interval $U_\sigma = (\tfrac12, \tfrac34)$: every real of $U_\sigma$ has a Cauchy name beginning with $\sigma$.]{#fig-prefix-interval}
<svg class="fig" viewBox="0 0 640 260" width="640" role="img" aria-label="The open intervals of radius 2 to the minus k around the first four terms of a Cauchy name, and their intersection U sigma"><line x1="93.6" y1="30" x2="566.4" y2="30" class="ink-stroke" stroke-width="2"/><circle cx="93.6" cy="30" r="3.5" class="node"/><circle cx="566.4" cy="30" r="3.5" class="node"/><circle cx="330.0" cy="30" r="3" class="accent-fill"/><text x="330.0" y="21.0" text-anchor="middle" class="math" font-size="14">q<tspan class="mrm" font-size="9" dy="4">0</tspan></text><text x="30.0" y="35.0" text-anchor="start" class="mrm" font-size="12">k = 0</text><line x1="93.6" y1="68" x2="330.0" y2="68" class="ink-stroke" stroke-width="2"/><circle cx="93.6" cy="68" r="3.5" class="node"/><circle cx="330.0" cy="68" r="3.5" class="node"/><circle cx="211.8" cy="68" r="3" class="accent-fill"/><text x="211.8" y="59.0" text-anchor="middle" class="math" font-size="14">q<tspan class="mrm" font-size="9" dy="4">1</tspan></text><text x="30.0" y="73.0" text-anchor="start" class="mrm" font-size="12">k = 1</text><line x1="211.8" y1="106" x2="330.0" y2="106" class="ink-stroke" stroke-width="2"/><circle cx="211.8" cy="106" r="3.5" class="node"/><circle cx="330.0" cy="106" r="3.5" class="node"/><circle cx="270.9" cy="106" r="3" class="accent-fill"/><text x="270.9" y="97.0" text-anchor="middle" class="math" font-size="14">q<tspan class="mrm" font-size="9" dy="4">2</tspan></text><text x="30.0" y="111.0" text-anchor="start" class="mrm" font-size="12">k = 2</text><line x1="211.8" y1="144" x2="270.9" y2="144" class="ink-stroke" stroke-width="2"/><circle cx="211.8" cy="144" r="3.5" class="node"/><circle cx="270.9" cy="144" r="3.5" class="node"/><circle cx="241.4" cy="144" r="3" class="accent-fill"/><text x="241.4" y="135.0" text-anchor="middle" class="math" font-size="14">q<tspan class="mrm" font-size="9" dy="4">3</tspan></text><text x="30.0" y="149.0" text-anchor="start" class="mrm" font-size="12">k = 3</text><rect x="211.8" y="179" width="59.1" height="18" class="cell head-cell"/><text x="280.9" y="193.0" text-anchor="start" class="math" font-size="15">U<tspan class="mrm" font-size="10" dy="4">σ</tspan></text><line x1="93.6" y1="216" x2="93.6" y2="222" class="ink-stroke" stroke-width="1"/><text x="93.6" y="238.0" text-anchor="middle" class="mrm" font-size="12">0</text><line x1="211.8" y1="216" x2="211.8" y2="222" class="ink-stroke" stroke-width="1"/><text x="211.8" y="238.0" text-anchor="middle" class="mrm" font-size="12">0.5</text><line x1="330.0" y1="216" x2="330.0" y2="222" class="ink-stroke" stroke-width="1"/><text x="330.0" y="238.0" text-anchor="middle" class="mrm" font-size="12">1</text><line x1="448.2" y1="216" x2="448.2" y2="222" class="ink-stroke" stroke-width="1"/><text x="448.2" y="238.0" text-anchor="middle" class="mrm" font-size="12">1.5</text><line x1="566.4" y1="216" x2="566.4" y2="222" class="ink-stroke" stroke-width="1"/><text x="566.4" y="238.0" text-anchor="middle" class="mrm" font-size="12">2</text><line x1="64" y1="219" x2="596" y2="219" class="axis"/><line x1="211.8" y1="197" x2="211.8" y2="219" class="muted-stroke" stroke-dasharray="2 3"/><line x1="270.9" y1="197" x2="270.9" y2="219" class="muted-stroke" stroke-dasharray="2 3"/></svg>
:::

:::lemma{#lem-prefix-interval}
1. If $\sigma$ is a valid prefix and $y \in U_\sigma$, then $y$ has a Cauchy name extending $\sigma$.
2. Every real $x$ has a Cauchy name $p$ such that $x \in U_{p \uh m}$ for every $m$; this holds for every name with $|q_k - x| < 2^{-k}$ for all $k$.
:::

:::proof{of=lem-prefix-interval}
1. Let $\sigma = (q_0, \dots, q_{m-1})$ and $\varepsilon = \min_{k < m} (2^{-k} - |y - q_k|) > 0$. For $l \geq m$, choose rationals $q_l$ with $|q_l - y| \leq \min(\varepsilon, 2^{-l-1})$. For $k < m \leq l$, $|q_k - q_l| \leq |q_k - y| + \varepsilon \leq 2^{-k}$; for $m \leq l \leq l'$, $|q_l - q_{l'}| \leq 2^{-l-1} + 2^{-l'-1} \leq 2^{-l}$; and the conditions for $k \leq l < m$ hold since $\sigma$ is valid. So $(q_l)_l$ is a Cauchy name of $y$ extending $\sigma$.
2. Take rationals $q_k$ with $|q_k - x| \leq 2^{-k-1}$; then $|q_k - q_l| \leq 2^{-k-1} + 2^{-l-1} \leq 2^{-k}$ for $k \leq l$, and $x \in U_{p \uh m}$ for every $m$ since $|q_k - x| < 2^{-k}$.
:::

The same holds in $\mathbb R^n$, with products of such intervals. The lemma is a precise form of the remark that a finite part of a name only localizes the real in an open set.

## Continuity

:::theorem{#thm-real-continuous}
Every computable function $f :\subseteq \mathbb R^n \to \mathbb R$ is continuous on its domain.
:::

The idea: to output an approximation of $f(x)$ within $2^{-k}$, a realizer reads a finite part of a name of $x$, which every point of a small interval around $x$ shares with one of its own names. All these points receive the same approximation, so their values are close to $f(x)$.

:::proof{of=thm-real-continuous}
We give the proof for $n = 1$; for $n > 1$, replace intervals by products of intervals. Let $F$ be a computable realizer of $f$, let $x \in \dom f$ and $k \in \nat$. Let $p$ be a name of $x$ as in :ref{#lem-prefix-interval} (2). The term of index $k+1$ of $F(p)$ is a rational $r$ with $|r - f(x)| \leq 2^{-k-1}$. By continuity of $F$ (:ref{#thm-type2-continuous}), there is $m$ such that the term of index $k+1$ of $F(q)$ is $r$ for every name $q \in [p \uh m]$ of a point of $\dom f$. The set $U = U_{p \uh m}$ is an open interval containing $x$. If $y \in U \cap \dom f$, then $y$ has a name $q$ extending $p \uh m$ by :ref{#lem-prefix-interval} (1), and $F(q)$ is a name of $f(y)$ whose term of index $k+1$ is $r$, so $|r - f(y)| \leq 2^{-k-1}$. Hence $|f(y) - f(x)| \leq 2^{-k}$ for every $y \in U \cap \dom f$.
:::

:::quiz[the continuity of computable real functions]
In the proof of :ref{#thm-real-continuous}, why is a special name of $x$ chosen?

- [x] Because $x$ must belong to the open interval $U_{p \uh m}$, whatever $m$ is; for a name with $|q_k - x| = 2^{-k}$ for some $k$, the point $x$ would lie on the boundary of $U_{p \uh m}$, and the interval would not be a neighborhood of $x$.
- [ ] Because the realizer is defined only on special names.

  A realizer must work on every name; the special name is a choice made by the proof.
- [ ] Because other names of $x$ would give a different value $f(x)$.

  Every name of $x$ is mapped to a name of $f(x)$; the names of $f(x)$ may differ, the value may not.

---

Where is :ref{#lem-prefix-interval} (1) used?

- [x] To transfer the finite information $p \uh m$, which determines the output $r$, to the points $y$ near $x$: each such $y$ has a name with this prefix, so the realizer outputs $r$ on it.
- [ ] To show that $U_{p \uh m}$ is open.

  $U_{p \uh m}$ is an intersection of finitely many open intervals, open by definition.
- [ ] To show that $F(q)$ is defined.

  $F(q)$ is defined because $q$ is a name of a point of $\dom f$ and $F$ is a realizer.
:::

The converse holds relative to an oracle, as in :ref{#thm-continuous-relative}. The oracle used for real functions is a **code** in the sense of reverse mathematics: the set of rational rectangles that the graph of the function does not leave (:ref{#def-continuous-code}).

:::theorem{#thm-real-continuous-relative}
A function $f :\subseteq \mathbb R \to \mathbb R$ is continuous if and only if it is $(\rho, \rho)$-computable relative to some oracle.
:::

:::proof{of=thm-real-continuous-relative}
A function computable relative to an oracle has a realizer that is continuous (:ref{#thm-continuous-relative}), and the proof of :ref{#thm-real-continuous} uses only the continuity of the realizer; so $f$ is continuous.

Conversely, let $f$ be continuous, and let $A$ be the set of quadruples of rationals $(a, r, b, s)$, with $r, s > 0$, such that $|f(y) - b| \leq s$ for every $y \in \dom f$ with $|y - a| < r$. Given a name $(q_l)$ of $x \in \dom f$ and $k \in \nat$, search for $(a, r, b, s) \in A$ and $l$ with $|q_l - a| + 2^{-l} < r$ and $s \leq 2^{-k}$, and output $b$. Any pair found gives $|x - a| \leq |x - q_l| + |q_l - a| < r$, so $|f(x) - b| \leq 2^{-k}$, and :ref{#lem-cauchy-variants} turns the outputs into a Cauchy name of $f(x)$. The search terminates: by continuity there is $\delta > 0$ with $|f(y) - f(x)| \leq 2^{-k-1}$ for $y \in \dom f$ with $|y - x| < \delta$; choose rationals $a$ and $r$ with $|x - a| < r/2$ and $r \leq \delta/2$, so that $(a - r, a + r) \subseteq (x - \delta, x + \delta)$, and a rational $b$ with $|b - f(x)| \leq 2^{-k-2}$; then $(a, r, b, 2^{-k}) \in A$, and $|q_l - a| + 2^{-l} \leq |x - a| + 2^{-l+1} < r$ for $l$ large.
:::

For a function on $[0, 1]$, the set $A$ is a code of $f$ in the sense of :ref{#def-continuous-code}, and the realizer of the proof is the evaluation of :ref{to="second-order-arithmetic/analysis-in-rca0"}, made uniform in the name of $x$. The next lesson uses codes as names of continuous functions.

## Discontinuous functions and the order of the reals

By :ref{#thm-real-continuous}, a function that is discontinuous at a point of its domain is not computable. The sign function, the floor function $x \mapsto \lfloor x \rfloor$, and the characteristic function of $\{ 0 \}$ are not computable. The same holds for functions with values in $\nat$, represented by $\delta_\nat$, since $\nat$ embeds into $\mathbb R$ computably: equality and order of reals are not decidable.

:::proposition{#prop-order-undecidable}
1. No computable function $\mathbb R^2 \to \nat$ maps $(x, y)$ to $1$ if $x < y$ and to $0$ otherwise; the same holds for $x = y$ and for $x \leq y$.
2. There is a Turing functional $\Phi$ such that, for every name $p$ of $(x, y) \in \mathbb R^2$, $\Phi^p(0)$ converges if and only if $x < y$.
:::

:::proof{of=prop-order-undecidable}
1. Such a function is not continuous at $(0, 0)$: its value there is $0$ (respectively $1$ for $=$ and $\leq$), and every neighborhood of $(0, 0)$ contains points $(0, \varepsilon)$ or $(\varepsilon, 0)$ where the value differs. A computable function with values in $\nat$ is continuous by the argument of :ref{#thm-real-continuous}.
2. With names $(q_k)$ of $x$ and $(p_k)$ of $y$, search for $k$ with $q_k + 2^{-k} < p_k - 2^{-k}$. If such a $k$ is found, then $x \leq q_k + 2^{-k} < p_k - 2^{-k} \leq y$. Conversely, if $x < y$, choose $k$ with $2^{-k+2} < y - x$; then $q_k + 2^{-k} \leq x + 2^{-k+1} < y - 2^{-k+1} \leq p_k - 2^{-k}$.
:::

Item 2 is the effective counterpart of the fact that $x < y$ is a $\Sigma^0_1$ property of codes in $\mathsf{RCA}_0$, and item 1 of the fact that equality is not $\Sigma^0_1$ (:ref{#ex-real-equality}). Item 1 does not depend on the Cauchy representation: equality and order are undecidable for every representation of $\mathbb R$ (Weihrauch, Theorem 4.1.16).

Restricting the domain can restore computability: the sign function is computable on $\mathbb R \setminus \{ 0 \}$, by a search for $k$ with $|q_k| > 2^{-k}$, which exists when $x \neq 0$.

::::exercise{#ex-positive-search difficulty=2 objective="Semi-decide the positivity of a computable function, and find a rational point where it does not vanish."}
Let $f : \mathbb R \to \mathbb R$ be computable. Show that there is a Turing functional $\Phi$ such that, for every name $p$ of $x$, $\Phi^p(0)$ converges if and only if $f(x) > 0$. Deduce that if $f$ is computable and $f(x_0) \neq 0$ for some $x_0$, then $f(q) \neq 0$ for some rational $q$, and such a $q$ can be found by an algorithm.

:::solution
Compose a realizer of $f$ with the functional of :ref{#prop-order-undecidable} (2), applied to the pair $(0, f(x))$: on a name $p$ of $x$, it searches for $k$ such that the term of index $k$ of the name of $f(x)$ exceeds $2^{-k+1}$. For the second part, $f$ is continuous, so $f \neq 0$ on an open interval around $x_0$, which contains a rational. An algorithm dovetails the computations of the functionals for $f(q) > 0$ and $-f(q) > 0$ over all rationals $q$, with their constant names, and stops at the first one that converges.
:::
::::

## Arithmetic and limits

:::theorem{#thm-arithmetic-computable}
The following functions are computable:
1. the constant functions with a computable value, and the projections $\mathbb R^n \to \mathbb R$;
2. $x \mapsto -x$, $(x, y) \mapsto x + y$, $(x, y) \mapsto xy$, $(x, y) \mapsto \max(x, y)$, $(x, y) \mapsto \min(x, y)$, $x \mapsto |x|$;
3. $x \mapsto 1/x$ on $\mathbb R \setminus \{ 0 \}$.
:::

:::proof{of=thm-arithmetic-computable}
Let $(q_k)$ and $(p_k)$ be names of $x$ and $y$. By :ref{#lem-cauchy-variants}, it suffices to compute rationals $r_k$ within $2^{-k}$ of the value.
1. Immediate.
2. For $-x$, take $r_k = -q_k$; for $x + y$, $r_k = q_{k+1} + p_{k+1}$. For the maximum, $r_k = \max(q_k, p_k)$, since $|\max(a, b) - \max(a', b')| \leq \max(|a - a'|, |b - b'|)$; similarly for the minimum, and $|x| = \max(x, -x)$. For the product, let $A = |q_0| + 2$ and $B = |p_0| + 2$, so that $|x| \leq A$ and $|p_j| \leq B$ for every $j$. Then
$$
|xy - q_j p_j| \leq |x|\, |y - p_j| + |p_j|\, |x - q_j| \leq (A + B)\, 2^{-j},
$$
and $r_k = q_j p_j$, with $j$ least such that $(A + B)\, 2^{-j} \leq 2^{-k}$, works.
3. Let $x \neq 0$. Search for $j_0$ with $|q_{j_0}| > 3 \cdot 2^{-j_0}$; it exists since $q_j \to x \neq 0$ and $3 \cdot 2^{-j} \to 0$. Let $c = 2^{-j_0}$. Then $|x| \geq |q_{j_0}| - 2^{-j_0} > 2c$, and for $j \geq j_0$, $|q_j| \geq |x| - 2^{-j} > c$. For such $j$, $|1/x - 1/q_j| = |q_j - x| / (|x|\, |q_j|) \leq 2^{-j}/c^2$, and $r_k = 1/q_j$, with $j \geq j_0$ such that $2^{-j} \leq c^2\, 2^{-k}$, works.
:::

Each algorithm uses bounds read from the name; for the inverse, the bound is found by a search that terminates only because $x \neq 0$. The computable reals form a field, and the computable sequences of reals are closed under the same operations, termwise.

The limit of a sequence is computable when a rate of convergence is known. This is the uniform content of :ref{#prop-rca-complete}.

:::proposition{#prop-effective-limit}
The function $\lim$, defined on the sequences of reals $(x_n)$ with $|x_n - x_m| \leq 2^{-n}$ for all $n \leq m$, is $(\rho^\omega, \rho)$-computable.
:::

:::proof{of=prop-effective-limit}
Let $(q_{n,k})_k$ be the given name of $x_n$. The proof of :ref{#prop-rca-complete} shows that the sequence $p_k = q_{k+2, k+2}$ is a Cauchy name of the limit, and it is computed from the names of the $x_n$ by a fixed algorithm.
:::

Together with :ref{#thm-arithmetic-computable}, this makes the functions defined by power series with a computable bound on the tail computable: the exponential, sine and cosine on $\mathbb R$, the logarithm on $(0, \infty)$, and so on (Weihrauch, Section 4.3). Without a rate of convergence, the limit is not computable: a Specker sequence (:ref{#prop-specker}) is a computable sequence of rationals with a non-computable limit. The last lesson of the course measures exactly how far from computable the limit operation is.

:::quiz[arithmetic on Cauchy names]
In the proof of :ref{#thm-arithmetic-computable} (3), why does the search for $j_0$ terminate only when $x \neq 0$?

- [x] Because $|q_j|$ converges to $|x|$, which exceeds $3 \cdot 2^{-j}$ for large $j$ only when $|x| > 0$; for $x = 0$ the inequality $|q_j| > 3 \cdot 2^{-j}$ never holds, since $|q_j| \leq 2^{-j}$.
- [ ] Because $1/x$ is not computable.

  It is computable on its domain $\mathbb R \setminus \{0\}$; the search is the reason why the domain matters.
- [ ] Because the name of $x$ might be finite.

  Names are infinite sequences; the issue is the bound on $|x|$.

---

In the proof of the product, what is $B$ for?

- [x] To bound $|p_j|$ independently of $j$, so that the error $|p_j|\,|x - q_j|$ is controlled by $2^{-j}$ times a constant read from the names.
- [ ] To bound the number of steps of the algorithm.

  The algorithm takes the least $j$ satisfying a computable inequality; $B$ bounds the error, not the time.
- [ ] To ensure that $y \neq 0$.

  The product is defined everywhere.
:::

::::exercise{#ex-exp difficulty=2 objective="Compute a function given by a power series from an explicit bound on its tail."}
Show that the exponential function is computable on $\mathbb R$.

:::solution
Given a name of $x$, compute an integer $M \geq |x|$, for instance $M = \lceil |q_0| \rceil + 1$. For $n \geq 2M$, the tail satisfies $\sum_{i > n} |x|^i / i! \leq \frac{M^{n+1}}{(n+1)!} \sum_{j \geq 0} 2^{-j} \leq 2 \frac{M^{n+1}}{(n+1)!}$, since successive terms decrease by a factor at most $M / (n+2) \leq 1/2$; this bound tends to $0$ and is computable. Let $n_k \geq 2M$ be least with $2 M^{n_k+1}/(n_k + 1)! \leq 2^{-k-1}$, and $s_k$ the partial sum $\sum_{i \leq n_k} x^i / i!$, computable from the name of $x$ by :ref{#thm-arithmetic-computable}. Then $|s_k - e^x| \leq 2^{-k-1}$, so $|s_k - s_l| \leq 2^{-k}$ for $k \leq l$, and :ref{#prop-effective-limit} computes $e^x = \lim_k s_k$, uniformly in the name of $x$.
:::
::::

## Notes and references

Computable real functions and their continuity are Weihrauch, Section 4.3: Theorem 4.3.1 (continuity) and Theorem 4.3.2 (the arithmetic operations, minimum, maximum and absolute value), with limits in Theorem 4.3.7 and power series in Theorem 4.3.11. The undecidability of equality and order for every representation is Theorem 4.1.16. The characterization of continuous functions by relative computability follows from the admissibility of $\rho$ (Weihrauch, Section 3.2); the proof given here uses codes of continuous functions as oracles, as in reverse mathematics (Simpson, Section II.6). The definition of computable real functions by Grzegorczyk (1955) and Lacombe (1955) is equivalent to the one given here; Pour-El and Richards define the computable functions on a compact interval by sequential computability and a computable modulus of uniform continuity (their Chapter 0); the equivalence with the definition given here follows from the next lesson (see also Weihrauch, Section 9.3).

- K. Weihrauch, *Computable Analysis: An Introduction*, Springer, 2000, Sections 3.2, 4.1 and 4.3.
- V. Brattka, P. Hertling and K. Weihrauch, *A tutorial on computable analysis*, in *New Computational Paradigms*, Springer, 2008, 425–491.
- M. B. Pour-El and J. I. Richards, *Computability in Analysis and Physics*, Springer, 1989, Chapter 0.
- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009, Section II.6.

:::::exercises
::::exercise{#ex-floor difficulty=1 objective="Restore computability by restricting the domain, and recognize discontinuity as the obstruction."}
Show that the floor function is computable on $\mathbb R \setminus \mathbb Z$, and not on any interval containing an integer in its interior.

:::solution
Given a name $(q_k)$ of $x \notin \mathbb Z$, search for $k$ and an integer $n$ with $n < q_k - 2^{-k}$ and $q_k + 2^{-k} < n + 1$; this exists since $x$ lies strictly between two consecutive integers, and then $n < x < n + 1$. Output the constant name of $n$. If $I$ is an interval containing an integer $n$ in its interior, the floor function restricted to $I$ is discontinuous at $n$, since it takes the value $n - 1$ immediately to the left of $n$; so it is not computable by :ref{#thm-real-continuous}.
:::
::::

::::exercise{#ex-sqrt difficulty=1 objective="Compute a function that is not Lipschitz, by reading the input with a precision adapted to its modulus of continuity."}
Show that $x \mapsto \sqrt x$ is computable on $[0, \infty)$. Use the inequality $|\sqrt a - \sqrt b| \leq \sqrt{|a - b|}$ for $a, b \geq 0$, and prove it.

:::solution
For $a \geq b \geq 0$, $(\sqrt b + \sqrt{a - b})^2 = a + 2 \sqrt{b (a - b)} \geq a$, so $\sqrt a - \sqrt b \leq \sqrt{a - b}$; the case $b \geq a$ is symmetric.

Let $(q_j)$ be a Cauchy name of $x \geq 0$, and $k \in \nat$. Let $s = \max(q_{2k+2}, 0)$. Since $x \geq 0$ and $u \mapsto \max(u, 0)$ does not increase distances, $|s - x| \leq |q_{2k+2} - x| \leq 2^{-2k-2}$, hence $|\sqrt s - \sqrt x| \leq 2^{-k-1}$. Let $r_k$ be the largest multiple of $2^{-k-1}$ with $r_k^2 \leq s$, found by a finite search as in :ref{#ex-computable-reals} (2); then $0 \leq \sqrt s - r_k < 2^{-k-1}$. So $|r_k - \sqrt x| \leq 2^{-k}$, and :ref{#lem-cauchy-variants} gives a Cauchy name of $\sqrt x$. Near $0$, an output precision $2^{-k}$ requires the input precision $2^{-2k-2}$: the precision read from the name depends on the modulus of continuity of the function.
:::
::::

::::exercise[Overlapping conditions]{#ex-overlapping-choice difficulty=2 objective="See that a choice between two overlapping conditions is computable on names, while no such choice depends only on the real."}
1. Show that there is a Turing functional $\Phi$ such that, for every Cauchy name $p$ of a real $x$, $\Phi^p(0)$ converges to $0$ or $1$, with $x < 1$ if the output is $0$, and $x > 0$ if the output is $1$.
2. Show that for every such $\Phi$, some real has two names on which $\Phi$ gives different outputs.

:::solution
1. On a name $p$ of $x$, run the two semi-decision procedures of :ref{#prop-order-undecidable} (2) for $x < 1$ and for $0 < x$, using the constant names of $0$ and $1$, alternately step by step. Output $0$ if the first terminates first, and $1$ otherwise. Every real satisfies $x < 1$ or $x > 0$, so one of them terminates, and the output satisfies the required condition.
2. Suppose that $\Phi^p(0)$ depends only on the real $x$ named by $p$, and let $f(x)$ be this value. Then $f : \mathbb R \to \nat$ is computable, realized by the functional that outputs $\Phi^p(0)$, hence continuous by the argument of :ref{#thm-real-continuous}, as in :ref{#prop-order-undecidable} (1). But $f(x) = 0$ for $x \leq 0$ and $f(x) = 1$ for $x \geq 1$, and a continuous function from $\mathbb R$ to $\nat \subseteq \mathbb R$ is constant, by the intermediate value theorem. So the output depends on the name. Such choices, where a realizer may give different correct answers on different names of the same input, are the reason why the problems studied later in the course are allowed to have several solutions.
:::
::::

::::exercise{#ex-sup-left-ce difficulty=2 objective="Compute the supremum of a bounded sequence from below, and show by a continuity argument that no realizer computes it from both sides." lessons="representations"}
1. Show that the map $(x_n) \mapsto \sup_n x_n$, defined on the bounded sequences of reals, is $(\rho^\omega, \rho_<)$-computable. Deduce that the supremum of a bounded computable sequence of reals is left-c.e.
2. Show that it is not $(\rho^\omega, \rho)$-continuous, even on the sequences with values in $\{0, 1\}$.

:::solution
1. Let $(q_{n,k})_k$ be the given name of $x_n$, and $x = \sup_n x_n$. For a rational $q$, $q < x$ if and only if $q < x_n$ for some $n$, if and only if $q < q_{n,k} - 2^{-k}$ for some $n$ and $k$: if $q < q_{n,k} - 2^{-k}$ then $q < x_n$, since $q_{n,k} - 2^{-k} \leq x_n$; and if $q < x_n$, choose $k$ with $2^{-k+1} < x_n - q$, so that $q_{n,k} - 2^{-k} \geq x_n - 2^{-k+1} > q$. A dovetailed search over the triples $(q, n, k)$ lists these rationals, which is a left name of $x$. A computable sequence has a computable name, and the algorithm turns it into a computable left name.
2. Suppose that a continuous $F$ maps $\rho^\omega$-names of bounded sequences to Cauchy names of their suprema. Let $p = \langle p_0, p_1, \dots \rangle$ with every $p_i$ the constant name of $0$. The term of index $2$ of $F(p)$ is a rational $r$ with $|r| \leq 1/4$, and by continuity there is $m$ such that the term of index $2$ of $F(q)$ is $r$ for every name $q \in [p \uh m]$ of a bounded sequence. The positions below $m$ are of the form $\langle i, n \rangle$ for finitely many $i$; choose $i_0$ different from all of them, and let $q$ be the name obtained from $p$ by replacing $p_{i_0}$ with the constant name of $1$. It agrees with $p$ below $m$ and names a sequence with values in $\{0, 1\}$ and supremum $1$, so $|r - 1| \leq 1/4$, a contradiction.

Part 1 is adapted from Weihrauch 2000, Exercise 4.2.11. The same continuity argument shows that the limit of a non-decreasing sequence is not computable, which the last lesson of the course classifies.
:::
::::

::::exercise{#ex-dedekind-cut difficulty=1 objective="Relate computable reals to decidable Dedekind cuts, and see that the equivalence is not uniform." lessons="representations"}
Show that a real $x$ is computable if and only if the set $L_x = \{ q \in \mathbb Q : q < x \}$ is decidable. Show that no Turing functional computes the characteristic function of $L_x$ from every Cauchy name of $x$.

:::solution
If $x$ is rational, $L_x$ is decidable, by comparing rationals. If $x$ is computable and irrational, then for every rational $q$ exactly one of $q < x$ and $x < q$ holds, and both are semi-decidable from the constant name of $q$ and a computable name of $x$ (:ref{#prop-order-undecidable} (2)); running both procedures alternately decides $q < x$. Conversely, if $L_x$ is decidable, then for each $k$ the integer $j$ with $j 2^{-k} \in L_x$ and $(j+1) 2^{-k} \notin L_x$ is found by testing $j = 0, -1, 1, -2, 2, \dots$; it exists and is unique, and $x - 2^{-k} \leq j 2^{-k} < x$, so these rationals give a Cauchy name of $x$ by :ref{#lem-cauchy-variants}.

A functional computing $L_x$ from all names of $x$ would in particular decide $0 < x$ from the names of $x$, uniformly, which :ref{#prop-order-undecidable} (1) excludes. The proof of the first part distinguishes whether $x$ is rational, and this case distinction is not effective.
:::
::::

::::exercise[A rate of convergence cannot always be computed]{#ex-modulus-convergence difficulty=2 objective="See when a computable null sequence has a computable modulus of convergence, and build one that has none."}
A **modulus of convergence** of a sequence $(a_k)$ converging to $0$ is a function $m : \nat \to \nat$ with $|a_k| \leq 2^{-n}$ for all $k \geq m(n)$.
1. Show that a computable non-increasing sequence of reals converging to $0$ has a computable modulus of convergence.
2. Let $g : \nat \to \nat$ be a computable injective function whose range $A$ is not computable. Show that the computable sequence $b_k = 2^{-g(k)}$ converges to $0$ and has no computable modulus of convergence.

:::solution
1. A non-increasing sequence converging to $0$ has non-negative terms. Given $n$, search for $k$ with $a_k < 2^{-n}$, by running the semi-decision procedures of :ref{#prop-order-undecidable} (2) for the pairs $(a_k, 2^{-n})$, $k \in \nat$, in parallel, using the computable names of the $a_k$; such a $k$ exists since $a_k \to 0$. Let $m(n)$ be the first $k$ found. For $k' \geq m(n)$, $0 \leq a_{k'} \leq a_{m(n)} < 2^{-n}$.
2. Since $g$ is injective, for each $n$ only finitely many $k$ satisfy $g(k) \leq n$, so $b_k < 2^{-n}$ for $k$ large: $b_k \to 0$. Suppose that $m$ is a computable modulus. For $k \geq m(n+1)$, $2^{-g(k)} \leq 2^{-n-1}$, that is, $g(k) > n$. So $n \in A$ if and only if $n = g(k)$ for some $k < m(n+1)$, a finite and computable check; this makes $A$ computable, a contradiction.

Without a modulus, :ref{#prop-effective-limit} does not apply, even when the limit is known to be $0$. Adapted from Weihrauch 2000, Exercise 4.2.4.
:::
::::
:::::
