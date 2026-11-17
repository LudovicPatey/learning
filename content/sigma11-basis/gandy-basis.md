---
title: The Gandy basis theorem
summary: Σ¹₁ classes as projections of trees of tuples; every non-empty Σ¹₁ class has a member X whose hyperjump is computable in O, so that X does not compute O hyperarithmetically and ω₁ˣ = ω₁ᶜᵏ (Gandy).
duration: 25
prerequisites: [hyperjump, hyperarithmetic/sigma11-classes, descriptive-set-theory/perfect-sets]
---

By the Kleene basis theorem, every non-empty $\Sigma^1_1$ class has a member computable in $\mathcal O$ (:ref{#thm-kleene-basis}), and by Kleene's theorem on trees without hyperarithmetic paths, $\mathcal O$ cannot be replaced by a hyperarithmetic set. Gandy refined the bound in the way the low basis theorem refines the bound $\emptyset'$ for $\Pi^0_1$ classes: every non-empty $\Sigma^1_1$ class has a **hyperlow** member $X$, whose hyperjump $\mathcal O^X$ is computable in $\mathcal O$. Such a member is not hyperarithmetically above $\mathcal O$, so by Spector's theorem it does not collapse $\omega_1^{\mathrm{CK}}$.

The proof follows the proof of the low basis theorem: decide, for each $n$, whether $n \in \mathcal O^X$, by restricting the class to the members with $n \notin \mathcal O^X$ when possible. The condition $n \notin \mathcal O^X$ is $\Sigma^1_1$, so the restricted class is again $\Sigma^1_1$, and $\mathcal O$ can decide whether it is empty. The difficulty is that a decreasing sequence of non-empty $\Sigma^1_1$ classes may have an empty intersection, unlike a decreasing sequence of non-empty $\Pi^0_1$ classes. The construction therefore builds, together with $X$, the **witnesses** that $X$ belongs to each class: these are infinite paths of trees, and building all of them by finite approximations keeps the limit inside every class.

## Trees of tuples

A **tree of $k$-tuples** is a set $R$ of $k$-tuples $(\sigma_1, \dots, \sigma_k)$ of strings of numbers, all of the same length, closed under taking prefixes of the same length in every coordinate. A **path** of $R$ is a $k$-tuple of functions $(f_1, \dots, f_k)$ such that $(f_1 \uh n, \dots, f_k \uh n) \in R$ for every $n$; the paths form the class $[R]$. Coding tuples of strings by strings of numbers, trees of tuples are trees on $\nat$, and the notions of the previous courses apply.

By the normal form theorem, every $\Sigma^1_1$ class $\mathcal A$ of sets or functions is the **projection** of the class of paths of a computable tree of pairs: there is a computable tree $S$ of pairs with $f \in \mathcal A$ if and only if $(f, g) \in [S]$ for some $g$, as in :ref{#def-sigma11-class}. The witness $g$ certifies the membership of $f$. The construction is uniform: for the relation $n \notin \mathcal O^f$, which is $\Sigma^1_1$ uniformly in $n$, there is a computable sequence of trees of pairs $(W_n)$ with
$$
n \notin \mathcal O^f \iff \exists g\ (f, g) \in [W_n].
$$
Indeed, by the normal form theorem relativized to $f$, uniformly, there are trees $T^f_n$, computable in $f$ uniformly in $n$, with $n \in \mathcal O^f$ if and only if $T^f_n$ is well-founded; let $W_n$ be the set of pairs $(\sigma, \tau)$ of strings of the same length such that every prefix of $\tau$ belongs to the tree $T^\sigma_n$ computed with the finite oracle $\sigma$, within $|\sigma|$ steps. With the usual convention that a computation with oracle $\sigma$ only queries $\sigma$ and that the membership of a string of length $\ell$ in $T^f_n$ is decided by a computation using $f \uh \ell$, a pair $(f, g)$ is a path of $W_n$ exactly when $g$ is a path of $T^f_n$.

For example, the class of the sets $X$ that are not hyperarithmetic is $\Sigma^1_1$ (:ref{#prop-sigma11-singleton}), and a witness of the membership of $X$ is a path through a tree computable in $X$, uniformly: since "$X \in \mathrm{HYP}$" is $\Pi^1_1$, it says that a tree computable in $X$ is well-founded, and its negation that this tree has a path.

For a computable tree of tuples $R$ and a node $\rho \in R$, the question whether $R$ has a path extending $\rho$ is $\Sigma^1_1$, uniformly in $R$ and $\rho$; its negation is $\Pi^1_1$, hence many-one reducible to $\mathcal O$ (:ref{#thm-o-complete}). So **$\mathcal O$ decides, uniformly, whether a computable tree of tuples has a path through a given node**.

## The theorem

:::theorem[Gandy]{#thm-gandy-basis}
Every non-empty $\Sigma^1_1$ class $\mathcal A \subseteq \cs$ has a member $X$ with $\mathcal O^X \leq_T \mathcal O$. Such an $X$ satisfies $\mathcal O \not\leq_h X$ and $\omega_1^X = \omega_1^{\mathrm{CK}}$.
:::

:::proof{of=thm-gandy-basis}
Let $S$ be a computable tree of pairs whose projection is $\mathcal A$, with first coordinates in $\{0, 1\}$, and $(W_n)$ as above. We build, computably in $\mathcal O$, a sequence of computable trees of tuples $R_n$, of $(n + 2)$-tuples, and nodes $\rho_n \in R_n$ of length $n$, such that:

1. $R_0 = S$ and $\rho_0 = (\varepsilon, \varepsilon)$;
2. if $(\sigma_1, \dots, \sigma_{n+3}) \in R_{n+1}$, then $(\sigma_1, \dots, \sigma_{n+2}) \in R_n$;
3. $\rho_{n+1}$, without its last coordinate, extends $\rho_n$;
4. $R_n$ has a path extending $\rho_n$.

*Step $n$.* Ask $\mathcal O$ whether $R_n$ has a path $(f_1, \dots, f_{n+2})$ extending $\rho_n$ with $n \notin \mathcal O^{f_1}$. This is a $\Sigma^1_1$ question: it asks whether the computable tree $R'$ of the $(n + 3)$-tuples $(\sigma_1, \dots, \sigma_{n+2}, \tau)$ with $(\sigma_1, \dots, \sigma_{n+2}) \in R_n$ and $(\sigma_1, \tau) \in W_n$ has a path extending $\rho_n$.

- If the answer is yes, let $R_{n+1} = R'$.
- If the answer is no, let $R_{n+1}$ be the tree of the tuples $(\sigma_1, \dots, \sigma_{n+2}, 0^{|\sigma_1|})$ with $(\sigma_1, \dots, \sigma_{n+2}) \in R_n$: a last coordinate that carries no information. In this case, every path of $R_n$ extending $\rho_n$ satisfies $n \in \mathcal O^{f_1}$.

In both cases, $R_{n+1}$ has a path whose first $n + 2$ coordinates extend $\rho_n$, by 4 and the answer. Let $\rho_{n+1}$ be the first node of length $n + 1$ in $R_{n+1}$, in a fixed enumeration, whose first $n + 2$ coordinates extend $\rho_n$ and through which $R_{n+1}$ has a path; $\mathcal O$ finds it, by the remark above. Conditions 2 to 4 hold.

*The limit.* For each $i \geq 1$, the $i$-th coordinates of the nodes $\rho_n$, for $n \geq i - 2$, form an increasing chain of strings whose lengths tend to infinity, by 3; let $f_i$ be their union. Fix $k$. For $m \geq k$, the node $\rho_m$, restricted to its first $k + 2$ coordinates, belongs to $R_k$, by 2 applied repeatedly; and the prefixes of $\rho_k$ belong to $R_k$. So $(f_1, \dots, f_{k+2})$ is a path of $R_k$ extending $\rho_k$, for every $k$. With $k = 0$, $(f_1, f_2) \in [S]$, so $X = f_1 \in \mathcal A$.

*The hyperjump.* If the answer at step $n$ was yes, then $(f_1, \dots, f_{n+3})$ is a path of $R'$, so $(f_1, f_{n+3}) \in [W_n]$ and $n \notin \mathcal O^X$. If it was no, then $(f_1, \dots, f_{n+2})$ is a path of $R_n$ extending $\rho_n$, so $n \in \mathcal O^X$. Hence $n \in \mathcal O^X$ if and only if the answer at step $n$ is no. The construction is computable in $\mathcal O$, so $\mathcal O^X \leq_T \mathcal O$.

*Consequences.* If $\mathcal O \leq_h X$, then $\mathcal O^{\mathcal O} \leq_m \mathcal O^X \leq_T \mathcal O$ by :ref{#prop-hyperjump} (2), so $\mathcal O^{\mathcal O} \leq_h \mathcal O$, contradicting :ref{#prop-hyperjump} (1). So $\mathcal O \not\leq_h X$, and $\omega_1^X = \omega_1^{\mathrm{CK}}$ by :ref{#thm-spector-collapse}.
:::

:::figure[The trees of tuples in the proof of :ref{#thm-gandy-basis}. At each step, the tree acquires a coordinate: a witness that $n \notin \mathcal O^{f_1}$ when such a witness can be found above the current node, a constant coordinate otherwise. The nodes $\rho_n$ grow in every coordinate, and their limit is a path of every tree.]
<svg class="fig" viewBox="0 0 600 200" width="600" role="img" aria-label="A table: columns are steps 0, 1, 2, 3; rows are coordinates f1 (the set X), f2 (witness of membership in A), f3 (witness for step 0), f4 (witness for step 1); each step adds one row; cells show prefixes of growing length"><text x="20" y="34" class="label">coordinate</text><text x="160" y="34" text-anchor="middle" class="label">ρ₀</text><text x="270" y="34" text-anchor="middle" class="label">ρ₁</text><text x="380" y="34" text-anchor="middle" class="label">ρ₂</text><text x="490" y="34" text-anchor="middle" class="label">ρ₃</text><text x="20" y="64" class="label">f₁ = X</text><text x="20" y="94" class="label">f₂: X ∈ A</text><text x="20" y="124" class="label">f₃: step 0</text><text x="20" y="154" class="label">f₄: step 1</text><rect x="140" y="50" width="40" height="20" class="cell head-cell"/><rect x="140" y="80" width="40" height="20" class="cell"/><rect x="240" y="50" width="60" height="20" class="cell head-cell"/><rect x="240" y="80" width="60" height="20" class="cell"/><rect x="240" y="110" width="60" height="20" class="soft-fill"/><rect x="340" y="50" width="80" height="20" class="cell head-cell"/><rect x="340" y="80" width="80" height="20" class="cell"/><rect x="340" y="110" width="80" height="20" class="soft-fill"/><rect x="340" y="140" width="80" height="20" class="muted-fill"/><rect x="440" y="50" width="100" height="20" class="cell head-cell"/><rect x="440" y="80" width="100" height="20" class="cell"/><rect x="440" y="110" width="100" height="20" class="soft-fill"/><rect x="440" y="140" width="100" height="20" class="muted-fill"/><text x="160" y="64" text-anchor="middle" class="mrm" font-size="11">ε</text><text x="160" y="94" text-anchor="middle" class="mrm" font-size="11">ε</text><text x="20" y="186" class="label">soft: a witness that 0 ∉ O^X was found; muted: no witness for 1, a constant coordinate, and 1 ∈ O^X</text></svg>
:::

:::quiz[the Gandy basis theorem]
In the proof of :ref{#thm-gandy-basis}, why does the construction keep the witnesses $f_2, f_3, \dots$ instead of only a decreasing sequence of $\Sigma^1_1$ classes containing $X$?

- [x] A decreasing sequence of non-empty $\Sigma^1_1$ classes may have an empty intersection; building the witnesses by finite approximations makes the limit a path of every tree $R_k$, hence a member of every class.
- [ ] Because $\mathcal O$ cannot decide whether a $\Sigma^1_1$ class is empty.

  It can: emptiness of a $\Sigma^1_1$ class is a $\Pi^1_1$ question.
- [ ] To make the trees $R_n$ computable.

  The trees would be computable with or without the choice of the nodes; the witnesses are needed for the limit.

---

When the answer at step $n$ is no, why does $X$ satisfy $n \in \mathcal O^X$?

- [x] Because the answer means that every path of $R_n$ extending $\rho_n$ has $n \in \mathcal O^{f_1}$, and the limit $(f_1, \dots, f_{n+2})$ is such a path.
- [ ] Because $\mathcal O^X \leq_T \mathcal O$.

  This is the conclusion of the proof, not the reason for this step.
- [ ] Because the last coordinate is constant.

  The constant coordinate only keeps the shape of the trees uniform; it carries no information.
:::

Gandy's theorem gives non-hyperarithmetic sets that preserve $\omega_1^{\mathrm{CK}}$: apply it to the $\Sigma^1_1$ class of sets that are not hyperarithmetic (:ref{#prop-sigma11-singleton} (2)). So the converse of :ref{#cor-h-omega1} fails: a set $X$ with $\omega_1^X = \omega_1^{\emptyset}$ need not satisfy $X \leq_h \emptyset$. It also shows that the class $\{ Y : \omega_1^Y > \omega_1^{\mathrm{CK}} \}$ contains no non-empty $\Sigma^1_1$ class, although it has many members, such as $\mathcal O$.

::::exercise[A hyperlow non-hyperarithmetic set]{#ex-hyperlow-nonhyp difficulty=1 objective="Apply the Gandy basis theorem to the class of non-hyperarithmetic sets."}
Show that there is a set $X \leq_T \mathcal O$ that is not hyperarithmetic, with $X <_h \mathcal O$ and $\omega_1^X = \omega_1^{\mathrm{CK}}$.

:::solution
The class of non-hyperarithmetic sets is the complement of the $\Pi^1_1$ class $\mathrm{HYP}$ (:ref{#prop-sigma11-singleton} (2)), so it is $\Sigma^1_1$, and it is non-empty since $\mathrm{HYP}$ is countable. By :ref{#thm-gandy-basis}, it has a member $X$ with $\mathcal O^X \leq_T \mathcal O$, $\mathcal O \not\leq_h X$ and $\omega_1^X = \omega_1^{\mathrm{CK}}$. Then $X \leq_m \mathcal O^X \leq_T \mathcal O$, so $X \leq_T \mathcal O$, and $X <_h \mathcal O$.
:::
::::

## Notes and references

Gandy proved the basis theorem in 1960, answering a question of Kleene. The proof given here, with trees of tuples carrying the witnesses, follows the proof of Monin and Patey (Theorem "Gandy's basis theorem" of their chapter on $\Sigma^1_1$ and $\Pi^1_1$ classes). It is often presented as a forcing argument with $\Sigma^1_1$ classes as conditions, **Gandy forcing**; the next lesson develops this point of view.

- R. O. Gandy, *On a problem of Kleene's*, Bulletin of the American Mathematical Society 66 (1960), 501–502.
- B. Monin and L. Patey, *Computability theory*, chapter "$\Sigma^1_1$ and $\Pi^1_1$ classes", section "Basis theorems for $\Sigma^1_1$ classes".
- G. E. Sacks, *Higher Recursion Theory*, Springer, 1990, Part A.
- C. T. Chong and L. Yu, *Recursion Theory: Computational Aspects of Definability*, De Gruyter, 2015.

:::::exercises
::::exercise{#ex-tuples-projection difficulty=1 objective="Check that projections of trees of tuples give no new classes."}
Let $R$ be a computable tree of triples. Show that the class $\{ f : \exists g\, \exists h\ (f, g, h) \in [R] \}$ is the projection of a computable tree of pairs.

:::solution
Let $\langle g, h \rangle$ denote the function $n \mapsto \langle g(n), h(n) \rangle$, and let $S$ be the set of pairs $(\sigma, \tau)$ of strings of the same length $\ell$ such that every $\tau(i)$ codes a pair $\langle \tau_0(i), \tau_1(i) \rangle$ and $(\sigma, \tau_0, \tau_1) \in R$. It is a computable tree of pairs, and $(f, \langle g, h \rangle) \in [S]$ if and only if $(f, g, h) \in [R]$. Every function $k$ is of the form $\langle g, h \rangle$, so the projections coincide. This is why the trees $R_n$ of the proof of :ref{#thm-gandy-basis}, with more and more coordinates, still define $\Sigma^1_1$ classes.
:::
::::

::::exercise{#ex-gandy-pi11-fails difficulty=1 objective="See why the Gandy basis theorem needs the hypothesis Σ¹₁."}
Give a non-empty $\Pi^1_1$ class none of whose members $X$ satisfies $\omega_1^X = \omega_1^{\mathrm{CK}}$.

:::solution
The class $\{ Y : \omega_1^Y > \omega_1^{\mathrm{CK}} \}$ is $\Pi^1_1$ (:ref{#prop-collapse-pi11} of the next lesson) and contains $\mathcal O$. A simpler example is the class $\{ \mathcal O \}$, which is $\Pi^1_1$ (:ref{#prop-o-pi11-singleton}): its only member collapses $\omega_1^{\mathrm{CK}}$. So the basis theorem cannot be extended to $\Pi^1_1$ classes, in the same way as the low basis theorem cannot be extended to $\Sigma^0_1$ classes.
:::
::::

::::exercise{#ex-gandy-kleene-tree difficulty=2 objective="Combine the Gandy basis theorem with Kleene's tree without hyperarithmetic paths."}
Show that there is a computable tree $T \subseteq \nat^{<\nat}$ with a path, no hyperarithmetic path, and a path $f$ with $\omega_1^f = \omega_1^{\mathrm{CK}}$ and $\mathcal O \not\leq_h f$.

:::solution
Kleene's theorem gives a computable tree $T$ with a path but no hyperarithmetic path. Its class of paths, a class of functions identified with sets through their graphs, is $\Pi^0_1$, hence $\Sigma^1_1$, and non-empty, so by :ref{#thm-gandy-basis} it has a path $f$ with $\mathcal O^f \leq_T \mathcal O$, hence $\mathcal O \not\leq_h f$ and $\omega_1^f = \omega_1^{\mathrm{CK}}$. So the paths of $T$ escape the hyperarithmetic sets, but some of them stay below $\mathcal O$ and preserve $\omega_1^{\mathrm{CK}}$: to have a path, a computable tree does not need the full strength of $\mathcal O$.
:::
::::

::::exercise{#ex-gandy-relativized difficulty=1 objective="Relativize the Gandy basis theorem."}
Let $Z$ be a set. Show that every non-empty $\Sigma^1_1(Z)$ class has a member $X$ with $\mathcal O^{X \oplus Z} \leq_T \mathcal O^Z$ and $\omega_1^{X \oplus Z} = \omega_1^Z$.

:::solution
The proof of :ref{#thm-gandy-basis} relativizes to $Z$: the trees are $Z$-computable, the questions are $\Sigma^1_1(Z)$ and decided by $\mathcal O^Z$, and the relation $n \notin \mathcal O^{f \oplus Z}$ is $\Sigma^1_1(Z)$ uniformly. The construction is computable in $\mathcal O^Z$ and decides $\mathcal O^{X \oplus Z}$. If $\omega_1^{X \oplus Z} > \omega_1^Z$, Spector's theorem relativized to $Z$ gives $\mathcal O^Z \leq_h X \oplus Z$, and then $\mathcal O^{\mathcal O^Z} \leq_m \mathcal O^{X \oplus Z} \leq_T \mathcal O^Z$, which contradicts :ref{#prop-hyperjump} (1) for $\mathcal O^Z$.
:::
::::

::::exercise{#ex-gandy-not-pi01-style difficulty=2 objective="See that decreasing sequences of non-empty Σ¹₁ classes can have an empty intersection."}
Give a decreasing sequence of non-empty $\Sigma^1_1$ classes $\mathcal A_0 \supseteq \mathcal A_1 \supseteq \cdots$ of subsets of $\nat$ with empty intersection. Explain why this cannot happen for $\Pi^0_1$ classes.

:::solution
Let $\mathcal A_n = \{ X : X \text{ is finite and } |X| \geq n \}$. Each class is arithmetic, hence $\Sigma^1_1$, non-empty and decreasing, and a member of every $\mathcal A_n$ would be a finite set with at least $n$ elements for every $n$. For $\Pi^0_1$ classes, which are closed in the compact space $\cs$, a decreasing sequence of non-empty closed sets has a non-empty intersection by compactness. The classes $\mathcal A_n$ are not closed: $\mathbb N$ is a limit of finite sets of growing size, but it is not finite.
:::
::::
:::::
