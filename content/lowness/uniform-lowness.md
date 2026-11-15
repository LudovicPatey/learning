---
title: Uniform lowness
summary: Lowness indices name low sets so that ∅′ computes their jumps uniformly, and the low basis theorem holds with lowness indices; a low code of a Scott ideal lets ∅′ answer Σ⁰₁ questions about all members of the ideal, and about their joins, uniformly in their indices.
duration: 30
prerequisites: [coded-ideals, arithmetic-hierarchy/codes, pi01-classes/basis-theorems]
---

The constructions of the following lessons run with an oracle, $\emptyset'$ or a set PA relative to $\emptyset'$, and handle infinitely many sets: the reservoirs of the successive conditions. Each reservoir is low, but lowness of each set separately is not enough. The oracle receives the reservoirs through finite names, and must answer questions about them, such as "is this $\Pi^0_1$ class relative to the reservoir empty?", uniformly in the names. This lesson describes two ways of naming low sets for which this is possible. A **lowness index** names a single low set together with a procedure computing its jump from $\emptyset'$. A **low code** of a Scott ideal names all the members of the ideal at once, by their column numbers, and one reduction of the jump of the code to $\emptyset'$ serves for all of them. Both appear in proofs of the Cholak–Jockusch–Slaman theorem: Hirschfeldt uses the first, Patey's monograph the second, and this course follows the monograph.

## The low basis theorem with lowness indices

