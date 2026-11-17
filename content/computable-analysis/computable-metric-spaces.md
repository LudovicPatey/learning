---
title: Computable metric spaces
summary: Computable metric spaces and their Cauchy representation; the space of continuous functions on the unit interval with the uniform metric, whose Cauchy names are equivalent to rectangle names.
duration: 20
prerequisites: [continuous-functions]
---

The previous lesson named a continuous function $f \in C[0, 1]$ by a list of rational rectangles that its graph does not leave, and computed from such a name a modulus of uniform continuity and the maximum value of $f$. This lesson gives a second kind of name, a sequence of rational polygons converging uniformly to $f$ at a fixed rate. It is an instance of a general construction. The Cauchy representation of $\mathbb R$ uses only a dense sequence, the rationals, and the computability of the distances between its terms; the same construction applies to every complete separable metric space with a dense sequence whose mutual distances are computable. The two kinds of names of continuous functions are equivalent, and the proof uses the modulus of the previous lesson.

## Definition and examples

:::definition{#def-computable-metric-space}
A **computable metric space** is a triple $(X, d, \alpha)$ where $(X, d)$ is a complete metric space and $\alpha : \nat \to X$ is a sequence with dense range such that the double sequence of reals $(d(\alpha(i), \alpha(j)))_{i,j}$ is computable. Its **Cauchy representation** $\delta_X$ is defined by $\delta_X(p) = x$ if $d(\alpha(p(k)), \alpha(p(l))) \leq 2^{-k}$ for all $k \leq l$ and $x = \lim_k \alpha(p(k))$. The points $\alpha(i)$ are the **rational points**, and the open balls $B(\alpha(i), r)$ with $r$ rational are the **rational balls**.
:::

:::example{#ex-computable-metric-spaces}
1. $\mathbb R$ with $|x - y|$ and an enumeration of $\mathbb Q$: the Cauchy representation is $\rho$. The same holds for $[0, 1]$ with an enumeration of $\mathbb Q \cap [0, 1]$, and for $\mathbb R^n$ with the Euclidean metric and rational vectors, whose Cauchy representation is equivalent to $\rho^n$.
2. Cantor space with $d(X, Y) = 2^{-n}$, $n$ least with $X(n) \neq Y(n)$, and $\alpha(i) = \sigma_i 0^\infty$, where $\sigma_i$ is the $i$-th binary string: the distances are rationals computed from $i$ and $j$. Its Cauchy representation is equivalent to the identity (:ref{#ex-cantor-cauchy}). Baire space is similar.
3. $C[0, 1]$ with the uniform metric $d(f, g) = \max_{x \in [0, 1]} |f(x) - g(x)|$, and an enumeration of the **rational polygons**: the continuous functions that are piecewise linear with finitely many rational breakpoints in $[0, 1]$, including $0$ and $1$, and rational values at the breakpoints. They are dense, since every continuous function on $[0, 1]$ is uniformly continuous; the distance between two rational polygons is a rational, the maximum of their difference over the union of their breakpoints, where the piecewise linear difference attains its extrema. We write $\delta_C$ for the Cauchy representation of $C[0, 1]$.
:::

## Cauchy names of continuous functions

In a computable metric space, the computable points are the limits of computable sequences of rational points converging at the rate $2^{-k}$, and the proof of :ref{#lem-cauchy-variants} shows again that a sequence of rational points with $d(\alpha(p(k)), x) \leq 2^{-k}$ can be turned into a name of $x$. A $\delta_C$-name of $f$ is a sequence of rational polygons $P_k$ with $d(P_k, P_l) \leq 2^{-k}$ for $k \leq l$, converging uniformly to $f$.

:::theorem{#thm-cauchy-rectangle}
$\delta_C \equiv \delta_\square$ on $C[0, 1]$.
:::

:::proof{of=thm-cauchy-rectangle}
($\delta_C \leq \delta_\square$) Let $(P_k)$ be a $\delta_C$-name of $f$, so that $|f(y) - P_k(y)| \leq 2^{-k}$ for every $y$. For every $k$ and every rational $a \in [0, 1]$ and rational $r > 0$, compute the minimum $c$ and the maximum $d$ of $P_k$ on $[a - r, a + r] \cap [0, 1]$, attained at the endpoints or at breakpoints, and list the rectangle $(a, r, (c + d)/2, (d - c)/2 + 2^{-k})$. It is valid for $f$: for $y \in [0, 1]$ with $|y - a| < r$, $|f(y) - (c + d)/2| \leq 2^{-k} + (d - c)/2$. Totality: given $x \in [0, 1]$ and $\varepsilon > 0$, choose $k$ with $2^{-k} < \varepsilon/2$; since $P_k$ is continuous, there is a rational $r > 0$ such that $P_k$ varies by less than $\varepsilon/2$ on $[x - 2r, x + 2r]$, and a rational $a \in [0, 1]$ with $|x - a| < r$; the rectangle listed for $(k, a, r)$ has height less than $\varepsilon/4 + 2^{-k} < \varepsilon$.

($\delta_\square \leq \delta_C$) From a $\delta_\square$-name of $f$, compute a modulus $\mu$ by :ref{#thm-modulus-max}. For each $k$, let $N = 2^{\mu(k+2)}$, compute rationals $c_j$ with $|c_j - f(j/N)| \leq 2^{-k-2}$ for $j \leq N$, and let $P_k$ be the rational polygon with values $c_j$ at the breakpoints $j/N$. For $x \in [j/N, (j+1)/N]$, $P_k(x)$ is a convex combination of $c_j$ and $c_{j+1}$, and $|c_i - f(x)| \leq |c_i - f(i/N)| + |f(i/N) - f(x)| \leq 2^{-k-1}$ for $i \in \{j, j+1\}$; so $d(P_k, f) \leq 2^{-k-1}$. Hence $d(P_k, P_l) \leq 2^{-k-1} + 2^{-l-1} \leq 2^{-k}$ for $k \leq l$, and $(P_k)$ is a $\delta_C$-name of $f$.
:::


From now on, $C[0, 1]$ is represented by $\delta_C$, or equivalently by $\delta_\square$. The computable points of $C[0, 1]$ are exactly the computable functions $f : [0, 1] \to \mathbb R$, and evaluation, the arithmetic operations applied pointwise, the maximum value and a modulus of uniform continuity are all computable on $C[0, 1]$.

:::quiz[the space of continuous functions]
In the proof that $\delta_\square \leq \delta_C$, why is the modulus computed before the polygon?

- [x] Because the grid $j/N$ must be fine enough that $f$ varies by at most $2^{-k-2}$ between consecutive points, and only a modulus gives such an $N$ from the name.
- [ ] Because evaluation at $j/N$ needs a modulus.

  Evaluation is computable from a rectangle name directly, by :ref{#thm-rectangle-computable}.
- [ ] Because rational polygons have rational breakpoints.

  The breakpoints $j/N$ are rational for every $N$; the question is which $N$ suffices.
:::

::::exercise{#ex-integral difficulty=1 objective="Compute the integral from a Cauchy name for the uniform metric."}
Show that the integral $f \mapsto \int_0^1 f(x)\, dx$ is $(\delta_C, \rho)$-computable.

:::solution
The integral of a rational polygon is a rational, computed by the trapezoid formula on each piece. If $(P_k)$ is a $\delta_C$-name of $f$, then $|\int_0^1 f - \int_0^1 P_k| \leq d(f, P_k) \leq 2^{-k}$, and :ref{#lem-cauchy-variants} gives a Cauchy name of the integral.
:::
::::

## Notes and references

Weihrauch, Section 6.1, shows the equivalence of the representation of $C[0, 1]$ by rectangles ("box properties", Definition 6.1.3), the Cauchy representation for the uniform metric (Definition 6.1.9, Lemma 6.1.10) and the representation by realizers; integration is his Theorem 6.4.1. Computable metric spaces are Weihrauch, Section 8.1 (Definition 8.1.2 and Example 8.1.3), and Brattka and Presser (2003) develop their theory.

- K. Weihrauch, *Computable Analysis: An Introduction*, Springer, 2000, Sections 6.1, 6.4 and 8.1.
- V. Brattka and G. Presser, *Computability on subsets of metric spaces*, Theoretical Computer Science 305 (2003), 43–76.

:::::exercises
::::exercise{#ex-cantor-cauchy difficulty=2 objective="Compare the Cauchy representation of Cantor space with its identity representation."}
Show that the Cauchy representation of Cantor space of :ref{#ex-computable-metric-spaces} is equivalent to the identity representation.

:::solution
Given $X$, the sequence $p(k) = $ the index of $(X \uh (k+1)) 0^\infty$ satisfies $d(\alpha(p(k)), X) \leq 2^{-k-1}$, so $d(\alpha(p(k)), \alpha(p(l))) \leq 2^{-k}$ for $k \leq l$, and $p$ is a name of $X$. Conversely, if $p$ is a name of $X$, then $d(\alpha(p(k)), X) \leq 2^{-k}$, so $\alpha(p(k))$ and $X$ agree on the positions $n < k$; hence $X(n)$ is the $n$-th bit of $\alpha(p(n+1))$, computed from $p$.
:::
::::

::::exercise{#ex-modulus-from-cauchy difficulty=1 objective="Compute a modulus of uniform continuity from a Cauchy name for the uniform metric, and locate the use of compactness."}
Show that a modulus of uniform continuity of $f \in C[0, 1]$ is computed from a $\delta_C$-name of $f$ without :ref{#lem-effective-heine-borel}, using the slopes of the polygons of the name.

:::solution
Let $(P_k)$ be a $\delta_C$-name of $f$, so that $d(P_k, f) \leq 2^{-k}$. Given $k$, let $P = P_{k+2}$, and let $L$ be $1$ plus the largest absolute value of the slopes of $P$, a positive rational computed from the breakpoints and values of $P$; then $|P(x) - P(y)| \leq L |x - y|$. Let $\mu(k)$ be least with $2^{-\mu(k)} \leq 2^{-k-1}/L$. If $|x - y| \leq 2^{-\mu(k)}$, then
$$
|f(x) - f(y)| \leq |f(x) - P(x)| + |P(x) - P(y)| + |P(y) - f(y)| \leq 2^{-k-2} + 2^{-k-1} + 2^{-k-2} = 2^{-k}.
$$
Compactness is used in :ref{#thm-cauchy-rectangle}, to pass from a rectangle name to a Cauchy name, and in the density of the rational polygons, which rests on the uniform continuity of continuous functions on $[0, 1]$.
:::
::::

::::exercise{#ex-max-prefix difficulty=2 objective="Combine a Cauchy name of a function with a Lipschitz bound on its polygons to compute a running maximum."}
Show that the function $(f, x) \mapsto \max_{y \in [0, x]} f(y)$, for $f \in C[0, 1]$ and $x \in [0, 1]$, is $([\delta_C, \rho], \rho)$-computable.

:::solution
Write $M_g(x) = \max_{y \in [0, x]} g(y)$ for $g \in C[0, 1]$. If $|g - h| \leq \varepsilon$ everywhere, then $|M_g(x) - M_h(x)| \leq \varepsilon$. If $P$ is a rational polygon with $|P(y) - P(y')| \leq L |y - y'|$, then for $x \leq x'$, $M_P(x') = \max(M_P(x), \max_{[x, x']} P)$ and $\max_{[x, x']} P \leq P(x) + L(x' - x) \leq M_P(x) + L (x' - x)$, so $|M_P(x') - M_P(x)| \leq L |x' - x|$. For a rational $x' \in [0, 1]$, $M_P(x')$ is the largest value of $P$ at $0$, at $x'$ and at the breakpoints in $[0, x']$, a rational computed exactly.

Given names $(P_j)$ of $f$ and $(q_j)$ of $x$, and $k$, let $P = P_{k+1}$ and $L$ a Lipschitz constant of $P$ as in :ref{#ex-modulus-from-cauchy}. Choose $j$ with $2^{-j} \leq 2^{-k-1}/L$, and let $x' = \min(1, \max(0, q_j))$; since $x \in [0, 1]$, $|x' - x| \leq |q_j - x| \leq 2^{-j}$. Output $r_k = M_P(x')$. Then
$$
|r_k - M_f(x)| \leq |M_P(x') - M_P(x)| + |M_P(x) - M_f(x)| \leq 2^{-k-1} + 2^{-k-1} = 2^{-k}.
$$
:::
::::

::::exercise{#ex-values-at-rationals difficulty=2 objective="See by a continuity argument that the values of a function at the rational points do not name it: a modulus of continuity is the missing information."}
Let $(r_i)_i$ be a computable enumeration of $\mathbb Q \cap [0, 1]$, and let $\delta_{\mathbb Q}$ be the representation of $C[0, 1]$ defined by $\delta_{\mathbb Q}(\langle p_0, p_1, \dots \rangle) = f$ if $p_i$ is a Cauchy name of $f(r_i)$ for every $i$. Show that $\delta_C \leq \delta_{\mathbb Q}$ and $\delta_{\mathbb Q} \not\leq_t \delta_C$.

:::solution
From a $\delta_C$-name $(P_k)$ of $f$, the rationals $P_k(r_i)$ satisfy $|P_k(r_i) - f(r_i)| \leq 2^{-k}$, so a Cauchy name of each $f(r_i)$ is computed, uniformly in $i$, by :ref{#lem-cauchy-variants}; this gives $\delta_C \leq \delta_{\mathbb Q}$.

Suppose that a continuous $F$ translates $\delta_{\mathbb Q}$ to $\delta_C$. Let $p = \langle p_0, p_1, \dots \rangle$ with every $p_i$ the constant name of $0$, a name of the function $0$. The term of index $2$ of $F(p)$ is a polygon $P$ with $d(P, 0) \leq 1/4$, and by continuity there is $m$ such that the term of index $2$ of $F(q)$ is $P$ for every $\delta_{\mathbb Q}$-name $q \in [p \uh m]$. Let $I$ be the finite set of $i$ such that $\langle i, n \rangle < m$ for some $n$. Choose rationals $0 \leq c < d \leq 1$ such that $(c, d)$ contains none of the points $r_i$, $i \in I$, and let $g$ be the tent function with $g = 0$ outside $(c, d)$ and $g((c+d)/2) = 1$. Let $q = \langle q_0, q_1, \dots \rangle$, with $q_i = p_i$ for $i \in I$, which is a name of $g(r_i) = 0$, and $q_i$ a Cauchy name of $g(r_i)$ for $i \notin I$. Then $q$ is a $\delta_{\mathbb Q}$-name of $g$ which agrees with $p$ below $m$, so $d(P, g) \leq 1/4$, and $d(g, 0) \leq d(g, P) + d(P, 0) \leq 1/2$, which contradicts $g((c+d)/2) = 1$.

The values at the rationals together with a modulus of uniform continuity name $f$ computably, by the remark after :ref{#thm-modulus-max}.
:::
::::

::::exercise{#ex-composition difficulty=2 objective="Compute composition on the space of continuous functions, using a modulus of uniform continuity of the outer function."}
Show that the composition $(f, g) \mapsto f \circ g$, for $f, g \in C[0, 1]$ with $g$ taking values in $[0, 1]$, is $([\delta_C, \delta_C], \delta_C)$-computable.

:::solution
Let $(P_j)$ and $(Q_j)$ be $\delta_C$-names of $f$ and $g$, and $\kappa(u) = \min(1, \max(0, u))$. Compute a modulus $\mu$ of $f$ (:ref{#ex-modulus-from-cauchy}). Given $k$, let $P = P_{k+2}$ and $Q = Q_{\mu(k+2)}$, and $R_k = P \circ \kappa \circ Q$. The function $\kappa \circ Q$ is piecewise linear, with values in $[0, 1]$, and its breakpoints are those of $Q$ and the rational points where $Q$ crosses $0$ or $1$; on each of its linear pieces, $P \circ \kappa \circ Q$ is linear between the rational preimages of the breakpoints of $P$. So $R_k$ is a rational polygon, computed from the names.

For $x \in [0, 1]$, $g(x) = \kappa(g(x))$ and $\kappa$ does not increase distances, so $|g(x) - \kappa(Q(x))| \leq |g(x) - Q(x)| \leq 2^{-\mu(k+2)}$. Hence
$$
\begin{aligned}
|f(g(x)) - R_k(x)| &\leq |f(g(x)) - f(\kappa(Q(x)))| + |f(\kappa(Q(x))) - P(\kappa(Q(x)))| \\
&\leq 2^{-k-2} + 2^{-k-2} = 2^{-k-1}.
\end{aligned}
$$
So $d(R_k, f \circ g) \leq 2^{-k-1}$, $d(R_k, R_l) \leq 2^{-k}$ for $k \leq l$, and $(R_k)$ is a $\delta_C$-name of $f \circ g$.
:::
::::
:::::
