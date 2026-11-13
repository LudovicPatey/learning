---
title: The low basis theorem in IΣ₁
summary: Binary trees and their paths inside a model of IΣ₁; the Σ₁ properties of a path and its jump over the model; every unbounded Δ₁-definable binary tree has a path whose jump is Δ₂-definable in the model, obtained by choosing at each length the least guess that keeps the tree unbounded.
duration: 45
prerequisites: [cuts-and-extensions/weak-konig-cuts, truth-and-provability/truth-definitions, pi01-classes/basis-theorems]
---

The completeness theorem builds a model of a consistent theory from a path through the tree of finite attempts to complete the theory. To build models *inside* a model $M$ of arithmetic, as the next lesson does, one needs a path through a tree definable in $M$, with enough control to reason about it in $M$. In $\nat$, the low basis theorem of Jockusch and Soare (:ref{#thm-low-basis}) gives a path whose jump is computable in $\emptyset'$. This lesson proves the same result inside an arbitrary model of $\mathrm I\Sigma_1$, where the answers of $\emptyset'$ must be described by a formula. The track assumes first-order logic: completeness and compactness, and, in the next lessons, Gödel's incompleteness theorems.

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

## The low basis theorem

:::theorem[Low basis theorem in IΣ₁]{#thm-ee-low-basis}
Let $M \models \mathrm I\Sigma_1$, and let $T$ be an unbounded binary tree of $M$, $\Delta_1$-definable in $M$ with parameters. Then $T$ has a path $X$ that is low over $M$.
:::

**Idea.** The proof of :ref{#thm-low-basis} asks $\emptyset'$, at step $e$, whether the class can be shrunk so that the $e$-th property fails on all its members. Here the decisions form a **guess**, a string $c$ where $c(i) = 0$ means "force property $i$ to fail" and $c(i) = 1$ "leave it free"; the right guess forces as many failures as possible, the earlier ones first, keeping the tree unbounded. A recursion on $e$ is not available in $\mathrm I\Sigma_1$, since "the correct guess of length $e$ exists" is $\Sigma_2$. But the right guess is the *least* guess, in a suitable order, whose tree is unbounded, and the least number principle for $\Pi_1$ formulas gives it for each $e$ separately. We call this device the **least admissible guess**.

:::proof{of=thm-ee-low-basis}
*Guesses.* For a string $c$, let
$$
T_c = \{ \tau \in T : \forall i < \mathrm{len}(c)\ (c(i) = 0 \rightarrow \neg W(i, \tau)) \},
$$
where $c(i)$ is the digit of $c$ at $i$. By monotonicity of $W$, $T_c$ is a binary tree; it is $\Delta_1$, uniformly in $c$, by :ref{#lem-fo-collection-closure}. Let $U(c)$ say that $T_c$ is unbounded, a $\Pi_1$ formula by :ref{#lem-ee-tree-complexity}. Two facts follow from the definition: if $c \sqsubseteq c'$, then $T_{c'} \subseteq T_c$, since $c'$ imposes more conditions; and appending digits $1$ to $c$ does not change $T_c$.

For strings $c \neq c'$ of the same length, let $c \prec c'$ if $c(i) = 0$ at the least $i$ where they differ. This is a bounded relation, and the map sending $c$ to the string with the same digits in reverse order, which exists by :ref{#thm-delta0-comprehension}, turns $\prec$ into the order $<$ of $M$.

*The least admissible guess.* Let $e \in M$. The string $1^e$ of length $e$ satisfies $U(1^e)$, since $T_{1^e} = T$. By the least number principle for $\Pi_1$ formulas (:ref{#prop-fo-least-number}), applied through the reversal, there is a $\prec$-least string $c_e$ of length $e$ with $U(c_e)$. It is unique, and its graph is defined by
$$
G(e, c) \equiv \mathrm{len}(c) = e \wedge U(c) \wedge \forall c' < 2^{e+1}\ \big(\mathrm{len}(c') = e \wedge c' \prec c \rightarrow \neg U(c')\big),
$$
the conjunction of a $\Pi_1$ formula and of a bounded quantifier in front of a $\Sigma_1$ formula, which is $\Sigma_1$ in $M$ by :ref{#lem-fo-collection-closure}.

*Coherence.* Let $e \leq e'$ and $d = c_{e'} \restriction e$. Since $T_{c_{e'}} \subseteq T_d$, $U(d)$ holds, so $c_e \preceq d$. The string $c_e 1^{e' - e}$ satisfies $U$, since its tree is $T_{c_e}$; so $c_{e'} \preceq c_e 1^{e'-e}$, and comparing the first $e$ digits, $d \preceq c_e$. Hence $c_{e'} \restriction e = c_e$. Let $J(i)$ be the digit of $c_{i+1}$ at $i$; then $J(i) = c_e(i)$ for every $e > i$.

*The path.* Let $X(x) = J(e_x)$. Fix $\ell$, and let $e \geq e_\ell$, so that $e > e_x$ for all $x < \ell$. We show that some $\tau \in T_{c_e}$ of length at least $\ell$ has digit $X(x)$ at every $x < \ell$. For $x < \ell$ with $X(x) = 0$, we have $c_e(e_x) = 0$, so every $\tau \in T_{c_e}$ satisfies $\neg W(e_x, \tau)$: if $\mathrm{len}(\tau) > x$, its digit at $x$ is $0$. For $x < \ell$ with $X(x) = 1$, let $d = (c_e \restriction e_x) 0$. Then $d \prec c_{e_x + 1}$, so $\neg U(d)$: there is a length $L$ at which $T_d$ has no string. By :ref{#lem-ee-tree-complexity}, $T_d$ has no string of length $\geq L$. If $\tau \in T_{c_e}$ has length $\geq L$, then $\tau \restriction L \in T_{c_e \restriction e_x}$ but $\tau \restriction L \notin T_d$, so $W(e_x, \tau \restriction L)$, hence $W(e_x, \tau)$, and the digit of $\tau$ at $x$ is $1$. The statement "for every $x < \ell$ with $c_e(e_x) = 1$ there is such an $L$" is a bounded quantifier in front of a $\Sigma_1$ formula, so $\mathrm B\Sigma_1$ gives one $L^*$ that works for all these $x$. Since $U(c_e)$, take $\tau \in T_{c_e}$ of length $\max(\ell, L^*)$: its digits below $\ell$ are the $X(x)$.

So $X \restriction \ell = \tau \restriction \ell$ exists and belongs to $T_{c_e}$ for every $e \geq e_\ell$, hence to $T_{c_e}$ for every $e$, since $T_{c_{e'}} \subseteq T_{c_e}$ for $e \leq e'$. In particular $X \restriction \ell \in T$, and $X$ is a path through $T$.

*The jump.* We show $J_X(e) = J(e)$. If $J(e) = 0$, then $c_{e+1}(e) = 0$ and $X \restriction \ell \in T_{c_{e+1}}$ for every $\ell$, so $\neg W(e, X \restriction \ell)$ for every $\ell$: $e \notin J_X$. If $J(e) = 1$, let $d = c_e 0$; then $d \prec c_{e+1}$, so $T_d$ has no string of some length $L$. But $X \restriction L \in T_{c_e}$, so $X \restriction L \notin T_d$ means $W(e, X \restriction L)$: $e \in J_X$.

*Complexity.* By existence and uniqueness of $c_{e+1}$,
$$
e \in J_X \iff \exists c\ (G(e+1, c) \wedge c(e) = 1) \iff \forall c\ (G(e+1, c) \rightarrow c(e) = 1).
$$
The first formula is $\Sigma_2$ and the second $\Pi_2$, since $G$ is the conjunction of a $\Pi_1$ and a $\Sigma_1$ formula. So $J_X$ is $\Delta_2$-definable, and $X$ is low over $M$.
:::

:::figure[The guesses of the proof of :ref{#thm-ee-low-basis} for $e \leq 3$. Each guess $c$ determines the tree $T_c$; the digit $0$ adds the condition that property $i$ fails. The least admissible guess $c_e$ is the $\prec$-least guess of length $e$ whose tree is unbounded, here $c_3 = 010$; the guess $00$ is rejected because $T_{00}$ is bounded. Admissible guesses extend each other.]
<svg class="fig" viewBox="0 0 600 250" width="600" role="img" aria-label="The tree of guesses of length at most 3; the least admissible guesses 0, 01, 010 form a branch, and the guess 00 is rejected because its tree is bounded"><line x1="300.0" y1="225.0" x2="160.0" y2="163.0" class="accent-stroke" stroke-width="2.2"/><line x1="300.0" y1="225.0" x2="440.0" y2="163.0" class="muted-stroke" stroke-width="1.2"/><line x1="160.0" y1="163.0" x2="90.0" y2="101.0" class="muted-stroke" stroke-width="1.0" stroke-dasharray="3 3"/><line x1="160.0" y1="163.0" x2="230.0" y2="101.0" class="accent-stroke" stroke-width="2.2"/><line x1="440.0" y1="163.0" x2="370.0" y2="101.0" class="muted-stroke" stroke-width="1.2"/><line x1="440.0" y1="163.0" x2="510.0" y2="101.0" class="muted-stroke" stroke-width="1.2"/><line x1="230.0" y1="101.0" x2="195.0" y2="39.0" class="accent-stroke" stroke-width="2.2"/><line x1="230.0" y1="101.0" x2="265.0" y2="39.0" class="muted-stroke" stroke-width="1.2"/><line x1="370.0" y1="101.0" x2="335.0" y2="39.0" class="muted-stroke" stroke-width="1.2"/><line x1="370.0" y1="101.0" x2="405.0" y2="39.0" class="muted-stroke" stroke-width="1.2"/><line x1="510.0" y1="101.0" x2="475.0" y2="39.0" class="muted-stroke" stroke-width="1.2"/><line x1="510.0" y1="101.0" x2="545.0" y2="39.0" class="muted-stroke" stroke-width="1.2"/><circle cx="300.0" cy="225.0" r="4.5" class="accent-fill"/><circle cx="160.0" cy="163.0" r="4.5" class="accent-fill"/><text x="160.0" y="153.0" text-anchor="middle" class="mrm" font-size="12">0</text><circle cx="440.0" cy="163.0" r="3.5" class="node"/><text x="440.0" y="153.0" text-anchor="middle" class="mrm" font-size="12">1</text><circle cx="90.0" cy="101.0" r="3.5" class="node"/><text x="90.0" y="91.0" text-anchor="middle" class="mrm" font-size="12">00</text><circle cx="230.0" cy="101.0" r="4.5" class="accent-fill"/><text x="230.0" y="91.0" text-anchor="middle" class="mrm" font-size="12">01</text><circle cx="370.0" cy="101.0" r="3.5" class="node"/><text x="370.0" y="91.0" text-anchor="middle" class="mrm" font-size="12">10</text><circle cx="510.0" cy="101.0" r="3.5" class="node"/><text x="510.0" y="91.0" text-anchor="middle" class="mrm" font-size="12">11</text><circle cx="195.0" cy="39.0" r="4.5" class="accent-fill"/><text x="195.0" y="29.0" text-anchor="middle" class="mrm" font-size="12">010</text><circle cx="265.0" cy="39.0" r="3.5" class="node"/><text x="265.0" y="29.0" text-anchor="middle" class="mrm" font-size="12">011</text><circle cx="335.0" cy="39.0" r="3.5" class="node"/><text x="335.0" y="29.0" text-anchor="middle" class="mrm" font-size="12">100</text><circle cx="405.0" cy="39.0" r="3.5" class="node"/><text x="405.0" y="29.0" text-anchor="middle" class="mrm" font-size="12">101</text><circle cx="475.0" cy="39.0" r="3.5" class="node"/><text x="475.0" y="29.0" text-anchor="middle" class="mrm" font-size="12">110</text><circle cx="545.0" cy="39.0" r="3.5" class="node"/><text x="545.0" y="29.0" text-anchor="middle" class="mrm" font-size="12">111</text><path d="M84.0,95.0 L96.0,107.0 M84.0,107.0 L96.0,95.0" class="ink-stroke" stroke-width="1.6"/><text x="86.0" y="123.0" text-anchor="middle" class="label">T₀₀ bounded: rejected</text><text x="300.0" y="244.0" text-anchor="middle" class="label">empty guess: T itself</text><text x="520.0" y="40.0" text-anchor="middle" class="label">c₃ = 010</text><text x="520.0" y="102.0" text-anchor="middle" class="label">c₂ = 01</text><text x="520.0" y="164.0" text-anchor="middle" class="label">c₁ = 0</text></svg>
:::

:::quiz[the least admissible guess]
Why does the proof define $c_e$ as a least element, instead of building the guesses by recursion on $e$?

- [x] A recursion would need induction for the statement "the correct guess of length $e$ exists", which is $\Sigma_2$; the least number principle for the $\Pi_1$ formula $U$ gives $c_e$ for each $e$ directly, and coherence is then checked without induction.
- [ ] Because the least number principle holds for all formulas in $\mathrm I\Sigma_1$.

  $\mathrm I\Sigma_1$ proves the least number principle for $\Sigma_1$ and $\Pi_1$ formulas (:ref{#prop-fo-least-number}), not for all formulas; the proof applies it only to $U$.
- [ ] Because there may be several admissible guesses of the same length.

  The least guess is unique, but uniqueness is not the issue: the problem is to prove existence without an induction of too high complexity.

:::

:::corollary{#cor-ee-low-basis-classical}
Every infinite computable binary tree has a low path.
:::

:::proof{of=cor-ee-low-basis-classical}
Apply :ref{#thm-ee-low-basis} with $M = \nat$, and the description of lowness over $\nat$ above.
:::

This is :ref{#thm-low-basis}, since every $\Pi^0_1$ class is $[T]$ for a computable binary tree $T$ (:ref{#prop-pi01-equivalent}); the classes $\mathcal P_e$ there play the role of the classes $[T_{c_e}]$ here. The proof uses exponentiation, for strings; the least number principle for $\Pi_1$ formulas, for $c_e$; and $\Sigma_1$ collection, for the complexity of $G$ and the bound $L^*$.

:::remark{#rem-ee-low-basis-relativized}
The proof relativizes: if $M \models \mathrm I\Sigma_{m+1}$ and $T$ is $\Delta_{m+1}$-definable, the same proof with $\Sigma_{m+1}$, $\Pi_{m+1}$ and $\Delta_{m+1}$ in place of $\Sigma_1$, $\Pi_1$ and $\Delta_1$, using $\mathrm L\Pi_{m+1}$ and $\mathrm B\Sigma_{m+1}$, gives a $\Delta_{m+2}$-definable path.
:::

## Exercises

::::exercise{#ex-ee-leftmost difficulty=2}
(**Kreisel basis theorem in $\mathrm I\Sigma_1$.**) Let $M \models \mathrm I\Sigma_1$ and $T$ an unbounded $\Delta_1$ binary tree of $M$. Call a string $\sigma$ *extendible* if $\{ \tau \in T : \sigma \sqsubseteq \tau \}$ is unbounded. Show that the extendible strings form an unbounded tree, that for each $\ell$ there is a $\prec$-least extendible string $\sigma_\ell$ of length $\ell$, that the $\sigma_\ell$ extend each other, and that they define a path whose graph is defined by the conjunction of a $\Pi_1$ and a $\Sigma_1$ formula.

:::solution
Extendibility is $\Pi_1$ (:ref{#lem-ee-tree-complexity}), and prefixes of extendible strings are extendible. If no extension of length $\ell'$ of an extendible $\sigma$ were extendible, $\mathrm B\Sigma_1$ would give one length beyond which none of them has extensions in $T$, and $\sigma$ would not be extendible. So the least number principle for $\Pi_1$ formulas, through the reversal, gives $\sigma_\ell$, and an extendible extension $\rho$ of $\sigma_\ell$ of length $\ell'$. Then $\sigma_\ell \preceq \sigma_{\ell'} \restriction \ell$, since the restriction is extendible, and $\sigma_{\ell'} \preceq \rho$ gives $\sigma_{\ell'} \restriction \ell \preceq \sigma_\ell$. So the $\sigma_\ell$ cohere and define a path. The graph is "$\sigma$ is extendible of length $\ell$, and no $\sigma' \prec \sigma$ of length $\ell$ is", a $\Pi_1$ formula and a bounded quantifier in front of a $\Sigma_1$ formula.
:::
::::

## Notes and references

The low basis theorem is due to Jockusch and Soare (1972). Clote (1985) proved it in models of $\mathrm B\Sigma_2$, and Hájek and Kučera (1989) in models of $\mathrm I\Sigma_1$, with a path whose jump is "low $\Sigma_0(\Sigma_1)$"; this is Theorem I.3.8 of Hájek and Pudlák, whose Remark I.3.21 notes the case of binary trees, and whose bibliographical remarks to Chapter I give this history. The proof given here, with the least admissible guess, is a reformulation of their construction that needs induction only for $\Pi_1$ formulas; its correctness is checked in full above. The classical version is :ref{#thm-low-basis} of the course on $\Pi^0_1$ classes. The Kreisel basis theorem of the first exercise goes back to Kreisel.

- C. G. Jockusch and R. I. Soare, *Π⁰₁ classes and degrees of theories*, Transactions of the American Mathematical Society 173 (1972), 33–56.
- P. Clote, *Applications of the low basis theorem in arithmetic*, in Recursion Theory Week (Oberwolfach 1984), Lecture Notes in Mathematics 1141, Springer, 1985, 65–88.
- P. Hájek and A. Kučera, *On recursion theory in IΣ₁*, Journal of Symbolic Logic 54 (1989), 576–589.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapter I, Section 3(b).