Recall that a **lowness index** of a low set $Z$ is a number $\ell$ with $\Phi^{\emptyset'}_\ell = Z'$ (:ref{to="arithmetic-hierarchy/codes"}). By :ref{#prop-no-lowness-index}, a lowness index cannot in general be computed from a $\Delta^0_2$ index: knowing how $\emptyset'$ computes $Z$ does not tell how it computes $Z'$. Lowness indices are preserved by Turing reductions, uniformly (:ref{#exr-lowness-index-reduction} below). The construction of :ref{#thm-low-basis} relativizes, and the relativized construction is uniform in lowness indices.

:::proposition[Jockusch, Soare]{#prop-uniform-low-basis}
There is a total computable function $u$ with the following property. Let $\ell$ be a lowness index of a low set $Z$, and $t$ such that $\Phi^Z_t$ is the characteristic function of an infinite binary tree $T$. Then $u(\ell, t)$ is a lowness index of $Z \oplus X$ for some path $X$ of $T$.
:::

:::proof{of=prop-uniform-low-basis}
We describe a procedure with oracle $\emptyset'$, uniform in $\ell$ and $t$, that computes $(Z \oplus X)'$ for some path $X$; its index $u(\ell, t)$ is computable by the parameter form of SMN. Let $\mathcal P_0 = [T]$, a non-empty $\Pi^0_1(Z)$ class. Given a non-empty $\Pi^0_1(Z)$ class $\mathcal P_e$, by an index, let $\mathcal Q_e = \mathcal P_e \cap \{ X : \Phi^{Z \oplus X}_e(e)\diverge \}$. Emptiness of $\mathcal Q_e$ is a $\Sigma^0_1(Z)$ property of its index, by :ref{#prop-pi01-emptiness} relativized; by item 2 of :ref{#thm-jump}, there is a computable $g$, independent of $Z$, such that $\mathcal Q_e$ is empty if and only if $g(\text{index}) \in Z'$. The procedure evaluates $Z'(g(\text{index}))$ as $\Phi^{\emptyset'}_\ell(g(\text{index}))$. If $\mathcal Q_e \neq \emptyset$, let $\mathcal P_{e+1} = \mathcal Q_e$ and $J(e) = 0$; otherwise $\mathcal P_{e+1} = \mathcal P_e$ and $J(e) = 1$. As in :ref{#thm-low-basis}, every $X$ in the non-empty intersection of the classes $\mathcal P_e$ satisfies $(Z \oplus X)' = J$, and $J = \Phi^{\emptyset'}_{u(\ell, t)}$.
:::

The function $u$ is total even when its arguments are not what the proposition assumes; its output is then meaningless. This is how lowness indices are used: a construction with oracle $\emptyset'$ manipulates lowness indices of the sets it has built, and the correctness of each index is proved by induction. For instance, starting from a lowness index of $\emptyset$ and applying $u$ to the trees of $\{0, 1\}$-valued functions DNC relative to the current set gives a $\emptyset'$-computable sequence of lowness indices of sets $Z_0 \leq_T Z_1 \leq_T \cdots$, each PA relative to the previous one: the proof of :ref{#thm-low-scott}, made uniform. Uniformity of the indices does not make the join $\bigoplus_n Z_n$ low: a computation with this oracle may query infinitely many columns, and the jumps of the sets $Z_n$ say nothing about it. The low codes of :ref{#cor-scott-codes} are obtained instead by a single application of the low basis theorem, to the class of codes.

:::quiz[lowness indices]
In the proof of :ref{#prop-uniform-low-basis}, why is a lowness index of $Z$ needed, rather than a $\Delta^0_2$ index of $Z$?

- [x] Because the questions asked are $\Sigma^0_1(Z)$, that is, questions about $Z'$; a $\Delta^0_2$ index gives $Z$ but not $Z'$, and :ref{#prop-no-lowness-index} shows that $Z'$ cannot be recovered uniformly from it.
- [ ] Because $Z$ is not computable in $\emptyset'$.

  It is, since $Z$ is low.
- [ ] Because the tree $T$ is computable in $Z'$.

  It is computable in $Z$, by hypothesis.
:::

## Questions about the members of a low code

Let $M = \bigoplus_n Z_n$ be a low code of a Scott ideal $\mathcal M$, as given by :ref{#cor-scott-codes}. The point of lowness of the code, rather than of each member, is that $\emptyset'$ answers questions about the members of $\mathcal M$ uniformly in their $M$-indices, as if they were computable sets.

:::proposition{#prop-low-code-questions}
Let $M = \bigoplus_n Z_n$ be a low set.
1. If $R(a, \vec y)$ is $\Sigma^0_1(Z_a)$ uniformly in $a$, that is, $R(a, \vec y) \iff \exists s\ Q(Z_a \uh s, a, \vec y, s)$ for a computable relation $Q$, then $R$ is computable in $\emptyset'$.
2. If $R(a, \vec y)$ is $\Sigma^0_2(Z_a)$ or $\Pi^0_2(Z_a)$ uniformly in $a$, then $R$ is $\Sigma^0_2$ or $\Pi^0_2$, respectively.
:::

:::proof{of=prop-low-code-questions}
1. The column $Z_a \uh s$ is computed from $M$ uniformly in $a$, so $R$ is $\Sigma^0_1(M)$, hence computable in $M'$ by Post's theorem relativized, hence in $\emptyset'$ since $M$ is low.
2. Uniformly in $a$, a $\Sigma^0_2(Z_a)$ relation is $\Sigma^0_2(M)$, that is, $\Sigma^0_1(M')$ by Post's theorem relativized. Since $M' \leq_T \emptyset'$, it is $\Sigma^0_1(\emptyset')$, that is, $\Sigma^0_2$. The case of $\Pi^0_2$ is the complement.
:::

For instance, given $a$ and an index of a $\Pi^0_1(Z_a)$ class, $\emptyset'$ decides whether the class is empty, by item 1 and :ref{#prop-pi01-emptiness}; and the set of $a$ such that $Z_a$ is infinite, or such that $Z_a \cap Z_b$ is infinite, is $\Pi^0_2$ by item 2. These are exactly the complexities that the codes of computable sets have, as $\Delta^0_1$ indices: from the point of view of $\emptyset'$, the members of a low Scott ideal behave like computable sets. But the ideal $\mathcal M$ is closed under paths of trees, with computable indices (:ref{#lem-scott-paths}), which the computable sets are not. This is what makes it possible, in :ref{to="lowness/cjs-theorem"}, to run the Dzhafarov–Jockusch forcing effectively.

:::quiz[questions about a low code]
In item 1 of :ref{#prop-low-code-questions}, why is it important that the relation be uniform in $a$?

- [x] Because a single reduction of $M'$ to $\emptyset'$ must answer the questions for all members at once; uniformity makes $R$ one $\Sigma^0_1(M)$ relation rather than countably many unrelated ones.
- [ ] Because the members of $\mathcal M$ are not low.

  They are low, being computable in $M$.
- [ ] Because $\emptyset'$ cannot compute $M$.

  It can, since $M$ is low; the point is that it computes $M'$.

---

The members of the ideal of :ref{#thm-low-scott} are low. Why does the proof of :ref{to="lowness/cjs-theorem"} use a low code, rather than only the ideal of :ref{#thm-low-scott}?

- [x] Because the construction must answer questions about all the reservoirs it uses with one oracle, uniformly in their names; lowness of each member separately gives a reduction for each member, with no uniformity.
- [ ] Because the ideal of :ref{#thm-low-scott} is not a Scott ideal.

  It is a Scott ideal.
- [ ] Because a low code is computable.

  A code of a Scott ideal is PA, hence not computable.
:::


The two kinds of names differ in what they say about several sets at once. A lowness index is attached to one set, and lowness indices of $X$ and of $B$ say nothing about $X \oplus B$, which need not be low: there are low sets whose join computes $\emptyset'$ (see :ref{to="turing-degrees/low-and-high"}). Constructions with lowness indices therefore choose each new set together with the sets it will be combined with, as in :ref{#prop-uniform-low-basis}, which gives a lowness index of $Z \oplus X$ and not only of $X$. A low code of a Scott ideal answers questions about any finite family of members, since their join is again a column, with an $M$-index computable from theirs. The price is that the reservoirs are restricted to one ideal, fixed in advance.

## Exercises

::::exercise{#exr-lowness-index-reduction difficulty=1 objective="Transfer lowness indices along Turing reductions, uniformly."}
Show that there is a computable function $v$ such that if $\ell$ is a lowness index of $Z$ and $\Phi^Z_e$ is the characteristic function of a set $Y$, then $v(\ell, e)$ is a lowness index of $Y$.

:::solution
The set $Y'$ is $Y$-c.e., hence $Z$-c.e., uniformly in $e$: $x \in Y'$ if and only if $\Phi^{\Phi^Z_e}_x(x)$ converges, where the inner oracle is simulated by $\Phi^Z_e$. By item 2 of :ref{#thm-jump}, there is a computable injective $f$, depending computably on $e$ and not on $Z$, with $x \in Y' \iff f(e, x) \in Z'$. The procedure $x \mapsto \Phi^{\emptyset'}_\ell(f(e, x))$ computes $Y'$; its index $v(\ell, e)$ is given by SMN.
:::
::::

## Notes and references

The low basis theorem is due to Jockusch and Soare (1972), who observed that it is uniform; :ref{#prop-uniform-low-basis} is Exercise 3.12 of Hirschfeldt, stated there for low trees, and lowness indices are used in Hirschfeldt's proof of the Cholak–Jockusch–Slaman theorem for $\Delta^0_2$ sets (proof of Theorem 6.57), whose reservoirs are low sets; Dzhafarov and Mummert also use low reservoirs (Lemma 8.5.12). The use of a low code of a Scott ideal instead follows the section *Ramsey's theorem for pairs* of the chapter *Lowness* of Patey's monograph; the low code itself is Simpson's construction (Simpson, Lemma VIII.2.9 and Theorem VIII.2.17).

- C. G. Jockusch, Jr. and R. I. Soare, *Π⁰₁ classes and degrees of theories*, Transactions of the American Mathematical Society 173 (1972), 33–56.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2014, Sections 3.1 and 6.6.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Section 8.5.
- S. G. Simpson, *Subsystems of Second Order Arithmetic*, second edition, Cambridge University Press, 2009, Section VIII.2.
- L. Patey, *Lowness and avoidance*, monograph, chapter *Lowness*, sections *Indices* and *Ramsey's theorem for pairs*.

:::::exercises
::::exercise{#ex-low-code-path-names difficulty=2 objective="Combine the questions answered by a low code with the path function of the Scott class, to name paths of trees in the ideal."}
Let $M = \bigoplus_n Z_n$ be a low member of $\mathcal S_\emptyset$. Show that $\emptyset'$ computes a function $g$ such that, for every $a$ and every $t$ such that $\Phi^{Z_a}_t$ is the characteristic function of a binary tree $T$, $g(a, t) = 0$ if $T$ is finite, and otherwise $g(a, t) = 1 + m$ where $m$ is an $M$-index of a path of $T$.

:::solution
The tree $T$ is finite if and only if it has no node of some length (:ref{#prop-pi01-emptiness}, relativized), a $\Sigma^0_1(Z_a)$ property uniformly in $a$ and $t$. By :ref{#prop-low-code-questions}, $\emptyset'$ decides it. If $T$ is infinite, let $g(a, t) = 1 + p(a, t)$, with $p$ as in :ref{#lem-scott-paths}.
:::
::::

::::exercise{#ex-uniform-low-basis-iterate difficulty=1 objective="Iterate the uniform low basis theorem to choose two paths whose join with the oracle is low, with a lowness index."}
Let $\ell$ be a lowness index of a low set $Z$, and $t_1$, $t_2$ such that $\Phi^Z_{t_1}$ and $\Phi^Z_{t_2}$ are the characteristic functions of infinite binary trees $T_1$ and $T_2$. Show that a lowness index of $Z \oplus X_1 \oplus X_2$, for some paths $X_1$ of $T_1$ and $X_2$ of $T_2$, is computable from $\ell$, $t_1$ and $t_2$. What do $u(\ell, t_1)$ and $u(\ell, t_2)$ say about $X_1 \oplus X_2$?

:::solution
By :ref{#prop-uniform-low-basis}, $\ell_1 = u(\ell, t_1)$ is a lowness index of $Z \oplus X_1$ for some path $X_1$ of $T_1$. Let $t_2'$ be an index, computable from $t_2$, of the functional that, with oracle $Y \oplus W$, runs $\Phi^Y_{t_2}$; then $\Phi^{Z \oplus X_1}_{t_2'} = \Phi^Z_{t_2}$ is the characteristic function of $T_2$. So $u(\ell_1, t_2')$ is a lowness index of $(Z \oplus X_1) \oplus X_2$ for some path $X_2$ of $T_2$, and a lowness index of $Z \oplus X_1 \oplus X_2$, in any bracketing, follows by :ref{#exr-lowness-index-reduction}. Separately, $u(\ell, t_1)$ and $u(\ell, t_2)$ are lowness indices of $Z \oplus X_1$ and $Z \oplus X_2$ for paths chosen independently of each other; they give no information on $X_1 \oplus X_2$. This is why constructions with lowness indices choose each new set relative to the join of the sets already built.
:::
::::

::::exercise{#ex-low-code-equality difficulty=1 objective="Use the lowness of a code to compare its columns with $\emptyset'$, and remove repetitions from the code."}
Let $M = \bigoplus_n Z_n$ be a low set.

1. Show that $\emptyset'$ decides, given $a$ and $b$, whether $Z_a \subseteq Z_b$, and whether $Z_a = Z_b$.
2. Deduce that $\emptyset'$ computes the function sending $a$ to the least $b$ with $Z_b = Z_a$.
3. Suppose that $M$ codes an infinite family, for instance a Scott ideal. Show that $\emptyset'$ computes a code $N$ of the same family in which every member has exactly one $N$-index.

:::solution
1. $Z_a \not\subseteq Z_b$ if and only if there is $x$ with $\langle a, x \rangle \in M$ and $\langle b, x \rangle \notin M$. This is $\Sigma^0_1(M)$ uniformly in $a$ and $b$, so, as in item 1 of :ref{#prop-low-code-questions}, it is decided by $M'$, hence by $\emptyset'$. Equality is the conjunction of two inclusions.
2. Search for the least $b \leq a$ with $Z_b = Z_a$, using item 1.
3. Let $B$ be the set of $b$ such that $Z_c \neq Z_b$ for every $c < b$. It is computable in $\emptyset'$ by item 1, and it is infinite, since every member of the family has a least index and there are infinitely many members. Let $b_0 < b_1 < \cdots$ enumerate $B$, and $N = \bigoplus_n Z_{b_n}$, that is, $\langle n, x \rangle \in N$ if and only if $\langle b_n, x \rangle \in M$. Then $N \leq_T M \oplus \emptyset' \equiv_T \emptyset'$, since $M \leq_T M' \leq_T \emptyset'$. Every member of the family is $Z_a$ for some $a$, hence $Z_{b_n}$ for the least index $b_n$ of $Z_a$, and for no other $n$.
:::
::::

::::exercise{#ex-low-code-lowness-indices difficulty=1 objective="Compute lowness indices of all members of a low code from one lowness index of the code, and compare with the uniform low basis theorem."}
Let $M = \bigoplus_n Z_n$ be a low set with lowness index $\ell$.

1. Show that a lowness index of $Z_a$ is computable from $\ell$ and $a$.
2. Suppose moreover $M \in \mathcal S_\emptyset$. Show that there is a computable function $g$ such that, whenever $\Phi_t$ is the characteristic function of an infinite binary tree $T$, $g(t)$ is a lowness index of a path of $T$.

:::solution
1. Let $c(a)$ be an index, computable from $a$, of the functional $\Phi^W(x) = W(\langle a, x \rangle)$. Then $\Phi^M_{c(a)}$ is the characteristic function of $Z_a$, and $v(\ell, c(a))$ is a lowness index of $Z_a$, with $v$ as in :ref{#exr-lowness-index-reduction}.
2. Let $t'$ be an index, computable from $t$, of the functional that ignores its oracle and runs $\Phi_t$. Since $Z_0 = \emptyset$, $\Phi^{Z_0}_{t'}$ is the characteristic function of $T$, and by :ref{#lem-scott-paths} the column $Z_{p(0, t')}$ is a path of $T$. Let $g(t) = v(\ell, c(p(0, t')))$. Unlike the function $u$ of :ref{#prop-uniform-low-basis}, which chooses a new path for each call, $g$ takes all its paths from one ideal; so the join of two of them is again a column, with a lowness index computable in the same way.
:::
::::

::::exercise{#ex-lowness-index-sequences difficulty=2 objective="See that a $\emptyset'$-computable sequence of lowness indices answers questions about each member uniformly, but does not make the join low."}
Let $(\ell_n)$ be a $\emptyset'$-computable sequence such that each $\ell_n$ is a lowness index of a set $Z_n$.

1. Show that if $R(n, y)$ is $\Sigma^0_1(Z_n)$ uniformly in $n$, that is, $R(n, y) \iff \exists s\ Q(Z_n \uh s, n, y, s)$ for a computable relation $Q$, then $R$ is computable in $\emptyset'$.
2. Let $Z_n = \emptyset' \cap \{ 0, \dots, n - 1 \}$. Show that $\emptyset'$ computes a sequence of lowness indices of the sets $Z_n$, and that $\bigoplus_n Z_n$ is not low.

:::solution
1. The set of pairs $\langle n, y \rangle$ such that $\exists s\ Q(W \uh s, n, y, s)$ is $W^W_a$ for a fixed $a$. By item 2 of :ref{#thm-jump}, there is a computable $f$ with $\langle n, y \rangle \in W^W_a \iff f(\langle n, y \rangle) \in W'$ for every $W$. So $R(n, y)$ holds if and only if $f(\langle n, y \rangle) \in Z_n'$, that is, $\Phi^{\emptyset'}_{\ell_n}(f(\langle n, y \rangle)) = 1$; the oracle $\emptyset'$ computes $\ell_n$ and evaluates this.
2. The finite set $D_c$ is computable uniformly in its canonical index $c$, so the set of pairs $\langle c, x \rangle$ with $x \in (D_c)'$ is c.e., and many-one reducible to $\emptyset'$ by a computable $h$. By SMN there is a computable $\lambda$ with $\Phi^{\emptyset'}_{\lambda(c)}(x) = \emptyset'(h(\langle c, x \rangle))$, so $\lambda(c)$ is a lowness index of $D_c$. The oracle $\emptyset'$ computes the canonical index $c_n$ of $\emptyset' \cap \{ 0, \dots, n - 1 \}$, hence $\ell_n = \lambda(c_n)$. But $x \in \emptyset'$ if and only if $\langle x + 1, x \rangle \in \bigoplus_n Z_n$, so $\emptyset' \leq_T \bigoplus_n Z_n$, and the join is not low: by item 5 of :ref{#thm-jump}, its jump computes $\emptyset''$, which is not computable in $\emptyset'$ by item 4. Item 1 still applies to this sequence: a question about the join may query infinitely many columns, and no single $\ell_n$ answers it.
:::
::::
:::::
