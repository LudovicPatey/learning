---
title: Trees and the jump in IΣ₁
summary: Binary trees and their paths inside a model of IΣ₁; the Σ₁ properties of a path, indexed by the jump of the path over the model; the order of guesses on strings, and the Kreisel basis theorem in IΣ₁ obtained from the least number principle for Π₁ formulas.
duration: 25
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

:::quiz[the complexity of trees in a model]
Why is "$T$ contains a string of length $\ell$" $\Delta_1$ in $M$, and not only $\Sigma_1$?

- [x] The strings of length $\ell$ are bounded by $2^{\ell + 1}$, so the existential quantifier is bounded, and $\mathrm B\Sigma_1$ makes a bounded quantifier in front of a $\Delta_1$ formula again $\Delta_1$.
- [ ] Because $\ell$ is a standard number.

  $\ell$ ranges over all elements of $M$, standard or not; the bound $2^{\ell + 1}$ is what matters.
- [ ] Because $T$ is finite in $M$.

  $T$ is a $\Delta_1$-definable set of $M$, in general unbounded; only its strings of a given length form a bounded set.

---

Why is "$T$ is unbounded" only $\Pi_1$?

- [x] It quantifies over all lengths $\ell \in M$, an unbounded universal quantifier in front of the $\Delta_1$ formula of the first part.
- [ ] Because $T$ may have no path.

  The existence of a path is a different, more complex, statement; unboundedness concerns lengths only.
- [ ] Because $\mathrm B\Sigma_1$ fails in $M$.

  $M$ satisfies $\mathrm B\Sigma_1$; collection does not remove an unbounded quantifier.
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

