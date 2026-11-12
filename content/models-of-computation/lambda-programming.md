---
title: Computing with λ-terms
summary: Church numerals, arithmetic, booleans and pairs in the pure λ-calculus, Kleene's predecessor, and fixed-point combinators.
duration: 20
prerequisites: [lambda-calculus]
---

The pure λ-calculus has no built-in data. To compute functions on integers, we represent integers, booleans and pairs by λ-terms in normal form, and operations on them by terms which reduce correctly when applied to these representations.

The guiding idea is that a datum is represented by what can be done with it. An integer $n$ is used to repeat something $n$ times, so it is represented by the operation of iterating a function $n$ times; a boolean is used to choose between two branches, so it is represented by the selection of one of two arguments. Iteration gives primitive recursion, with one difficulty, the predecessor, solved by Kleene with pairs. Unbounded search needs recursion without a bound fixed in advance, which is provided by fixed-point combinators. These are the ingredients of the proof, in the lesson :ref{to="models-of-computation/lambda-definability"}, that the λ-definable functions are exactly the partial recursive functions.

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

:::figure[Kleene's predecessor on the input $3$. The numeral $\overline 3$ applies $\Phi$ three times to the pair $(\overline 0, \overline 0)$; the first component lags one step behind the second, and $\mathsf{fst}$ returns $\overline 2$. The pairs and integers stand for the terms $\mathsf{pair}\, \overline a\, \overline b$ and the numerals.]
<svg class="fig" viewBox="0 0 560 150" width="560" role="img" aria-label="Iteration of Φ on pairs of numerals"><defs><marker id="ah-pred" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><rect class="node" x="16" y="30" width="88" height="38" rx="8"/><text x="60" y="56" text-anchor="middle" class="mrm" font-size="18">(0, 0)</text><rect class="node" x="156" y="30" width="88" height="38" rx="8"/><text x="200" y="56" text-anchor="middle" class="mrm" font-size="18">(0, 1)</text><rect class="node" x="296" y="30" width="88" height="38" rx="8"/><text x="340" y="56" text-anchor="middle" class="mrm" font-size="18">(1, 2)</text><rect class="node" x="436" y="30" width="88" height="38" rx="8"/><text x="480" y="56" text-anchor="middle" class="mrm" font-size="18">(2, 3)</text><line x1="106.0" y1="50.0" x2="153.0" y2="50.0" class="ink-stroke" stroke-width="1.4" marker-end="url(#ah-pred)"/><text x="130.0" y="40" text-anchor="middle" class="math" font-size="16">Φ</text><line x1="246.0" y1="50.0" x2="293.0" y2="50.0" class="ink-stroke" stroke-width="1.4" marker-end="url(#ah-pred)"/><text x="270.0" y="40" text-anchor="middle" class="math" font-size="16">Φ</text><line x1="386.0" y1="50.0" x2="433.0" y2="50.0" class="ink-stroke" stroke-width="1.4" marker-end="url(#ah-pred)"/><text x="410.0" y="40" text-anchor="middle" class="math" font-size="16">Φ</text><line x1="480.0" y1="70.0" x2="480.0" y2="116.0" class="ink-stroke" stroke-width="1.4" marker-end="url(#ah-pred)"/><text x="490" y="100" class="label">fst</text><text x="480" y="138" text-anchor="middle" class="mrm" font-size="18">2</text><text x="16" y="138" class="label">the pair after n steps is (n ∸ 1, n)</text></svg>
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

The definability of the predecessor was found by Kleene in 1932, as he recounts in his historical account of 1981. The combinator $\Theta$ is due to Turing (1937).

- S. C. Kleene, *Origins of recursive function theory*, Annals of the History of Computing 3 (1981), 52–67.
- A. M. Turing, *The p-function in λ-K-conversion*, Journal of Symbolic Logic 2 (1937), 164.
- H. P. Barendregt, *The Lambda Calculus: Its Syntax and Semantics*, North-Holland, 1984.
- J. R. Hindley, J. P. Seldin, *Lambda-Calculus and Combinators: An Introduction*, Cambridge University Press, 2008.
