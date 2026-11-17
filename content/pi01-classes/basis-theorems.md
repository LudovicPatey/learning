---
title: Basis theorems
summary: The low basis theorem, the computably dominated basis theorem and the cone avoidance basis theorem, proved by forcing with Π⁰₁ classes.
duration: 35
prerequisites: [computable-members, turing-degrees/low-and-high, turing-degrees/limit-computability]
---

A class $\mathcal B$ of sets is a **basis** for the $\Pi^0_1$ classes if every non-empty $\Pi^0_1$ class has a member in $\mathcal B$. The Kreisel basis theorem says that the sets computable in $\emptyset'$ form a basis. This lesson proves three finer basis theorems, due to Jockusch and Soare: every non-empty $\Pi^0_1$ class has a low member, a member $X$ such that every total $X$-computable function is dominated by a computable function, and a member that does not compute a given non-computable set. The three proofs build a member as the intersection of a decreasing sequence of non-empty $\Pi^0_1$ classes, each class settling one requirement for all its members at once. This is **forcing with $\Pi^0_1$ classes**: the finite extension method with $\Pi^0_1$ classes in place of strings as conditions.

The construction relies on two facts. A decreasing sequence of non-empty closed classes has a non-empty intersection (:ref{#prop-cantor-compact}). The emptiness of a $\Pi^0_1$ class is a $\Sigma^0_1$ property of its index (:ref{#prop-pi01-emptiness}).

A string, as a condition in :ref{to="turing-degrees/finite-extensions"}, says nothing about the bits beyond it, so the set built has no reason to lie in a given class. A $\Pi^0_1$ class constrains all bits at once, and removing from it the members on which a computation converges leaves a $\Pi^0_1$ class. The price is to know whether the smaller class is empty: by effective compactness, a question for $\emptyset'$.

## The low basis theorem

:::theorem[Low basis theorem]{#thm-low-basis}
Every non-empty $\Pi^0_1$ class has a low member.
:::

:::proof{of=thm-low-basis}
Let $\mathcal P$ be a non-empty $\Pi^0_1$ class. We define, with the oracle $\emptyset'$, a decreasing sequence of non-empty $\Pi^0_1$ classes $\mathcal P_0 = \mathcal P \supseteq \mathcal P_1 \supseteq \cdots$, given by indices, and a set $J$.

Given $\mathcal P_e$, let $\mathcal Q_e = \mathcal P_e \cap \{ X : \Phi^X_e(e)\diverge \}$. It is a $\Pi^0_1$ class, with an index computable from that of $\mathcal P_e$ and from $e$ (:ref{#prop-pi01-equivalent} and :ref{#ex-pi01-intersection-union}). Ask $\emptyset'$ whether $\mathcal Q_e$ is empty, a $\Sigma^0_1$ question.

- If $\mathcal Q_e \neq \emptyset$, let $\mathcal P_{e+1} = \mathcal Q_e$ and $J(e) = 0$. Every $X \in \mathcal P_{e+1}$ satisfies $\Phi^X_e(e)\diverge$.
- If $\mathcal Q_e = \emptyset$, let $\mathcal P_{e+1} = \mathcal P_e$ and $J(e) = 1$. Every $X \in \mathcal P_{e+1}$ satisfies $\Phi^X_e(e)\converge$.

The classes are non-empty, so their intersection contains some $X$. For every $e$, $X \in \mathcal P_{e+1}$, so $X'(e) = J(e)$. The set $J$ is computable in $\emptyset'$, by the construction, so $X' = J \leq_T \emptyset'$.
:::

:::figure[The first steps of the construction of :ref{#thm-low-basis}, with classes drawn schematically as unions of intervals of Cantor space. When $\mathcal Q_e$ is non-empty, the class shrinks to the members on which $\Phi^X_e(e)$ diverges; otherwise it is kept, and the computation converges on all its members. Every member of the intersection has the jump $J$.]
<svg class="fig" viewBox="0 0 600 236" width="600" role="img" aria-label="A decreasing sequence of classes P0, P1, P2, P3 drawn as unions of intervals of Cantor space, with the decision taken at each step"><line x1="60" y1="29" x2="330" y2="29" class="axis"/><rect x="65.4" y="20" width="75.6" height="18" class="cell head-cell"/><rect x="162.6" y="20" width="64.8" height="18" class="cell head-cell"/><rect x="249.0" y="20" width="75.6" height="18" class="cell head-cell"/><text x="20" y="34" text-anchor="middle" class="math" font-size="16">P<tspan class="mrm" font-size="10" dy="4">0</tspan></text><text x="348" y="34" class="label">the given class</text><line x1="60" y1="75" x2="330" y2="75" class="axis"/><rect x="70.8" y="66" width="62.1" height="18" class="cell head-cell"/><rect x="254.4" y="66" width="21.6" height="18" class="cell head-cell"/><rect x="289.5" y="66" width="32.4" height="18" class="cell head-cell"/><text x="20" y="80" text-anchor="middle" class="math" font-size="16">P<tspan class="mrm" font-size="10" dy="4">1</tspan></text><text x="348" y="80" class="label">step 0: Q₀ ≠ ∅, so P₁ = Q₀, J(0) = 0</text><line x1="60" y1="121" x2="330" y2="121" class="axis"/><rect x="70.8" y="112" width="62.1" height="18" class="cell head-cell"/><rect x="254.4" y="112" width="21.6" height="18" class="cell head-cell"/><rect x="289.5" y="112" width="32.4" height="18" class="cell head-cell"/><text x="20" y="126" text-anchor="middle" class="math" font-size="16">P<tspan class="mrm" font-size="10" dy="4">2</tspan></text><text x="348" y="126" class="label">step 1: Q₁ = ∅, so P₂ = P₁, J(1) = 1</text><line x1="60" y1="167" x2="330" y2="167" class="axis"/><rect x="87.0" y="158" width="32.4" height="18" class="cell head-cell"/><rect x="294.9" y="158" width="21.6" height="18" class="cell head-cell"/><text x="20" y="172" text-anchor="middle" class="math" font-size="16">P<tspan class="mrm" font-size="10" dy="4">3</tspan></text><text x="348" y="172" class="label">step 2: Q₂ ≠ ∅, so P₃ = Q₂, J(2) = 0</text><text x="195.0" y="198" text-anchor="middle" class="mrm muted" font-size="13">⋮</text><line x1="60" y1="213" x2="330" y2="213" class="axis"/><circle cx="305.7" cy="213" r="4.5" class="accent-fill"/><text x="295.7" y="218" text-anchor="end" class="math" font-size="15">X</text><text x="348" y="218" class="label">a member of every Pₑ: X′(e) = J(e) for all e</text></svg>
:::

The construction computes, with $\emptyset'$, the jump of **every** member of $\bigcap_e \mathcal P_e$. It is uniform: from an index of $\mathcal P$, one computes an index $j$ with $\Phi^{\emptyset'}_j = X'$, that is, a lowness index of every member of $\bigcap_e \mathcal P_e$ (see :ref{to="arithmetic-hierarchy/codes"}). By :ref{#prop-no-lowness-index}, such an index cannot in general be computed from a $\Delta^0_2$ index of a low set.

:::remark{#rem-superlow}
To compute $J(e)$, the construction asks $e + 1$ questions to $\emptyset'$, each determined by the previous answers, and it halts whatever the answers. So $X'(e)$ is a Boolean combination, computable from $e$, of the bits of $\emptyset'$ at the at most $2^{e+1} - 1$ questions that can occur. A reduction of this kind is a **truth-table reduction** (see the course on immunity and growth), and a set whose jump is truth-table reducible to $\emptyset'$ is called **superlow**. So every non-empty $\Pi^0_1$ class has a superlow member; Downey and Hirschfeldt attribute the observation to Schaefer (Corollary 2.19.9).
:::

:::corollary{#cor-low-noncomputable-member}
Every non-empty $\Pi^0_1$ class without computable member, such as $\mathrm{DNC}_2$, has a non-computable low member.
:::

:::proof{of=cor-low-noncomputable-member}
By :ref{#thm-low-basis}, the class has a low member, which is not computable since the class has no computable member.
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

Computable sets are computably dominated. A non-computable $\Delta^0_2$ set $A$ is never computably dominated: by :ref{#thm-computation-function}, $A$ computes the computation function of a $\Delta^0_2$ approximation of $A$, and every function dominating it computes $A$, so a computable function dominating it would make $A$ computable.

For each $e$, the construction makes $\Phi^X_e$ partial on a subclass if it can. Otherwise $\Phi^X_e$ is total on all members of the current class, and compactness gives a bound: the computations on all members converge by a common stage, found by a search over finitely many strings at a time.

:::lemma{#lem-uniform-bound}
Let $T$ be a computable tree, and $\Phi_e$ a functional such that $\Phi^X_e$ is total for every $X \in [T]$. Then there is a computable function $g$ with $\Phi^X_e(n) \leq g(n)$ for every $X \in [T]$ and every $n$.
:::

:::proof{of=lem-uniform-bound}
Fix $n$. The set $T_n = \{ \sigma \in T : \Phi^\sigma_e(n)[|\sigma|]\diverge \}$ is a computable tree, closed under prefixes by monotonicity of stages. If it had a path $X$, then $X \in [T]$ and $\Phi^{X \uh s}_e(n)[s]\diverge$ for every $s$, so $\Phi^X_e(n)\diverge$ by :ref{#prop-oracle-stages}, contradicting the hypothesis. So $T_n$ is finite, and there is a length $\ell$ such that every $\sigma \in T$ of length $\ell$ has $\Phi^\sigma_e(n)[\ell]\converge$. Such an $\ell$ is found by a computable search, since for each $\ell$ the condition involves finitely many strings. Let $g(n)$ be the maximum of the values $\Phi^\sigma_e(n)[\ell]$ for $\sigma \in T$ of length $\ell$, or $0$ if there is no such $\sigma$. For $X \in [T]$, the prefix $X \uh \ell$ belongs to $T$, and $\Phi^X_e(n) = \Phi^{X \uh \ell}_e(n) \leq g(n)$.
:::

The lemma needs a closed class. Let $\Phi^X(n)$ be the least $k$ with $X(k) = 1$. On the open class $\cs \setminus \{ 0^\infty \}$, $\Phi^X$ is total, but $\Phi^{0^k 1 0^\infty}(0) = k$, so no function bounds it uniformly; on $\cs$, it is not total at $0^\infty$.

:::theorem[Computably dominated basis theorem]{#thm-dominated-basis}
Every non-empty $\Pi^0_1$ class has a computably dominated member.
:::

:::proof{of=thm-dominated-basis}
Let $\mathcal P_0 = \mathcal P$. Given a non-empty $\Pi^0_1$ class $\mathcal P_e$, consider the classes $\mathcal B_{e,m} = \mathcal P_e \cap \{ X : \Phi^X_e(m)\diverge \}$, which are $\Pi^0_1$.

- If some $\mathcal B_{e,m}$ is non-empty, let $\mathcal P_{e+1} = \mathcal B_{e,m}$ for the least such $m$. Every member $X$ of $\mathcal P_{e+1}$ has $\Phi^X_e(m)\diverge$, so $\Phi^X_e$ is not total.
- Otherwise, $\Phi^X_e$ is total for every $X \in \mathcal P_e$; let $\mathcal P_{e+1} = \mathcal P_e$. By :ref{#lem-uniform-bound}, applied to a computable tree of $\mathcal P_e$, there is a computable $g_e$ with $\Phi^X_e \leq g_e$ for every $X \in \mathcal P_{e+1}$.

Let $X \in \bigcap_e \mathcal P_e$, which is non-empty by compactness. If $\Phi^X_e$ is total, then the first case did not occur at step $e$, so $\Phi^X_e$ is dominated by the computable function $g_e$. Hence $X$ is computably dominated.
:::

The question asked at each step is $\Sigma^0_2$, and the construction can be carried out with $\emptyset''$ (:ref{#ex-dominated-double-jump}). In general $\emptyset'$ does not suffice: in a class without computable member, a computably dominated member is not computable, hence not $\Delta^0_2$.

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

::::exercise{#ex-cone-from-low-dominated difficulty=1 objective="Derive the cone avoidance basis theorem from the low and computably dominated basis theorems."}
Show that a computably dominated set computes no non-computable $\Delta^0_2$ set, and that a low set computes no set that is not $\Delta^0_2$. Deduce a second proof of :ref{#thm-cone-avoidance-basis} from the low and computably dominated basis theorems.

:::solution
If $X$ is computably dominated and $D \leq_T X$, then every $D$-computable total function is $X$-computable, hence dominated by a computable function: $D$ is computably dominated. A non-computable $\Delta^0_2$ set is not computably dominated, so it is not computable from $X$. If $X$ is low and $D \leq_T X$, then $D \leq_T X \leq_T \emptyset'$, so $D$ is $\Delta^0_2$. Now let $C$ be non-computable. If $C$ is $\Delta^0_2$, a computably dominated member of $\mathcal P$ does not compute $C$; otherwise, a low member does not compute $C$.
:::
::::

::::exercise{#ex-dominated-double-jump difficulty=2 objective="Bound the complexity of the construction of a computably dominated member by $\emptyset''$."}
Show that every non-empty $\Pi^0_1$ class has a computably dominated member computable in $\emptyset''$.

:::solution
In the construction of :ref{#thm-dominated-basis}, also choose $\sigma_{e+1} = \sigma_e i$, with $i$ the least bit such that $\mathcal P_{e+1} \cap [\sigma_e i] \neq \emptyset$, and replace $\mathcal P_{e+1}$ by $\mathcal P_{e+1} \cap [\sigma_{e+1}]$. The member built is $X = \bigcup_e \sigma_e$, the only element of the intersection. Each step uses the oracle $\emptyset''$: the question "is some $\mathcal B_{e,m}$ non-empty?" is $\Sigma^0_2$, since non-emptiness of a $\Pi^0_1$ class is a $\Pi^0_1$ property of its index; the least such $m$ is then found by asking $\emptyset'$ about each $m$ in turn; and the choice of the bit $i$ asks $\emptyset'$ whether a $\Pi^0_1$ class is non-empty. So the sequence $(\sigma_e)$, and $X$, are computable in $\emptyset''$. Adding the string condition does not affect the argument for domination.
:::
::::

## Notes and references

The proof of the low basis theorem is an instance of first-jump control by forcing; the general method is developed in the course on lowness (:ref{to="lowness/forcing-the-jump"}).

The constructions of this lesson are instances of forcing with Π⁰₁ classes (Jockusch–Soare forcing). Its forcing relation, and the forcing question used to prove preservation theorems such as cone avoidance, are developed in the course on effective forcing (:ref{to="effective-forcing/forcing-with-trees"}, :ref{to="effective-forcing/forcing-question"}).

The three basis theorems are due to Jockusch and Soare, in *Π⁰₁ classes and degrees of theories* (1972). The derivation of cone avoidance from the first two, as in :ref{#ex-cone-from-low-dominated}, is given in Hirschfeldt's *Slicing the Truth* (Section 3.1), and Monin and Patey attribute it to him. An earlier form of cone avoidance, with "primitive recursive in" in place of "computable from", is due to Gandy, Kreisel and Tait (1960), according to Hirschfeldt. Forcing with $\Pi^0_1$ classes, also called Jockusch–Soare forcing, is a basic tool in the computability theory of combinatorial principles studied in reverse mathematics; Monin and Patey study it as a forcing notion in their chapter on effective forcing.

The low and computably dominated basis theorems are Theorems 3.7.2 and 9.5.1 in Soare's *Turing Computability*, Theorems 2.19.8 and 2.19.11 in Downey and Hirschfeldt, and Theorems 1.8.37 and 1.8.42 in Nies. Brattka, de Brecht and Pauly (2012) prove a uniform version of the low basis theorem in the framework of Weihrauch reducibility: closed choice on Cantor space, the problem of finding a member of a non-empty closed class given by an enumeration of its complement, is low computable.

- C. G. Jockusch and R. I. Soare, *Π⁰₁ classes and degrees of theories*, Transactions of the American Mathematical Society 173 (1972), 33–56.
- D. R. Hirschfeldt, *Slicing the Truth*, Lecture Notes Series of the Institute for Mathematical Sciences, National University of Singapore, 28, World Scientific, 2015, Section 3.1.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, Sections 3.7 and 9.4–9.5.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Section 2.19.3.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Section 1.8.
- V. Brattka, M. de Brecht and A. Pauly, *Closed choice and a uniform low basis theorem*, Annals of Pure and Applied Logic 163 (2012), 986–1008.

:::::exercises
::::exercise{#ex-eventual-domination difficulty=1 objective="Check that domination everywhere and eventual domination give the same notion of computably dominated set."}
Show that $X$ is computably dominated if and only if every total $X$-computable function $f$ is dominated **eventually** by a computable function $g$, that is, $f(n) \leq g(n)$ for all but finitely many $n$.

:::solution
Domination everywhere implies eventual domination. Conversely, if $f(n) \leq g(n)$ for all $n \geq n_0$, the function $g'$ equal to $\max(g(n), f(n))$ for $n < n_0$ and to $g(n)$ for $n \geq n_0$ is computable, since it differs from $g$ at finitely many points, whose values can be written into the algorithm; and it dominates $f$ everywhere.
:::
::::

::::exercise{#ex-low-join difficulty=1 objective="Apply the low basis theorem to a product class to choose members of two classes with a low join."}
Let $\mathcal P$ and $\mathcal Q$ be non-empty $\Pi^0_1$ classes. Show that there are $X \in \mathcal P$ and $Y \in \mathcal Q$ such that $X \oplus Y$ is low.

:::solution
Let $\mathcal P = [S]$ and $\mathcal Q = [T]$ with $S$ and $T$ computable, and let $\mathcal R = \{ X \oplus Y : X \in \mathcal P, Y \in \mathcal Q \}$. A sequence $Z$ is outside $\mathcal R$ if and only if its even part has a prefix outside $S$ or its odd part has a prefix outside $T$; such a prefix of length $n$ is determined by $Z \uh 2n$, so the complement of $\mathcal R$ is a $\Sigma^0_1$ class and $\mathcal R$ is a non-empty $\Pi^0_1$ class. By :ref{#thm-low-basis}, it has a low member $X \oplus Y$, with $X \in \mathcal P$ and $Y \in \mathcal Q$. (In particular $X$ and $Y$ are low, since lowness is closed downward.)
:::
::::

::::exercise{#ex-low-tree-lowness-index difficulty=2 objective="Relativize the low basis theorem to a low tree, uniformly in a lowness index."}
Code strings by integers, so that a binary tree is a set of integers. Let $T$ be an infinite binary tree that is low, and $j$ an index with $\Phi^{\emptyset'}_j = T'$, a **lowness index** of $T$. Show that from $j$ one can compute an index $k$ such that $\Phi^{\emptyset'}_k = X'$ for some path $X$ of $T$.

:::solution
Run the construction of :ref{#thm-low-basis} relative to $T$. For a finite set $F$, let $\mathcal P_F = [T] \cap \{ X : \Phi^X_i(i)\diverge \text{ for all } i \in F \}$, the class of paths through the tree $T \cap \{ \sigma : \Phi^\sigma_i(i)[|\sigma|]\diverge \text{ for all } i \in F \}$, which is computable in $T$, uniformly in $F$. By :ref{#prop-pi01-emptiness} relativized to $T$, emptiness of $\mathcal P_F$ is $\Sigma^0_1$ relative to $T$, uniformly in $F$: by SMN, there is a computable $g$ such that $\mathcal P_F = \emptyset$ if and only if $g(F) \in T'$.

Define $F_0 = \emptyset$, and $F_{e+1} = F_e \cup \{e\}$ and $J(e) = 0$ if $g(F_e \cup \{e\}) \notin T'$, that is, if $\mathcal P_{F_e \cup \{e\}} \neq \emptyset$; otherwise $F_{e+1} = F_e$ and $J(e) = 1$. As in the proof of the theorem, the classes $\mathcal P_{F_e}$ are non-empty and decreasing, and every $X$ in their intersection, which is non-empty by :ref{#prop-cantor-compact}, is a path of $T$ with $X' = J$. The construction uses only the bits $T'(g(F))$, and $T'(m) = \Phi^{\emptyset'}_j(m)$; so $J$ is computed by an algorithm with oracle $\emptyset'$ that depends computably on $j$, and its index is the required $k$. Adapted from Hirschfeldt, *Slicing the Truth*, Exercise 3.12 (Jockusch and Soare).
:::
::::

::::exercise{#ex-pi02-singleton difficulty=1 objective="See that the low basis theorem fails for $\Pi^0_2$ classes."}
Call a class $\Pi^0_2$ if it is of the form $\{ X : \forall n\ \exists m\ R(X \uh m, n) \}$ for a computable relation $R$. Show that $\{ \emptyset' \}$ is a $\Pi^0_2$ class, and deduce that the low basis theorem fails for non-empty $\Pi^0_2$ classes.

:::solution
Let $R(\tau, \langle e, s \rangle)$ hold if $|\tau| > e$, if $\tau(e) = 1$ implies $\Phi_e(e)[|\tau|]\converge$, and if $\Phi_e(e)[s]\converge$ implies $\tau(e) = 1$. It is computable. For fixed $e$ and $s$, $\exists m\ R(X \uh m, \langle e, s \rangle)$ holds if and only if ($X(e) = 1$ implies $\Phi_e(e)\converge$) and ($\Phi_e(e)[s]\converge$ implies $X(e) = 1$): if $X(e) = 1$ and $\Phi_e(e)[t]\converge$, take $m > \max(e, t)$, using the monotonicity of stages; if $X(e) = 0$, any $m > e$ works; and the second condition does not depend on $m$. Taking all $e$ and $s$, the class defined by $R$ is the class of $X$ such that $X(e) = 1 \Rightarrow e \in \emptyset'$ and $e \in \emptyset' \Rightarrow X(e) = 1$, that is, $\{ \emptyset' \}$. Its only member is not low, since $\emptyset'' \not\leq_T \emptyset'$. So a non-empty $\Pi^0_2$ class need not have a low member; the closedness of $\Pi^0_1$ classes, and the effective compactness it gives, is what the proof of :ref{#thm-low-basis} uses.
:::
::::

::::exercise{#ex-countable-cone-avoidance difficulty=1 objective="Interleave the requirements of the cone avoidance construction to avoid countably many cones at once."}
Let $C_0, C_1, \dots$ be non-computable sets. Show that every non-empty $\Pi^0_1$ class has a member that computes none of the $C_i$.

:::solution
Modify the proof of :ref{#thm-cone-avoidance-basis}: at step $s = \langle e, i \rangle$, given the non-empty $\Pi^0_1$ class $\mathcal P_s$, apply :ref{#lem-uniform-cone} with the set $C_i$ to find $m$ such that $\mathcal P_s \cap \{ Y : \neg\, (\Phi^Y_e(m)\converge = C_i(m)) \}$ is non-empty, and let $\mathcal P_{s+1}$ be this class, for the least such $m$. It is $\Pi^0_1$, as in the proof of the theorem. A member $Y$ of $\bigcap_s \mathcal P_s$, which exists by :ref{#prop-cantor-compact}, satisfies $\Phi^Y_e \neq C_i$ for all $e$ and $i$, so it computes no $C_i$.
:::
::::

::::exercise{#ex-low-cone-avoidance difficulty=2 objective="Combine the low basis and cone avoidance constructions into a single construction effective in $\emptyset'$."}
Let $C$ be a non-computable set. Show that every non-empty $\Pi^0_1$ class has a low member that does not compute $C$.

:::solution
If $C$ is not $\Delta^0_2$, any low member $X$ works: every set computable in $X$ is computable in $\emptyset'$. Suppose that $C$ is $\Delta^0_2$. Alternate the steps of the two constructions. At step $2e$, given $\mathcal P_{2e}$, proceed as in :ref{#thm-low-basis}: ask $\emptyset'$ whether $\mathcal P_{2e} \cap \{ X : \Phi^X_e(e)\diverge \}$ is empty, and let $\mathcal P_{2e+1}$ be this class if it is not empty, and $\mathcal P_{2e}$ otherwise. At step $2e+1$, proceed as in :ref{#thm-cone-avoidance-basis}: for $m = 0, 1, \dots$, compute $C(m)$ with $\emptyset'$ and ask $\emptyset'$ whether $\mathcal B_m = \mathcal P_{2e+1} \cap \{ Y : \neg\, (\Phi^Y_e(m)\converge = C(m)) \}$ is empty, an index of this $\Pi^0_1$ class being computable from $e$, $m$, $C(m)$ and an index of $\mathcal P_{2e+1}$; stop at the first $m$ for which it is not, and let $\mathcal P_{2e+2} = \mathcal B_m$. Such an $m$ exists by :ref{#lem-uniform-cone}, so the search ends. The whole sequence of indices is computable in $\emptyset'$. A member $X$ of the intersection satisfies $X'(e) = 1$ if and only if the class was kept at step $2e$, which $\emptyset'$ computes, so $X$ is low; and $\Phi^X_e \neq C$ for every $e$, by step $2e+1$. This is a particular case of a theorem of Jockusch and Soare: for every non-computable $C$, a non-empty $\Pi^0_1$ class has a member $X$ with $C \not\leq_T X$ and $X' \leq_T C \oplus \emptyset'$ (Downey and Hirschfeldt, Theorem 2.19.10).
:::
::::

::::exercise{#ex-dominated-continuum difficulty=2 objective="Split the construction of the computably dominated basis theorem along a binary tree to obtain continuum many members."}
Let $\mathcal P$ be a non-empty $\Pi^0_1$ class without computable member. Show that $\mathcal P$ has continuum many computably dominated members.

:::solution
*One step.* Let $\mathcal R$ be a non-empty $\Pi^0_1$ class and $e \in \nat$. As in the proof of :ref{#thm-dominated-basis}, there is a non-empty $\Pi^0_1$ class $\mathcal R' \subseteq \mathcal R$ such that either $\Phi^X_e$ is partial for every $X \in \mathcal R'$, or there is a computable function dominating $\Phi^X_e$ for every $X \in \mathcal R'$: take $\mathcal R' = \mathcal R \cap \{ X : \Phi^X_e(m)\diverge \}$ for the least $m$ for which it is non-empty, if there is one, and $\mathcal R' = \mathcal R$ otherwise, using :ref{#lem-uniform-bound}.

*Splitting.* A non-empty $\Pi^0_1$ subclass $\mathcal R$ of $\mathcal P$ has no computable member, so it has two members, since the member of a $\Pi^0_1$ class with one member is computable (:ref{#cor-countable-computable}). If $X \neq Y$ are members and $n$ is the first position where they differ, the classes $\mathcal R \cap [(X \uh n)\, 0]$ and $\mathcal R \cap [(X \uh n)\, 1]$ are disjoint non-empty $\Pi^0_1$ subclasses of $\mathcal R$.

*Construction.* Define non-empty $\Pi^0_1$ classes $\mathcal P_\rho \subseteq \mathcal P$, for $\rho \in \bstr$. Let $\mathcal P_\varepsilon = \mathcal P$. Given $\mathcal P_\rho$ with $|\rho| = e$, split it into two disjoint non-empty $\Pi^0_1$ subclasses, and apply the first step with $e$ to each of them; call the results $\mathcal P_{\rho 0}$ and $\mathcal P_{\rho 1}$. For $Z \in \cs$, the classes $\mathcal P_{Z \uh e}$ are non-empty, closed and decreasing, so they have a common member $X_Z$ (:ref{#prop-cantor-compact}). If $\Phi^{X_Z}_e$ is total, then the class $\mathcal P_{Z \uh (e+1)}$, which contains $X_Z$, was obtained by the first step in its second case, so a computable function dominates $\Phi^{X_Z}_e$. Hence $X_Z$ is computably dominated. If $Z \neq Z'$ first differ at position $e$, then $X_Z$ and $X_{Z'}$ belong to the disjoint classes $\mathcal P_{(Z \uh e) 0}$ and $\mathcal P_{(Z \uh e) 1}$, so $X_Z \neq X_{Z'}$. The map $Z \mapsto X_Z$ is injective, and $\mathcal P$ has continuum many computably dominated members. Downey and Hirschfeldt state this after their Theorem 2.19.11.
:::
::::
:::::