::::exercise{#ex-ee-leftmost difficulty=2 objective="Apply the least number principle for $\Pi_1$ formulas to obtain the leftmost path of an unbounded $\Delta_1$ tree."}
(**Kreisel basis theorem in $\mathrm I\Sigma_1$.**) Let $M \models \mathrm I\Sigma_1$ and $T$ an unbounded $\Delta_1$ binary tree of $M$. Call a string $\sigma$ *extendible* if $T$ contains extensions of $\sigma$ of every length $\ell \geq \mathrm{len}(\sigma)$, that is, if the tree $\{ \tau \in T : \tau \sqsubseteq \sigma \vee \sigma \sqsubseteq \tau \}$ is unbounded. Show that the extendible strings form an unbounded tree, that for each $\ell$ there is a $\prec$-least extendible string $\sigma_\ell$ of length $\ell$, that the $\sigma_\ell$ extend each other, and that they define a path whose graph is defined by the conjunction of a $\Pi_1$ and a $\Sigma_1$ formula.

:::solution
Extendibility is $\Pi_1$ (:ref{#lem-ee-tree-complexity}), and prefixes of extendible strings are extendible. If no extension of length $\ell'$ of an extendible $\sigma$ were extendible, $\mathrm B\Sigma_1$ would give one length beyond which none of them has extensions in $T$, and $\sigma$ would not be extendible. So the least number principle for $\Pi_1$ formulas, through the reversal, gives $\sigma_\ell$, and an extendible extension $\rho$ of $\sigma_\ell$ of length $\ell'$. Then $\sigma_\ell \preceq \sigma_{\ell'} \restriction \ell$, since the restriction is extendible, and $\sigma_{\ell'} \preceq \rho$ gives $\sigma_{\ell'} \restriction \ell \preceq \sigma_\ell$. So the $\sigma_\ell$ cohere and define a path. The graph is "$\sigma$ is extendible of length $\ell$, and no $\sigma' \prec \sigma$ of length $\ell$ is", a $\Pi_1$ formula and a bounded quantifier in front of a $\Sigma_1$ formula, which is $\Sigma_1$ by :ref{#lem-fo-collection-closure}.
:::
::::

## Notes and references

Trees in models of fragments are treated by Hájek and Pudlák in Chapter I, Section 3(b), for trees of sequences; binary trees suffice here, coded as in the course on cuts and extensions. The jump $J_X$ is a version, for $\Delta^*_0$ matrices and the satisfaction formula $\mathrm{Sat}_0$, of the relativized satisfaction of Hájek and Kučera (1989). Slaman proved that $\mathrm I\Delta_n$ and $\mathrm B\Sigma_n$ are equivalent over $\mathrm I\Delta_0 + \mathrm{exp}$; since $\mathrm I\Sigma_1$ does not prove $\mathrm B\Sigma_2$ (:ref{to="fragments-of-arithmetic/induction-collection"}), it does not prove $\Delta_2$ induction. The Kreisel basis theorem of :ref{#ex-ee-leftmost}, the existence of a path computable in $\emptyset'$ through every infinite computable binary tree, goes back to Kreisel (Soare, Theorem 8.5.1).

- P. Hájek and A. Kučera, *On recursion theory in IΣ₁*, Journal of Symbolic Logic 54 (1989), 576–589.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapter I, Section 3(b).
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, Section 8.5.
- T. A. Slaman, *Σₙ-bounding and Δₙ-induction*, Proceedings of the American Mathematical Society 132 (2004), 2449–2456.

:::::exercises
::::exercise{#ex-ee-tree-lengths difficulty=1 objective="Distinguish unbounded trees from trees with strings of every standard length in a non-standard model."}
Let $M \models \mathrm I\Sigma_1$ be non-standard and $a \in M$ non-standard.

1. Show that $T = \{ \sigma : \sigma \text{ is a string and } \mathrm{len}(\sigma) \leq a \}$ is a $\Delta_1$-definable binary tree of $M$ that contains strings of every length $\ell \leq a$, in particular of every standard length, but is not unbounded and has no path.
2. Let $T$ be a binary tree of $M$ such that for every $\ell \in M$ there is $\ell' \geq \ell$ for which $T$ contains a string of length $\ell'$. Show that $T$ is unbounded.

:::solution
1. The relation $\ell = \mathrm{len}(\sigma)$ is bounded (remark after :ref{#def-strings-model}), so $T$ is defined by a bounded formula with parameter $a$, and it is $\Delta_1$-definable. If $\tau \in T$ and $\sigma \sqsubseteq \tau$, then $\sigma$ is a string with $\mathrm{len}(\sigma) \leq \mathrm{len}(\tau) \leq a$, so $\sigma \in T$. For $\ell \leq a$, the number $2^\ell$ is a string of length $\ell$, since $2^\ell \leq 2^\ell < 2^{\ell + 1}$; it belongs to $T$. Every standard $\ell$ is below $a$. There is no string of length $a + 1$ in $T$, so $T$ is not unbounded; and a path $X$ would give a string $X \restriction (a + 1) \in T$ of length $a + 1$.
2. Let $\ell \in M$, and let $\tau \in T$ have length $\ell' \geq \ell$. Then $\tau \restriction \ell$ is a string of length $\ell$ (:ref{#lem-strings-model}) and a prefix of $\tau$, so it belongs to $T$. Hence $T$ contains a string of every length.

In $\nat$, the two notions coincide: a tree with strings of every standard length is unbounded, since every length is standard.
:::
::::

::::exercise{#ex-ee-delta1-path-low difficulty=1 objective="Show that a $\Delta_1$-definable path is low over the model."}
Let $M \models \mathrm I\Sigma_1$ and let $X$ be a path through a binary tree of $M$ such that $\{ x : X(x) = 1 \}$ is $\Delta_1$-definable in $M$. Show that $J_X$ is $\Sigma_1$-definable in $M$, and deduce that $X$ is low over $M$. What does this give for $M = \nat$?

:::solution
The relation "$s$ is a string of length $\ell$ and $\forall i < \ell\ (i \in s \leftrightarrow X(i) = 1)$" is a bounded quantifier in front of a $\Delta_1$ formula, so it is $\Delta_1$ in $M$ by :ref{#lem-fo-collection-closure}; by definition of a path, it holds exactly when $s = X \restriction \ell$. Hence
$$
e \in J_X \iff \exists \ell\ \exists s\ \big(s = X \restriction \ell \wedge W(e, s)\big),
$$
a $\Sigma_1$ formula, since $W$ is $\Delta_1$. A $\Sigma_1$ formula is $\Sigma_2$, and it is equivalent to a $\Pi_2$ formula obtained by adding a universal quantifier on a variable that does not occur. So $J_X$ is $\Delta_2$-definable and $X$ is low over $M$. For $M = \nat$, the $\Delta_1$-definable sets are the computable sets (:ref{#thm-definable-arithmetic}), and the statement is that a computable path is low, which is clear since $X' \equiv_T \emptyset'$ for computable $X$.
:::
::::

::::exercise{#ex-ee-guess-order-facts difficulty=1 objective="Verify the properties of the order of guesses used in the least admissible guess argument."}
Let $M \models \mathrm I\Sigma_1$ and $\ell \in M$.

1. Show that $\prec$ (:ref{#def-ee-guess-order}) is a strict linear order on the strings of length $\ell$.
2. Let $c, c'$ be strings of length $\ell$ and $k \leq \ell$. Show that $c \preceq c'$ implies $c \restriction k \preceq c' \restriction k$, and that $c \restriction k \prec c' \restriction k$ implies $c \prec c'$.
3. For a string $c$ of length $\ell$, let $r(c)$ be the string of length $\ell$ whose digit at $j < \ell$ is the digit of $c$ at $\ell - 1 - j$. Show that $c \prec c'$ if and only if $r(c) < r(c')$.

:::solution
1. For $c \neq c'$ of length $\ell$, the set of $i < \ell$ at which the digits differ is non-empty: otherwise $c = c'$ by extensionality (:ref{#lem-ack-basic}), both being below $2^{\ell + 1}$ with the same digits. It is defined by a bounded formula, so it has a least element $i_0$ by the least number principle for bounded formulas (:ref{#prop-fo-least-number}). Exactly one of $c, c'$ has digit $0$ at $i_0$, so exactly one of $c \prec c'$ and $c' \prec c$ holds. For transitivity, let $c \prec c'$ with first difference $i$ and $c' \prec c''$ with first difference $j$. If $i = j$, the digit of $c'$ at $i$ would be both $1$ and $0$. If $i < j$, then $c$ and $c''$ agree below $i$, $c$ has digit $0$ and $c''$ has the digit $1$ of $c'$ at $i$. If $j < i$, they agree below $j$, $c$ has the digit $0$ of $c'$ at $j$, and $c''$ has digit $1$. In both cases $c \prec c''$.
2. The digits of $c \restriction k$ are those of $c$ below $k$ (:ref{#lem-strings-model}). If $c = c'$ there is nothing to prove. If $c \prec c'$ with first difference $i$, then $c \restriction k \prec c' \restriction k$ if $i < k$, and $c \restriction k = c' \restriction k$ if $i \geq k$. If $c \restriction k \prec c' \restriction k$ with first difference $i < k$, then $c$ and $c'$ agree below $i$ and differ at $i$, with digit $0$ for $c$; so $c \prec c'$.
3. Let $c \prec c'$ with first difference $i$, and $j_0 = \ell - 1 - i$. Then $r(c)$ and $r(c')$ have the same digits at the positions $j$ with $j_0 < j \leq \ell$ (the digit at $\ell$ is the leading $1$), and $r(c)$ has digit $0$, $r(c')$ digit $1$ at $j_0$. Write $r(c) = 2^{j_0 + 1} u + q$ and $r(c') = 2^{j_0 + 1} u' + q'$ with $q, q' < 2^{j_0 + 1}$. By the splitting property of :ref{#lem-ack-basic}, $u$ and $u'$ have the same digits, so $u = u'$ by extensionality. The elements of $q$ are below $j_0$, so $q < 2^{j_0}$, and $j_0 \in q'$, so $q' \geq 2^{j_0}$ (:ref{#lem-ack-basic}, items 1 and 3). Hence $r(c) < 2^{j_0 + 1} u + 2^{j_0} \leq r(c')$. Conversely, if $r(c) < r(c')$, then $c \neq c'$, and $c' \prec c$ would give $r(c') < r(c)$; so $c \prec c'$ by item 1.
:::
::::

::::exercise{#ex-ee-leftmost-minimal difficulty=1 objective="Check that the path of the Kreisel basis theorem is the leftmost path of the tree."}
In the situation of :ref{#ex-ee-leftmost}, let $X_L$ be the path defined by the strings $\sigma_\ell$. Show that $X_L \restriction \ell \preceq Y \restriction \ell$ for every path $Y$ through $T$ and every $\ell \in M$.

:::solution
Let $Y$ be a path and $\ell \in M$. For every $\ell' \geq \ell$, the string $Y \restriction \ell'$ belongs to $T$, has length $\ell'$ and extends $Y \restriction \ell$; so $Y \restriction \ell$ is extendible. Since $\sigma_\ell = X_L \restriction \ell$ is the $\prec$-least extendible string of length $\ell$, $X_L \restriction \ell \preceq Y \restriction \ell$.
:::
::::

::::exercise{#ex-ee-countable-paths difficulty=2 objective="Build paths through a tree of a countable model by an external construction, and see why the low basis theorem is needed for definable paths."}
Let $M \models \mathrm I\Sigma_1$ be countable and $T$ an unbounded $\Delta_1$ binary tree of $M$; extendible strings are as in :ref{#ex-ee-leftmost}.

1. Without using the next lesson, show that $T$ has a path, by choosing extendible strings along a sequence $\ell_0 < \ell_1 < \cdots$ cofinal in $M$.
2. Suppose that every extendible string has two incomparable extendible extensions. Show that $T$ has $2^{\aleph_0}$ paths, and that some of them are not definable in $M$.

:::solution
1. Enumerate $M$ as $m_0, m_1, \dots$ and let $\ell_0 = m_0$, $\ell_{k+1} = \max(\ell_k, m_{k+1}) + 1$; the sequence is increasing and cofinal in $M$, since $\ell_k \geq m_k$. The empty string is extendible since $T$ is unbounded, and by the solution of :ref{#ex-ee-leftmost}, an extendible string of length $\ell$ has an extendible extension of each length $\ell' \geq \ell$. Choose extendible strings $\sigma_0 \sqsubseteq \sigma_1 \sqsubseteq \cdots$ with $\mathrm{len}(\sigma_k) = \ell_k$, and let $X(i)$ be the digit of $\sigma_k$ at $i$ for any $k$ with $\ell_k > i$; it does not depend on $k$. For $\ell \in M$, take $k$ with $\ell_k \geq \ell$: the string $\sigma_k \restriction \ell$ of $M$ has digit $X(i)$ at every $i < \ell$, and it belongs to $T$, since $\sigma_k$ is extendible, hence in $T$, and $T$ is closed under prefixes. So $X$ is a path.
2. Assign to each finite binary sequence $s$ an extendible string $\sigma_s$ of length at least $\ell_{|s|}$: let $\sigma_\emptyset$ be an extendible string of length $\ell_0$; given $\sigma_s$, take two incomparable extendible extensions $\rho_0, \rho_1$ of $\sigma_s$, and extendible extensions $\sigma_{s0} \sqsupseteq \rho_0$ and $\sigma_{s1} \sqsupseteq \rho_1$ of length at least $\ell_{|s| + 1}$. For $b \in 2^\nat$, the strings $\sigma_{b \restriction k}$ extend each other and have lengths cofinal in $M$, so they define a path $X_b$ as in item 1. If $b$ and $b'$ first differ at $k$, then $X_b$ and $X_{b'}$ pass through the two incomparable strings chosen above $\sigma_{b \restriction k}$, which differ at some position below both lengths; so $X_b \neq X_{b'}$. There are $2^{\aleph_0}$ paths. Since $M$ is countable, it has countably many formulas with parameters, hence countably many definable sets, and some $X_b$ is not definable.

The full binary tree satisfies the hypothesis of item 2. The construction gives paths, but no control over their definability; the low basis theorem of the next lesson gives a $\Delta_2$-definable one, for models of any cardinality.
:::
::::

::::exercise{#ex-ee-unique-path difficulty=2 objective="Combine the Kreisel basis theorem with $\Sigma_1$ collection to show that an isolated path is $\Delta_1$-definable."}
Let $M \models \mathrm I\Sigma_1$ and $T$ an unbounded $\Delta_1$ binary tree of $M$ with exactly one path $X$. Show that $\{ x : X(x) = 1 \}$ is $\Delta_1$-definable in $M$, so that $X$ is low over $M$ by :ref{#ex-ee-delta1-path-low}.

:::solution
Let $n \in M$ and let $\sigma'$ be a string of length $n$ different from $X \restriction n$. Then $\sigma'$ is not extendible (:ref{#ex-ee-leftmost}): otherwise the tree $T_{\sigma'} = \{ \tau \in T : \tau \sqsubseteq \sigma' \vee \sigma' \sqsubseteq \tau \}$ is $\Delta_1$ and unbounded, and by :ref{#ex-ee-leftmost} it has a path $Y$; the only string of length $n$ in $T_{\sigma'}$ is $\sigma'$, so $Y \restriction n = \sigma' \neq X \restriction n$, and $Y$ is a second path through $T$. So there is a length $L_{\sigma'} \geq n$ such that no string of $T$ of length $L_{\sigma'}$ extends $\sigma'$, a $\Sigma_1$ property of $\sigma'$ (a bounded quantifier in front of a $\Delta_1$ formula, :ref{#lem-fo-collection-closure}). By $\mathrm B\Sigma_1$ applied to the strings $\sigma' < 2^{n+1}$, there is a single $L_0 \geq n$ that bounds all the $L_{\sigma'}$; then no string of $T$ of length $L_0$ extends any $\sigma' \neq X \restriction n$ of length $n$, since its restriction to $L_{\sigma'}$ would. So every string of $T$ of length $L_0$ extends $X \restriction n$. Conversely, if $\sigma$ has length $n$ and every string of $T$ of some length $L$ extends $\sigma$, then $X \restriction L$ extends $\sigma$, so $\sigma = X \restriction n$. Hence
$$
\sigma = X \restriction n \iff \mathrm{len}(\sigma) = n \wedge \exists L\ \forall \tau < 2^{L+1}\ \big(\tau \in T \wedge \mathrm{len}(\tau) = L \rightarrow \sigma \sqsubseteq \tau\big),
$$
a $\Sigma_1$ formula. Then $X(x) = 1$ if and only if some $\sigma$ with $\sigma = X \restriction (x + 1)$ has digit $1$ at $x$, and $X(x) = 0$ if and only if some such $\sigma$ has digit $0$ at $x$: both are $\Sigma_1$, and $X$ is $\Delta_1$-definable. In $\nat$, this is the classical fact that the only path of a computable tree with a single path is computable.
:::
::::
:::::
