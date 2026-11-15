---
title: The Erdős–Moser theorem, cone avoidance and hyperimmunities
summary: Reservoirs in a Scott ideal; the Erdős–Moser theorem admits cone avoidance and preservation of countably many hyperimmunities, because its forcing question is not disjunctive.
duration: 45
prerequisites: [erdos-moser-design, avoidance/hyperimmunities]
---

This lesson completes the design of the previous one with its third step, the choice of the reservoirs, and proves two preservation theorems for $\mathsf{EM}$. The second is read off one feature of the question: it is not disjunctive. A construction for Ramsey's theorem for pairs satisfies each requirement on one of two sides that it does not choose, so two families of requirements may end up satisfied on different sides; a construction for $\mathsf{EM}$ satisfies every requirement on the set it builds. The next lesson turns this difference into a separation.

## Step 3: computational properties

The three-case argument of :ref{to="avoidance/forcing-question-method"} compares the answers of the question with the property to be preserved; since they are $\Sigma^0_1(X \oplus Z)$, the reservoirs $X$ must themselves be weak. The operations performed on reservoirs are restrictions computable in $X \oplus Z$ (:ref{#lem-sd-em-extension} and property 1 of the question), and the choice of a member of a non-empty $\Pi^0_1(X \oplus Z)$ class, followed by a restriction computable from it (property 2). So the reservoirs can be taken in any Scott ideal $\mathcal M$ containing $Z$, and if a weakness property $\mathcal W$ is preserved by $\mathsf{WKL}$, there is such an ideal inside $\mathcal W$ (:ref{#lem-scott-preservation}). The pigeonhole principle used in the restrictions is computably true and imposes nothing. As in most designs, the reservoirs must have the property the solution should have, with closure conditions given by the list of operations.

:::theorem{#thm-sd-em-cone}
Let $Z$ be a set and $C \not\leq_T Z$. Every $Z$-computable tournament $T$ has an infinite transitive set $G$ with $C \not\leq_T Z \oplus G$. So $\mathsf{EM}$ admits cone avoidance.
:::

:::proof{of=thm-sd-em-cone}
Let $\mathcal M$ be a Scott ideal containing $Z$ and not $C$ (:ref{#lem-scott-cone}), and use $\mathsf{EM}$ conditions with reservoirs in $\mathcal M$. Starting from $(\varepsilon, \nat)$, build a decreasing sequence $c_0 \geq c_1 \geq \cdots$, handling infinitely often each of the following tasks.

- *Growth.* Pass from $(\sigma, X)$ to the extension of :ref{#lem-sd-em-extension} for $x = \min X$; its reservoir is computable in $X \oplus Z$, hence in $\mathcal M$.
- *Requirement $e$.* For the current condition $c = (\sigma, X)$, let $U$ be the set of pairs $(x, v)$ with $v < 2$ and $c \mathrel{?{\vdash}} \Phi^{Z \oplus G}_e(x)\converge = v$, a $\Sigma^0_1(X \oplus Z)$ set. If $(x, 1 - C(x)) \in U$ for some $x$, property 1 gives an extension forcing $\Phi^{Z \oplus G}_e(x)\converge = 1 - C(x)$. If $(x, C(x)) \notin U$ for some $x$, property 2 gives an extension forcing that $\Phi^{Z \oplus G}_e(x)$ does not converge to $C(x)$. Otherwise $U$ is the graph of $C$, and $C \leq_T X \oplus Z \in \mathcal M$, which is excluded.

Let $G$ be the union of the stems. It is infinite by the growth task, and transitive since every finite subset lies in a stem. It is a member of every $c_s$: it extends the stem of $c_s$, and its later elements come from later reservoirs, contained in that of $c_s$. So $\Phi^{Z \oplus G}_e \neq C$ for every $e$.
:::

This is the argument of :ref{#thm-local-cone-avoidance} along a sequence of conditions; the abstract theorem does not apply verbatim, since $\mathsf{EM}$ conditions lack the refinement property of :ref{#def-forcing-notion} (:ref{#ex-sd-em-block}).

## Several hyperimmunities

:::definition{#def-sd-k-hyperimmunities}
Let $1 \leq k \leq \omega$. A problem $\mathsf P$ admits **preservation of $k$ hyperimmunities** if for every set $Z$, every sequence $(h_i)_{i < k}$ of $Z$-hyperimmune functions and every instance $X \leq_T Z$, there is a solution $Y$ such that every $h_i$ is $(Z \oplus Y)$-hyperimmune.
:::

For $k = 1$ this is :ref{#def-preserve-hyperimmunity}. For a fixed sequence $(h_i)$, the class $\mathcal W_{\vec h}$ of sets $W$ such that every $h_i$ is $W$-hyperimmune is a weakness property, and preservation of $k$ hyperimmunities is the preservation of all these classes. $\mathsf{WKL}$ preserves them for $k = \omega$ (:ref{#exr-wkl-hyperimmunities}). By :ref{#thm-hyperimmunity-examples}, $\mathsf{RT}^2_2$ admits preservation of one hyperimmunity. The proof uses a disjunctive question: for a pair of indices, some side $G_i$ satisfies "$\Phi^{Z \oplus G_i}_{e_i}$ does not dominate $h$", and Lachlan's disjunction gives one side satisfying all the requirements. With two functions $h_0$ and $h_1$, the requirements for $h_0$ may be satisfied on side $0$ and those for $h_1$ on side $1$, and nothing forces a common side. For $\mathsf{EM}$ the question is not disjunctive. The next lesson shows that this difference is real: $\mathsf{RT}^2_2$ does not preserve two hyperimmunities.

::::exercise{#exr-wkl-hyperimmunities difficulty=1 objective="Apply the computably dominated basis theorem to preserve countably many hyperimmunities with weak König's lemma."}
Let $(h_i)_{i \in \nat}$ be functions that are $Z$-hyperimmune. Show that every infinite $Z$-computable binary tree has a path $P$ such that every $h_i$ is $(Z \oplus P)$-hyperimmune. Deduce that $\mathsf{WKL}$ preserves $\mathcal W_{\vec h}$.

:::solution
By the computably dominated basis theorem (:ref{#thm-dominated-basis}) relativized to $Z$, the tree has a path $P$ such that every $(Z \oplus P)$-computable function is dominated by a $Z$-computable function. If a $(Z \oplus P)$-computable function $g$ dominated $h_i$, a $Z$-computable function dominating $g$ would dominate $h_i$. Given $W \in \mathcal W_{\vec h}$ and a $W$-computable tree, apply this with $Z = W$.
:::
::::

:::lemma{#lem-sd-em-compact}
Let $\mathcal M$ be a Scott ideal containing $Z$. The question of :ref{#lem-sd-em-question} is compact: if $c \mathrel{?{\vdash}} \Phi^{Z \oplus G}_e(x)\converge$, there is $k$ with $c \mathrel{?{\vdash}} \Phi^{Z \oplus G}_e(x)\converge < k$.
:::

:::proof{of=lem-sd-em-compact}
In the proof of :ref{#lem-sd-em-question}, a positive answer gives a bound $\ell$ such that for every string $\beta$ of length $\ell$ there is a witness $(i, \tau)$ with $|\tau| \leq \ell$ and $\Phi^{Z \oplus \tau}_e(x)[\ell]\converge$. There are finitely many such pairs; let $k$ exceed all the values $\Phi^{Z \oplus \tau}_e(x)[\ell]$. For every set $B$, the witness for $B \uh \ell$ is a witness for the sentence $\Phi^{Z \oplus G}_e(x)\converge < k$.
:::

:::theorem[Patey]{#thm-sd-em-hyperimmunities}
$\mathsf{EM}$ admits preservation of $\omega$ hyperimmunities: for every set $Z$, every sequence $(h_i)_{i \in \nat}$ of $Z$-hyperimmune functions and every $Z$-computable tournament $T$, there is an infinite transitive set $G$ such that every $h_i$ is $(Z \oplus G)$-hyperimmune.
:::

:::proof{of=thm-sd-em-hyperimmunities}
By :ref{#exr-wkl-hyperimmunities} and :ref{#lem-scott-preservation}, there is a Scott ideal $\mathcal M$ containing $Z$ such that every $h_i$ is $X$-hyperimmune for every $X \in \mathcal M$. Build a sequence of $\mathsf{EM}$ conditions with reservoirs in $\mathcal M$ as in :ref{#thm-sd-em-cone}, with the growth task and, for each pair $(e, i)$, the following task. Let $c = (\sigma, X)$ be the current condition.

- If $c \mathrel{?{\nvdash}} \Phi^{Z \oplus G}_e(x)\converge$ for some $x$, property 2 gives an extension forcing $\Phi^{Z \oplus G}_e(x)\diverge$.
- Otherwise, by :ref{#lem-sd-em-compact}, for every $x$ there is $k$ with $c \mathrel{?{\vdash}} \Phi^{Z \oplus G}_e(x)\converge < k$. Let $g(x)$ be the first such $k$ found in an enumeration of these pairs computable in $X \oplus Z$; $g$ is total and $(X \oplus Z)$-computable. Since $X \oplus Z \in \mathcal M$, $h_i$ is $(X \oplus Z)$-hyperimmune, so $g(x) < h_i(x)$ for some $x$, and property 1 gives an extension forcing $\Phi^{Z \oplus G}_e(x)\converge < g(x)$.

In both cases every member $G$ of the extension has $\Phi^{Z \oplus G}_e$ partial or below $h_i$ at some point, so $\Phi^{Z \oplus G}_e$ does not dominate $h_i$. The union $G$ of the stems is an infinite transitive set and a member of every condition of the sequence, so no $\Phi^{Z \oplus G}_e$ dominates any $h_i$.
:::

:::quiz[several hyperimmunities]
Why can the requirements for all the functions $h_i$ be satisfied by the same set $G$?

- [x] Because each extension given by the question acts on the set being built, not on a side chosen by the question; the requirements are conjunctive, and a sequence of conditions can handle them all.
- [ ] Because the functions $h_i$ are hyperimmune relative to a common Scott ideal.

  This is needed for each requirement; for $\mathsf{RT}^2_2$ such an ideal exists too.
- [ ] Because the question is compact.

  The Seetapun question is compact too.

---

Where is the Scott ideal used in the proof of :ref{#thm-sd-em-hyperimmunities}?

- [x] In property 2 of the question, for a partition in $\mathcal M$ witnessing a negative answer; and in the second case, to know that $h_i$ is hyperimmune relative to $X \oplus Z$.
- [ ] To make $g$ total.

  Totality comes from the positive answers for every $x$.
- [ ] Only in the growth task.

  The growth task only needs closure under computability in $X \oplus Z$.
:::

::::exercise{#exr-em-strong-cone difficulty=3 objective="Design a forcing question over tournaments and colorings to prove that the Erdős–Moser theorem admits strong cone avoidance."}
Show that $\mathsf{EM}$ admits strong cone avoidance (:ref{#def-cone-avoidance-problem}): for every set $Z$, every $C \not\leq_T Z$ and every tournament $T$ on $\nat$, not necessarily computable in $Z$, there is an infinite $T$-transitive set $G$ with $C \not\leq_T Z \oplus G$. Use the $\mathsf{EM}$ conditions $(\sigma, X)$ of :ref{#def-sd-em-condition} whose reservoirs satisfy $C \not\leq_T Z \oplus X$, and proceed in five steps.

1. Show with :ref{#thm-dj-cone-avoidance} that every condition has an extension with one more element in the stem.
2. For a condition $(\sigma, X)$ and a $\Sigma^0_1$ sentence $\varphi$, let $(\sigma, X) \mathrel{?{\vdash}} \varphi$ hold if for every tournament $S$ on $\nat$ and every $g : \nat \to 2$, some string $\tau$ compatible with $(\sigma, X)$ satisfies $\varphi$, and its set $\rho$ of new elements is $S$-transitive and **$g$-compatible**: $S(a, b)$ implies $g(a) \geq g(b)$ for all $a, b \in \rho$. Show that this relation is $\Sigma^0_1(Z \oplus X)$.
3. Show that if $(\sigma, X) \mathrel{?{\vdash}} \varphi$, some extension forces $\varphi$.
4. Show with :ref{#thm-cone-avoidance-basis} and :ref{#thm-sd-em-cone} that otherwise some extension forces $\neg \varphi$.
5. Conclude as in the proof of :ref{#thm-sd-em-cone}.

:::solution
1. Let $x \in X$, and let $p_X$ enumerate $X$ in increasing order. By :ref{#thm-dj-cone-avoidance} relative to $Z \oplus X$, applied to $\{ n : T(x, p_X(n)) \}$, there is an infinite set $H$, contained in this set or in its complement, with $C \not\leq_T Z \oplus X \oplus H$. The set $Y = \{ p_X(n) : n \in H \} \setminus [0, x]$ is computable in $X \oplus H$, and $x$ beats all its elements or is beaten by all of them. The proof of :ref{#lem-sd-em-extension} shows that $(\sigma \cup \{ x \}, Y)$ is a condition extending $(\sigma, X)$.

2. A pair $(S, g)$ is an element of Cantor space. Whether a string $\tau$ is a witness for $(S, g)$ depends on $X$, on a convergence with oracle $Z \oplus \tau$, and on finitely many bits of $S$ and $g$. So the pairs without a witness form a $\Pi^0_1(Z \oplus X)$ class $\mathcal P$, and the answer is positive if and only if $\mathcal P$ is empty, which is $\Sigma^0_1(Z \oplus X)$ by compactness.

3. By compactness there is $\ell \geq |\sigma|$ such that every pair $(S, g)$ has a witness of length at most $\ell$. Let $F = X \cap [0, \ell)$. Applying the argument of step 1 to each $a \in F$ in turn gives an infinite $Y \subseteq X \setminus [0, \ell)$ with $C \not\leq_T Z \oplus Y$, and $\gamma : F \to 2$ such that each $a \in F$ beats every $y \in Y$ if $\gamma(a) = 1$ and is beaten by every $y \in Y$ if $\gamma(a) = 0$. Take $S = T$ and $g$ extending $\gamma$, and let $\tau$ be a witness, with new elements $\rho \subseteq F$, $T$-transitive and $\gamma$-compatible. Property (a) holds for $(\tau, Y)$ by the choice of $\gamma$. For (b), triples with an element of $\sigma$ are handled as in the proof of :ref{#lem-sd-em-question}; a 3-cycle $\{ a, b, y \}$ with $a, b \in \rho$, $y \in Y$ and $T(a, b)$ would have $T(b, y)$ and $T(y, a)$, so $\gamma(b) = 1 > 0 = \gamma(a)$, against compatibility, as in :ref{#exr-em-l-compatible}. So $(\tau, Y)$ is a condition, and it forces $\varphi$.

4. The class $\mathcal P$ is non-empty. By :ref{#thm-cone-avoidance-basis} relative to $Z \oplus X$, it has a member $(S, g)$ with $C \not\leq_T W$, where $W = Z \oplus X \oplus S \oplus g$. Some $X_i = \{ x \in X : g(x) = i \}$ is infinite, and computable in $W$. By :ref{#thm-sd-em-cone} relative to $W$, applied to the tournament $S$ transported to $\nat$ through the enumeration of $X_i$, there is an infinite $S$-transitive set $Y \subseteq X_i$ with $C \not\leq_T W \oplus Y$. Then $(\sigma, Y)$ is a condition extending $(\sigma, X)$. If a member $G$ satisfied $\varphi$, some initial segment of $G$ would be a string compatible with $(\sigma, Y)$ satisfying $\varphi$, whose new elements lie in $Y$: they are $S$-transitive, and $g$-compatible since $g$ is constant on $Y$. It would be a witness for $(S, g) \in \mathcal P$. So $(\sigma, Y)$ forces $\neg \varphi$.

5. Start from $(\varepsilon, \nat)$ and alternate step 1 with the requirements. For a condition $(\sigma, X)$ and an index $e$, the set of pairs $(x, v)$ with $(\sigma, X) \mathrel{?{\vdash}} \Phi^{Z \oplus G}_e(x)\converge = v$ is $\Sigma^0_1(Z \oplus X)$; it is not the graph of $C$, since $C \not\leq_T Z \oplus X$, and steps 3 and 4 give an extension forcing $\Phi^{Z \oplus G}_e(x) \neq C(x)$ or its divergence for some $x$. The union of the stems is infinite, $T$-transitive, a member of every condition, and does not compute $C$ together with $Z$.
:::
::::

## Notes and references

The design of the reservoirs, cone avoidance and preservation of hyperimmunities for $\mathsf{EM}$ follow the section *Erdős–Moser theorem* of the chapter *Custom properties* of Patey's monograph, and the sections *Core concepts* and *Erdős–Moser theorem* of its chapter *Forcing design*; :ref{#thm-sd-em-hyperimmunities} is due to Patey (2017). The question with partitions is the one of the chapter *Custom properties*. Strong cone avoidance of $\mathsf{EM}$ (:ref{#exr-em-strong-cone}) is an exercise of the chapter *Forcing design*, attributed there to Wang and to Patey; the version with partitions given here follows the same plan.

- L. Patey, *Lowness and avoidance*, chapters *Custom properties* and *Forcing design*.
- L. Patey, *Iterative forcing and hyperimmunity in reverse mathematics*, Computability 6 (2017), 209–221; arXiv:1501.07709.
- C. G. Jockusch, Jr. and R. I. Soare, *Π⁰₁ classes and degrees of theories*, Transactions of the American Mathematical Society 173 (1972), 33–56.
- D. D. Dzhafarov and C. G. Jockusch, Jr., *Ramsey's theorem and cone avoidance*, Journal of Symbolic Logic 74 (2009), 557–578.

:::::exercises
::::exercise{#ex-em-non-sigma1 difficulty=2 objective="Adapt the cone avoidance argument for $\mathsf{EM}$ to preserve countably many non-$\Sigma^0_1$ definitions at once."}
Let $Z$ be a set and $C_0, C_1, \dots$ sets none of which is $\Sigma^0_1(Z)$ (:ref{#def-preserve-non-sigma1}). Show that every $Z$-computable tournament has an infinite transitive set $G$ such that no $C_j$ is $\Sigma^0_1(Z \oplus G)$. Deduce that for every sequence of sets $D_0, D_1, \dots$ none of which is computable in $Z$, there is an infinite transitive set $G$ such that no $D_j$ is computable in $Z \oplus G$.

:::solution
Let $\mathcal W$ be the class of sets $W$ such that no $C_j$ is $\Sigma^0_1(W)$; it is a weakness property containing $Z$. It is preserved by $\mathsf{WKL}$: in the proof of item 1 of :ref{#thm-non-sigma1-examples}, the requirements for the different sets $C_j$ form countably many dense sets, indexed by $j$ and $e$, and a sufficiently generic path meets all of them (:ref{#ex-non-sigma1-countable}). By :ref{#lem-scott-preservation}, there is a Scott ideal $\mathcal M \subseteq \mathcal W$ containing $Z$. Build a sequence of $\mathsf{EM}$ conditions with reservoirs in $\mathcal M$ as in :ref{#thm-sd-em-cone}, with the growth task and, for each pair $(e, j)$, the following task. Let $c = (\sigma, X)$ be the current condition and $U = \{ x : c \mathrel{?{\vdash}} \Phi^{Z \oplus G}_e(x)\converge \}$, a set $\Sigma^0_1(X \oplus Z)$ by property 3 of :ref{#lem-sd-em-question}. Since $X \oplus Z \in \mathcal M \subseteq \mathcal W$, $U \neq C_j$. If some $x \in U$ is not in $C_j$, property 1 gives an extension forcing $\Phi^{Z \oplus G}_e(x)\converge$. If some $x \in C_j$ is not in $U$, property 2 gives an extension forcing $\Phi^{Z \oplus G}_e(x)\diverge$. In both cases every member $G$ of the extension has $W^{Z \oplus G}_e \neq C_j$. The union of the stems is an infinite transitive set and a member of every condition of the sequence, so $W^{Z \oplus G}_e \neq C_j$ for all $e$ and $j$.

For the second statement, let $D_j \not\leq_T Z$. By Post's theorem relativized to $Z$, $D_j$ or $\overline{D_j}$ is not $\Sigma^0_1(Z)$; call it $C_j$. Take $G$ as above. If $D_j \leq_T Z \oplus G$, then $D_j$ and $\overline{D_j}$ are both $\Sigma^0_1(Z \oplus G)$, and so is $C_j$, a contradiction. The question is not disjunctive, so all the sets are handled on the same set $G$; the first statement is a theorem of Wang.
:::
::::

::::exercise{#ex-em-cone-from-hyperimmunity difficulty=1 objective="Derive cone avoidance of $\mathsf{EM}$ from its preservation of hyperimmunity."}
Deduce :ref{#thm-sd-em-cone} from :ref{#thm-sd-em-hyperimmunities} and :ref{#thm-hyperimmunity-cone}.

:::solution
Let $Z$ be a set, $h$ a $Z$-hyperimmune function and $T$ a $Z$-computable tournament. Applying :ref{#thm-sd-em-hyperimmunities} to the constant sequence $h_i = h$ gives an infinite transitive set $G$ such that $h$ is $(Z \oplus G)$-hyperimmune. So $\mathsf{EM}$ admits preservation of hyperimmunity (:ref{#def-preserve-hyperimmunity}), and by :ref{#thm-hyperimmunity-cone} it admits cone avoidance. The direct proof of :ref{#thm-sd-em-cone} avoids the theorem of Downey, Greenberg, Harrison-Trainor, Patey and Turetsky, whose proof goes through moduli.
:::
::::

::::exercise{#ex-em-product difficulty=1 objective="Check that preservation of countably many hyperimmunities passes to products of problems."}
For problems $\mathsf P$ and $\mathsf Q$, let $\mathsf P \times \mathsf Q$ be the problem whose instances are the sets $X_0 \oplus X_1$ with $X_0$ an instance of $\mathsf P$ and $X_1$ an instance of $\mathsf Q$, and whose solutions are the sets $Y_0 \oplus Y_1$ with $Y_i$ a solution to $X_i$. Show that if $\mathsf P$ and $\mathsf Q$ admit preservation of $\omega$ hyperimmunities, so does $\mathsf P \times \mathsf Q$. Deduce that $\mathsf{EM} \times \mathsf{WKL}$ admits preservation of $\omega$ hyperimmunities.

:::solution
Let $Z$ be a set, $(h_i)$ a sequence of $Z$-hyperimmune functions and $X_0 \oplus X_1 \leq_T Z$ an instance. Since $X_0 \leq_T Z$, there is a solution $Y_0$ to $X_0$ such that every $h_i$ is $(Z \oplus Y_0)$-hyperimmune. Since $X_1 \leq_T Z \oplus Y_0$, applying the hypothesis on $\mathsf Q$ to the set $Z \oplus Y_0$ gives a solution $Y_1$ to $X_1$ such that every $h_i$ is $(Z \oplus Y_0 \oplus Y_1)$-hyperimmune. The sets $Z \oplus (Y_0 \oplus Y_1)$ and $Z \oplus Y_0 \oplus Y_1$ compute each other, and hyperimmunity relative to a set depends only on its Turing degree, so $Y_0 \oplus Y_1$ is the required solution. The second statement follows from :ref{#thm-sd-em-hyperimmunities} and :ref{#exr-wkl-hyperimmunities}.
:::
::::

::::exercise{#ex-em-hyperimmune-sets difficulty=1 objective="Transfer the preservation of hyperimmune functions to hyperimmune sets through principal functions."}
Let $Z$ be a set and $A_0, A_1, \dots$ infinite sets, each hyperimmune relative to $Z$. Show that every $Z$-computable tournament has an infinite transitive set $G$ such that every $A_i$ is hyperimmune relative to $Z \oplus G$.

:::solution
By :ref{#thm-hyperimmune-principal}, whose proof relativizes to any set $W$, an infinite set $A$ is hyperimmune relative to $W$ if and only if its principal function $p_A$ is $W$-hyperimmune. So the functions $p_{A_i}$ are $Z$-hyperimmune, and :ref{#thm-sd-em-hyperimmunities} gives an infinite transitive set $G$ such that every $p_{A_i}$ is $(Z \oplus G)$-hyperimmune, that is, every $A_i$ is hyperimmune relative to $Z \oplus G$.
:::
::::
:::::
