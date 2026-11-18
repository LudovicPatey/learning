---
title: The λ-calculus
summary: λ-terms, free variables and substitution, α-equivalence, β-reduction, normal forms, the Church–Rosser theorem, and reduction strategies.
duration: 35
prerequisites: [models-of-computation/equivalence-of-models]
---

Church's λ-calculus (1932–1936) takes a different view of computation. There are no machines and no numbers: the only objects are **functions**, and the only operations are forming a function by abstracting over a variable, and applying a function to an argument. Computation is the simplification of expressions by substituting arguments for variables. The λ-calculus is the theoretical basis of functional programming languages and of the proofs-as-programs correspondence in logic.

In the λ-calculus, functions take functions as arguments and return functions. Numbers, booleans and data structures must therefore be **encoded** as functions; this is the subject of the next lesson. Here we study the calculus itself: terms, substitution, β-reduction, and the two results that make β-reduction usable as a model of computation. The **Church–Rosser theorem** says that the order in which redexes are contracted does not affect the final result; the **standardization theorem** says that one fixed order, normal order, finds this result whenever it exists. Head reduction, the tool used to show that a term has no normal form, is introduced in the lesson :ref{to="other-models/lambda-definability"}.

## Terms

Fix an infinite set of **variables** $x, y, z, \dots$

