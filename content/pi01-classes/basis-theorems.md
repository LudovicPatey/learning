---
title: Basis theorems
summary: The low basis theorem, the computably dominated basis theorem and the cone avoidance basis theorem, proved by forcing with Π⁰₁ classes.
duration: 45
prerequisites: [computable-members, turing-degrees/low-and-high]
---

A class $\mathcal B$ of sets is a **basis** for the $\Pi^0_1$ classes if every non-empty $\Pi^0_1$ class has a member in $\mathcal B$. The Kreisel basis theorem says that the sets computable in $\emptyset'$ form a basis. This lesson proves three much finer basis theorems, due to Jockusch and Soare: every non-empty $\Pi^0_1$ class has a low member, a member that computes only slow-growing functions, and a member avoiding any given non-computable set. The three proofs share a method. A member is built as the intersection of a decreasing sequence of non-empty $\Pi^0_1$ classes, each class settling one requirement for all its members at once. This is the finite extension method of the course on Turing degrees, with $\Pi^0_1$ classes in place of strings as conditions; it is a form of **forcing with $\Pi^0_1$ classes**.

The construction relies on two facts. A decreasing sequence of non-empty closed classes has a non-empty intersection (:ref{#prop-cantor-compact}). The emptiness of a $\Pi^0_1$ class is a $\Sigma^0_1$ property of its index (:ref{#prop-pi01-emptiness}).

## The low basis theorem

:::theorem[Low basis theorem]{#thm-low-basis}
Every non-empty $\Pi^0_1$ class has a low member.
:::

:::proof{of=thm-low-basis}
Let $\mathcal P$ be a non-empty $\Pi^0_1$ class. We define, with the oracle $\emptyset'$, a decreasing sequence of non-empty $\Pi^0_1$ classes $\mathcal P_0 = \mathcal P \supseteq \mathcal P_1 \supseteq \cdots$, given by indices, and a set $J$.

Given $\mathcal P_e$, let $\mathcal Q_e = \mathcal P_e \cap \{ X : \Phi^X_e(e)\diverge \}$. It is a $\Pi^0_1$ class, with an index computable from that of $\mathcal P_e$ and from $e$ (:ref{#prop-pi01-equivalent} and the first exercise of :ref{to="pi01-classes/trees-and-classes"}). Ask $\emptyset'$ whether $\mathcal Q_e$ is empty, a $\Sigma^0_1$ question.

- If $\mathcal Q_e \neq \emptyset$, let $\mathcal P_{e+1} = \mathcal Q_e$ and $J(e) = 0$. Every $X \in \mathcal P_{e+1}$ satisfies $\Phi^X_e(e)\diverge$.
- If $\mathcal Q_e = \emptyset$, let $\mathcal P_{e+1} = \mathcal P_e$ and $J(e) = 1$. Every $X \in \mathcal P_{e+1}$ satisfies $\Phi^X_e(e)\converge$.

The classes are non-empty, so their intersection contains some $X$. For every $e$, $X \in \mathcal P_{e+1}$, so $X'(e) = J(e)$. The set $J$ is computable in $\emptyset'$, by the construction, so $X' = J \leq_T \emptyset'$.
:::

The construction computes, with $\emptyset'$, the jump of **every** member of $\bigcap_e \mathcal P_e$. It is uniform: from an index of $\mathcal P$, one computes an index $j$ with $\Phi^{\emptyset'}_j = X'$, that is, a lowness index of the member (:ref{#prop-no-lowness-index}).

:::corollary{#cor-low-noncomputable-member}
Every non-empty $\Pi^0_1$ class without computable member, such as $\mathrm{DNC}_2$, has a non-computable low member.
:::

:::quiz[the low basis theorem]
What does the oracle $\emptyset'$ decide at step $e$ of the construction?

- [x] Whether the $\Pi^0_1$ class $\mathcal Q_e$ is empty, which by compactness is a $\Sigma^0_1$ question.

  Deciding whether a particular set $X$ satisfies $\Phi^X_e(e)\converge$ would require the jump of $X$; the construction instead decides a question about a whole class.
- [ ] Whether $\Phi^X_e(e)$ converges for the member $X$ being built.

  The member is not known at step $e$; the decision is made for all members of the class at once.
- [ ] Whether $\mathcal P_e$ has a computable member.

  This question is $\Sigma^0_3$ in general, and plays no role.

---

Why do all members of $\mathcal P_{e+1}$ satisfy $\Phi^X_e(e)\converge$ when $\mathcal Q_e = \emptyset$?

- [x] Because $\mathcal Q_e$ is the set of members of $\mathcal P_e$ on which the computation diverges, and it is empty.
- [ ] Because $\Phi_e$ is total.

  Nothing is assumed about $\Phi_e$; the convergence comes from the emptiness of $\mathcal Q_e$.
- [ ] Because $\mathcal P_{e+1}$ is a singleton.

  $\mathcal P_{e+1}$ may contain many members.
:::

## The computably dominated basis theorem

:::definition{#def-computably-dominated}
A set $X$ is **computably dominated**, or **hyperimmune-free**, if every total $X$-computable function $f$ is dominated by a computable function $g$: $f(n) \leq g(n)$ for every $n$.
:::

Computable sets are computably dominated. A computably dominated set computes no fast-growing function. In particular, a non-computable $\Delta^0_2$ set is never computably dominated: it computes its computation function (:ref{#thm-computation-function}), and a computable function dominating it would compute the set.

:::lemma{#lem-uniform-bound}
Let $T$ be a computable tree, and $\Phi_e$ a functional such that $\Phi^X_e$ is total for every $X \in [T]$. Then there is a computable function $g$ with $\Phi^X_e(n) \leq g(n)$ for every $X \in [T]$ and every $n$.
:::

:::proof{of=lem-uniform-bound}
Fix $n$. The set $T_n = \{ \sigma \in T : \Phi^\sigma_e(n)[|\sigma|]\diverge \}$ is a computable tree, closed under prefixes by monotonicity of stages. If it had a path $X$, then $X \in [T]$ and $\Phi^{X \uh s}_e(n)[s]\diverge$ for every $s$, so $\Phi^X_e(n)\diverge$ by :ref{#prop-oracle-stages}, contradicting the hypothesis. So $T_n$ is finite, and there is a length $\ell$ such that every $\sigma \in T$ of length $\ell$ has $\Phi^\sigma_e(n)[\ell]\converge$. Such an $\ell$ is found by a computable search, since for each $\ell$ the condition involves finitely many strings. Let $g(n)$ be the maximum of the values $\Phi^\sigma_e(n)[\ell]$ for $\sigma \in T$ of length $\ell$, or $0$ if there is no such $\sigma$. For $X \in [T]$, the prefix $X \uh \ell$ belongs to $T$, and $\Phi^X_e(n) = \Phi^{X \uh \ell}_e(n) \leq g(n)$.
:::

:::theorem[Computably dominated basis theorem]{#thm-dominated-basis}
Every non-empty $\Pi^0_1$ class has a computably dominated member.
:::

:::proof{of=thm-dominated-basis}
Let $\mathcal P_0 = \mathcal P$. Given a non-empty $\Pi^0_1$ class $\mathcal P_e$, consider the classes $\mathcal B_{e,m} = \mathcal P_e \cap \{ X : \Phi^X_e(m)\diverge \}$, which are $\Pi^0_1$.

- If some $\mathcal B_{e,m}$ is non-empty, let $\mathcal P_{e+1} = \mathcal B_{e,m}$ for the least such $m$. Every member $X$ of $\mathcal P_{e+1}$ has $\Phi^X_e(m)\diverge$, so $\Phi^X_e$ is not total.
- Otherwise, $\Phi^X_e$ is total for every $X \in \mathcal P_e$; let $\mathcal P_{e+1} = \mathcal P_e$. By :ref{#lem-uniform-bound}, applied to a computable tree of $\mathcal P_e$, there is a computable $g_e$ with $\Phi^X_e \leq g_e$ for every $X \in \mathcal P_{e+1}$.

Let $X \in \bigcap_e \mathcal P_e$, which is non-empty by compactness. If $\Phi^X_e$ is total, then the first case did not occur at step $e$, so $\Phi^X_e$ is dominated by the computable function $g_e$. Hence $X$ is computably dominated.
:::

The construction asks, at each step, whether some $\mathcal B_{e,m}$ is non-empty, a $\Sigma^0_2$ question; so it is computable in $\emptyset''$, and gives a computably dominated member computable in $\emptyset''$. It cannot be computable in $\emptyset'$ in general: a class without computable member has no computably dominated member that is $\Delta^0_2$, since such a member would be non-computable.

:::quiz[the computably dominated basis theorem]
In :ref{#lem-uniform-bound}, where is it used that $\Phi^X_e$ is total on **every** member of $[T]$?

- [x] To show that the tree $T_n$ of strings on which the computation at $n$ has not yet converged is finite: a path through it would be a member on which $\Phi_e(n)$ diverges.

  Totality on all members, combined with compactness, gives a uniform stage of convergence, and hence a computable bound.
- [ ] To show that $g$ is computable.

  The computability of $g$ follows once the search for $\ell$ is known to terminate, which is the role of totality.
- [ ] To show that $g$ dominates $\Phi^X_e$.

  Domination follows from the choice of $\ell$; totality is needed before, for the existence of $\ell$.

---

Why can a non-empty $\Pi^0_1$ class without computable member not have a computably dominated member computable in $\emptyset'$?

- [x] A member computable in $\emptyset'$ is $\Delta^0_2$; being non-computable, it computes its computation function, which no computable function dominates.
- [ ] Because computably dominated sets are not $\Pi^0_1$.

  Sets are not classes; the question concerns the complexity of a member.
- [ ] Because the low basis theorem provides another member.

  Several members may coexist; the argument concerns any $\Delta^0_2$ member.
:::

## Cone avoidance

:::lemma{#lem-uniform-cone}
Let $\mathcal P$ be a non-empty $\Pi^0_1$ class, $\Phi_e$ a functional and $C$ a set. If $\Phi^Y_e = C$ for every $Y \in \mathcal P$, then $C$ is computable.
:::

:::proof{of=lem-uniform-cone}
Let $\mathcal P = [T]$ with $T$ computable; since $\mathcal P$ is non-empty, $T$ has strings of every length. To compute $C(n)$, search for a length $\ell$ such that all the strings $\sigma \in T$ of length $\ell$ satisfy $\Phi^\sigma_e(n)[\ell]\converge$ with one and the same value $v$, and output $v$.

*The search terminates.* The tree $T_n = \{ \sigma \in T : \neg\, (\Phi^\sigma_e(n)[|\sigma|]\converge = C(n)) \}$ is closed under prefixes by monotonicity of stages, and has no path, since a path $Y$ would be a member of $\mathcal P$ with $\Phi^Y_e(n) \neq C(n)$. So it is finite, and at any length $\ell$ beyond its nodes, every $\sigma \in T$ of length $\ell$ satisfies $\Phi^\sigma_e(n)[\ell]\converge = C(n)$.

*The output is correct.* If a length $\ell$ satisfies the condition with value $v$, take a member $Y$ of $\mathcal P$; then $Y \uh \ell \in T$, so $v = \Phi^{Y \uh \ell}_e(n) = \Phi^Y_e(n) = C(n)$.
:::

:::theorem[Cone avoidance basis theorem]{#thm-cone-avoidance-basis}
Let $C$ be a non-computable set. Every non-empty $\Pi^0_1$ class has a member that does not compute $C$.
:::

:::proof{of=thm-cone-avoidance-basis}
Let $\mathcal P_0 = \mathcal P$. Given a non-empty $\Pi^0_1$ class $\mathcal P_e$, by :ref{#lem-uniform-cone} it is not the case that $\Phi^Y_e = C$ for every $Y \in \mathcal P_e$. So there is $m$ such that the class $\mathcal B_{e,m} = \mathcal P_e \cap \{ Y : \neg\, (\Phi^Y_e(m)\converge = C(m)) \}$ is non-empty. It is $\Pi^0_1$: for the fixed value $C(m)$, its complement in $\mathcal P_e$ is defined by the $\Sigma^0_1$ condition $\Phi^Y_e(m)\converge = C(m)$. Let $\mathcal P_{e+1} = \mathcal B_{e,m}$ for the least such $m$. A member $Y$ of $\bigcap_e \mathcal P_e$ satisfies $\Phi^Y_e \neq C$ for every $e$, so $C \not\leq_T Y$.
:::

## Exercises

::::exercise{difficulty=1}
Show that a computably dominated set computes no non-computable $\Delta^0_2$ set, and that a low set computes no set that is not $\Delta^0_2$. Deduce a second proof of :ref{#thm-cone-avoidance-basis} from the low and computably dominated basis theorems.

:::solution
If $X$ is computably dominated and $D \leq_T X$, then every $D$-computable total function is $X$-computable, hence dominated by a computable function: $D$ is computably dominated. A non-computable $\Delta^0_2$ set is not computably dominated, so it is not computable from $X$. If $X$ is low and $D \leq_T X$, then $D \leq_T X \leq_T \emptyset'$, so $D$ is $\Delta^0_2$. Now let $C$ be non-computable. If $C$ is $\Delta^0_2$, a computably dominated member of $\mathcal P$ does not compute $C$; otherwise, a low member does not compute $C$.
:::
::::

::::exercise{difficulty=1}
Show that $X$ is computably dominated if and only if every total $X$-computable function $f$ is dominated **eventually** by a computable function $g$, that is, $f(n) \leq g(n)$ for all but finitely many $n$.

:::solution
Domination everywhere implies eventual domination. Conversely, if $f(n) \leq g(n)$ for all $n \geq n_0$, the function $g'$ equal to $\max(g(n), f(n))$ for $n < n_0$ and to $g(n)$ for $n \geq n_0$ is computable, since it differs from $g$ at finitely many points, whose values can be written into the algorithm; and it dominates $f$ everywhere.
:::
::::

::::exercise{difficulty=2}
Show that every non-empty $\Pi^0_1$ class has a computably dominated member computable in $\emptyset''$.

:::solution
Modify the construction of :ref{#thm-dominated-basis} so that it also builds a sequence of strings: alongside $\mathcal P_{e+1}$, choose $\sigma_{e+1} = \sigma_e i$, with $i$ the least bit such that $\mathcal P_{e+1} \cap [\sigma_e i] \neq \emptyset$, and replace $\mathcal P_{e+1}$ by $\mathcal P_{e+1} \cap [\sigma_{e+1}]$. The member built is $X = \bigcup_e \sigma_e$, the only element of the intersection. Each step uses the oracle $\emptyset''$: the question "is some $\mathcal B_{e,m}$ non-empty?" is $\Sigma^0_2$, since non-emptiness of a $\Pi^0_1$ class is a $\Pi^0_1$ property of its index; the least such $m$ is then found by asking $\emptyset'$ about each $m$ in turn; and the choice of the bit $i$ asks $\emptyset'$ whether a $\Pi^0_1$ class is non-empty. So the sequence $(\sigma_e)$, and $X$, are computable in $\emptyset''$. Adding the string condition does not affect the argument for domination.
:::
::::

## Notes and references

The three basis theorems are due to Jockusch and Soare (1972). Hirschfeldt observed that cone avoidance follows from the first two, as in the first exercise. Forcing with $\Pi^0_1$ classes, also called Jockusch–Soare forcing, is a basic tool in the computability theory of combinatorial principles studied in reverse mathematics.

- C. G. Jockusch and R. I. Soare, *Π⁰₁ classes and degrees of theories*, Transactions of the American Mathematical Society 173 (1972), 33–56.
- D. R. Hirschfeldt, *Slicing the Truth*, Lecture Notes Series of the Institute for Mathematical Sciences, National University of Singapore, 28, World Scientific, 2015.
