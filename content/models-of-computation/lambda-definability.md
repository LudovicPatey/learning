---
title: Computing with λ-terms
summary: Church numerals, arithmetic, booleans and pairs in the pure λ-calculus, Kleene's predecessor, fixed-point combinators, and the λ-definability of the partial recursive functions.
duration: 45
prerequisites: [lambda-calculus, mu-recursion]
---

The pure λ-calculus has no built-in data. To compute functions on integers, we represent integers, booleans and pairs by λ-terms in normal form, and operations on them by terms which reduce correctly when applied to these representations.

## Church numerals and arithmetic

:::definition{#def-church-numerals}
For $n \in \nat$, the **Church numeral** $\overline{n}$ is the term
$$
\overline{n} = \lambda f x.\, f^n(x), \qquad\text{where } f^0(x) = x \text{ and } f^{n+1}(x) = f\,(f^n(x)).
$$
Thus $\overline{0} = \lambda f x.\, x$, $\overline{1} = \lambda f x.\, f\, x$, $\overline{2} = \lambda f x.\, f\,(f\, x)$.
:::

The numeral $\overline n$ is the operation "iterate $n$ times": $\overline{n}\, F\, A \twoheadrightarrow_\beta F^n(A)$ for all terms $F, A$. Numerals are distinct normal forms, so by :ref{#cor-unique-normal-form} they are pairwise not β-convertible.

:::definition{#def-lambda-definable}
A partial function $f : \nat^k \rightharpoonup \nat$ is **λ-definable** if there is a term $F$ such that for all $\vec n = (n_1, \dots, n_k)$:

- if $f(\vec n)\converge$, then $F\, \overline{n_1} \cdots \overline{n_k} \twoheadrightarrow_\beta \overline{f(\vec n)}$;
- if $f(\vec n)\diverge$, then $F\, \overline{n_1} \cdots \overline{n_k}$ has no normal form.
:::

By Church–Rosser, the first condition determines $f(\vec n)$ uniquely.

:::proposition{#prop-church-arithmetic}
The following terms λ-define the successor, addition, multiplication and exponentiation:
$$
\begin{gathered}
\mathsf{succ} = \lambda n f x.\, f\,(n\, f\, x), \\
\mathsf{plus} = \lambda m n f x.\, m\, f\,(n\, f\, x), \\
\mathsf{mult} = \lambda m n f.\, m\,(n\, f), \\
\mathsf{exp} = \lambda m n.\, n\,(\mathsf{mult}\, m)\, \overline 1.
\end{gathered}
$$
Here $\mathsf{exp}\, \overline m\, \overline n \twoheadrightarrow_\beta \overline{m^n}$.
:::

:::proof{of=prop-church-arithmetic}
$\mathsf{succ}\, \overline n \to_\beta \lambda f x.\, f\,(\overline n\, f\, x) \twoheadrightarrow_\beta \lambda f x.\, f\,(f^n(x)) = \overline{n+1}$.

$\mathsf{plus}\, \overline m\, \overline n \twoheadrightarrow_\beta \lambda f x.\, \overline m\, f\,(\overline n\, f\, x) \twoheadrightarrow_\beta \lambda f x.\, f^m(f^n(x)) = \overline{m + n}$.

$\mathsf{mult}\, \overline m\, \overline n \twoheadrightarrow_\beta \lambda f.\, \overline m\,(\overline n\, f)$. Now $\overline n\, f \twoheadrightarrow_\beta \lambda x.\, f^n(x)$, and iterating this function $m$ times gives $\lambda x.\, f^{mn}(x)$ after reduction; so the result is $\lambda f x.\, f^{mn}(x) = \overline{mn}$.

$\mathsf{exp}\, \overline m\, \overline n \twoheadrightarrow_\beta \overline n\,(\mathsf{mult}\, \overline m)\, \overline 1 \twoheadrightarrow_\beta (\mathsf{mult}\, \overline m)^n(\overline 1)$, which reduces to $\overline{m^n}$ by induction on $n$, using the case of multiplication.

The shorter term $\lambda m n.\, n\, m$ also works for $n \geq 1$, but $\overline 0\, \overline m \twoheadrightarrow_\beta \lambda x.\, x$, which is not $\overline 1 = \lambda f x.\, f\, x$ (the two are only η-convertible).
:::

:::quiz[Church numerals]
What does $\mathsf{plus}\, \overline 1$ reduce to?

- [x] $\mathsf{succ}$.

  $\mathsf{plus}\, \overline 1 \twoheadrightarrow_\beta \lambda n f x.\, \overline 1\, f\,(n\, f\, x) \twoheadrightarrow_\beta \lambda n f x.\, f\,(n\, f\, x) = \mathsf{succ}$.
- [ ] $\overline 1$.

  $\mathsf{plus}\, \overline 1$ still expects an argument.
- [ ] It has no normal form.

---

In the definition of $\mathsf{mult}$, what is the role of $\overline n\, f$?

- [x] It is the $n$-fold iterate of $f$; iterating it $m$ times iterates $f$ exactly $mn$ times.
- [ ] It multiplies $f$ by $n$.

  There is no multiplication of functions; $\overline n\, f$ is iteration.
- [ ] It applies $f$ to $n$.
:::

## Booleans, conditionals and pairs

:::definition{#def-lambda-booleans}
$$
\begin{gathered}
\mathsf{true} = \lambda x y.\, x, \\
\mathsf{false} = \lambda x y.\, y, \\
\mathsf{iszero} = \lambda n.\, n\,(\lambda z.\, \mathsf{false})\, \mathsf{true},
\end{gathered}
$$
$$
\begin{gathered}
\mathsf{pair} = \lambda a b f.\, f\, a\, b, \\
\mathsf{fst} = \lambda p.\, p\, \mathsf{true}, \\
\mathsf{snd} = \lambda p.\, p\, \mathsf{false}.
\end{gathered}
$$
:::

A boolean selects one of its two arguments: $\mathsf{true}\, M\, N \twoheadrightarrow_\beta M$ and $\mathsf{false}\, M\, N \twoheadrightarrow_\beta N$. Hence "$\mathtt{if}\ B\ \mathtt{then}\ M\ \mathtt{else}\ N$" is simply $B\, M\, N$. The term $\mathsf{iszero}\, \overline n$ iterates the constant function $\lambda z.\, \mathsf{false}$ $n$ times on $\mathsf{true}$: it reduces to $\mathsf{true}$ if $n = 0$ and to $\mathsf{false}$ otherwise. Pairs store two terms: $\mathsf{fst}\,(\mathsf{pair}\, M\, N) \twoheadrightarrow_\beta M$ and $\mathsf{snd}\,(\mathsf{pair}\, M\, N) \twoheadrightarrow_\beta N$.

## The predecessor

Numerals iterate; they offer no direct way to "undo" an application of $f$. Church himself was for a while unsure whether the predecessor was λ-definable. Kleene found the following solution in 1932: iterate on pairs, keeping the previous value.

:::proposition[Kleene]{#prop-lambda-pred}
Let $\Phi = \lambda p.\, \mathsf{pair}\,(\mathsf{snd}\, p)\,(\mathsf{succ}\,(\mathsf{snd}\, p))$ and
$$
\mathsf{pred} = \lambda n.\, \mathsf{fst}\,\big(n\, \Phi\, (\mathsf{pair}\, \overline 0\, \overline 0)\big).
$$
Then $\mathsf{pred}\, \overline 0 \twoheadrightarrow_\beta \overline 0$ and $\mathsf{pred}\, \overline{n + 1} \twoheadrightarrow_\beta \overline n$.
:::

:::proof{of=prop-lambda-pred}
By induction on $n$, $\Phi^n(\mathsf{pair}\, \overline 0\, \overline 0)$ reduces to $\mathsf{pair}\, \overline{n \dotminus 1}\, \overline{n}$: this holds for $n = 0$, and $\Phi$ applied to $\mathsf{pair}\, \overline{a}\, \overline{n}$ reduces to $\mathsf{pair}\, \overline{n}\, \overline{n + 1}$. Since $\overline n\, \Phi\, A \twoheadrightarrow_\beta \Phi^n(A)$, the result follows by taking the first component.
:::

:::quiz[the predecessor]
What does $\Phi^3(\mathsf{pair}\, \overline 0\, \overline 0)$ reduce to?

- [x] $\mathsf{pair}\, \overline 2\, \overline 3$.

  The pairs are $(0, 0) \mapsto (0, 1) \mapsto (1, 2) \mapsto (2, 3)$.
- [ ] $\mathsf{pair}\, \overline 3\, \overline 3$.
- [ ] $\mathsf{pair}\, \overline 2\, \overline 2$.

---

Why is the predecessor harder to define than the successor with Church numerals?

- [x] A numeral can only apply a function a given number of times; computing $n - 1$ from the $n$-fold iteration requires recovering information that iteration does not directly provide, hence the pairing trick.
- [ ] Because the predecessor is not primitive recursive.

  It is primitive recursive.
- [ ] Because $\overline 0$ has no predecessor.

  The convention $0 \dotminus 1 = 0$ handles this case.
:::

## Fixed-point combinators

The λ-calculus has no names: a term cannot refer to itself. Recursion is nonetheless available, thanks to fixed-point combinators.

:::theorem[Fixed point theorem for the λ-calculus]{#thm-lambda-fixed-point}
Let $\mathsf{Y} = \lambda f.\, (\lambda x.\, f\,(x\, x))\,(\lambda x.\, f\,(x\, x))$. For every term $F$, $\mathsf{Y}\, F =_\beta F\,(\mathsf{Y}\, F)$. Moreover, Turing's combinator $\Theta = (\lambda x y.\, y\,(x\, x\, y))\,(\lambda x y.\, y\,(x\, x\, y))$ satisfies the stronger property $\Theta\, F \twoheadrightarrow_\beta F\,(\Theta\, F)$.
:::

:::proof{of=thm-lambda-fixed-point}
Let $W = \lambda x.\, F\,(x\, x)$. Then $\mathsf{Y}\, F \to_\beta W\, W \to_\beta F\,(W\, W)$, and also $F\,(\mathsf{Y}\, F) \to_\beta F\,(W\, W)$; so both sides reduce to $F\,(W\, W)$. For $\Theta$, let $A = \lambda x y.\, y\,(x\, x\, y)$, so that $\Theta = A\, A$; then $\Theta\, F = A\, A\, F \to_\beta (\lambda y.\, y\,(A\, A\, y))\, F \to_\beta F\,(A\, A\, F) = F\,(\Theta\, F)$.
:::

Fixed points allow recursive definitions. To obtain a term $G$ with $G\, x =_\beta M[G/g]$ — a function defined in terms of itself — take $G = \mathsf{Y}\,(\lambda g x.\, M)$. For instance, the factorial is
$$
\begin{aligned}
\mathsf{fact} = \mathsf{Y}\,\big(\lambda g n.\ & (\mathsf{iszero}\, n) \\
& \overline 1 \\
& (\mathsf{mult}\, n\, (g\, (\mathsf{pred}\, n)))\big).
\end{aligned}
$$

:::quiz[fixed-point combinators]
In the proof for $\mathsf Y$, why do we only obtain $\mathsf{Y}\, F =_\beta F\,(\mathsf{Y}\, F)$, and not a reduction $\mathsf{Y}\, F \twoheadrightarrow_\beta F\,(\mathsf{Y}\, F)$?

- [x] $\mathsf{Y}\, F$ reduces to $F\,(W\, W)$, in which $W\, W$ is not syntactically $\mathsf{Y}\, F$; the two terms only have a common reduct.
- [ ] Because $\mathsf{Y}\, F$ has no normal form.

  This is true for many $F$, but it is not the reason.
- [ ] Because β-reduction is not confluent.

  It is confluent (Church–Rosser).
:::

## λ-definability of the partial recursive functions

:::theorem[Kleene, 1936]{#thm-recursive-lambda-definable}
Every partial recursive function is λ-definable.
:::

:::proof{of=thm-recursive-lambda-definable}
By induction on the definition of $f$. We give the constructions and indicate the main difficulty.

*Basic functions.* $Z$ is λ-defined by $\lambda n.\, \overline 0$, $S$ by $\mathsf{succ}$, and $p^k_i$ by $\lambda x_1 \cdots x_k.\, x_i$.

*Primitive recursion.* If $G$ and $H$ λ-define $g$ and $h$, then $f(\vec x, y)$ is λ-defined by iterating on pairs (counter, value), as for the predecessor:
$$
\begin{aligned}
F = \lambda \vec x\, y.\, \mathsf{snd}\,\Big(y\ & \big(\lambda p.\, \mathsf{pair}\,(\mathsf{succ}\,(\mathsf{fst}\, p))\,(H\, \vec x\,(\mathsf{fst}\, p)\,(\mathsf{snd}\, p))\big) \\
& (\mathsf{pair}\, \overline 0\,(G\, \vec x))\Big).
\end{aligned}
$$

*Minimization.* If $G$ λ-defines $g$, let
$$
\begin{gathered}
\mathsf{search} = \mathsf{Y}\,\big(\lambda s\, \vec x\, z.\, (\mathsf{iszero}\,(G\, \vec x\, z))\; z\; (s\, \vec x\,(\mathsf{succ}\, z))\big), \\
F = \lambda \vec x.\, \mathsf{search}\, \vec x\, \overline 0.
\end{gathered}
$$
The term $\mathsf{search}\, \vec{\overline{x}}\, \overline z$ tests whether $g(\vec x, z) = 0$, returns $\overline z$ if so, and otherwise calls itself on $z + 1$. Normal order reduction performs exactly the search $\mu z\, [g(\vec x, z) = 0]$.

*Composition*, $f(\vec x) \simeq h(g_1(\vec x), \dots, g_m(\vec x))$, is the delicate case for partial functions. The naive term $\lambda \vec x.\, H\,(G_1\, \vec x) \cdots (G_m\, \vec x)$ may have a normal form even if some $g_i(\vec x)$ diverges, when $H$ discards its argument — whereas $f(\vec x)$ must then be undefined. One forces the evaluation of the arguments using the fact that $\overline n\, \mathsf I\, \mathsf I \twoheadrightarrow_\beta \mathsf I$ for every numeral: the term
$$
\begin{aligned}
\lambda \vec x.\ & (G_1\, \vec x\, \mathsf I\, \mathsf I) \cdots (G_m\, \vec x\, \mathsf I\, \mathsf I) \\
& \big(H\,(G_1\, \vec x) \cdots (G_m\, \vec x)\big)
\end{aligned}
$$
behaves as the naive term when all $G_i\, \vec{\overline x}$ reduce to numerals, since the prefix reduces to $\mathsf I \cdots \mathsf I$. To make the converse precise — that the term has no normal form when some $G_i\, \vec{\overline x}$ has none — one needs a stronger invariant than "has no normal form", namely **unsolvability**; it is preserved by the constructions above. We refer to Barendregt, *The Lambda Calculus*, §8.4, for the details.
:::

:::quiz[λ-definability of recursive functions]
In the minimization case, why must the recursion be implemented with a fixed-point combinator rather than with a numeral iteration, as for primitive recursion?

- [x] The number of steps of the search is not known in advance, so no numeral can be used to iterate it; a fixed point allows unbounded recursion.
- [ ] Because numerals cannot be compared with $\overline 0$.

  $\mathsf{iszero}$ does exactly this.
- [ ] Because the search must return a boolean.

  It returns a numeral.

---

Why is the naive term $\lambda \vec x.\, H\,(G_1\, \vec x) \cdots (G_m\, \vec x)$ inadequate for composition of partial functions?

- [x] If $H$ ignores its first argument and $g_1(\vec x)$ diverges, the naive term may still reduce to a numeral, while by our conventions $f(\vec x)$ is undefined.

  Normal order reduction is "lazy": it never evaluates arguments that are not used.
- [ ] Because application is not associative.
- [ ] Because $H$ may not be in normal form.
:::

:::theorem{#thm-lambda-definable-recursive}
Every λ-definable partial function is partial recursive.
:::

:::proof{of=thm-lambda-definable-recursive}
Code λ-terms by integers, for instance using de Bruijn indices to avoid α-equivalence issues and the sequence coding of the lesson :ref{to="models-of-computation/coding-sequences"}. The following are primitive recursive on codes: substitution, the predicate "$M$ is in normal form", the function computing the result of one normal order step, its $t$-th iterate $N(M, t)$, the code of $\overline n$ as a function of $n$, and the predicate "$M$ is a numeral" together with the extraction of its value. If $F$ λ-defines $f$, let $M_{\vec n}$ be the code of $F\, \overline{n_1} \cdots \overline{n_k}$; then
$$
f(\vec n) \simeq \mathrm{val}\big(N(M_{\vec n},\ \mu t\, [N(M_{\vec n}, t) \text{ is in normal form}])\big).
$$
By :ref{#thm-normal-order}, the search terminates exactly when $F\, \overline{n_1} \cdots \overline{n_k}$ has a normal form, which is then $\overline{f(\vec n)}$.
:::

Together with the previous lessons, this shows that λ-definability coincides with Turing computability, a fact established by Kleene and Turing in 1936. It was this equivalence that turned Church's proposal — identifying effective computability with λ-definability — into a widely accepted thesis.

## Exercises

::::exercise{difficulty=1}
Define λ-terms $\mathsf{and}$, $\mathsf{or}$ and $\mathsf{not}$ on the booleans $\mathsf{true}$, $\mathsf{false}$, and check them.

:::solution
$\mathsf{not} = \lambda b.\, b\, \mathsf{false}\, \mathsf{true}$, $\mathsf{and} = \lambda a b.\, a\, b\, \mathsf{false}$, $\mathsf{or} = \lambda a b.\, a\, \mathsf{true}\, b$. For instance $\mathsf{and}\, \mathsf{true}\, B \twoheadrightarrow_\beta \mathsf{true}\, B\, \mathsf{false} \twoheadrightarrow_\beta B$ and $\mathsf{and}\, \mathsf{false}\, B \twoheadrightarrow_\beta \mathsf{false}$.
:::
::::

::::exercise{difficulty=1}
Define truncated subtraction $\mathsf{minus}$ and the equality test $\mathsf{eq}$ on numerals.

:::solution
$\mathsf{minus} = \lambda m n.\, n\, \mathsf{pred}\, m$ iterates the predecessor $n$ times on $m$. Then $\mathsf{leq} = \lambda m n.\, \mathsf{iszero}\,(\mathsf{minus}\, m\, n)$ and $\mathsf{eq} = \lambda m n.\, \mathsf{and}\,(\mathsf{leq}\, m\, n)\,(\mathsf{leq}\, n\, m)$.
:::
::::

::::exercise{difficulty=2}
Show that $\mathsf{fact}\, \overline 3 \twoheadrightarrow_\beta \overline 6$ under normal order reduction, and explain what goes wrong with applicative order.

:::solution
Write $\mathsf{fact} = \mathsf{Y}\, F$. By the fixed point property, $\mathsf{fact}\, \overline 3 =_\beta F\, \mathsf{fact}\, \overline 3 \twoheadrightarrow_\beta (\mathsf{iszero}\, \overline 3)\, \overline 1\, (\mathsf{mult}\, \overline 3\, (\mathsf{fact}\,(\mathsf{pred}\, \overline 3)))$, which reduces to $\mathsf{mult}\, \overline 3\, (\mathsf{fact}\, \overline 2)$; continuing down to $\mathsf{fact}\, \overline 0 \twoheadrightarrow_\beta \overline 1$ gives $\overline 6$. Normal order contracts the conditional before evaluating the recursive call. Applicative order would first try to normalize the argument $\mathsf{Y}\, F$, whose reduction $\mathsf{Y}\, F \to W\, W \to F\,(W\, W) \to F\,(F\,(W\, W)) \to \cdots$ never terminates.
:::
::::
