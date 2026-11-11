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

  $\mathsf{plus}\, \overline 1$ is a partial application, which reduces to the normal form $\mathsf{succ}$.

---

In the definition of $\mathsf{mult}$, what is the role of $\overline n\, f$?

- [x] It is the $n$-fold iterate of $f$; iterating it $m$ times iterates $f$ exactly $mn$ times.
- [ ] It multiplies $f$ by $n$.

  There is no multiplication of functions; $\overline n\, f$ is iteration.
- [ ] It applies $f$ to $n$.

  Numerals are applied to functions, not functions to numerals: $\overline n\, f$ is the $n$-fold composition of $f$.
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

A boolean selects one of its two arguments: $\mathsf{true}\, M\, N \twoheadrightarrow_\beta M$ and $\mathsf{false}\, M\, N \twoheadrightarrow_\beta N$. Hence “$\mathtt{if}\ B\ \mathtt{then}\ M\ \mathtt{else}\ N$” is simply $B\, M\, N$. The term $\mathsf{iszero}\, \overline n$ iterates the constant function $\lambda z.\, \mathsf{false}$ $n$ times on $\mathsf{true}$: it reduces to $\mathsf{true}$ if $n = 0$ and to $\mathsf{false}$ otherwise. Pairs store two terms: $\mathsf{fst}\,(\mathsf{pair}\, M\, N) \twoheadrightarrow_\beta M$ and $\mathsf{snd}\,(\mathsf{pair}\, M\, N) \twoheadrightarrow_\beta N$.

## The predecessor

Numerals iterate; they offer no direct way to "undo" an application of $f$. Church himself was for a while unsure whether the predecessor was λ-definable. Kleene found a solution in 1932, based on the following idea: iterate on pairs, keeping the previous value.

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

  $\Phi$ sends $\mathsf{pair}\, a\, b$ to $\mathsf{pair}\, b\, (b + 1)$, so the two components always differ by one after the first step.
- [ ] $\mathsf{pair}\, \overline 2\, \overline 2$.

  The two components differ by one after each application of $\Phi$: three steps from $(0, 0)$ give $(0, 1)$, $(1, 2)$, $(2, 3)$.

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
We first treat the total recursive functions, which is Kleene's 1936 theorem, and then reduce the partial case to it with the normal form theorem.