:::definition{#def-lambda-terms}
The set $\Lambda$ of **λ-terms** is defined inductively:

- every variable $x$ is a term;
- if $M$ and $N$ are terms, then $(M\, N)$ is a term, the **application** of $M$ to $N$;
- if $M$ is a term and $x$ a variable, then $(\lambda x.\, M)$ is a term, the **abstraction** of $M$ over $x$.
:::

The intended meaning of $(\lambda x.\, M)$ is the function $x \mapsto M$. We use the following conventions to omit parentheses: outermost parentheses are dropped; application associates to the left, so $M\, N\, P$ stands for $((M\, N)\, P)$; the body of an abstraction extends as far right as possible, so $\lambda x.\, M\, N$ stands for $\lambda x.\, (M\, N)$; and $\lambda x y.\, M$ abbreviates $\lambda x.\, \lambda y.\, M$.

A function of several arguments is represented as a function returning a function (**currying**): $\lambda x y.\, M$ takes $x$ and returns the function $\lambda y.\, M$.

Some terms that will recur:
$$
\begin{gathered}
\mathsf{I} = \lambda x.\, x, \\
\mathsf{K} = \lambda x y.\, x, \\
\mathsf{S} = \lambda x y z.\, x\, z\, (y\, z), \\
\omega = \lambda x.\, x\, x, \\
\Omega = \omega\, \omega.
\end{gathered}
$$

## Free variables and substitution

:::definition{#def-free-variables}
The set $\mathrm{FV}(M)$ of **free variables** of $M$ is defined by
$$
\begin{gathered}
\mathrm{FV}(x) = \{x\}, \\
\mathrm{FV}(M\, N) = \mathrm{FV}(M) \cup \mathrm{FV}(N), \\
\mathrm{FV}(\lambda x.\, M) = \mathrm{FV}(M) \setminus \{x\}.
\end{gathered}
$$
Occurrences of $x$ in $M$ within $\lambda x.\, M$ are **bound**. A term without free variables is **closed**, or a **combinator**.
:::

For instance $\mathrm{FV}(\lambda x.\, x\, y) = \{y\}$, and $\mathsf{I}, \mathsf{K}, \mathsf{S}, \Omega$ are closed.

Substituting a term $N$ for a variable $x$ must not change the meaning of the free variables of $N$. In $\lambda y.\, x$, substituting $y$ for $x$ naively would give $\lambda y.\, y$, the identity, whereas $\lambda y.\, x$ is a constant function. The bound variable must be renamed first.

:::definition{#def-substitution}
The **substitution** $M[N/x]$ of $N$ for the free occurrences of $x$ in $M$ is defined by induction on the size of $M$ (renaming a bound variable does not change the size):

- $x[N/x] = N$, and $y[N/x] = y$ for $y \neq x$;
- $(M_1\, M_2)[N/x] = M_1[N/x]\ M_2[N/x]$;
- $(\lambda x.\, M)[N/x] = \lambda x.\, M$;
- $(\lambda y.\, M)[N/x] = \lambda y.\, M[N/x]$ if $y \neq x$ and ($y \notin \mathrm{FV}(N)$ or $x \notin \mathrm{FV}(M)$);
- $(\lambda y.\, M)[N/x] = \lambda z.\, M[z/y][N/x]$ if $y \neq x$, $y \in \mathrm{FV}(N)$ and $x \in \mathrm{FV}(M)$, where $z$ is a variable not occurring in $M$ or $N$.
:::

The last clause renames the bound variable $y$ to avoid **capturing** the free $y$ of $N$.

:::lemma[Substitution lemma]{#lem-substitution}
If $x \neq y$ and $x \notin \mathrm{FV}(L)$, then $M[N/x][L/y] = M[L/y][N[L/y]/x]$.
:::

:::proof{of=lem-substitution}
By induction on $M$, choosing bound variables of $M$ distinct from $x$, $y$ and from the free variables of $N$ and $L$ (renaming does not change the size). If $M = x$, both sides are $N[L/y]$. If $M = y$, the left side is $L$ and the right side is $L[N[L/y]/x] = L$, since $x \notin \mathrm{FV}(L)$. If $M$ is another variable, both sides are $M$. Applications follow directly from the induction hypothesis. If $M = \lambda z.\, M_1$, both sides push the substitutions inside the abstraction, and the induction hypothesis applies to $M_1$.
:::

The lemma says that two substitutions can be exchanged, provided the second one is also applied to the term substituted by the first. It is used whenever a reduction is combined with a substitution, as in the proof of the Church–Rosser theorem and in the study of head reduction in the lesson :ref{to="other-models/lambda-definability"}.

:::definition{#def-alpha}
Two terms are **α-equivalent** if one is obtained from the other by renaming bound variables, that is, by replacing subterms $\lambda y.\, M$ by $\lambda z.\, M[z/y]$ with $z \notin \mathrm{FV}(M)$.
:::

From now on, α-equivalent terms are identified: $\lambda x.\, x$ and $\lambda y.\, y$ are the same term. We also adopt the **variable convention**: in any discussion, bound variables are chosen different from the free variables. With this convention the last clause of :ref{#def-substitution} is never needed.

:::quiz[substitution]
What is $(\lambda y.\, x\, y)[y/x]$?

- [x] $\lambda z.\, y\, z$ (up to α-equivalence).

  The bound $y$ must be renamed before substituting, otherwise the free $y$ would be captured.
- [ ] $\lambda y.\, y\, y$.

  This is the result of naive substitution: the substituted $y$ has been captured by the binder.
- [ ] $\lambda y.\, x\, y$.

  $x$ is free in $\lambda y.\, x\, y$, so it is affected by the substitution.

---

What is $(\lambda x.\, x\, y)[z/x]$?

- [x] $\lambda x.\, x\, y$.

  $x$ is bound in this term: there is no free occurrence to replace.
- [ ] $\lambda x.\, z\, y$.

  The variable $x$ is bound in $\lambda x.\, x\, y$, and substitution only replaces free occurrences; the term is unchanged.
- [ ] $\lambda x.\, x\, z$.

  Only free occurrences of $x$ are replaced, and $y$ is not affected at all.
:::

## β-reduction

:::definition{#def-beta-reduction}
A **β-redex** is a term of the form $(\lambda x.\, M)\, N$; its **contractum** is $M[N/x]$. The **one-step β-reduction** $M \to_\beta M'$ holds if $M'$ is obtained from $M$ by replacing one occurrence of a redex by its contractum. Formally, $\to_\beta$ is the smallest relation such that

- $(\lambda x.\, M)\, N \to_\beta M[N/x]$;
- if $M \to_\beta M'$ then $M\, N \to_\beta M'\, N$, $N\, M \to_\beta N\, M'$ and $\lambda x.\, M \to_\beta \lambda x.\, M'$.

We write $\twoheadrightarrow_\beta$ for its reflexive transitive closure (**reduction**) and $=_\beta$ for the equivalence relation it generates (**β-conversion**).
:::

:::definition{#def-normal-form}
A term is in **β-normal form** if it contains no β-redex. A term $M$ **has a normal form** if $M \twoheadrightarrow_\beta N$ for some $N$ in normal form.
:::

Examples:

1. $\mathsf{I}\, M \to_\beta M$, and $\mathsf{K}\, M\, N \to_\beta (\lambda y.\, M)\, N \to_\beta M$ (with $y \notin \mathrm{FV}(M)$).
2. $\mathsf{S}\, \mathsf{K}\, \mathsf{K} \twoheadrightarrow_\beta \lambda z.\, \mathsf{K}\, z\, (\mathsf{K}\, z) \twoheadrightarrow_\beta \lambda z.\, z = \mathsf{I}$ (:ref{#ex-lambda-skk} gives the individual steps).
3. $\Omega = (\lambda x.\, x\, x)(\lambda x.\, x\, x) \to_\beta (\lambda x.\, x\, x)(\lambda x.\, x\, x) = \Omega$. The only reduction sequence from $\Omega$ is infinite, and $\Omega$ has no normal form: it is the λ-calculus analogue of a non-terminating computation.
4. $(\lambda x.\, y)\, \Omega$ reduces to the normal form $y$ by contracting the outer redex, but also reduces to itself by contracting $\Omega$. Some reduction sequences from this term are infinite, although it has a normal form.

:::figure[The two one-step reductions of $(\lambda x.\, y)\, \Omega$. Contracting $\Omega$ gives the same term again; contracting the outer redex gives the normal form $y$.]
<svg class="fig" viewBox="0 0 460 150" width="460" role="img" aria-label="The two reductions of the term (λx.y)Ω"><defs><marker id="ah-kom" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><rect class="node" x="72" y="74" width="116" height="40" rx="8"/><text x="130" y="101" text-anchor="middle" class="math" font-size="19"><tspan class="mrm">(</tspan>λx<tspan class="mrm">.</tspan>y<tspan class="mrm">)</tspan><tspan class="mrm">Ω</tspan></text><rect class="node" x="350" y="74" width="50" height="40" rx="8"/><text x="375" y="101" text-anchor="middle" class="math" font-size="19">y</text><line x1="188.0" y1="94.0" x2="347.0" y2="94.0" class="ink-stroke" stroke-width="1.4" marker-end="url(#ah-kom)"/><text x="269.0" y="84" text-anchor="middle" class="label">contract the outer redex</text><path d="M108,73 C80,11 180,11 152,71" class="ink-stroke" stroke-width="1.4" marker-end="url(#ah-kom)"/><text x="130" y="20" text-anchor="middle" class="label">contract Ω</text></svg>
:::

## Confluence

A term may contain several redexes, so reduction is not deterministic. The fundamental theorem of the λ-calculus states that the choices do not matter for the final result.

:::theorem[Church–Rosser, 1936]{#thm-church-rosser}
The relation $\twoheadrightarrow_\beta$ is **confluent**: if $M \twoheadrightarrow_\beta N_1$ and $M \twoheadrightarrow_\beta N_2$, there exists $P$ with $N_1 \twoheadrightarrow_\beta P$ and $N_2 \twoheadrightarrow_\beta P$.
:::

:::proof{of=thm-church-rosser}
We sketch the proof of Tait and Martin-Löf. The one-step relation $\to_\beta$ itself does not satisfy the "diamond property" (a single step on each side need not be joinable in one step each), because contracting a redex may duplicate other redexes. One introduces **parallel reduction** $\Rightarrow$, the smallest relation such that

- $x \Rightarrow x$;
- if $M \Rightarrow M'$ then $\lambda x.\, M \Rightarrow \lambda x.\, M'$;
- if $M \Rightarrow M'$ and $N \Rightarrow N'$ then $M\, N \Rightarrow M'\, N'$;
- if $M \Rightarrow M'$ and $N \Rightarrow N'$ then $(\lambda x.\, M)\, N \Rightarrow M'[N'/x]$.

Intuitively, $M \Rightarrow M'$ contracts any set of redexes present in $M$, simultaneously. One checks that ${\to_\beta} \subseteq {\Rightarrow} \subseteq {\twoheadrightarrow_\beta}$, so the reflexive transitive closure of $\Rightarrow$ is $\twoheadrightarrow_\beta$. The key lemma, proved by induction on the derivation of $M \Rightarrow M'$ with the substitution lemma (:ref{#lem-substitution}) in the case of a contracted redex, is that $M \Rightarrow M'$ and $N \Rightarrow N'$ imply $M[N/x] \Rightarrow M'[N'/x]$. From it one deduces the **diamond property**: if $M \Rightarrow N_1$ and $M \Rightarrow N_2$, then $N_1 \Rightarrow P$ and $N_2 \Rightarrow P$ for some $P$. Following Takahashi, one can take for $P$ the term $M^*$ obtained by contracting all redexes of $M$, and prove by induction on $M$ the stronger **triangle property**: $M \Rightarrow N$ implies $N \Rightarrow M^*$. A relation with the diamond property has a confluent transitive closure, by a "tiling" argument: given two sequences of $\Rightarrow$-steps from $M$, complete the grid of diamonds. The details are in Barendregt's monograph and in Takahashi's paper.
:::

:::figure[Confluence: two reduction sequences from $M$ can always be completed, by further reductions, to a common term $P$.]
<svg class="fig" viewBox="0 0 320 230" width="320" role="img" aria-label="Church–Rosser diamond"><defs><marker id="ah-cr" viewBox="0 0 14 10" refX="13" refY="5" markerWidth="11" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L7,5 L0,9 z M6,1 L13,5 L6,9 z" class="ink-fill"/></marker></defs><line x1="144.5" y1="46.7" x2="77.0" y2="102.1" class="ink-stroke" stroke-width="1.5" marker-end="url(#ah-cr)"/><line x1="175.5" y1="46.7" x2="243.0" y2="102.1" class="ink-stroke" stroke-width="1.5" marker-end="url(#ah-cr)"/><line x1="75.5" y1="128.7" x2="143.0" y2="184.1" class="muted-stroke" stroke-width="1.5" stroke-dasharray="5 4" marker-end="url(#ah-cr)"/><line x1="244.5" y1="128.7" x2="177.0" y2="184.1" class="muted-stroke" stroke-width="1.5" stroke-dasharray="5 4" marker-end="url(#ah-cr)"/><text x="160" y="40" text-anchor="middle" class="math" font-size="19">M</text><text x="60" y="122" text-anchor="middle" class="math" font-size="19">N<tspan class="mrm" font-size="12" dy="5">1</tspan></text><text x="260" y="122" text-anchor="middle" class="math" font-size="19">N<tspan class="mrm" font-size="12" dy="5">2</tspan></text><text x="160" y="204" text-anchor="middle" class="math" font-size="19">P</text><text x="160" y="120" text-anchor="middle" class="label">there exists</text></svg>
:::

:::corollary{#cor-unique-normal-form}
1. A term has at most one normal form.
2. If $M =_\beta N$, then $M$ and $N$ reduce to a common term.
3. Distinct normal forms are not β-convertible. In particular $=_\beta$ is not trivial: $\mathsf{K} \neq_\beta \mathsf{I}$.
:::

:::proof{of=cor-unique-normal-form}
1. If $M \twoheadrightarrow_\beta N_1$ and $M \twoheadrightarrow_\beta N_2$ with $N_1, N_2$ normal, confluence gives $P$ with $N_i \twoheadrightarrow_\beta P$; since normal forms do not reduce, $N_1 = P = N_2$.
2. By induction on the length of a chain of reductions and expansions connecting $M$ and $N$, using confluence to merge consecutive peaks.
3. If two normal forms are convertible, by 2 they reduce to a common term, hence are equal.
:::

:::quiz[confluence]
Which statements follow from the Church–Rosser theorem?

- [x] If a term has a normal form, every reduction sequence that terminates ends with that normal form.
- [ ] Every reduction sequence from a term with a normal form terminates.

  $(\lambda x.\, y)\, \Omega$ has normal form $y$, but contracting $\Omega$ again and again gives an infinite reduction sequence.
- [x] $\lambda x y.\, x$ and $\lambda x y.\, y$ are not β-convertible.

  They are distinct normal forms.
- [ ] Every term has a normal form.

  $\Omega$ has none.

---

Why does the proof go through parallel reduction rather than proving the diamond property for $\to_\beta$ directly?

- [x] Contracting a redex can duplicate another redex, so joining two single steps may require several steps on one side; parallel reduction can contract all copies at once.

  For instance, in $(\lambda x.\, x\, x)(\mathsf{I}\, y)$, contracting the outer redex yields two copies of $\mathsf{I}\, y$.
- [ ] Because $\to_\beta$ is not compatible with abstraction.

  $\to_\beta$ is compatible with abstraction by definition: it is the compatible closure of the contraction of redexes.
- [ ] Because $\to_\beta$ is not transitive.

  Non-transitivity is irrelevant; the issue is duplication.
:::

## Reduction strategies

Which redex should be contracted? Two natural strategies are:

- **normal order**: always contract the **leftmost outermost** redex (the one whose λ appears first from the left);
- **applicative order**: always contract a **leftmost innermost** redex, i.e. evaluate arguments before passing them.

On $(\lambda x.\, y)\, \Omega$, normal order terminates immediately with $y$, while applicative order loops forever on $\Omega$.

:::theorem[Standardization, Curry–Feys]{#thm-normal-order}
If a term has a normal form, the normal order reduction sequence starting from it is finite and ends with this normal form.
:::

We admit this theorem; proofs are in Curry and Feys and in Barendregt's monograph, and Takahashi gives a short proof with parallel reduction. It shows that normal order is a **deterministic algorithm** computing normal forms whenever they exist: a λ-term is evaluated like a program, which runs forever exactly when the term has no normal form.

:::quiz[reduction strategies]
What does applicative order do on $\mathsf{K}\, \mathsf{I}\, \Omega$?

- [x] It loops forever, trying to normalize the argument $\Omega$ before using it.

  Normal order reduces $\mathsf{K}\, \mathsf{I}\, \Omega \to (\lambda y.\, \mathsf{I})\, \Omega \to \mathsf{I}$ in two steps.
- [ ] It returns $\mathsf{I}$.

  $\mathsf K\, \mathsf I\, \Omega$ has the normal form $\mathsf I$, reached in normal order; applicative order never gets there, since it first reduces $\Omega$.
- [ ] It returns $\Omega$.

  $\Omega$ is the argument that is discarded by $\mathsf K\, \mathsf I$; no strategy returns it, and applicative order does not terminate.
:::

:::remark[η-conversion]
The relation $\lambda x.\, M\, x \to_\eta M$, for $x \notin \mathrm{FV}(M)$, expresses extensionality: both terms behave identically when applied to an argument. The theory of $\beta\eta$-conversion also satisfies the Church–Rosser theorem. We will not need it.
:::

## Exercises

::::exercise{#ex-lambda-skk difficulty=1 objective="Reduce a combinator to normal form step by step."}
Reduce $\mathsf{S}\, \mathsf{K}\, \mathsf{K}$ to normal form, writing every step, and check that $\mathsf{S}\, \mathsf{K}\, \mathsf{K}\, M \twoheadrightarrow_\beta M$ for every $M$.

:::solution
$\mathsf{S}\, \mathsf{K}\, \mathsf{K} = (\lambda x y z.\, x\, z\, (y\, z))\, \mathsf{K}\, \mathsf{K} \to_\beta (\lambda y z.\, \mathsf{K}\, z\, (y\, z))\, \mathsf{K} \to_\beta \lambda z.\, \mathsf{K}\, z\, (\mathsf{K}\, z) \to_\beta \lambda z.\, (\lambda y.\, z)\, (\mathsf{K}\, z) \to_\beta \lambda z.\, z$. Then $\mathsf{S}\, \mathsf{K}\, \mathsf{K}\, M \twoheadrightarrow_\beta \mathsf{I}\, M \to_\beta M$.
:::
::::

## Notes and references

The λ-calculus was introduced by Church in the early 1930s as part of a foundational system that turned out to be inconsistent; the pure calculus survived. The confluence theorem is due to Church and Rosser; the proof by parallel reduction is due to Tait and Martin-Löf, and its simplification by the term $M^*$ to Takahashi, who also proves the standardization theorem with parallel reductions. Barendregt's monograph is the standard reference; Hindley and Seldin give an introduction at the level of this lesson.

- A. Church, J. B. Rosser, *Some properties of conversion*, Transactions of the American Mathematical Society 39 (1936), 472–482.
- H. B. Curry, R. Feys, *Combinatory Logic*, volume I, North-Holland, 1958, for the standardization theorem.
- H. P. Barendregt, *The Lambda Calculus: Its Syntax and Semantics*, North-Holland, 1984.
- M. Takahashi, *Parallel reductions in λ-calculus*, Information and Computation 118 (1995), 120–127.
- J. R. Hindley, J. P. Seldin, *Lambda-Calculus and Combinators: An Introduction*, Cambridge University Press, 2008.

:::::exercises
::::exercise{#ex-lambda-www difficulty=1 objective="Show that a term has no normal form by describing all its reduction sequences."}
Show that the term $(\lambda x.\, x\, x\, x)(\lambda x.\, x\, x\, x)$ has no normal form, and that its reducts grow in size.

:::solution
Let $W = \lambda x.\, x\, x\, x$. Then $W\, W \to_\beta W\, W\, W \to_\beta W\, W\, W\, W \to \cdots$: the only redex of $W\, W\, \cdots\, W$ ($n$ copies) is the leftmost $W\, W$, whose contraction gives $n + 1$ copies. Every reduction sequence is therefore infinite.
:::
::::

::::exercise{#ex-lambda-fv-substitution difficulty=1 objective="Compute free variables and substitutions, renaming bound variables when needed."}
Compute $\mathrm{FV}(\lambda x.\, x\, y\, (\lambda y.\, y\, z))$, and the substitutions $(\lambda y.\, x\, y)[(\lambda z.\, z\, y)/x]$, $(x\, (\lambda x.\, x\, y))[y/x]$ and $(\lambda x.\, y)[x/y]$.

:::solution
The body $x\, y\, (\lambda y.\, y\, z)$ has free variables $\{x, y\} \cup (\{y, z\} \setminus \{y\}) = \{x, y, z\}$, so $\mathrm{FV}(\lambda x.\, x\, y\, (\lambda y.\, y\, z)) = \{y, z\}$. Note that $y$ is free at its first occurrence, although it is bound in the subterm $\lambda y.\, y\, z$.

In $(\lambda y.\, x\, y)[(\lambda z.\, z\, y)/x]$, the bound variable $y$ is free in the substituted term and $x$ is free in the body, so the last clause of :ref{#def-substitution} renames $y$ to a new variable $w$: the result is $\lambda w.\, (\lambda z.\, z\, y)\, w$.

In $(x\, (\lambda x.\, x\, y))[y/x]$, only the first occurrence of $x$ is free: the result is $y\, (\lambda x.\, x\, y)$.

In $(\lambda x.\, y)[x/y]$, the bound $x$ must be renamed: the result is $\lambda z.\, x$, a constant function with value $x$, and not the identity $\lambda x.\, x$.
:::
::::

::::exercise{#ex-lambda-substitution-hypotheses difficulty=1 objective="See why each hypothesis of the substitution lemma is needed, with counterexamples."}
Show by counterexamples that the substitution lemma :ref{#lem-substitution} fails without the hypothesis $x \neq y$, and without the hypothesis $x \notin \mathrm{FV}(L)$.

:::solution
Let $x$, $z$, $w$ be distinct variables. Without $x \neq y$: take $y = x$, $M = x$, $N = z$, $L = w$, so that $x \notin \mathrm{FV}(L)$. Then $M[N/x][L/x] = z[w/x] = z$, while $M[L/x][N[L/x]/x] = w[z/x] = w$.

Without $x \notin \mathrm{FV}(L)$: take $y$ distinct from $x$ and $z$, $M = y$, $N = z$ and $L = x$. Then $M[N/x][L/y] = y[x/y] = x$, while $M[L/y][N[L/y]/x] = x[z/x] = z$. In both cases the two sides are distinct variables.
:::
::::

::::exercise{#ex-lambda-parallel-reduction difficulty=2 objective="Complete a step of the Church–Rosser proof: parallel reduction lies between one-step reduction and reduction."}
Prove the following properties of the parallel reduction $\Rightarrow$ of the proof of :ref{#thm-church-rosser}: $M \Rightarrow M$ for every $M$; $M \to_\beta M'$ implies $M \Rightarrow M'$; and $M \Rightarrow M'$ implies $M \twoheadrightarrow_\beta M'$. Deduce that the reflexive transitive closure of $\Rightarrow$ is $\twoheadrightarrow_\beta$.

:::solution
*Reflexivity*, by induction on $M$: $x \Rightarrow x$; if $M \Rightarrow M$ then $\lambda x.\, M \Rightarrow \lambda x.\, M$; if $M \Rightarrow M$ and $N \Rightarrow N$ then $M\, N \Rightarrow M\, N$.

*${\to_\beta} \subseteq {\Rightarrow}$*, by induction on the definition of $\to_\beta$. A contraction $(\lambda x.\, M)\, N \to_\beta M[N/x]$ is obtained by the last rule of $\Rightarrow$ from $M \Rightarrow M$ and $N \Rightarrow N$. If $M \to_\beta M'$ and, by the induction hypothesis, $M \Rightarrow M'$, then $M\, N \Rightarrow M'\, N$ and $N\, M \Rightarrow N\, M'$ by the application rule and reflexivity, and $\lambda x.\, M \Rightarrow \lambda x.\, M'$.

*${\Rightarrow} \subseteq {\twoheadrightarrow_\beta}$*, by induction on the derivation of $M \Rightarrow M'$. The case $x \Rightarrow x$ is trivial. For abstraction and application, use that $\twoheadrightarrow_\beta$ is compatible with the term constructors (it is the reflexive transitive closure of a compatible relation): from $M \twoheadrightarrow_\beta M'$ and $N \twoheadrightarrow_\beta N'$ we get $\lambda x.\, M \twoheadrightarrow_\beta \lambda x.\, M'$ and $M\, N \twoheadrightarrow_\beta M'\, N \twoheadrightarrow_\beta M'\, N'$. For the last rule, $(\lambda x.\, M)\, N \twoheadrightarrow_\beta (\lambda x.\, M')\, N' \to_\beta M'[N'/x]$.

Finally, the reflexive transitive closure of $\to_\beta$ is contained in that of $\Rightarrow$, which is contained in that of $\twoheadrightarrow_\beta$, that is in $\twoheadrightarrow_\beta$ itself; the two closures are therefore equal to $\twoheadrightarrow_\beta$.
:::
::::

::::exercise{#ex-lambda-one-step-diamond difficulty=1 objective="See on an example that one-step reduction does not have the diamond property, while parallel reduction joins the two reducts."}
Let $f, y$ be variables and $M = (\lambda x.\, f\, x\, x)\, (\mathsf{I}\, y)$. Find the two terms $N_1, N_2$ with $M \to_\beta N_i$, and show that there is no term $P$ such that each $N_i$ is equal to $P$ or reduces to $P$ in one step. Show that $N_1 \Rightarrow P$ and $N_2 \Rightarrow P$ for some $P$.

:::solution
$M$ has two redexes, itself and $\mathsf{I}\, y$, so $N_1 = f\, (\mathsf{I}\, y)\, (\mathsf{I}\, y)$ and $N_2 = (\lambda x.\, f\, x\, x)\, y$. The terms reachable from $N_2$ in at most one step are $N_2$ and $f\, y\, y$, since $N_2$ has a single redex. Those reachable from $N_1$ in at most one step are $N_1$, $f\, y\, (\mathsf{I}\, y)$ and $f\, (\mathsf{I}\, y)\, y$. The two sets are disjoint. With parallel reduction, $N_1 \Rightarrow f\, y\, y$ by contracting both copies of $\mathsf{I}\, y$ at once, and $N_2 \Rightarrow f\, y\, y$.
:::
::::

::::exercise{#ex-lambda-strategy-cost difficulty=1 objective="Compare the number of steps of normal order and applicative order on a term that duplicates its argument."}
Reduce $(\lambda x.\, x\, x\, x)\, (\mathsf{I}\, \mathsf{I})$ to normal form by normal order and by applicative order, and count the steps.

:::solution
*Normal order.* The outer redex is contracted first, which copies the unevaluated argument three times:
$$
(\lambda x.\, x\, x\, x)(\mathsf{I}\, \mathsf{I}) \to (\mathsf{I}\, \mathsf{I})(\mathsf{I}\, \mathsf{I})(\mathsf{I}\, \mathsf{I}) \to \mathsf{I}\, (\mathsf{I}\, \mathsf{I})\, (\mathsf{I}\, \mathsf{I}) \to (\mathsf{I}\, \mathsf{I})(\mathsf{I}\, \mathsf{I}) \to \mathsf{I}\, (\mathsf{I}\, \mathsf{I}) \to \mathsf{I}\, \mathsf{I} \to \mathsf{I}.
$$
At each step the contracted redex is the leftmost outermost one; for instance, in $(\mathsf{I}\, \mathsf{I})(\mathsf{I}\, \mathsf{I})(\mathsf{I}\, \mathsf{I})$ the subterm $(\mathsf{I}\, \mathsf{I})(\mathsf{I}\, \mathsf{I})$ is not a redex, since $\mathsf{I}\, \mathsf{I}$ is not an abstraction. That is $6$ steps.

*Applicative order.* The argument is evaluated first:
$$
(\lambda x.\, x\, x\, x)(\mathsf{I}\, \mathsf{I}) \to (\lambda x.\, x\, x\, x)\, \mathsf{I} \to \mathsf{I}\, \mathsf{I}\, \mathsf{I} \to \mathsf{I}\, \mathsf{I} \to \mathsf{I},
$$
in $4$ steps. Normal order always finds the normal form when there is one (:ref{#thm-normal-order}), but it may repeat the evaluation of duplicated arguments; implementations with sharing of subterms avoid this.
:::
::::

::::exercise{#ex-lambda-k-equals-i difficulty=2 objective="Use the convertibility of terms to show that identifying two distinct normal forms makes all terms equal."}
Let $\approx$ be the smallest equivalence relation on terms that contains $=_\beta$ and the pair $(\mathsf{K}, \mathsf{I})$, and such that $M \approx M'$ implies $M\, N \approx M'\, N$ and $N\, M \approx N\, M'$ for all $N$. Show that $M \approx N$ for all terms $M, N$. Why does this not contradict :ref{#cor-unique-normal-form}?

:::solution
Let $N$ be any term. From $\mathsf{K} \approx \mathsf{I}$ we get $\mathsf{K}\, \mathsf{I}\, N \approx \mathsf{I}\, \mathsf{I}\, N$, applying the compatibility twice. Now $\mathsf{K}\, \mathsf{I}\, N \twoheadrightarrow_\beta \mathsf{I}$ and $\mathsf{I}\, \mathsf{I}\, N \to_\beta \mathsf{I}\, N \to_\beta N$. Since $\approx$ contains $=_\beta$ and is transitive, $\mathsf{I} \approx N$. Hence any two terms $M$, $N$ satisfy $M \approx \mathsf{I} \approx N$. There is no contradiction: :ref{#cor-unique-normal-form} says that $\mathsf{K} \neq_\beta \mathsf{I}$, so the pair $(\mathsf{K}, \mathsf{I})$ is a new equation, and the argument shows that adding it to β-conversion makes the theory trivial. The Church–Rosser theorem is what guarantees that β-conversion alone is not trivial.
:::
::::
:::::
