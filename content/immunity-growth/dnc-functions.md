---
title: Diagonally non-computable functions
summary: DNC and fixed-point free functions compute each other; the DNC degrees are the degrees of effectively immune sets; Arslanov's completeness criterion shows that a c.e. set computing a DNC function is complete.
duration: 45
prerequisites: [immune-sets, fundamentals/fixed-point, pi01-classes/pa-degrees, ce-degrees/low-simple-set]
---

The fixed point theorem says that every computable transformation of programs has a fixed point, up to the function computed. A function that transforms every program into one computing a different function cannot be computable; this lesson studies the degrees of such **fixed-point free** functions. They coincide with the degrees of **diagonally non-computable** functions, which differ from the diagonal $e \mapsto \Phi_e(e)$ wherever it is defined, and with the degrees of **effectively immune** sets. Arslanov's completeness criterion then shows that among c.e. sets, only the complete ones have this power.

## DNC and fixed-point free functions

:::definition{#def-dnc}
A total function $f : \nat \to \nat$ is **diagonally non-computable**, or **DNC**, if $f(e) \neq \Phi_e(e)$ for every $e$ such that $\Phi_e(e)\converge$. A total function $f$ is **fixed-point free** if $\Phi_{f(e)} \neq \Phi_e$ for every $e$.
:::

No DNC function is computable: if $f = \Phi_e$ were total, then $\Phi_e(e)\converge = f(e)$. The set $\emptyset'$ computes a DNC function, namely $f(e) = \Phi_e(e) + 1$ if $e \in \emptyset'$ and $f(e) = 0$ otherwise. The PA sets compute $\{0, 1\}$-valued DNC functions (:ref{#def-pa-degree}). No fixed-point free function is computable, by the fixed point theorem (:ref{#thm-fixed-point}).

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

:::theorem{#thm-dnc-effectively-immune}
For every set $X$, the following are equivalent:

1. $X$ computes a DNC function;
2. $X$ computes a function $h : \nat^2 \to \nat$ such that $h(e, n) \notin W_e$ whenever $|W_e| \leq n$;
3. $X$ computes an effectively immune set.
:::

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

## Arslanov's completeness criterion

The halting set computes a DNC function. Arslanov showed that it is the only c.e. degree with this property.

:::theorem[Arslanov's completeness criterion]{#thm-arslanov}
A c.e. set $A$ is Turing complete if and only if it computes a DNC function.
:::

:::proof{of=thm-arslanov}
If $A \equiv_T \emptyset'$, it computes a DNC function. Conversely, let $A$ be c.e., with a c.e. approximation $(A_s)$, and suppose that $A$ computes a DNC function. By :ref{#thm-dnc-fpf}, there is a functional $\Phi_i$ such that $f = \Phi^A_i$ is total and fixed-point free. Let $f_s(x) = \Phi^{A_s}_i(x)[s]$ if this computation converges, and $f_s(x) = 0$ otherwise; the function $(s, x) \mapsto f_s(x)$ is computable. Let $\emptyset'_t$ be the set of $n \leq t$ with $\Phi_n(n)[t]\converge$.

By SMN, there is a total computable function $r$ such that the program $r(n, x)$, on input $m$, searches for the least $t$ with $n \in \emptyset'_t$ and, if it finds one, runs $\Phi_{f_t(x)}(m)$. By the fixed point theorem with parameters (:ref{#thm-fixed-point-parameters}), there is a total computable function $p$ with $\Phi_{p(n)} = \Phi_{r(n, p(n))}$ for every $n$.

With oracle $A$, compute for each $n$ the least stage $s(n)$ such that $\Phi^{A_s}_i(p(n))[s]$ converges, with use $u$, and $A_s \uh u = A \uh u$, for $s = s(n)$. Such a stage exists, since $f(p(n))$ is defined and $A_s \uh u$ eventually equals $A \uh u$; and the condition is decided by $A$. Since $A$ is c.e., $A_t \uh u = A \uh u$ for every $t \geq s(n)$, so the same computation gives $f_t(p(n)) = f(p(n))$ for every $t \geq s(n)$.

We claim that $n \in \emptyset'$ if and only if $n \in \emptyset'_{s(n)}$, which shows $\emptyset' \leq_T A$. Suppose that $n \in \emptyset'$, and let $t$ be the least stage with $n \in \emptyset'_t$. If $t > s(n)$, then the program $r(n, p(n))$ runs $\Phi_{f_t(p(n))} = \Phi_{f(p(n))}$, so $\Phi_{p(n)} = \Phi_{r(n, p(n))} = \Phi_{f(p(n))}$, contradicting the fact that $f$ is fixed-point free. So $t \leq s(n)$, and $n \in \emptyset'_{s(n)}$, since $\emptyset'_t \subseteq \emptyset'_{s(n)}$. Conversely, $\emptyset'_{s(n)} \subseteq \emptyset'$.
:::

The program $p(n)$ waits for $n$ to enter $\emptyset'$ and then copies the program that the current approximation of $f$ assigns to it. If $n$ entered $\emptyset'$ after the approximation of $f(p(n))$ has settled, $p(n)$ would be a fixed point of $f$. So, once $A$ knows that the approximation has settled, the entry of $n$ into $\emptyset'$ is already decided. The c.e. hypothesis is necessary: there are low PA sets (:ref{#cor-pa-basis}), which compute DNC functions without computing $\emptyset'$.

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

Arslanov (1981) proved the completeness criterion, in the form of fixed-point free functions; Martin (1966) had proved that effectively simple sets are complete. The equivalence between DNC and fixed-point free functions is due to Jockusch, Lerman, Soare and Solovay (1989), and the characterization through effectively immune sets to Jockusch. In the course on algorithmic randomness, DNC functions reappear through the complexity of the initial segments of a set.

- M. M. Arslanov, *Some generalizations of a fixed-point theorem*, Soviet Mathematics (Izvestiya VUZ. Matematika) 25 (1981), 1–10.
- D. A. Martin, *Completeness, the recursion theorem and effectively simple sets*, Proceedings of the American Mathematical Society 17 (1966), 838–842.
- C. G. Jockusch, M. Lerman, R. I. Soare and R. M. Solovay, *Recursively enumerable sets modulo iterated jumps and extensions of Arslanov's completeness criterion*, Journal of Symbolic Logic 54 (1989), 1288–1323.
- C. G. Jockusch, *Degrees of functions with no fixed points*, in *Logic, Methodology and Philosophy of Science VIII*, North-Holland, 1989, 191–201.