**Total functions.** By :ref{#cor-regular-mu}, every total recursive function has a derivation from the basic functions by composition, primitive recursion and minimization of regular functions, in which all the functions are total. We show by induction on such a derivation that each of its functions $f : \nat^k \to \nat$ is λ-defined by some term $F$; since $f$ is total, this means $F\, \overline{n_1} \cdots \overline{n_k} \twoheadrightarrow_\beta \overline{f(\vec n)}$ for all $\vec n$. Below, $\vec{\overline n}$ stands for $\overline{n_1} \cdots \overline{n_k}$.

*Basic functions.* $Z$ is λ-defined by $\lambda n.\, \overline 0$, $S$ by $\mathsf{succ}$, and $p^k_i$ by $\lambda x_1 \cdots x_k.\, x_i$.

*Composition.* If $H, G_1, \dots, G_m$ λ-define $h, g_1, \dots, g_m$, then $F = \lambda \vec x.\, H\,(G_1\, \vec x) \cdots (G_m\, \vec x)$ satisfies $F\, \vec{\overline n} \twoheadrightarrow_\beta H\, \overline{g_1(\vec n)} \cdots \overline{g_m(\vec n)} \twoheadrightarrow_\beta \overline{f(\vec n)}$.

*Primitive recursion.* If $G$ and $H$ λ-define $g$ and $h$, then $f(\vec x, y)$ is λ-defined by iterating on pairs (counter, value), as for the predecessor:
$$
\begin{aligned}
F = \lambda \vec x\, y.\, \mathsf{snd}\,\Big(y\ & \big(\lambda p.\, \mathsf{pair}\,(\mathsf{succ}\,(\mathsf{fst}\, p))\,(H\, \vec x\,(\mathsf{fst}\, p)\,(\mathsf{snd}\, p))\big) \\
& (\mathsf{pair}\, \overline 0\,(G\, \vec x))\Big).
\end{aligned}
$$
Let $\Psi$ be the term $\lambda p.\, \cdots$ above with $\vec{\overline n}$ substituted for $\vec x$. By induction on $j$, $\Psi^j(\mathsf{pair}\, \overline 0\,(G\, \vec{\overline n}))$ reduces to $\mathsf{pair}\, \overline j\, \overline{f(\vec n, j)}$: for $j = 0$ because $G\, \vec{\overline n} \twoheadrightarrow_\beta \overline{g(\vec n)}$, and for $j + 1$ because $\Psi\,(\mathsf{pair}\, \overline j\, \overline v) \twoheadrightarrow_\beta \mathsf{pair}\, \overline{j + 1}\, \overline{h(\vec n, j, v)}$. Since $\overline y\, \Psi\, A \twoheadrightarrow_\beta \Psi^y(A)$, taking the second component gives $F\, \vec{\overline n}\, \overline y \twoheadrightarrow_\beta \overline{f(\vec n, y)}$. (For $k = 0$, $G\, \vec x$ is replaced by the numeral of the constant.)

*Regular minimization.* Let $f(\vec x) = \mu z\, [g(\vec x, z) = 0]$ with $g$ total and regular, λ-defined by $G$. With Turing's combinator, let
$$
\begin{gathered}
\mathsf{search} = \Theta\,\big(\lambda s\, \vec x\, z.\, (\mathsf{iszero}\,(G\, \vec x\, z))\; z\; (s\, \vec x\,(\mathsf{succ}\, z))\big), \\
F = \lambda \vec x.\, \mathsf{search}\, \vec x\, \overline 0.
\end{gathered}
$$
By :ref{#thm-lambda-fixed-point}, $\mathsf{search}\, \vec{\overline n}\, \overline z \twoheadrightarrow_\beta (\mathsf{iszero}\,(G\, \vec{\overline n}\, \overline z))\; \overline z\; (\mathsf{search}\, \vec{\overline n}\,(\mathsf{succ}\, \overline z))$. If $g(\vec n, z) = 0$, this reduces to $\overline z$; otherwise it reduces to $\mathsf{search}\, \vec{\overline n}\,(\mathsf{succ}\, \overline z)$, hence to $\mathsf{search}\, \vec{\overline n}\, \overline{z + 1}$. By induction, $F\, \vec{\overline n} \twoheadrightarrow_\beta \mathsf{search}\, \vec{\overline n}\, \overline z$ for every $z \leq z_0 = f(\vec n)$, which exists by regularity, and finally $F\, \vec{\overline n} \twoheadrightarrow_\beta \overline{z_0}$.

**Partial functions.** For partial functions the constructions above are not adequate as they stand. For instance, the term for composition may have a normal form even if some $g_i(\vec x)$ diverges, when $H$ discards its argument — whereas $f(\vec x)$ must then be undefined. The normal form theorem avoids this problem: by :ref{#thm-kleene-normal-form}, proved in the lesson :ref{to="models-of-computation/equivalence-of-models"} by arithmetization of Turing machines (without using the λ-calculus), $f(\vec x) \simeq U(\mu s\, [g(\vec x, s) = 0])$ where $g(\vec x, s) = \overline{\mathrm{sg}}(\chi_{T_k}(e, \vec x, s))$ and $U$ are primitive recursive. Let $G$ and $U'$ λ-define $g$ and $U$, let $\mathsf{search}$ be built from $G$ as above, and let
$$
F = \lambda \vec x.\, (\mathsf{search}\, \vec x\, \overline 0)\, \mathsf I\, \mathsf I\, \big(U'\,(\mathsf{search}\, \vec x\, \overline 0)\big).
$$
If $f(\vec n)\converge$, the search succeeds at some $s_0$: then $\mathsf{search}\, \vec{\overline n}\, \overline 0 \twoheadrightarrow_\beta \overline{s_0}$ as in the total case, $\overline{s_0}\, \mathsf I\, \mathsf I \twoheadrightarrow_\beta \mathsf I^{s_0}(\mathsf I) \twoheadrightarrow_\beta \mathsf I$, and $F\, \vec{\overline n} \twoheadrightarrow_\beta \mathsf I\,\big(U'\, \overline{s_0}\big) \twoheadrightarrow_\beta \overline{U(s_0)} = \overline{f(\vec n)}$. If $f(\vec n)\diverge$, it remains to show that $F\, \vec{\overline n}$ has no normal form; by confluence, it suffices to show this for its reduct $(\mathsf{search}\, \vec{\overline n}\, \overline 0)\, \mathsf I\, \mathsf I\, (U'\,(\mathsf{search}\, \vec{\overline n}\, \overline 0))$. Here $\mathsf{search}\, \vec{\overline n}\, \overline 0$ reduces to $\mathsf{search}\, \vec{\overline n}\, \overline z$ for every $z$, and one shows that it has no **head normal form**: it reduces to no term of the form $\lambda y_1 \cdots y_j.\, y\, M_1 \cdots M_r$ (one says that it is **unsolvable**). Moreover, if $M$ has no head normal form, then neither has $M\, P_1 \cdots P_r$, which therefore has no normal form. We admit these two facts about head normal forms; they are proved in Barendregt's monograph, in the chapters on solvability and on the representation of computable functions, where this construction is carried out in detail.
:::

:::quiz[λ-definability of recursive functions]
In the case of regular minimization, why must the recursion be implemented with a fixed-point combinator rather than with a numeral iteration, as for primitive recursion?

- [x] The number of steps of the search is not known in advance, so no numeral can be used to iterate it; a fixed point allows unbounded recursion.
- [ ] Because numerals cannot be compared with $\overline 0$.

  $\mathsf{iszero}$ does exactly this.
- [ ] Because the search must return a boolean.

  It returns a numeral.

---

Why is the naive term $\lambda \vec x.\, H\,(G_1\, \vec x) \cdots (G_m\, \vec x)$ inadequate for composition of partial functions?

- [x] If $H$ ignores its first argument and $g_1(\vec x)$ diverges, the naive term may still reduce to a numeral, while by our conventions $f(\vec x)$ is undefined.

  β-reduction does not have to evaluate an argument that is discarded: normal order reduction, in particular, never does.
- [ ] Because application is not associative.

  Application associates to the left by convention; the problem is the evaluation of arguments, not the bracketing.
- [ ] Because $H$ may not be in normal form.

  Being in normal form is not the issue; the problem is that the naive term may ignore a divergent argument.
:::

:::theorem{#thm-lambda-definable-recursive}
Every λ-definable partial function is partial recursive.
:::

:::proof{of=thm-lambda-definable-recursive}
Code λ-terms by integers, for instance using de Bruijn indices to avoid α-equivalence issues and the sequence coding of the lesson :ref{to="models-of-computation/coding-sequences"}. The following are primitive recursive on codes (we omit the routine verifications): substitution, the predicate "$M$ is in normal form", the function computing the result of one normal order step, its $t$-th iterate $N(M, t)$, the code of $\overline n$ as a function of $n$, and the predicate "$M$ is a numeral" together with the extraction of its value. If $F$ λ-defines $f$, let $M_{\vec n}$ be the code of $F\, \overline{n_1} \cdots \overline{n_k}$; then
$$
f(\vec n) \simeq \mathrm{val}\big(N(M_{\vec n},\ \mu t\, [N(M_{\vec n}, t) \text{ is in normal form}])\big).
$$
By :ref{#thm-normal-order}, the search terminates exactly when $F\, \overline{n_1} \cdots \overline{n_k}$ has a normal form, which is then $\overline{f(\vec n)}$.
:::

Thus λ-definability coincides with partial recursiveness, and the next lesson shows that both coincide with Turing computability. These equivalences were established by Kleene (1936) and Turing (1936–1937). Together with Turing's analysis of mechanical computation, they turned Church's proposal — identifying effective computability with λ-definability — into a widely accepted thesis (see the lesson :ref{to="models-of-computation/church-turing-thesis"}).

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
Write $\mathsf{fact} = \mathsf{Y}\, F$. By the fixed point property, $\mathsf{fact}\, \overline 3 =_\beta F\, \mathsf{fact}\, \overline 3 \twoheadrightarrow_\beta (\mathsf{iszero}\, \overline 3)\, \overline 1\, (\mathsf{mult}\, \overline 3\, (\mathsf{fact}\,(\mathsf{pred}\, \overline 3)))$, which reduces to $\mathsf{mult}\, \overline 3\, (\mathsf{fact}\, \overline 2)$; continuing down to $\mathsf{fact}\, \overline 0 =_\beta \overline 1$ gives $\mathsf{fact}\, \overline 3 =_\beta \overline 6$. Since $\overline 6$ is a normal form, $\mathsf{fact}\, \overline 3 \twoheadrightarrow_\beta \overline 6$ by :ref{#cor-unique-normal-form}, and normal order reaches it by :ref{#thm-normal-order}. Normal order contracts the conditional before evaluating the recursive call. Applicative order would first try to normalize the subterm $\mathsf{Y}\, F$, whose reduction $\mathsf{Y}\, F \to W\, W \to F\,(W\, W) \to F\,(F\,(W\, W)) \to \cdots$ never terminates.
:::
::::

## Notes and references

The definability of the predecessor was found by Kleene in 1932, and the equivalence between λ-definability and general recursiveness (for total functions) was proved by Kleene in 1936. The combinator $\Theta$ is due to Turing (1937).

- S. C. Kleene, *λ-definability and recursiveness*, Duke Mathematical Journal 2 (1936), 340–353.
- A. M. Turing, *The p-function in λ-K-conversion*, Journal of Symbolic Logic 2 (1937), 164.
- H. P. Barendregt, *The Lambda Calculus: Its Syntax and Semantics*, North-Holland, 1984.
