---
title: Trees and the jump in IΣ₁
summary: Binary trees and their paths inside a model of IΣ₁; the Σ₁ properties of a path, indexed by the jump of the path over the model; the order of guesses on strings, and the Kreisel basis theorem in IΣ₁ obtained from the least number principle for Π₁ formulas.
duration: 30
prerequisites: [cuts-and-extensions/weak-konig-cuts, truth-and-provability/truth-definitions, pi01-classes/computable-members, pi01-classes/basis-theorems]
---

The completeness theorem builds a model of a consistent theory from a path through the tree of finite attempts to complete the theory. To build models *inside* a model $M$ of arithmetic, as the third lesson of this course does, one needs a path through a tree definable in $M$, with enough control to reason about it in $M$. In $\nat$, the low basis theorem of Jockusch and Soare (:ref{#thm-low-basis}) gives a path whose jump is computable in $\emptyset'$. The next lesson proves the same result inside an arbitrary model of $\mathrm I\Sigma_1$, where the answers of $\emptyset'$ must be described by a formula. This lesson sets up the objects: trees and paths in $M$, the jump of a path over $M$, and an order on strings. As a first use of the least number principle for $\Pi_1$ formulas, it ends with the Kreisel basis theorem in $\mathrm I\Sigma_1$. The course assumes first-order logic: completeness and compactness, and, from the fourth lesson on, Gödel's incompleteness theorems.

## Trees and paths in a model

Strings are coded as in :ref{#def-strings-model}: a string of length $\ell$ is a number $s$ with $2^\ell \leq s < 2^{\ell+1}$, whose digit at $i < \ell$ is $1$ if $i \in s$ and $0$ otherwise. Exponentiation is available in $\mathrm I\Sigma_1$ (:ref{#prop-isigma1-exp}), and :ref{#lem-strings-model} applies. Throughout the lesson, $M$ is a model of $\mathrm I\Sigma_1$, and definable means definable in $M$ with parameters.

:::definition{#def-ee-tree}
A **binary tree** of $M$ is a set $T \subseteq M$ of strings closed under prefixes: if $\tau \in T$ and $\sigma \sqsubseteq \tau$, then $\sigma \in T$. It is **unbounded** if it contains strings of every length $\ell \in M$. A **path** through $T$ is a function $X : M \to \{0, 1\}$ such that for every $\ell \in M$ there is a string of length $\ell$ in $M$, written $X \restriction \ell$, whose digit at $i$ is $X(i)$ for every $i < \ell$, and $X \restriction \ell \in T$.
:::

The requirement that each $X \restriction \ell$ be an element of $M$ lets $M$ see every initial segment of the path.

:::lemma{#lem-ee-tree-complexity}
Let $T$ be a $\Delta_1$-definable binary tree of $M$. Then "$T$ contains a string of length $\ell$" is $\Delta_1$ in $M$, and "$T$ is unbounded" is $\Pi_1$. If $T$ contains a string of length $\ell$, it contains strings of every length $\ell' \leq \ell$.
:::

:::proof{of=lem-ee-tree-complexity}
The strings of length $\ell$ are below $2^{\ell + 1}$, so the first property is a bounded existential quantifier in front of a $\Delta_1$ formula, which is $\Delta_1$ in $\mathrm B\Sigma_1$ by :ref{#lem-fo-collection-closure}; $M \models \mathrm B\Sigma_1$ by :ref{#thm-fo-parsons}. Unboundedness is a universal quantifier in front of it. The last statement holds because $\tau \restriction \ell' \in T$ for $\tau \in T$ (:ref{#lem-strings-model}).
:::

:::example{#ex-ee-trees}
In $\nat$, the $\Delta_1$-definable binary trees are the computable ones (:ref{#thm-definable-arithmetic}), and unbounded means infinite. The tree of initial segments of $\{0,1\}$-valued diagonally non-computable functions, cut at the stage $\mathrm{len}(\sigma)$ of the computations, is computable and infinite, and has no computable path (:ref{#thm-dnc2-no-computable}). So an unbounded $\Delta_1$ tree need not have a $\Delta_1$-definable path.
:::

## The jump of a path

A $\Sigma_1$ property of a path is witnessed by a finite part of it. As the jump does in computability, we index all of them by elements of $M$, through the formula $\mathrm{Sat}_0$ (:ref{#def-sat0}), which is $\Delta_1$ in $\mathrm I\Sigma_1$ (:ref{#thm-sat0}).

:::definition{#def-ee-jump}
For $e, \tau \in M$, let $W(e, \tau)$ be the formula: $\tau$ is a string, $e = \langle z, a \rangle$, and
$$
\exists \ell \leq \mathrm{len}(\tau)\ \exists w \leq \tau\ \mathrm{Sat}_0\big(z, \langle \tau \restriction \ell, a, w \rangle\big).
$$
The **jump of $X$ over $M$** is $J_X = \{ e \in M : W(e, X \restriction \ell) \text{ for some } \ell \}$. A set $A \subseteq M$ is **$\Sigma_1$ in $X$** if $A = \{ a : \exists \ell\ \exists w\ \delta(X \restriction \ell, a, w) \}$ for some $\Delta^*_0$ formula $\delta$ with parameters in $M$. The path $X$ is **low over $M$** if $J_X$ is $\Delta_2$-definable in $M$.
:::

The formula $W$ is $\Delta_1$ in $\mathrm I\Sigma_1$ (:ref{#lem-fo-collection-closure}) and **monotone**: if $W(e, \sigma)$ and $\sigma \sqsubseteq \tau$, then $W(e, \tau)$, since $\tau \restriction \ell = \sigma \restriction \ell$ for $\ell \leq \mathrm{len}(\sigma)$ and $\sigma \leq \tau$. If $A$ is $\Sigma_1$ in $X$ by $\delta(s, a, w)$, with its parameter paired with $a$, then $a \in A$ if and only if $\langle \ulcorner \delta \urcorner, a \rangle \in J_X$, by :ref{#cor-snowing}, since a witness $w$ is below $X \restriction L$ for $L \geq \max(\ell, w)$. So if $X$ is low over $M$, every set $\Sigma_1$ in $X$ is $\Delta_2$-definable; by :ref{#lem-variable-bounds}, the same holds with $\Delta_0$ formulas $\delta$.

The path itself is $\Sigma_1$ in $X$. Fix a $\Delta^*_0$ formula $\delta_{\mathrm{dig}}(s, a)$ that expresses $a < \mathrm{len}(s) \wedge a \in s$ in $\mathrm I\Sigma_1$, all quantities involved being below $s$, and let $e_x = \langle \ulcorner \delta_{\mathrm{dig}} \urcorner, x \rangle$. Then $W(e_x, \tau)$ holds if and only if $x < \mathrm{len}(\tau)$ and the digit of $\tau$ at $x$ is $1$, and
$$
X(x) = 1 \iff e_x \in J_X.
$$
The map $x \mapsto e_x$ is $\Delta_1$ and strictly increasing. So a path that is low over $M$ is itself $\Delta_2$-definable.

In $\nat$, $J_X \equiv_T X'$, since $J_X$ is $\Sigma^0_1(X)$ and every $\Sigma^0_1(X)$ set reduces to it; and the $\Delta_2$-definable sets are those computable in $\emptyset'$ (:ref{#thm-definable-arithmetic}, :ref{#thm-post}). So low over $\nat$ means low.

In a model of $\mathrm I\Sigma_1$, "$\Delta_2$-definable" says only that a set has a $\Sigma_2$ and a $\Pi_2$ definition. It does not give induction for the set: $\mathrm I\Sigma_1$ does not prove induction for $\Delta_2$ formulas, which is equivalent to $\mathrm B\Sigma_2$ over $\mathrm I\Delta_0 + \mathrm{exp}$ (Slaman 2004). The lessons of this course use low paths only through definability, and never by induction along them.

## The order of guesses

The proofs of this lesson and the next choose, among the strings of a given length, the least one with a $\Pi_1$ property, for the following order.

:::definition{#def-ee-guess-order}
For strings $c \neq c'$ of the same length, $c \prec c'$ if $c(i) = 0$ at the least $i$ where they differ; $c \preceq c'$ means $c \prec c'$ or $c = c'$.
:::

This is the lexicographic order with $0$ before $1$, a bounded relation. The map sending $c$ to the string with the same digits in reverse order, which exists by :ref{#thm-delta0-comprehension}, turns $\prec$ into the order $<$ of $M$: the first digit becomes the most significant one. So the least number principle for $\Pi_1$ formulas (:ref{#prop-fo-least-number}), applied to the reversed strings, gives a $\prec$-least string of length $\ell$ with a $\Pi_1$ property, whenever some string of length $\ell$ has it. Two facts are used repeatedly: if $c \preceq c'$ and both have length $\ell \geq k$, then $c \restriction k \preceq c' \restriction k$; and if $c \restriction k \prec c' \restriction k$, then $c \prec c'$.

## Exercises

::::exercise{#ex-ee-leftmost difficulty=2}
(**Kreisel basis theorem in $\mathrm I\Sigma_1$.**) Let $M \models \mathrm I\Sigma_1$ and $T$ an unbounded $\Delta_1$ binary tree of $M$. Call a string $\sigma$ *extendible* if $\{ \tau \in T : \sigma \sqsubseteq \tau \}$ is unbounded. Show that the extendible strings form an unbounded tree, that for each $\ell$ there is a $\prec$-least extendible string $\sigma_\ell$ of length $\ell$, that the $\sigma_\ell$ extend each other, and that they define a path whose graph is defined by the conjunction of a $\Pi_1$ and a $\Sigma_1$ formula.

:::solution
Extendibility is $\Pi_1$ (:ref{#lem-ee-tree-complexity}), and prefixes of extendible strings are extendible. If no extension of length $\ell'$ of an extendible $\sigma$ were extendible, $\mathrm B\Sigma_1$ would give one length beyond which none of them has extensions in $T$, and $\sigma$ would not be extendible. So the least number principle for $\Pi_1$ formulas, through the reversal, gives $\sigma_\ell$, and an extendible extension $\rho$ of $\sigma_\ell$ of length $\ell'$. Then $\sigma_\ell \preceq \sigma_{\ell'} \restriction \ell$, since the restriction is extendible, and $\sigma_{\ell'} \preceq \rho$ gives $\sigma_{\ell'} \restriction \ell \preceq \sigma_\ell$. So the $\sigma_\ell$ cohere and define a path. The graph is "$\sigma$ is extendible of length $\ell$, and no $\sigma' \prec \sigma$ of length $\ell$ is", a $\Pi_1$ formula and a bounded quantifier in front of a $\Sigma_1$ formula, which is $\Sigma_1$ by :ref{#lem-fo-collection-closure}.
:::
::::

## Notes and references

Trees in models of fragments are treated by Hájek and Pudlák in Chapter I, Section 3(b), for trees of sequences; binary trees suffice here, coded as in the course on cuts and extensions. The jump $J_X$ is a version, for $\Delta^*_0$ matrices and the satisfaction formula $\mathrm{Sat}_0$, of the relativized satisfaction of Hájek and Kučera (1989). Slaman proved that $\mathrm I\Delta_n$ and $\mathrm B\Sigma_n$ are equivalent over $\mathrm I\Delta_0 + \mathrm{exp}$; since $\mathrm I\Sigma_1$ does not prove $\mathrm B\Sigma_2$ (:ref{to="fragments-of-arithmetic/induction-collection"}), it does not prove $\Delta_2$ induction. The Kreisel basis theorem of the exercise, the existence of a path computable in $\emptyset'$ through every infinite computable binary tree, goes back to Kreisel (Soare, Theorem 8.5.1).

- P. Hájek and A. Kučera, *On recursion theory in IΣ₁*, Journal of Symbolic Logic 54 (1989), 576–589.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapter I, Section 3(b).
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, Section 8.5.
- T. A. Slaman, *Σₙ-bounding and Δₙ-induction*, Proceedings of the American Mathematical Society 132 (2004), 2449–2456.
