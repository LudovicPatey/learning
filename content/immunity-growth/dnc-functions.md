---
title: Diagonally non-computable functions
summary: DNC and fixed-point free functions compute each other, and the DNC degrees are the degrees of effectively immune sets; DNC functions avoid every c.e. set of known bounded size.
duration: 45
prerequisites: [immune-sets, fundamentals/fixed-point, pi01-classes/pa-degrees]
---

The fixed point theorem says that every computable transformation of programs has a fixed point, up to the function computed. A function that transforms every program into one computing a different function cannot be computable; this lesson studies the degrees of such **fixed-point free** functions. They coincide with the degrees of **diagonally non-computable** functions, which differ from the diagonal $e \mapsto \Phi_e(e)$ wherever it is defined, and with the degrees of **effectively immune** sets.

A DNC function has to avoid one value at each input, the value $\Phi_e(e)$, without knowing whether it is defined. The central result of the lesson shows that this weak ability can be amplified: a DNC function computes a function that avoids, at each input, any finite c.e. set whose size is bounded in advance. This amplified form is the one used in applications, in :ref{to="immunity-growth/arslanov"} and :ref{to="immunity-growth/high-or-dnc"} and in the course on algorithmic randomness.

## DNC and fixed-point free functions

:::definition{#def-dnc}
A total function $f : \nat \to \nat$ is **diagonally non-computable**, or **DNC**, if $f(e) \neq \Phi_e(e)$ for every $e$ such that $\Phi_e(e)\converge$. A total function $f$ is **fixed-point free** if $\Phi_{f(e)} \neq \Phi_e$ for every $e$.
:::

No DNC function is computable: if $f = \Phi_e$ were total, then $\Phi_e(e)\converge = f(e)$. The set $\emptyset'$ computes a DNC function, namely $f(e) = \Phi_e(e) + 1$ if $e \in \emptyset'$ and $f(e) = 0$ otherwise. The PA sets compute $\{0, 1\}$-valued DNC functions (:ref{#def-pa-degree}). No fixed-point free function is computable, by the fixed point theorem (:ref{#thm-fixed-point}).

Both directions of the next theorem rest on the same device: a program, obtained by SMN, whose behavior on its own index, or whose index, encodes the value to be avoided. A function that refutes the program then refutes the value.

:::theorem[Jockusch, Lerman, Soare, Solovay]{#thm-dnc-fpf}
A set $X$ computes a DNC function if and only if it computes a fixed-point free function.
:::

:::proof{of=thm-dnc-fpf}
($\Rightarrow$) Let $g \leq_T X$ be DNC. By the parameter form of SMN (:ref{#cor-smn-parameters}), there is a total computable function $q$ such that $\Phi_{q(n, v)}$ is the function defined only at the input $n$, with value $v$. Let $f(n) = q(n, g(n))$; it is $X$-computable. If $\Phi_{f(n)} = \Phi_n$ for some $n$, then $\Phi_n(n)\converge = \Phi_{f(n)}(n) = g(n)$, contradicting the fact that $g$ is DNC. So $f$ is fixed-point free.

($\Leftarrow$) Let $f \leq_T X$ be fixed-point free. By SMN, there is a total computable function $d$ such that the program $d(n)$, on input $m$, computes $\Phi_n(n)$ and, if this converges with value $v$, runs $\Phi_v(m)$. So $\Phi_{d(n)} = \Phi_{\Phi_n(n)}$ when $\Phi_n(n)\converge$. Let $g(n) = f(d(n))$; it is $X$-computable and total, since it does not run the computation $\Phi_n(n)$. If $g(n) = \Phi_n(n)$ for some $n$ with $\Phi_n(n)\converge$, then $\Phi_{f(d(n))} = \Phi_{\Phi_n(n)} = \Phi_{d(n)}$, contradicting the fact that $f$ is fixed-point free. So $g$ is DNC.
:::

The reductions are uniform. A DNC function avoids, at each $e$, the single value $\Phi_e(e)$. The next theorem shows that DNC functions can be used to avoid, uniformly, any finite c.e. set whose size is bounded in advance.

## Effectively immune sets

:::definition{#def-effectively-immune}
An infinite set $A$ is **effectively immune** if there is a total computable function $q$ such that $|W_e| \leq q(e)$ for every $e$ with $W_e \subseteq A$. A c.e. set is **effectively simple** if its complement is effectively immune.
:::

An effectively immune set is immune: an infinite c.e. subset $W_e$ would have more than $q(e)$ elements. Effective immunity requires that a c.e. subset of $A$ reveals, through its index, a bound on its size.

:::example{#ex-post-effectively-simple}
Post's simple set $S$ (:ref{#thm-post-simple}) is effectively simple. If $W_e \subseteq \nat \setminus S$, then $W_e$ has no element larger than $2e$: otherwise the element $x_e$ of the construction is defined, and $x_e \in W_e \cap S$. So $|W_e| \leq 2e + 1$, and $q(e) = 2e + 1$ witnesses effective immunity. By contrast, the complement of a low simple set is not effectively immune (:ref{#cor-arslanov}).
:::

:::theorem{#thm-dnc-effectively-immune}
For every set $X$, the following are equivalent:

1. $X$ computes a DNC function;
2. $X$ computes a function $h : \nat^2 \to \nat$ such that $h(e, n) \notin W_e$ whenever $|W_e| \leq n$;
3. $X$ computes an effectively immune set.
:::

Statement (2) strengthens DNC: $h(e, n)$ avoids the c.e. set $W_e$ whenever it has at most $n$ elements, while a DNC function avoids the set $\{ \Phi_e(e) \}$, of size at most one. In (1 ⇒ 2), $n$ values are needed, and they are obtained by applying a DNC function to $n$ programs, each predicting one coordinate of an element of $W_e$. In (2 ⇒ 3), the effectively immune set is built greedily: each new element is chosen, with $h$, outside a finite c.e. set that collects all the dangers known so far. In (3 ⇒ 1), a large finite subset of an effectively immune set gives a program that cannot be a fixed point.

:::proof{of=thm-dnc-effectively-immune}
Let $\langle k_0, \dots, k_{n-1} \rangle$ denote a computable bijection between $\nat^n$ and $\nat$, uniform in $n \geq 1$.

(1 ⇒ 2) Let $f \leq_T X$ be DNC. By SMN, there is a total computable function $u$ such that the program $u(e, n, i)$, for $i < n$, on any input, waits for the $i$-th element $k$ enumerated into $W_e$ (counting from $0$), and if it appears, outputs the $i$-th component $k_i$ of the tuple $k = \langle k_0, \dots, k_{n-1} \rangle$; otherwise it diverges. For $n \geq 1$, let
$$
h(e, n) = \langle f(u(e, n, 0)), \dots, f(u(e, n, n-1)) \rangle,
$$
and $h(e, 0) = 0$. It is $X$-computable. Suppose that $|W_e| \leq n$ and $h(e, n) \in W_e$. Then $n \geq 1$, and $h(e, n)$ is the $i$-th element enumerated into $W_e$ for some $i < n$. So the program $u(e, n, i)$, on input $u(e, n, i)$, outputs the $i$-th component of $h(e, n)$, which is $f(u(e, n, i))$. This contradicts the fact that $f$ is DNC.

(2 ⇒ 3) Let $h \leq_T X$ be as in (2). Let $\gamma$ be the partial computable function such that $\gamma(e)$ is the canonical index of the set of the first $e + 1$ elements enumerated into $W_e$, defined if and only if $|W_e| \geq e + 1$. We build an $X$-computable strictly increasing sequence $x_0 < x_1 < \cdots$ such that, for every $s$,
$$
(\star_s) \qquad \text{for every } e \leq s \text{ with } \gamma(e)\converge, \quad D_{\gamma(e)} \not\subseteq \{ x_0, \dots, x_s \}.
$$
Suppose that $x_0, \dots, x_{s-1}$ are defined, for some $s \geq 0$. By SMN, uniformly in $s$ and in the finite sequence $x_0, \dots, x_{s-1}$, one computes an index $v$ with
$$
W_v = \{ y : y \leq x_{s-1} \} \cup \bigcup_{e \leq s,\ \gamma(e)\converge} D_{\gamma(e)},
$$
where the first part is empty for $s = 0$. This set has at most $n_s = (x_{s-1} + 1) + \sum_{e \leq s} (e + 1)$ elements, a number computable from $s$ and $x_{s-1}$. Let $x_s = h(v, n_s)$; then $x_s \notin W_v$. So $x_s > x_{s-1}$, and $x_s \notin D_{\gamma(e)}$ for every $e \leq s$ with $\gamma(e)\converge$.

We check $(\star_s)$. Let $e \leq s$ with $\gamma(e)\converge$. If $e < s$, by $(\star_{s-1})$ some element of $D_{\gamma(e)}$ is not among $x_0, \dots, x_{s-1}$, and it is not $x_s$ either, since $x_s \notin D_{\gamma(e)}$. If $e = s$, the set $D_{\gamma(s)}$ has $s + 1$ elements and does not contain $x_s$; it cannot be contained in the $s$-element set $\{ x_0, \dots, x_{s-1} \}$.

Let $H = \{ x_s : s \in \nat \}$; it is infinite and $X$-computable, since the sequence is increasing. If $W_e \subseteq H$ and $|W_e| \geq e + 1$, then $\gamma(e)\converge$ and $D_{\gamma(e)} \subseteq H$ is finite, so $D_{\gamma(e)} \subseteq \{ x_0, \dots, x_s \}$ for some $s \geq e$, contradicting $(\star_s)$. So $|W_e| \leq e$ whenever $W_e \subseteq H$: $H$ is effectively immune, with $q(e) = e$.

(3 ⇒ 1) Let $H \leq_T X$ be effectively immune, with bound $q$. By SMN, there is a total computable $k$ with $W_{k(n)} = D_n$. Let $f(e) = k(c(e))$, where $c(e)$ is the canonical index of the set of the first $q(e) + 1$ elements of $H$; $f$ is $X$-computable. If $W_{f(e)} = W_e$, then $W_e$ is a subset of $H$ with $q(e) + 1$ elements, contradicting the choice of $q$. So $W_{f(e)} \neq W_e$, hence $\Phi_{f(e)} \neq \Phi_e$ for every $e$: $f$ is fixed-point free, and $X$ computes a DNC function by :ref{#thm-dnc-fpf}.
:::

:::quiz[DNC functions and effective immunity]
In (1 ⇒ 2), why does $h(e, n)$ combine $n$ values of $f$ into a tuple, rather than use a single value?

- [x] Because $h(e, n)$ must avoid up to $n$ elements; each program $u(e, n, i)$ predicts that the $i$-th element of $W_e$ is the value of $h$, and $f$ refutes each prediction on one component.
- [ ] Because $f$ takes values in $\{0, 1\}$.

  $f$ is an arbitrary DNC function, with values in $\nat$.
- [ ] Because $W_e$ is not computable.

  The construction never decides $W_e$; it only waits for its elements in the programs $u(e, n, i)$.

---

In (2 ⇒ 3), why does the set $W_v$ contain all the numbers $y \leq x_{s-1}$?

- [x] To force $x_s > x_{s-1}$, so that the sequence is increasing and $H$ is computable in $X$.

  An $X$-computable sequence that is not increasing has an $X$-c.e. range, which need not be $X$-computable.
- [ ] To make $W_v$ infinite.

  $W_v$ is finite; its size is bounded by $n_s$, which is what allows applying $h$.
- [ ] To ensure $(\star_s)$ for $e = s$.

  This case uses only that $D_{\gamma(s)}$ has $s + 1$ elements and does not contain $x_s$.
:::

## Bounded DNC functions

The PA degrees are the degrees of $\{0, 1\}$-valued DNC functions (:ref{#def-pa-degree}). More generally, for a non-decreasing computable function $b \geq 2$, a DNC function $f$ with $f(n) < b(n)$ for every $n$ is a $\mathrm{DNC}_b$ function. The $\mathrm{DNC}_b$ functions are the paths of a computable, computably bounded tree. Two results, admitted here, describe the role of the bound.

- *Constant bounds.* For every $k \geq 2$, a $\mathrm{DNC}_k$ function computes a $\mathrm{DNC}_2$ function, so the sets computing a DNC function with a constant bound are exactly the PA sets (Jockusch 1989; Nies 2009, Exercise 4.3.5).
- *Growing bounds.* For every computable bound $b$, there is a larger computable bound $b'$ and a set computing a $\mathrm{DNC}_{b'}$ function but no $\mathrm{DNC}_b$ function (Ambos-Spies, Kjos-Hanssen, Lempp and Slaman 2004). The DNC degrees are therefore stratified by the growth of the bound, from the PA degrees to the DNC degrees with no computable bound.

## Exercises

::::exercise{difficulty=1}
Show that if $X$ computes a DNC function, then the degree of $X$ contains a DNC function.

:::solution
Let $g \leq_T X$ be DNC. By the padding lemma, there is a computable strictly increasing sequence $a_0 < a_1 < \cdots$ of indices of the nowhere defined function; its range $R$ is computable. Let $f(x) = X(n)$ if $x = a_n$, and $f(x) = g(x)$ if $x \notin R$. Then $f \leq_T X$, and $X \leq_T f$ since $X(n) = f(a_n)$. For $x \notin R$, $f(x) = g(x) \neq \Phi_x(x)$ when $\Phi_x(x)\converge$; for $x \in R$, $\Phi_x(x)$ diverges. So $f$ is DNC.
:::
::::

::::exercise{difficulty=2}
Show that there is a non-computable set, computable in $\emptyset''$, that computes no DNC function.

:::hint
Build the set by finite extensions. For a functional $\Phi_i$ and a string $\sigma$, either $\Phi^{\sigma\tau}_i(m)$ diverges for some $m$ and all $\tau$, or the first convergent extension defines a total computable function, which agrees with the diagonal somewhere.
:::

:::solution
Build $\sigma_0 \prec \sigma_1 \prec \cdots$ with oracle $\emptyset''$, alternating two kinds of steps. To make the set $X$ different from $\Phi_e$, extend $\sigma$ by a bit $b$ different from $\Phi_e(|\sigma|)$ if it converges, by $0$ otherwise; $\emptyset'$ decides this. To defeat $\Phi_i$ as a DNC function, given $\sigma$, ask $\emptyset''$ whether there is $m$ such that $\Phi^{\sigma\tau}_i(m)\diverge$ for every $\tau$, a $\Sigma^0_2$ question.

- If yes, find such an $m$ with $\emptyset''$ and keep $\sigma$: every $X \succ \sigma$ has $\Phi^X_i(m)\diverge$, so $\Phi^X_i$ is not total.
- If no, let $\psi(m)$ be the value $\Phi^{\sigma\tau}_i(m)$ for the first $\tau$ found with convergence; $\psi$ is total computable. By the fixed point theorem applied to the function $y \mapsto$ (an index of the constant function with value $\psi(y)$), there is $a$ with $\Phi_a$ constant equal to $\psi(a)$, so $\Phi_a(a)\converge = \psi(a)$. Extend $\sigma$ to the string $\sigma\tau$ found for $m = a$. Then every $X \succ \sigma\tau$ has $\Phi^X_i(a) = \psi(a) = \Phi_a(a)$, so $\Phi^X_i$ is not DNC.

The limit $X$ is computable in $\emptyset''$, is not computable, and computes no DNC function.
:::
::::

## Notes and references

Fixed-point free functions were studied by Arslanov, whose completeness criterion is the subject of :ref{to="immunity-growth/arslanov"}. The equivalence between DNC and fixed-point free functions is due to Jockusch, Lerman, Soare and Solovay (1989); see Downey and Hirschfeldt (2010, Theorem 2.22.1), Nies (2009, Proposition 4.1.4), and Soare (2016, Exercise 5.4.5), who attributes it to Jockusch. The implication from effective immunity to fixed-point free functions is the argument of Martin's proof that effectively simple sets are complete (Martin 1966; Nies 2009, Proposition 4.1.13). The equivalence of the three conditions of :ref{#thm-dnc-effectively-immune} is presented by Monin and Patey in the section *DNC functions* of their chapter *Immunity and function growth*. In the course on algorithmic randomness, DNC functions reappear through the complexity of the initial segments of a set.

- D. A. Martin, *Completeness, the recursion theorem and effectively simple sets*, Proceedings of the American Mathematical Society 17 (1966), 838–842.
- C. G. Jockusch, M. Lerman, R. I. Soare and R. M. Solovay, *Recursively enumerable sets modulo iterated jumps and extensions of Arslanov's completeness criterion*, Journal of Symbolic Logic 54 (1989), 1288–1323.
- C. G. Jockusch, *Degrees of functions with no fixed points*, in *Logic, Methodology and Philosophy of Science VIII*, North-Holland, 1989, 191–201.
- K. Ambos-Spies, B. Kjos-Hanssen, S. Lempp and T. A. Slaman, *Comparing DNR and WWKL*, Journal of Symbolic Logic 69 (2004), 1089–1104.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Section 2.22.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Section 4.1.
- B. Monin and L. Patey, *Computability theory*, chapter *Immunity and function growth*.
