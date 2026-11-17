---
title: The low basis theorem in IΣ₁
summary: Every unbounded Δ₁-definable binary tree of a model of IΣ₁ has a path whose jump is Δ₂-definable in the model, obtained by choosing at each length the least guess that keeps the tree unbounded; the classical low basis theorem, and the relativization to IΣₘ₊₁.
duration: 30
prerequisites: [trees-isigma1, pi01-classes/basis-theorems]
---

The classical proof of the low basis theorem (:ref{#thm-low-basis}) is a recursion: at step $e$, the oracle $\emptyset'$ says whether the class can be shrunk so that the $e$-th property of the path fails on all its members. Inside a model $M$ of $\mathrm I\Sigma_1$, this recursion is not available, since the statement that the correct answers up to $e$ exist is $\Sigma_2$, and $\mathrm I\Sigma_1$ has no induction for it. This lesson replaces the recursion by a minimality condition: the sequence of correct answers up to $e$ is the least string, in the order :ref{#def-ee-guess-order}, whose tree is unbounded, and the least number principle for $\Pi_1$ formulas provides it for each $e$ separately. The trees, paths and the jump $J_X$ of a path over $M$ are those of the previous lesson.

:::theorem[Low basis theorem in IΣ₁]{#thm-ee-low-basis}
Let $M \models \mathrm I\Sigma_1$, and let $T$ be an unbounded binary tree of $M$, $\Delta_1$-definable in $M$ with parameters. Then $T$ has a path $X$ that is low over $M$.
:::

**Idea.** The decisions of the classical proof form a **guess**, a string $c$ where $c(i) = 0$ means "force property $i$ to fail" and $c(i) = 1$ "leave it free". The right guess forces as many failures as possible, the earlier ones first, keeping the tree unbounded: it is the $\prec$-least guess of its length whose tree is unbounded. Its existence needs only the least number principle for the $\Pi_1$ formula "the tree of $c$ is unbounded", and the guesses of different lengths cohere without any induction. We call this device the **least admissible guess**.

:::proof{of=thm-ee-low-basis}
*Guesses.* For a string $c$, let
$$
T_c = \{ \tau \in T : \forall i < \mathrm{len}(c)\ (c(i) = 0 \rightarrow \neg W(i, \tau)) \},
$$
where $c(i)$ is the digit of $c$ at $i$. By monotonicity of $W$, $T_c$ is a binary tree; it is $\Delta_1$, uniformly in $c$, by :ref{#lem-fo-collection-closure}. Let $U(c)$ say that $T_c$ is unbounded, a $\Pi_1$ formula by :ref{#lem-ee-tree-complexity}. Two facts follow from the definition: if $c \sqsubseteq c'$, then $T_{c'} \subseteq T_c$, since $c'$ imposes more conditions; and appending digits $1$ to $c$ does not change $T_c$.

*The least admissible guess.* Let $e \in M$. The string $1^e$ of length $e$ satisfies $U(1^e)$, since $T_{1^e} = T$. By the least number principle for $\Pi_1$ formulas (:ref{#prop-fo-least-number}), applied through the reversal of strings, there is a string $c_e$ of length $e$ with $U(c_e)$ that is least for the order $\prec$ of :ref{#def-ee-guess-order}. It is unique, and its graph is defined by
$$
G(e, c) \equiv \mathrm{len}(c) = e \wedge U(c) \wedge \forall c' < 2^{e+1}\ \big(\mathrm{len}(c') = e \wedge c' \prec c \rightarrow \neg U(c')\big),
$$
where the last conjunct, a bounded quantifier in front of a $\Sigma_1$ formula, is $\Sigma_1$ in $M$ by :ref{#lem-fo-collection-closure}. So $G$ is the conjunction of a $\Pi_1$ and a $\Sigma_1$ formula.

*Coherence.* Let $e \leq e'$ and $d = c_{e'} \restriction e$. Since $T_{c_{e'}} \subseteq T_d$, $U(d)$ holds, so $c_e \preceq d$. The string $c_e 1^{e' - e}$ satisfies $U$, since its tree is $T_{c_e}$; so $c_{e'} \preceq c_e 1^{e'-e}$, and comparing the first $e$ digits, $d \preceq c_e$. Hence $c_{e'} \restriction e = c_e$. Let $J(i)$ be the digit of $c_{i+1}$ at $i$; then $J(i) = c_e(i)$ for every $e > i$.

*The path.* Let $X(x) = J(e_x)$. Fix $\ell$, and let $e \geq e_\ell$, so that $e > e_x$ for all $x < \ell$. We show that some $\tau \in T_{c_e}$ of length at least $\ell$ has digit $X(x)$ at every $x < \ell$. For $x < \ell$ with $X(x) = 0$, we have $c_e(e_x) = 0$, so every $\tau \in T_{c_e}$ satisfies $\neg W(e_x, \tau)$: if $\mathrm{len}(\tau) > x$, its digit at $x$ is $0$. For $x < \ell$ with $X(x) = 1$, let $d = (c_e \restriction e_x) 0$. Then $d \prec c_{e_x + 1}$, since $c_{e_x+1} = c_e \restriction (e_x + 1)$ has digit $J(e_x) = 1$ at $e_x$, so $\neg U(d)$: there is a length $L$ at which $T_d$ has no string. By :ref{#lem-ee-tree-complexity}, $T_d$ has no string of length $\geq L$. If $\tau \in T_{c_e}$ has length $\geq L$, then $\tau \restriction L \in T_{c_e \restriction e_x}$ but $\tau \restriction L \notin T_d$, so $W(e_x, \tau \restriction L)$, hence $W(e_x, \tau)$, and the digit of $\tau$ at $x$ is $1$. The statement "for every $x < \ell$ with $c_e(e_x) = 1$ there is such an $L$" is a bounded quantifier in front of a $\Sigma_1$ formula, so $\mathrm B\Sigma_1$ gives one $L^*$ that works for all these $x$. Since $U(c_e)$, take $\tau \in T_{c_e}$ of length $\max(\ell, L^*)$: its digits below $\ell$ are the $X(x)$.

So $X \restriction \ell = \tau \restriction \ell$ exists and belongs to $T_{c_e}$ for every $e \geq e_\ell$, hence to $T_{c_e}$ for every $e$, since $T_{c_{e'}} \subseteq T_{c_e}$ for $e \leq e'$. In particular $X \restriction \ell \in T$, and $X$ is a path through $T$.

*The jump.* We show $J_X(e) = J(e)$. If $J(e) = 0$, then $c_{e+1}(e) = 0$ and $X \restriction \ell \in T_{c_{e+1}}$ for every $\ell$, so $\neg W(e, X \restriction \ell)$ for every $\ell$: $e \notin J_X$. If $J(e) = 1$, let $d = c_e 0$; then $d \prec c_{e+1}$, so $T_d$ has no string of some length $L$. But $X \restriction L \in T_{c_e}$, so $X \restriction L \notin T_d$ means $W(e, X \restriction L)$: $e \in J_X$.

*Complexity.* By existence and uniqueness of $c_{e+1}$,
$$
e \in J_X \iff \exists c\ (G(e+1, c) \wedge c(e) = 1) \iff \forall c\ (G(e+1, c) \rightarrow c(e) = 1).
$$
The first formula is $\Sigma_2$ and the second $\Pi_2$, since $G$ is the conjunction of a $\Pi_1$ and a $\Sigma_1$ formula. So $J_X$ is $\Delta_2$-definable, and $X$ is low over $M$.
:::

:::figure[The guesses of the proof of :ref{#thm-ee-low-basis} for $e \leq 3$. Each guess $c$ determines the tree $T_c$; the digit $0$ adds the condition that property $i$ fails. The least admissible guess $c_e$ is the $\prec$-least guess of length $e$ whose tree is unbounded, here $c_3 = 010$; the guess $00$ is rejected because $T_{00}$ is bounded. Admissible guesses extend each other.]
<svg class="fig" viewBox="0 0 600 250" width="600" role="img" aria-label="The tree of guesses of length at most 3; the least admissible guesses 0, 01, 010 form a branch, and the guess 00 is rejected because its tree is bounded"><line x1="300.0" y1="225.0" x2="160.0" y2="163.0" class="accent-stroke" stroke-width="2.2"/><line x1="300.0" y1="225.0" x2="440.0" y2="163.0" class="muted-stroke" stroke-width="1.2"/><line x1="160.0" y1="163.0" x2="90.0" y2="101.0" class="muted-stroke" stroke-width="1.0" stroke-dasharray="3 3"/><line x1="160.0" y1="163.0" x2="230.0" y2="101.0" class="accent-stroke" stroke-width="2.2"/><line x1="440.0" y1="163.0" x2="370.0" y2="101.0" class="muted-stroke" stroke-width="1.2"/><line x1="440.0" y1="163.0" x2="510.0" y2="101.0" class="muted-stroke" stroke-width="1.2"/><line x1="230.0" y1="101.0" x2="195.0" y2="39.0" class="accent-stroke" stroke-width="2.2"/><line x1="230.0" y1="101.0" x2="265.0" y2="39.0" class="muted-stroke" stroke-width="1.2"/><line x1="370.0" y1="101.0" x2="335.0" y2="39.0" class="muted-stroke" stroke-width="1.2"/><line x1="370.0" y1="101.0" x2="405.0" y2="39.0" class="muted-stroke" stroke-width="1.2"/><line x1="510.0" y1="101.0" x2="475.0" y2="39.0" class="muted-stroke" stroke-width="1.2"/><line x1="510.0" y1="101.0" x2="545.0" y2="39.0" class="muted-stroke" stroke-width="1.2"/><circle cx="300.0" cy="225.0" r="4.5" class="accent-fill"/><circle cx="160.0" cy="163.0" r="4.5" class="accent-fill"/><text x="160.0" y="153.0" text-anchor="middle" class="mrm" font-size="12">0</text><circle cx="440.0" cy="163.0" r="3.5" class="node"/><text x="440.0" y="153.0" text-anchor="middle" class="mrm" font-size="12">1</text><circle cx="90.0" cy="101.0" r="3.5" class="node"/><text x="90.0" y="91.0" text-anchor="middle" class="mrm" font-size="12">00</text><circle cx="230.0" cy="101.0" r="4.5" class="accent-fill"/><text x="230.0" y="91.0" text-anchor="middle" class="mrm" font-size="12">01</text><circle cx="370.0" cy="101.0" r="3.5" class="node"/><text x="370.0" y="91.0" text-anchor="middle" class="mrm" font-size="12">10</text><circle cx="510.0" cy="101.0" r="3.5" class="node"/><text x="510.0" y="91.0" text-anchor="middle" class="mrm" font-size="12">11</text><circle cx="195.0" cy="39.0" r="4.5" class="accent-fill"/><text x="195.0" y="29.0" text-anchor="middle" class="mrm" font-size="12">010</text><circle cx="265.0" cy="39.0" r="3.5" class="node"/><text x="265.0" y="29.0" text-anchor="middle" class="mrm" font-size="12">011</text><circle cx="335.0" cy="39.0" r="3.5" class="node"/><text x="335.0" y="29.0" text-anchor="middle" class="mrm" font-size="12">100</text><circle cx="405.0" cy="39.0" r="3.5" class="node"/><text x="405.0" y="29.0" text-anchor="middle" class="mrm" font-size="12">101</text><circle cx="475.0" cy="39.0" r="3.5" class="node"/><text x="475.0" y="29.0" text-anchor="middle" class="mrm" font-size="12">110</text><circle cx="545.0" cy="39.0" r="3.5" class="node"/><text x="545.0" y="29.0" text-anchor="middle" class="mrm" font-size="12">111</text><path d="M84.0,95.0 L96.0,107.0 M84.0,107.0 L96.0,95.0" class="ink-stroke" stroke-width="1.6"/><text x="86.0" y="123.0" text-anchor="middle" class="label">T₀₀ bounded: rejected</text><text x="300.0" y="244.0" text-anchor="middle" class="label">empty guess: T itself</text><text x="14.0" y="44.0" text-anchor="start" class="label">c₃ = 010</text><text x="14.0" y="106.0" text-anchor="start" class="label">c₂ = 01</text><text x="14.0" y="168.0" text-anchor="start" class="label">c₁ = 0</text></svg>
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
Apply :ref{#thm-ee-low-basis} with $M = \nat$: low over $\nat$ means low (:ref{#def-ee-jump} and the remarks after it).
:::

This is :ref{#thm-low-basis}, since every $\Pi^0_1$ class is $[T]$ for a computable binary tree $T$ (:ref{#prop-pi01-equivalent}); the classes $\mathcal P_e$ there play the role of the classes $[T_{c_e}]$ here. The proof uses exponentiation, for strings; the least number principle for $\Pi_1$ formulas, for $c_e$; and $\Sigma_1$ collection, for the complexity of $G$ and the bound $L^*$. The admissible guesses, the strings $c$ with $U(c)$, form a tree defined by a $\Pi_1$ formula, in which every node extends to nodes of every length by digits $1$; the sequence $(c_e)$ is its leftmost path, obtained as in the Kreisel basis theorem (:ref{#ex-ee-leftmost}), and the low path $X$ is read off this leftmost path.

:::remark{#rem-ee-low-basis-relativized}
The proof relativizes: if $M \models \mathrm I\Sigma_{m+1}$ and $T$ is $\Delta_{m+1}$-definable, the same proof with $\Sigma_{m+1}$, $\Pi_{m+1}$ and $\Delta_{m+1}$ in place of $\Sigma_1$, $\Pi_1$ and $\Delta_1$, using $\mathrm L\Pi_{m+1}$ and $\mathrm B\Sigma_{m+1}$, gives a path $X$ such that $J_X$, and hence $X$, is $\Delta_{m+2}$-definable.
:::

::::exercise{#ex-ee-pi1-trees difficulty=2 objective="Extend the low basis theorem in $\mathrm I\Sigma_1$ from $\Delta_1$ trees to $\Pi_1$ trees, by the same device as for $\Pi^0_1$ classes."}
Let $M \models \mathrm I\Sigma_1$ and let $T$ be an unbounded binary tree of $M$ defined by a $\Pi_1$ formula $\forall s\ \delta(\tau, s)$, with $\delta$ bounded and with parameters. Show that $T$ has a path that is low over $M$.

:::solution
Let $T'$ be the set of strings $\tau$ such that $\delta(\sigma, s)$ holds for every string $\sigma \sqsubseteq \tau$ and every $s < \mathrm{len}(\tau)$. Since $\sigma \sqsubseteq \tau$ implies $\sigma \leq \tau$ (:ref{#lem-strings-model}), the quantifier over $\sigma$ is bounded by $\tau$, and $T'$ is defined by a bounded formula, so it is $\Delta_1$-definable. It is a tree: if $\tau' \sqsubseteq \tau \in T'$, the prefixes of $\tau'$ are prefixes of $\tau$ and $\mathrm{len}(\tau') \leq \mathrm{len}(\tau)$, so the conditions for $\tau'$ are among those for $\tau$. It contains $T$: if $\tau \in T$, every prefix $\sigma$ of $\tau$ is in $T$, so $\delta(\sigma, s)$ holds for all $s$. Hence $T'$ is unbounded, and :ref{#thm-ee-low-basis} gives a path $X$ through $T'$ that is low over $M$.

$X$ is a path through $T$. Let $\ell \in M$ and $\sigma = X \restriction \ell$. For $s \in M$, let $L = \max(\ell, s + 1)$. Then $X \restriction L \in T'$, $\sigma \sqsubseteq X \restriction L$ and $s < L$, so $\delta(\sigma, s)$. Hence $\forall s\ \delta(\sigma, s)$, that is, $\sigma \in T$. In $\nat$, this is the passage from a $\Pi^0_1$ class given by a co-c.e. tree to the same class given by a computable tree (:ref{#prop-pi01-equivalent}).
:::
::::

## Notes and references

The low basis theorem is due to Jockusch and Soare (1972). Clote (1985) proved it in models of $\mathrm B\Sigma_2$, and Hájek and Kučera (1989) in models of $\mathrm I\Sigma_1$, with a path that is "low $\Sigma_0(\Sigma_1)$": its jump is defined by a formula built from $\Sigma_1$ formulas by connectives and bounded quantifiers, a class for which $\mathrm I\Sigma_1$ proves induction. This is Theorem I.3.8 of Hájek and Pudlák, stated for $\Delta_1$-estimated trees of sequences; their Remark I.3.21 notes the case of binary trees, and their bibliographical remarks to Chapter I give this history. In $\mathrm B\Sigma_2$, as in Clote's version, the path is low $\Delta_2$, the form that Hájek and Pudlák use in part (2) of their Theorem I.4.27; in $\mathrm I\Sigma_1$ they keep the class $\Sigma_0(\Sigma_1)$, because their arguments use induction for the low sets inside the theory. The proof given here is not taken from these sources, and we know of no published source with this formulation: it applies the leftmost path argument of the Kreisel basis theorem to the tree of admissible guesses, and gives explicit $\Sigma_2$ and $\Pi_2$ definitions of the jump in $\mathrm I\Sigma_1$, used only externally. Its correctness is checked in full above. The classical version is :ref{#thm-low-basis} of the course on $\Pi^0_1$ classes.

- C. G. Jockusch and R. I. Soare, *Π⁰₁ classes and degrees of theories*, Transactions of the American Mathematical Society 173 (1972), 33–56.
- P. Clote, *Applications of the low basis theorem in arithmetic*, in Recursion Theory Week (Oberwolfach 1984), Lecture Notes in Mathematics 1141, Springer, 1985, 65–88.
- P. Hájek and A. Kučera, *On recursion theory in IΣ₁*, Journal of Symbolic Logic 54 (1989), 576–589.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapter I, Section 3(b).


:::::exercises
::::exercise{#ex-ee-delta2-tree-no-low difficulty=1 objective="See that the low basis theorem fails for $\Delta_2$ trees, as the relativized version predicts."}
Give an infinite binary tree $T \subseteq 2^{<\nat}$, $\Delta_2$-definable in $\nat$, none of whose paths is low over $\nat$. Compare with :ref{#rem-ee-low-basis-relativized}.

:::solution
Let $T$ be the set of initial segments of the characteristic function of $\emptyset'$. It is computable in $\emptyset'$, hence $\Delta_2$-definable in $\nat$ (:ref{#thm-definable-arithmetic}, :ref{#thm-post}), infinite, and its only path is $\emptyset'$. The jump $J_{\emptyset'}$ is Turing equivalent to $\emptyset''$ (remarks after :ref{#def-ee-jump}), which is not computable in $\emptyset'$, so it is not $\Delta_2$-definable: $\emptyset'$ is not low over $\nat$. The remark, with $m = 1$, only promises a path whose jump is $\Delta_3$-definable, and $\emptyset''$ is $\Delta_3$-definable.
:::
::::

::::exercise[The leftmost path can be complete]{#ex-ee-leftmost-jump difficulty=2 lessons="trees-isigma1" objective="Contrast the Kreisel basis theorem with the low basis theorem, with a computable tree whose leftmost path is $\emptyset'$."}
Let $(\emptyset'_s)_{s \in \nat}$ be a computable enumeration of $\emptyset'$, with $\emptyset'_s \subseteq \emptyset'_{s+1}$ finite. Let $T$ be the set of strings $\sigma$ such that $i \notin \emptyset'_{\mathrm{len}(\sigma)}$ for every $i < \mathrm{len}(\sigma)$ with $\sigma(i) = 0$. Show that $T$ is an infinite computable tree whose leftmost path, in the sense of :ref{#ex-ee-leftmost-minimal}, is the characteristic function of $\emptyset'$. Deduce that the path of :ref{#ex-ee-leftmost} need not be low, while :ref{#thm-ee-low-basis} gives a low path through the same tree.

:::solution
$T$ is computable. If $\sigma \sqsubseteq \tau \in T$ and $\sigma(i) = 0$ with $i < \mathrm{len}(\sigma)$, then $\tau(i) = 0$, so $i \notin \emptyset'_{\mathrm{len}(\tau)} \supseteq \emptyset'_{\mathrm{len}(\sigma)}$; so $T$ is a tree. Let $X$ be the characteristic function of $\emptyset'$. For every $\ell$, $X \restriction \ell \in T$: if $X(i) = 0$, then $i \notin \emptyset'$, so $i \notin \emptyset'_\ell$. So $T$ is infinite and $X$ is a path. Let $Y$ be any path and $i$ with $Y(i) = 0$. If $i \in \emptyset'$, say $i \in \emptyset'_s$, then $Y \restriction \ell$ for $\ell > \max(i, s)$ has digit $0$ at $i$ and $i \in \emptyset'_\ell$, so $Y \restriction \ell \notin T$, a contradiction. So $Y(i) = 0$ implies $X(i) = 0$. If $X \neq Y$, at the first difference $i$, $X(i) = 0$ and $Y(i) = 1$; so $X \restriction \ell \preceq Y \restriction \ell$ for every $\ell$, and $X$ is the leftmost path. It is the path built in :ref{#ex-ee-leftmost}, by :ref{#ex-ee-leftmost-minimal}: the strings $\sigma_\ell$ are the restrictions of the leftmost path. Since $\emptyset'' \not\leq_T \emptyset'$, $X$ is not low. The low path given by :ref{#thm-ee-low-basis} is another path; it is not the leftmost one.
:::
::::

::::exercise{#ex-ee-low-initial-segments difficulty=2 objective="Define the initial segments of the low path by $\Sigma_2$ and $\Pi_2$ formulas without collection for $\Sigma_2$ formulas."}
In the proof of :ref{#thm-ee-low-basis}, show that the relation $s = X \restriction L$ is defined in $M$ both by a $\Sigma_2$ formula and by a $\Pi_2$ formula. Explain why the definition "$s$ is a string of length $L$ and $\forall x < L\ (x \in s \leftrightarrow X(x) = 1)$" does not give this directly in $\mathrm I\Sigma_1$.

:::solution
For $x < L$, $e_x < e_L$, since $x \mapsto e_x$ is strictly increasing, and $X(x) = J(e_x) = c_{e_L}(e_x)$ by the coherence of the guesses. Let $\beta(s, L, c)$ be "$s$ is a string of length $L$ and $\forall x < L\ (x \in s \leftrightarrow c(e_x) = 1)$", a bounded quantifier in front of a $\Delta_1$ formula, hence $\Delta_1$ by :ref{#lem-fo-collection-closure}. By existence and uniqueness of $c_{e_L}$,
$$
s = X \restriction L \iff \exists c\ \big(G(e_L, c) \wedge \beta(s, L, c)\big) \iff \forall c\ \big(G(e_L, c) \rightarrow \beta(s, L, c)\big).
$$
Since $G$ is the conjunction of a $\Pi_1$ and a $\Sigma_1$ formula, the first formula is $\Sigma_2$ and the second $\Pi_2$. The direct definition puts a bounded quantifier $\forall x < L$ in front of the $\Delta_2$ formula $X(x) = 1$. A bounded quantifier in front of a $\Sigma_2$ formula is equivalent to a $\Sigma_2$ formula in $\mathrm B\Sigma_2$ (:ref{#lem-fo-collection-closure}), which $\mathrm I\Sigma_1$ does not prove; the single guess $c_{e_L}$ replaces the $L$ separate questions $X(x) = 1$.
:::
::::

::::exercise{#ex-ee-low-separation difficulty=2 objective="Apply the low basis theorem in $\mathrm I\Sigma_1$ to separate two disjoint $\Sigma_1$-definable sets by a $\Delta_2$-definable set."}
Let $M \models \mathrm I\Sigma_1$, and let $A = \{ i : \exists w\ \alpha(i, w) \}$ and $B = \{ i : \exists w\ \beta(i, w) \}$ be disjoint, with $\alpha, \beta$ bounded formulas with parameters. Show that there is a $\Delta_2$-definable set $C \subseteq M$ with $A \subseteq C$ and $B \cap C = \emptyset$.

:::solution
Let $T$ be the set of strings $\sigma$ such that for all $i, w < \mathrm{len}(\sigma)$, $\alpha(i, w)$ implies $\sigma(i) = 1$ and $\beta(i, w)$ implies $\sigma(i) = 0$. It is defined by a bounded formula. It is a tree, since the conditions for a prefix are among those for the string. It is unbounded: for $\ell \in M$, by :ref{#thm-delta0-comprehension} some $c < 2^\ell$ satisfies $\forall i < \ell\ (i \in c \leftrightarrow \exists w < \ell\ \alpha(i, w))$, and $\sigma = 2^\ell + c$ is a string of length $\ell$ with these digits (:ref{#lem-ack-basic}). If $i, w < \ell$ and $\beta(i, w)$, then $\sigma(i) = 0$: otherwise $\alpha(i, w')$ for some $w'$, and $i \in A \cap B$. So $\sigma \in T$.

By :ref{#thm-ee-low-basis}, $T$ has a path $X$ low over $M$, hence $\Delta_2$-definable (remarks after :ref{#def-ee-jump}). Let $C = \{ i : X(i) = 1 \}$. If $i \in A$, with $\alpha(i, w)$, let $\ell > \max(i, w)$: $X \restriction \ell \in T$, so $X(i) = 1$. Similarly $i \in B$ implies $X(i) = 0$. In $\nat$, this is the classical fact that two disjoint c.e. sets are separated by a low set.
:::
::::
:::::
