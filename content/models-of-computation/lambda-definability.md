---
title: λ-definability of the partial recursive functions
summary: Head reduction, and the theorem that the λ-definable partial functions are exactly the partial recursive functions.
duration: 40
prerequisites: [lambda-programming, mu-recursion]
---

The previous lesson represented integers, booleans and pairs by λ-terms, and gave the tools to program iteration and unbounded recursion. This lesson proves that the λ-definable partial functions (:ref{#def-lambda-definable}) are exactly the partial recursive functions. One direction follows the inductive definition of the partial recursive functions, as for LOOP and WHILE programs. For partial functions one must also show that a term has **no** normal form when the function is undefined; this is done by following its head reduction, introduced in the first section. The other direction codes λ-terms by integers and searches for the normal form along normal order reduction.

## Head reduction

Normal order finds the normal form of a term when there is one, but it does not tell us when there is none. To show that a term has no normal form, it is often enough to follow only the redex at the head of the term. This section gives the two facts about head reduction used for the λ-definability of partial functions.

:::definition{#def-head-normal-form}
Every term can be written uniquely as $\lambda x_1 \cdots x_n.\, H\, R_1 \cdots R_m$, with $n, m \geq 0$, where either $H$ is a variable, or $H$ is an abstraction and $m \geq 1$. In the first case the term is in **head normal form**. In the second case the redex $H\, R_1$ is the **head redex** of the term, and contracting it is a **head step**, written $\to_h$:
$$
\lambda \vec x.\, (\lambda y.\, P)\, R_1\, R_2 \cdots R_m \to_h \lambda \vec x.\, P[R_1/y]\, R_2 \cdots R_m.
$$
The **head reduction** of a term is the sequence of head steps starting from it; it stops at a head normal form, and may be infinite. We write $\twoheadrightarrow_h$ for a finite sequence of head steps.
:::

For instance, $\mathsf{K}\, \mathsf{I}\, \Omega \to_h (\lambda y.\, \mathsf{I})\, \Omega \to_h \mathsf{I}$; the head reduction of $\Omega$ is $\Omega \to_h \Omega \to_h \cdots$; and $\lambda x.\, x\, \Omega$ is in head normal form, although it has no normal form (its only reduct is itself). Every normal form is a head normal form, since it contains no redex.

:::lemma{#lem-head-normal-order}
If a term has a normal form, its head reduction is finite. Equivalently, a term whose head reduction is infinite has no normal form.
:::

:::proof{of=lem-head-normal-order}
Let $M = \lambda \vec x.\, (\lambda y.\, P)\, R_1 \cdots R_m$ be a term which is not in head normal form. The abstractions $\lambda x_i$ are not applied to anything, so they belong to no redex, and the λ of the head redex is the leftmost λ of $M$ which belongs to a redex. Hence the head redex is the leftmost outermost redex, and the normal order step from $M$ is a head step. So the normal order reduction sequence from a term coincides with its head reduction as long as no head normal form is reached. If $M$ has a normal form, then by :ref{#thm-normal-order} its normal order reduction sequence is finite and ends with a normal form, which is a head normal form. Hence the head reduction of $M$ reaches a head normal form after finitely many steps.
:::

:::quiz[head reduction]
The term $\lambda x.\, x\, \Omega$ is in head normal form. What does this example show about :ref{#lem-head-normal-order}?

- [x] Its converse fails: a term with a finite head reduction need not have a normal form.

  Its head reduction has length $0$, while every reduct of $\lambda x.\, x\, \Omega$ is the term itself, which contains the redex of $\Omega$.
- [ ] It contradicts the lemma.

  The lemma assumes that the term has a normal form, which is not the case here.
- [ ] It shows that $\lambda x.\, x\, \Omega$ has a normal form.

  Contracting the redex inside $\Omega$ gives the same term, and there is no other redex: no reduct is in normal form.
:::

The second fact describes head reduction inside a larger term: in an application $M\, N$, the head reduction first follows that of $M$, until $M$ has become an abstraction.

:::lemma[Head reduction in context]{#lem-head-context}
1. If $M \to_h M'$, then $M[N/x] \to_h M'[N/x]$.
2. If $M \twoheadrightarrow_h M'$ and $M'$ is not an abstraction, then $M\, N \twoheadrightarrow_h M'\, N$.
3. If $M \twoheadrightarrow_h \lambda x.\, B$, then $M\, N \twoheadrightarrow_h B[N/x]$.
:::

:::proof{of=lem-head-context}
1. Write $M = \lambda \vec y.\, (\lambda z.\, P)\, R_1\, \vec R$, with bound variables distinct from $x$ and not free in $N$. Then $M[N/x] = \lambda \vec y.\, (\lambda z.\, P[N/x])\, R_1[N/x]\, \vec R[N/x]$, whose head step gives $\lambda \vec y.\, P[N/x][R_1[N/x]/z]\, \vec R[N/x]$. By :ref{#lem-substitution}, $P[N/x][R_1[N/x]/z] = P[R_1/z][N/x]$, so the result is $M'[N/x]$.
2. Two observations. First, a head step does not remove a leading abstraction: if $\lambda y.\, B$ is not in head normal form, its head redex lies in $B$, and its head step gives $\lambda y.\, B'$ with $B \to_h B'$. Hence if some term of the sequence from $M$ to $M'$ were an abstraction, all later terms would be, including $M'$; so none is. Second, a term $K$ which is not an abstraction and not in head normal form has the form $(\lambda z.\, P)\, R_1 \cdots R_m$ with $m \geq 1$; then $K\, N = (\lambda z.\, P)\, R_1 \cdots R_m\, N$ has the same head redex, so $K \to_h K'$ implies $K\, N \to_h K'\, N$. Applying this to each step gives the claim.
3. Let $M = M_0 \to_h M_1 \to_h \cdots \to_h M_r = \lambda x.\, B$, and let $i$ be the least index such that $M_i$ is an abstraction, say $M_i = \lambda x.\, B_i$. By the first observation in 2, $B_i \twoheadrightarrow_h B$. By the second observation, applied to $M_0, \dots, M_{i-1}$, which are not abstractions, $M\, N \twoheadrightarrow_h M_i\, N$. Then $M_i\, N = (\lambda x.\, B_i)\, N \to_h B_i[N/x]$, and by 1, $B_i[N/x] \twoheadrightarrow_h B[N/x]$.
:::

## Numerals in head position

The following lemma describes the head reduction of a term which computes a numeral. It is what allows one to follow the head reduction of a term that tests the value of a numeral, as the conditional $\mathsf{iszero}$ does.

:::lemma{#lem-numeral-head}
Let $M \twoheadrightarrow_\beta \overline n$. Then the head reduction of $M$ is finite, and it ends with a term of the form $\lambda f x.\, x$ if $n = 0$, and of the form $\lambda f x.\, f\, N$, for some term $N$, if $n \geq 1$.
:::

:::proof{of=lem-numeral-head}
By :ref{#lem-head-normal-order}, the head reduction of $M$ ends with a head normal form $H = \lambda y_1 \cdots y_j.\, y\, M_1 \cdots M_m$. Since head steps are β-reduction steps, $M \twoheadrightarrow_\beta H$, and by the Church–Rosser theorem $H$ and $\overline n$ have a common reduct, which is $\overline n$ itself since $\overline n$ is in normal form. As $y$ is a variable, every redex of $H$ lies inside some $M_i$; hence every reduct of $H$ has the form $\lambda y_1 \cdots y_j.\, y\, M'_1 \cdots M'_m$, with the same $j$, $y$ and $m$. Comparing with $\overline n = \lambda f x.\, f^n(x)$: $j = 2$, and either $n = 0$, $y$ is the second bound variable and $m = 0$, or $n \geq 1$, $y$ is the first bound variable and $m = 1$.
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
If $f(\vec n)\converge$, the search succeeds at some $s_0$: then $\mathsf{search}\, \vec{\overline n}\, \overline 0 \twoheadrightarrow_\beta \overline{s_0}$ as in the total case, $\overline{s_0}\, \mathsf I\, \mathsf I \twoheadrightarrow_\beta \mathsf I^{s_0}(\mathsf I) \twoheadrightarrow_\beta \mathsf I$, and $F\, \vec{\overline n} \twoheadrightarrow_\beta \mathsf I\,\big(U'\, \overline{s_0}\big) \twoheadrightarrow_\beta \overline{U(s_0)} = \overline{f(\vec n)}$. If $f(\vec n)\diverge$, then $T_k(e, \vec n, s)$ fails for every $s$, so $g(\vec n, s) = 1$ for every $s$. We show that the head reduction of $F\, \vec{\overline n}$ is infinite; by :ref{#lem-head-normal-order}, $F\, \vec{\overline n}$ then has no normal form.

Write $\mathsf{search} = \Theta\, A$ with $A = \lambda s\, \vec x\, z.\, (\mathsf{iszero}\,(G\, \vec x\, z))\; z\; (s\, \vec x\,(\mathsf{succ}\, z))$, and $\Theta = Q\, Q$ with $Q = \lambda x y.\, y\,(x\, x\, y)$. The first $k$ head steps from $F\, \vec{\overline n}$ substitute the arguments and give $\Theta\, A\, \vec{\overline n}\, \overline 0\, \mathsf I\, \mathsf I\, (U'\,(\mathsf{search}\, \vec{\overline n}\, \overline 0))$. It suffices to show that for every term $t$ such that $t \twoheadrightarrow_\beta \overline z$ for some $z$, and all terms $\vec R$,
$$
\Theta\, A\, \vec{\overline n}\, t\, \vec R \twoheadrightarrow_h \Theta\, A\, \vec{\overline n}\, (\mathsf{succ}\, t)\, \vec R \quad \text{in at least one step.}
$$
Indeed $\mathsf{succ}\, t \twoheadrightarrow_\beta \overline{z + 1}$, so the claim applies again, and the head reduction never stops.

The head reduction of $\Theta\, A\, \vec{\overline n}\, t\, \vec R$ unfolds the fixed point, $Q\, Q\, A \cdots \to_h (\lambda y.\, y\,(Q\, Q\, y))\, A \cdots \to_h A\,(\Theta\, A) \cdots$, then substitutes the arguments of $A$ and unfolds $\mathsf{iszero} = \lambda m.\, m\,(\lambda w.\, \mathsf{false})\, \mathsf{true}$. It reaches
$$
M\, (\lambda w.\, \mathsf{false})\, \mathsf{true}\; t\; T\, \vec R, \qquad \text{where } M = G\, \vec{\overline n}\, t \text{ and } T = \Theta\, A\, \vec{\overline n}\,(\mathsf{succ}\, t).
$$
Now $M \twoheadrightarrow_\beta G\, \vec{\overline n}\, \overline z \twoheadrightarrow_\beta \overline 1$, so by :ref{#lem-numeral-head}, $M \twoheadrightarrow_h \lambda f x.\, f\, N$ for some $N$. By :ref{#lem-head-context} (3), applied twice, $M\, (\lambda w.\, \mathsf{false})\, \mathsf{true} \twoheadrightarrow_h (\lambda w.\, \mathsf{false})\, N'$, where $N'$ is obtained from $N$ by substitution. This term is not an abstraction, so by :ref{#lem-head-context} (2),
$$
M\, (\lambda w.\, \mathsf{false})\, \mathsf{true}\; t\; T\, \vec R \twoheadrightarrow_h (\lambda w.\, \mathsf{false})\, N'\, t\, T\, \vec R \to_h \mathsf{false}\; t\; T\, \vec R \to_h (\lambda y.\, y)\, T\, \vec R \to_h T\, \vec R,
$$
which proves the claim. (With $\vec R$ empty, the argument shows that the head reduction of $\mathsf{search}\, \vec{\overline n}\, \overline 0$ is infinite. Barendregt's monograph calls such terms **unsolvable** and develops their theory; the proof above only needs the two lemmas on head reduction.)
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

## Notes and references

The equivalence between λ-definability and general recursiveness (for total functions) was proved by Kleene in 1936. The treatment of partial functions through head normal forms and unsolvable terms follows Barendregt's monograph; the proof given here uses only the standardization theorem (:ref{#thm-normal-order}) and the lemmas on head reduction of this lesson.

- S. C. Kleene, *λ-definability and recursiveness*, Duke Mathematical Journal 2 (1936), 340–353.
- H. P. Barendregt, *The Lambda Calculus: Its Syntax and Semantics*, North-Holland, 1984.
- J. R. Hindley, J. P. Seldin, *Lambda-Calculus and Combinators: An Introduction*, Cambridge University Press, 2008.
