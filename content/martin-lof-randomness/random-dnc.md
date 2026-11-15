---
title: Random sequences and DNC functions
summary: A set computes a DNC function exactly when it computes a sequence of strings of high prefix-free complexity; every Martin-Löf random sequence computes a DNC function; infinite subsets of random sequences.
duration: 30
prerequisites: [randomness-and-degrees, immunity-growth/dnc-functions, immunity-growth/arslanov]
---

The previous lessons showed that random sequences can compute every set, but that a given non-computable set is computed by few of them. This lesson identifies a computational property shared by all random sequences: they compute diagonally non-computable functions. The bridge between the two notions is Kolmogorov complexity: a DNC function is a function whose values cannot be predicted, and a random sequence produces strings that cannot be compressed.

## DNC functions and complexity

Recall from :ref{#def-dnc} that a function $f$ is **diagonally non-computable** if $f(e) \neq \Phi_e(e)$ for every $e$ with $\Phi_e(e)\converge$. Strings are identified with numbers through the length-lexicographic enumeration of :ref{to="kolmogorov-complexity/plain-complexity"}.

A DNC function avoids, on each input $e$, the one value $\Phi_e(e)$ that an algorithm could predict from $e$. A function whose values have high complexity avoids much more: every value with a short description, and $\Phi_e(e)$, when it is defined, has a description of length about $K(e)$. Conversely, a DNC function computes a function avoiding any c.e. set of a given size, uniformly (:ref{#thm-dnc-effectively-immune}), and the strings of complexity less than $n$ form a c.e. set of fewer than $2^n$ elements. The next theorem makes both observations precise.

:::theorem[Kjos-Hanssen, Merkle, Stephan]{#thm-dnc-complexity}
A set $X$ computes a DNC function if and only if $X$ computes a function $f : \nat \to \bstr$ with $K(f(n)) \geq n$ for every $n$.
:::

:::proof{of=thm-dnc-complexity}
($\Rightarrow$) Let $h \leq_T X$ be as in :ref{#thm-dnc-effectively-immune} (2): $h(e, m) \notin W_e$ whenever $|W_e| \leq m$. Since $K$ is approximable from above, the set of strings $\sigma$ with $K(\sigma) < n$ is c.e. uniformly in $n$, and by SMN there is a total computable function $a$ such that $W_{a(n)}$ is this set. It has fewer than $2^n$ elements, since distinct strings have distinct shortest descriptions, of length less than $n$. Let $f(n) = h(a(n), 2^n)$. Then $f \leq_T X$ and $f(n) \notin W_{a(n)}$, that is, $K(f(n)) \geq n$.

($\Leftarrow$) Let $f \leq_T X$ with $K(f(n)) \geq n$ for every $n$. The machine $M(\tau) = \Phi_{U(\tau)}(U(\tau))$ is prefix-free, since its domain is contained in that of $U$, and $M$ applied to a shortest description of $n$ gives $\Phi_n(n)$ when it converges. So there is a constant $d$ with
$$
K(\Phi_n(n)) \leq K(n) + d \leq 2 \log n + d'
$$
for every $n \geq 2$ with $\Phi_n(n)\converge$, by :ref{#prop-k-basic} (2). Let $n_0 \geq 2$ be such that $2 \log n + d' < n$ for $n \geq n_0$. For $n \geq n_0$ with $\Phi_n(n)\converge$, $K(\Phi_n(n)) < n \leq K(f(n))$, so $f(n) \neq \Phi_n(n)$. Modify $f$ on the finitely many $n < n_0$, setting $g(n) = \Phi_n(n) + 1$ if $\Phi_n(n)\converge$ and $g(n) = 0$ otherwise, and $g(n) = f(n)$ for $n \geq n_0$. The function $g$ is $X$-computable, as a finite modification of $f$, and DNC.
:::

## Random sequences compute DNC functions

A random sequence has incompressible prefixes, by the Levin–Schnorr theorem, and its prefixes form a function of high complexity computable from it.

:::corollary[Kučera]{#cor-random-dnc}
Every Martin-Löf random sequence computes a DNC function. Consequently, the class of sequences computing a DNC function is conull.
:::

:::proof{of=cor-random-dnc}
Let $Z$ be random. By :ref{#thm-levin-schnorr}, there is $c$ with $K(Z \uh m) \geq m - c$ for every $m$. The function $f(n) = Z \uh (n + c)$ is $Z$-computable and satisfies $K(f(n)) \geq n$, so $Z$ computes a DNC function by :ref{#thm-dnc-complexity}. The class MLR is conull (:ref{#cor-mlr-structure}) and contained in the class of sequences computing a DNC function, which is therefore conull.
:::

:::quiz[randomness and DNC functions]
In the proof of :ref{#thm-dnc-complexity} ($\Leftarrow$), why is $f(n) \neq \Phi_n(n)$ for large $n$?

- [x] Because the value $\Phi_n(n)$, when defined, is computed from $n$ and has complexity at most about $2 \log n$, whereas $f(n)$ has complexity at least $n$.
- [ ] Because $f$ is not computable.

  A non-computable function may agree with $\Phi_n(n)$ for infinitely many $n$; the argument uses the complexity bound.
- [ ] Because $K(n) \geq n$.

  On the contrary, $K(n) \leq^+ 2 \log n$ is much smaller than $n$.

---

In the proof of :ref{#cor-random-dnc}, why is $Z \uh (n + c)$ used rather than $Z \uh n$?

- [x] To compensate the constant $c$ of the Levin–Schnorr theorem: $K(Z \uh (n + c)) \geq n$, as required by :ref{#thm-dnc-complexity}.
- [ ] Because $Z \uh n$ is not $Z$-computable.

  Both are $Z$-computable; the shift adjusts the complexity bound.
- [ ] Because $c$ must be computable from $Z$.

  $c$ is a fixed constant; no computation of it is needed.
:::

:::remark{#rem-generic-random}
A 1-generic set computes no DNC function, by a theorem of Demuth and Kučera proved in the specialized course on Cohen genericity (:ref{#thm-generic-not-dnc}). By :ref{#cor-random-dnc}, a 1-generic set therefore computes no random sequence. The two notions of typicality, by measure and by category, are thus incompatible in the Turing degrees in one direction; in the other, every 1-generic set is computable from a random sequence, by :ref{#thm-kucera-gacs}.
:::

The converse of :ref{#cor-random-dnc} fails: there are DNC functions that compute no random sequence. Ambos-Spies, Kjos-Hanssen, Lempp and Slaman (2004) built such a function, and Kumabe and Lewis (2009) built a DNC function of minimal degree, which computes no random sequence since a random sequence $Z = Z_0 \oplus Z_1$ computes the two Turing incomparable halves $Z_0$ and $Z_1$ (van Lambalgen's theorem, in the course on notions of randomness). These results are admitted here.

The DNC degrees are nevertheless characterized by randomness: a set computes a DNC function if and only if it computes an infinite subset of a random sequence. The direction from subsets to DNC functions is :ref{#ex-random-subsets-dnc}. The other direction was proved by Greenberg and Miller (2009), and by Kjos-Hanssen (2009) for DNC functions of slow growth; Downey and Hirschfeldt (Theorem 8.10.2) give a short proof due to Miller. Finally, a random sequence computes a $\{0, 1\}$-valued DNC function only if it computes $\emptyset'$, by a theorem of Stephan (2006): the random sequences of PA degree are exactly those above $\emptyset'$. These results are admitted here.

## Exercises

::::exercise{#ex-random-subsets-dnc difficulty=2 objective="Bound from below the complexity of the finite subsets of a random set, and apply the characterization of DNC degrees by complexity."}
Let $X$ be Martin-Löf random, and let $S$ be an infinite subset of $X$ (viewed as a set of numbers). Show that every set $A$ computing $S$ computes a DNC function. For a finite set $F$, write $K(F)$ for the complexity of its canonical index.

:::hint
Show first that there is $k$ with $K(F) \geq |F| - k$ for every finite $F \subseteq X$, using a test made of the classes $\{ Y : F \subseteq Y \}$.
:::

:::solution
For a finite set $F$, the class $\mathcal C_F = \{ Y : F \subseteq Y \}$ is clopen, computable from $F$, of measure $2^{-|F|}$. Let $\mathcal V_k$ be the union of the classes $\mathcal C_F$ over the finite sets $F$ with $K(F) < |F| - k$. These sets form a c.e. set, uniformly in $k$, since $K$ is approximable from above; so $(\mathcal V_k)$ is uniformly $\Sigma^0_1$. Distinct finite sets have distinct canonical indices, so by the Kraft inequality for $K$ (:ref{#prop-k-basic} (4)),
$$
\lambda(\mathcal V_k) \leq \sum_{K(F) < |F| - k} 2^{-|F|} \leq \sum_{F} 2^{-K(F) - k} \leq 2^{-k}.
$$
So $(\mathcal V_k)$ is a Martin-Löf test, and since $X$ is random, there is $k$ with $X \notin \mathcal V_k$: every finite subset $F$ of $X$ satisfies $K(F) \geq |F| - k$. Let $s_0 < s_1 < \cdots$ be the elements of $S$, and let $f(n)$ be the canonical index of $\{ s_0, \dots, s_{n+k-1} \}$. Then $f \leq_T S \leq_T A$, and $K(f(n)) \geq n$ since this set is a subset of $X$ with $n + k$ elements. By :ref{#thm-dnc-complexity}, $A$ computes a DNC function.
:::
::::

::::exercise{#ex-random-ce-complete difficulty=1 objective="Combine Kučera's theorem with Arslanov's completeness criterion."}
Show that if a random sequence $Z$ is Turing equivalent to a c.e. set $A$, then $Z \equiv_T \emptyset'$.

:::solution
By :ref{#cor-random-dnc}, $Z$ computes a DNC function, hence so does $A$. By Arslanov's completeness criterion (:ref{#thm-arslanov}), $A \equiv_T \emptyset'$.
:::
::::

## Notes and references

The weak weak König lemma for homogeneous sets and its relation to DNC functions are studied in the course on compactness avoidance (:ref{to="compactness-avoidance/rwwkl-dnc"}).

Kučera (1985) proved that random sequences compute DNC functions; the proof through complexity follows Downey and Hirschfeldt (Theorem 8.8.1). The characterization of DNC degrees by complexity is due to Kjos-Hanssen, Merkle and Stephan (2011; conference version 2006), who state it for plain complexity, in terms of **autocomplex** sets (Downey–Hirschfeldt, Theorem 8.16.4); the version with $K$ given here is proved in the same way (compare Nies, Theorem 4.1.9). The history of the characterization by infinite subsets of random sequences is given by Downey and Hirschfeldt in a footnote to Theorem 8.10.2: Kjos-Hanssen proved the direction of :ref{#ex-random-subsets-dnc}, and the converse for DNC functions of slow growth; Greenberg and Miller proved the converse in general; the short proof is due to Miller. Nies proves this direction as Exercise 8.3.6. Stephan's theorem is Downey–Hirschfeldt, Theorem 8.8.4, and the existence of DNC functions computing no random sequence is Theorem 8.10.3.

- A. Kučera, *Measure, Π⁰₁-classes and complete extensions of PA*, in: Recursion Theory Week, Lecture Notes in Mathematics 1141, Springer, 1985, 245–259.
- B. Kjos-Hanssen, W. Merkle and F. Stephan, *Kolmogorov complexity and the recursion theorem*, Transactions of the American Mathematical Society 363 (2011), 5465–5480.
- K. Ambos-Spies, B. Kjos-Hanssen, S. Lempp and T. A. Slaman, *Comparing DNR and WWKL*, Journal of Symbolic Logic 69 (2004), 1089–1104.
- M. Kumabe and A. E. M. Lewis, *A fixed-point-free minimal degree*, Journal of the London Mathematical Society 80 (2009), 785–797.
- B. Kjos-Hanssen, *Infinite subsets of random sets of integers*, Mathematical Research Letters 16 (2009), 103–110.
- N. Greenberg and J. S. Miller, *Lowness for Kurtz randomness*, Journal of Symbolic Logic 74 (2009), 665–678.
- F. Stephan, *Martin-Löf random and PA-complete sets*, in: Logic Colloquium '02, Lecture Notes in Logic 27, Association for Symbolic Logic, 2006, 342–348.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Sections 8.8, 8.10 and 8.16.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Section 4.1.

:::::exercises
::::exercise{#ex-dnc-order difficulty=1 objective="See that the bound $n$ in the characterization of DNC degrees by complexity can be replaced by any computable order."}
An **order** is a computable non-decreasing unbounded function $h : \nat \to \nat$. Show that a set $X$ computes a DNC function if and only if, for some order $h$, $X$ computes a function $f : \nat \to \bstr$ with $K(f(n)) \geq h(n)$ for every $n$, and if and only if this holds for every order $h$.

:::solution
If $X$ computes a DNC function, :ref{#thm-dnc-complexity} gives $f \leq_T X$ with $K(f(n)) \geq n$ for every $n$. For an order $h$, the function $n \mapsto f(h(n))$ is $X$-computable and $K(f(h(n))) \geq h(n)$. So the condition holds for every order, in particular for some order.

Conversely, let $h$ be an order and $g \leq_T X$ with $K(g(n)) \geq h(n)$ for every $n$. Let $m(n)$ be the least $m$ with $h(m) \geq n$; it exists since $h$ is unbounded, and it is computable. Then $n \mapsto g(m(n))$ is $X$-computable, and $K(g(m(n))) \geq h(m(n)) \geq n$. By :ref{#thm-dnc-complexity}, $X$ computes a DNC function.
:::
::::

::::exercise{#ex-dnc-solovay difficulty=2 objective="Prove that random sequences compute DNC functions with a Solovay test, and obtain a computable bound on the values." lessons="solovay-tests"}
Let $Z$ be Martin-Löf random. Cut $\nat$ into consecutive intervals $B_e = [b_e, b_e + e]$ of length $e + 1$, with $b_0 = 0$ and $b_{e+1} = b_e + e + 1$, and let $f(e)$ be the number associated with the string $Z(b_e) \cdots Z(b_e + e)$. Show, with a Solovay test and without :ref{#thm-dnc-complexity}, that $f(e) \neq \Phi_e(e)$ for almost every $e$. Deduce that $Z$ computes a DNC function $g$ with $g(e) < 2^{e+2}$ for every $e$.

:::solution
For each $e$, let $\mathcal S_e$ be the class of the sequences $Y$ such that $\Phi_e(e)\converge$, the string associated with $\Phi_e(e)$ has length $e + 1$, and $Y(b_e) \cdots Y(b_e + e)$ is this string; it is empty if $\Phi_e(e)$ diverges or if the string has another length. The class $\mathcal S_e$ is clopen when it is non-empty, and it is enumerated once $\Phi_e(e)$ converges, so $(\mathcal S_e)$ is uniformly $\Sigma^0_1$. It fixes $e + 1$ bits, so $\lambda(\mathcal S_e) \leq 2^{-e-1}$, and $\sum_e \lambda(\mathcal S_e) \leq 1$: this is a Solovay test. By :ref{#thm-solovay}, there is $e_0$ such that $Z \notin \mathcal S_e$ for $e \geq e_0$. For such $e$, if $\Phi_e(e)$ converges, either the associated string has length different from $e + 1$, or it differs from $Z(b_e) \cdots Z(b_e + e)$; in both cases $f(e) \neq \Phi_e(e)$, since distinct strings are associated with distinct numbers.

Let $g(e) = f(e)$ for $e \geq e_0$, and, for $e < e_0$, $g(e) = 1$ if $\Phi_e(e)\converge = 0$ and $g(e) = 0$ otherwise. The finitely many values $g(e)$, $e < e_0$, are fixed in the program, so $g \leq_T Z$, and $g$ is DNC. In the length-lexicographic enumeration, the strings of length at most $e + 1$ are associated with the numbers less than $2^{e+2} - 1$, so $g(e) < 2^{e+2}$ for every $e$.

By Stephan's theorem, quoted in the lesson, the bound cannot be lowered to the constant $2$ unless $Z$ computes $\emptyset'$.
:::
::::

::::exercise{#ex-dnc-low-dominated difficulty=1 objective="Combine the basis theorems with Kučera's theorem, and see that Arslanov's criterion needs the hypothesis that the set is c.e." lessons="martin-lof-tests"}
Show that there is a low set that computes a DNC function, and a computably dominated set that computes a DNC function, and that neither of them computes $\emptyset'$. Why does this not contradict :ref{#thm-arslanov}?

:::solution
By :ref{#cor-mlr-structure} (3), there are a low random sequence $Z_1$ and a computably dominated random sequence $Z_2$, and both compute DNC functions by :ref{#cor-random-dnc}.

If $\emptyset' \leq_T Z_1$, then $\emptyset'' \leq_T Z_1' \equiv_T \emptyset'$, which is false. If $\emptyset' \leq_T Z_2$, then $\emptyset'$ is computably dominated, since every $\emptyset'$-computable function is $Z_2$-computable; but $\emptyset'$ is a non-computable $\Delta^0_2$ set, hence of hyperimmune degree (:ref{#thm-computation-function}), a contradiction.

:ref{#thm-arslanov} concerns c.e. sets, and $Z_1$ and $Z_2$ are not c.e., being random (:ref{#ex-mlr-not-ce}). Neither is any set of the degree of $Z_1$ or $Z_2$, since a c.e. set computing a DNC function computes $\emptyset'$.
:::
::::

::::exercise{#ex-dnc-supersets difficulty=1 objective="Transfer the result on infinite subsets of random sets to coinfinite supersets, through complements." lessons="martin-lof-tests"}
Let $X$ be Martin-Löf random, viewed as a set, and let $Y \supseteq X$ be coinfinite. Show that every set computing $Y$ computes a DNC function. Show that the hypothesis that $Y$ is coinfinite cannot be dropped.

:::solution
The complement $\nat \setminus Y$ is an infinite subset of $\nat \setminus X$, which is random by :ref{#ex-complement-join}. A set computing $Y$ computes $\nat \setminus Y$, hence computes a DNC function by :ref{#ex-random-subsets-dnc}.

The set $\nat$ is a superset of $X$; it is computable, and computes no DNC function, since a computable DNC function $g = \Phi_c$ would satisfy $g(c) \neq \Phi_c(c) = g(c)$.
:::
::::
:::::
