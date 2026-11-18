---
title: Continuous degrees
summary: Points of computable metric spaces compared by uniform computation of names (Miller); the points of the Hilbert cube embed into the enumeration degrees; points of Cantor space and of the reals have total degrees; nontotal continuous degrees exist; the continuous degrees are the almost total degrees and are definable; represented spaces, where the Sierpiński space gives all enumeration degrees.
duration: 25
prerequisites: [definability-and-automorphisms, computable-analysis/computable-metric-spaces, enumeration-reducibility/selman-theorem]
---

A real number has a Turing degree: the degree of its Dedekind cut, or of any of its fast Cauchy sequences. Pour-El and Lempp asked whether the same holds for continuous functions on the reals, or for points of other natural spaces. Miller answered with a new degree structure, the continuous degrees, and showed that it sits inside the enumeration degrees, strictly between the total degrees and all degrees. This lesson defines the continuous degrees, proves the embedding into $\mathcal D_e$, and states the characterization of Andrews, Igusa, Miller and Soskova that makes them first-order definable. It ends with the general framework of represented spaces, in which the enumeration degrees appear as the degrees of points of a simple non-metrizable space.

## Names and the continuous degrees

Recall from the course on computable analysis that a computable metric space is a metric space $M$ with a dense sequence $(q_n)$ on which the distance is computable (:ref{#def-computable-metric-space}). A **name** of a point $x \in M$ is a function $\lambda$ such that $d(x, q_{\lambda(k)}) < 2^{-k}$ for every $k$.

:::definition[Miller]{#def-continuous-reducibility}
For points $x$ and $y$ of computable metric spaces, $x \leq_r y$ if there is a Turing functional that computes a name of $x$ from every name of $y$. The equivalence classes are the **continuous degrees**.
:::

Miller showed that two spaces are universal: every continuous degree contains a point of the Hilbert cube $[0, 1]^\nat$, and a point of $C[0, 1]$. For a point $\alpha$ of the Hilbert cube, let
$$
C_\alpha = \bigoplus_{i \in \nat} \big( \{ q \in \mathbb Q : q < \alpha(i) \} \oplus \{ q \in \mathbb Q : q > \alpha(i) \} \big),
$$
with rationals coded by numbers.

:::proposition[Miller]{#prop-continuous-embedding}
For points $\alpha$ and $\beta$ of the Hilbert cube, $\alpha \leq_r \beta$ if and only if $C_\alpha \leq_e C_\beta$. So $\alpha \mapsto \deg_e(C_\alpha)$ embeds the continuous degrees into the enumeration degrees.
:::

:::proof{of=prop-continuous-embedding}
We show that enumerations of $C_\alpha$ and names of $\alpha$ can be converted into each other uniformly. The statement follows. If $C_\alpha \leq_e C_\beta$, a name of $\beta$ gives an enumeration of $C_\beta$, hence of $C_\alpha$, hence a name of $\alpha$, uniformly. Conversely, if $\alpha \leq_r \beta$, every set computing an enumeration of $C_\beta$ computes a name of $\beta$, hence of $\alpha$, hence an enumeration of $C_\alpha$; by Selman's theorem (:ref{#thm-selman}), $C_\alpha \leq_e C_\beta$.

From a name of $\alpha$, enumerate $C_\alpha$: with the usual metric of the Hilbert cube, a name gives, for each $i$ and $k$, a rational $r$ with $|r - \alpha(i)| < 2^{-k}$, computably. Enumerate $q$ in the left part of coordinate $i$ when $q < r - 2^{-k}$ for such an approximation $r$, and in the right part when $q > r + 2^{-k}$. Every $q < \alpha(i)$ is eventually enumerated, once $2^{-k+1} < \alpha(i) - q$, and nothing wrong is.

From an enumeration of $C_\alpha$, compute a name: to approximate $\alpha(i)$ within $\varepsilon$, wait until rationals $q$ and $q'$ with $q' - q < \varepsilon$ appear in the left and the right parts of coordinate $i$; then $q < \alpha(i) < q'$, and $q$ is within $\varepsilon$. Such rationals exist and are eventually enumerated. Finitely many coordinates determine a point of the Hilbert cube up to any given precision, so this gives a name.
:::

For a real $x \in [0, 1]$, the set $\{ q : q < x \} \oplus \{ q : q > x \}$ is total: its complement is the same pair of sets, exchanged, together with $x$ itself if $x$ is rational, which is computable. So the continuous degree of a real, and similarly of a point of Cantor space or Baire space, is total, the image of its Turing degree. The question of Pour-El and Lempp becomes: is every continuous degree total?

:::theorem[Miller]{#thm-nontotal-continuous}
There is a continuous degree that is not total.
:::

We admit the theorem. All known proofs use topology: Miller used a fixed point theorem for multivalued functions on an infinite-dimensional space; Day and Miller gave a proof through neutral measures; Kihara and Pauly, and independently Hoyrup, used the fact that the Hilbert cube is not a countable union of finite-dimensional spaces. Miller also proved that no continuous degree is quasi-minimal. So the continuous degrees lie strictly between the total degrees and all degrees.

## The almost total degrees

:::theorem[Andrews, Igusa, Miller, Soskova]{#thm-almost-total}
An enumeration degree $\mathbf a$ is continuous if and only if it is **almost total**: for every total degree $\mathbf x \not\leq \mathbf a$, the degree $\mathbf a \vee \mathbf x$ is total.
:::

We admit the theorem; its proof uses an effective version of Urysohn's metrization theorem due to Schröder. Since the total degrees are definable (:ref{#thm-totality-definable}), the condition "almost total" is first-order, and the continuous degrees are definable in $\mathcal D_e$. Ganchev, Kalimullin, Miller and Soskova gave another definition, without totality: a degree is continuous if and only if it is not half of a nontrivial relativized K-pair. Their result is a dichotomy: for every degree $\mathbf a$, either $\mathbf a$ is continuous, or there is a total degree $\mathbf x \not\leq \mathbf a$ such that $\mathbf a \vee \mathbf x$ is a strong quasi-minimal cover of $\mathbf x$.

Miller related nontotal continuous degrees to PA degrees: for total degrees $\mathbf a$ and $\mathbf b$, $\mathbf a$ is PA above $\mathbf b$ (it computes a path through every infinite $\mathbf b$-computable binary tree) if and only if there is a nontotal continuous degree $\mathbf c$ with $\mathbf b < \mathbf c < \mathbf a$. With the definability of the continuous degrees, the relation "PA above" on the image of the Turing degrees is definable in $\mathcal D_e$.

:::quiz[continuous degrees]
In :ref{#prop-continuous-embedding}, why does an enumeration of $C_\alpha$ give arbitrarily good approximations of $\alpha(i)$?

- [x] Every rational below $\alpha(i)$ and every rational above it is eventually enumerated, so pairs bracketing $\alpha(i)$ as closely as needed appear.
- [ ] Because $C_\alpha$ is total.

  $C_\alpha$ need not be total; the argument only uses the positive information that it contains.
- [ ] Because the enumeration lists the rationals in increasing order.

  An enumeration may list them in any order; one waits for a good pair.

---

Why is the continuous degree of a real number total?

- [x] The complement of $\{ q : q < x \} \oplus \{ q : q > x \}$ is the same two sets exchanged, plus possibly the rational $x$, so the set is enumeration reducible to its complement and conversely.
- [ ] Because every real is computable in some set.

  That is true of every point; totality comes from the complement being enumerable.
- [ ] Because the Hilbert cube is compact.

  Compactness is not used; one coordinate suffices for a real.
:::

## Represented spaces

Kihara and Pauly proposed to study the degrees of points of second countable spaces in general. A **represented space** is a second countable topological space with a listing $(B_i)$ of a base; a name of a point $x$ is an enumeration of $N_x = \{ i : x \in B_i \}$, and $x \leq y$ if every name of $y$ uniformly computes a name of $x$, that is, $N_x \leq_e N_y$. Each space $X$ gives a class $\mathcal D_X$ of enumeration degrees.

:::proposition{#prop-sierpinski}
Let $\mathbb S = \{ 0, 1 \}$ with the open sets $\emptyset$, $\{ 1 \}$, $\{ 0, 1 \}$ (the Sierpiński space), and $\mathbb S^\nat$ the product, with the base of the sets $U_u = \{ x : x(n) = 1 \text{ for all } n \in D_u \}$. Then every enumeration degree is the degree of a point of $\mathbb S^\nat$. With the discrete space $\{ 0, 1 \}$ instead, the product $2^\nat$ gives exactly the total degrees.
:::

:::proof{of=prop-sierpinski}
Identify a point $x \in \mathbb S^\nat$ with the set $A = \{ n : x(n) = 1 \}$. Then $N_x = \{ u : D_u \subseteq A \}$, and $N_x \equiv_e A$: $A$ is enumerated from $N_x$ by the singletons, and $N_x$ from $A$ by the axioms $\langle u, u \rangle$. So $\mathcal D_{\mathbb S^\nat}$ is the set of all enumeration degrees. In $2^\nat$, a base is given by the cylinders, and the name of $x$ enumerates the prefixes of $x$, which is enumeration equivalent to $A \oplus \overline A$; so the degrees are the total ones.
:::

The Hilbert cube gives the continuous degrees, the reals with the lower topology the degrees of semi-computable sets, and Kihara, Ng and Pauly studied many other spaces; the cototal degrees are the degrees of points of computable $G_\delta$ spaces. Each such class is a candidate for first-order definability in $\mathcal D_e$.

::::exercise{#ex-cantor-total difficulty=1 objective="Compute the degree of a point of Cantor space as a represented space."}
For $X \in 2^\nat$, show directly that the set of prefixes of $X$ is enumeration equivalent to $X \oplus \overline X$.

:::solution
From an enumeration of the prefixes of $X$, enumerate $2n$ when a prefix of length $n + 1$ ending with $1$ appears, and $2n + 1$ when one ending with $0$ appears: this enumerates $X \oplus \overline X$. Conversely, a string $\sigma$ is a prefix of $X$ if and only if $\sigma(n) = 1$ implies $2n \in X \oplus \overline X$ and $\sigma(n) = 0$ implies $2n + 1 \in X \oplus \overline X$, for all $n < |\sigma|$: the axiom for $\sigma$ is the finite set of these numbers.
:::
::::

## Notes and references

The continuous degrees and :ref{#prop-continuous-embedding} are due to Miller (2004), who also proved :ref{#thm-nontotal-continuous} and the characterization of PA above. :ref{#thm-almost-total} is Andrews, Igusa, Miller and Soskova (2019). Represented spaces and their degrees are from Kihara and Pauly, and Kihara, Ng and Pauly. The presentation follows Soskova's survey, Section 3.2.

- J. S. Miller, *Degrees of unsolvability of continuous functions*, Journal of Symbolic Logic 69 (2004), 555–584.
- U. Andrews, G. Igusa, J. S. Miller and M. I. Soskova, *Characterizing the continuous degrees*, Israel Journal of Mathematics 234 (2019), 743–767.
- T. Kihara, K. M. Ng and A. Pauly, *Enumeration degrees and non-metrizable topology*, arXiv:1904.04107.
- M. I. Soskova, *The theory of the enumeration degrees, definability, and automorphisms*, College Publications, 2020, Section 3.2.

