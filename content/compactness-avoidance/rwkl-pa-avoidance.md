---
title: Liu's theorem for the Ramsey-type weak König lemma
summary: Every non-empty Π⁰₁ class has an infinite homogeneous set that is not PA, so the Ramsey-type weak König lemma admits PA avoidance; the solution follows a branch of parts chosen at the end by König's lemma.
duration: 25
prerequisites: [partition-forcing]
---

The previous lesson defined forcing with partitions and proved that every condition has an extension all of whose parts settle a given requirement (:ref{#lem-partition-progress}). This lesson builds a sequence of conditions that settles all the requirements and makes every acceptable part grow, and extracts the solution along a branch of parts. The number of parts grows along the sequence, and which parts remain infinite depends on members of the classes that are never chosen; the branch is therefore found only at the end, by König's lemma. The same set $Z$ and $D \leq_T Z$, with $Z$ not PA relative to $D$, are fixed throughout.

## The theorem

:::theorem[Liu]{#thm-rwkl-pa-avoidance}
Let $D \leq_T Z$ be sets such that $Z$ is not PA relative to $D$. Every non-empty $\Pi^0_1(Z)$ class $\mathcal P \subseteq \cs$ has an infinite homogeneous set $H$, that is, $H \subseteq P^{-1}(i)$ for some $P \in \mathcal P$ and $i < 2$, such that $Z \oplus H$ is not PA relative to $D$. In particular, $\mathsf{RWKL}$ admits PA avoidance.
:::

:::proof{of=thm-rwkl-pa-avoidance}
Let $p_0 = (2, (\varepsilon, \varepsilon), \mathcal P)$, where a set $P \in \mathcal P$ is seen as the partition $(P_0, P_1)$. Build a sequence of conditions $p_0 \geq p_1 \geq \cdots$, with maps $f_s$ through which $p_{s+1}$ extends $p_s$, $p_s = (k_s, \vec \sigma^s, \mathcal A_s)$, as follows.

- At the steps $2e + 1$, apply :ref{#lem-partition-progress} to $e$.
- At the steps $2n + 2$, consider the parts of the current condition one after the other. If part $\nu$ is acceptable at its turn, choose $X$ in the current class with $X_\nu$ infinite and $x \in X_\nu$ with $x > n$ and $x \geq |\sigma_\nu|$, and apply the part extension with $\tau = \sigma_\nu \cup \{ x \}$; since $X$ remains in the class, part $\nu$ remains acceptable. A part that is not acceptable at its turn remains not acceptable afterwards, by property 2. After the pass, every acceptable part has an element larger than $n$ in its stem.

*The path.* Every condition has an acceptable part, since a partition of $\nat$ into finitely many parts has an infinite part. Consider the tree whose nodes at level $s$ are the acceptable parts of $p_s$, the parent of $\mu$ being $f_s(\mu)$, which is acceptable by property 2. It is infinite and finitely branching, so by König's lemma (:ref{#lem-konig}) it has an infinite branch $(\nu_s)$, with $f_s(\nu_{s+1}) = \nu_s$. The stems $\sigma^s_{\nu_s}$ form an increasing sequence of strings, by the definition of extension; let $H$ be their union.

*$H$ is infinite.* After step $2n + 2$, the part $\nu_s$ is acceptable, so its stem has an element larger than $n$.

*$H$ is homogeneous.* By transitivity, $p_s$ extends $p_0$ through the composite map, which sends $\nu_s$ to a color $c < 2$ independent of $s$. Applying the definition of extension to a member of $\mathcal A_s$ gives $P \in \mathcal P$ such that $\sigma^s_{\nu_s}$ is compatible with part $c$ of $p_0$ relative to $P$, that is, $\sigma^s_{\nu_s} \subseteq P^{-1}(c)$. Every finite subset of $H$ is contained in some $\sigma^s_{\nu_s}$, so it is contained in $P^{-1}(c)$ for some $P \in \mathcal P$, and it is homogeneous with color $c$. By :ref{#prop-homogeneous-member}, $H \subseteq P^{-1}(c)$ for some $P \in \mathcal P$.

*$Z \oplus H$ is not PA relative to $D$.* Fix $e$, and let $s$ be the step $2e + 1$, after which every part of $p_s$ settles $e$, in particular part $\nu_s$. In case (a), $H$ extends $\sigma^s_{\nu_s}$, so $\Phi^{Z \oplus H}_e(n)$ converges to a value not in $\{0, 1\}$ or equal to $J^D(n)$. In case (b), every prefix $\tau$ of $H$ with $|\tau| \geq |\sigma^s_{\nu_s}|$ is a prefix of some $\sigma^t_{\nu_t}$ with $t \geq s$, which is compatible with part $\nu_s$ of $p_s$ by property 1; hence $\tau$ is compatible too, and $\Phi^{Z \oplus \tau}_e(n)$ diverges. By the use principle, $\Phi^{Z \oplus H}_e(n)$ diverges. In both cases $\Phi^{Z \oplus H}_e$ is not $\mathrm{DNC}_2$ relative to $D$.

For the last statement, an instance of $\mathsf{RWKL}$ computable in $Z$ is a $Z$-computable tree $T$, and $[T]$ is a non-empty $\Pi^0_1(Z)$ class.
:::

The construction is not effective: acceptability is not decidable, and the branch is chosen by König's lemma at the end. Only the existence of the solution matters. The proof uses compactness twice, in a way that does not produce PA sets: in the definition of $U$, to bring a question about all members of a class down to $\Sigma^0_1(Z)$, and at the end, to choose the branch of parts and a path through $\mathcal P$, outside of any computation.

:::quiz[Liu's theorem]
Why is the solution $H$ built along a branch of acceptable parts chosen at the end, rather than along one part fixed at the start?

- [x] Because splitting extensions replace each part by several parts, and which of them has infinitely many elements depends on members of the classes that are never chosen; König's lemma finds a branch along which all parts are acceptable.
- [ ] Because the parts are not ordered.

  The parts are indexed by numbers; the issue is which ones remain infinite.
- [ ] Because $H$ must be computable in $Z$.

  $H$ is not computable in $Z$ in general; the construction is not effective.

---

In the proof that $H$ is homogeneous, why is the color $c$ the same for all $s$?

- [x] Because $f_s(\nu_{s+1}) = \nu_s$, so the composite map to the parts of $p_0$ sends all the parts $\nu_s$ of the branch to the same part of $p_0$.
- [ ] Because $\mathcal P$ has a single member.

  $\mathcal P$ may have many members; different $s$ may give different members $P$.
- [ ] Because $H$ is infinite.

  Infinity is proved separately and does not determine the color.
:::

::::exercise{#exr-rwkl-subset difficulty=2 objective="Relativize Liu's theorem to an infinite set $X$, to find a homogeneous set inside $X$ by composing with the enumeration of $X$."}
Using :ref{#thm-rwkl-pa-avoidance} and :ref{#prop-homogeneous-member}, show that for all $D \leq_T Z$ with $Z$ not PA relative to $D$ and every non-empty $\Pi^0_1(Z)$ class $\mathcal P \subseteq \cs$ and infinite set $X \leq_T Z$, there are $P \in \mathcal P$, $i < 2$ and an infinite set $H \subseteq X \cap P^{-1}(i)$ such that $Z \oplus H$ is not PA relative to $D$.

:::solution
Let $p_X$ be the increasing enumeration of $X$, computable in $Z$, and $\mathcal Q = \{ P \circ p_X : P \in \mathcal P \}$, where $(P \circ p_X)(k) = P(p_X(k))$. It is non-empty, and it is a $\Pi^0_1(Z)$ class. Let $S$ be a $Z$-computable tree with $[S] = \mathcal P$. If $Q \notin \mathcal Q$, the strings of $S$ that agree with $Q$ at the positions $p_X(j)$ below their length form a subtree of $S$ without path, hence finite, so some level $p_X(n) + 1$ of $S$ contains no string agreeing with $Q \uh (n + 1)$ at the positions $p_X(0), \dots, p_X(n)$; conversely, this condition excludes $Q$ from $\mathcal Q$. It is $\Sigma^0_1(Z)$, so the complement of $\mathcal Q$ is $\Sigma^0_1(Z)$. By the theorem, $\mathcal Q$ has an infinite homogeneous set $K$, with $Z \oplus K$ not PA relative to $D$, and $K \subseteq (P \circ p_X)^{-1}(i)$ for some $P \in \mathcal P$. Then $H = p_X[K]$ is an infinite subset of $X \cap P^{-1}(i)$, computable in $Z \oplus K$, so $Z \oplus H$ is not PA relative to $D$.
:::
::::

## Notes and references

The theorem that every non-empty $\Pi^0_1$ class has a homogeneous set that is not PA is implicit in Liu's proof (2012) that Ramsey's theorem for pairs does not imply weak König's lemma; Flood (2012) used Liu's argument to show that $\mathsf{RWKL}$ does not imply $\mathsf{WKL}_0$. The proof given here, with partitions that split along extensions, follows the chapter *Compactness avoidance* of Patey's monograph, section *Ramsey-type WKL*; the infinity of the solution is obtained here by a separate density step, at the steps $2n + 2$. The monograph notes that a shorter proof exists, using that the class $\mathrm{DNC}_2$ is $\Pi^0_1$ (Monin and Patey, 2019), but that the proof given here is the one whose combinatorics extend to the avoidance of arbitrary closed classes (:ref{to="compactness-avoidance/closed-classes"}).

- J. Liu, *RT²₂ does not imply WKL₀*, Journal of Symbolic Logic 77 (2012), 609–620.
- S. Flood, *Reverse mathematics and a Ramsey-type König's lemma*, Journal of Symbolic Logic 77 (2012), 1272–1280.
- B. Monin and L. Patey, *Pigeons do not jump high*, Advances in Mathematics 352 (2019), 1066–1095.
- L. Patey, *Lowness and avoidance*, chapter *Compactness avoidance*, section *Ramsey-type WKL*.

:::::exercises
::::exercise[Cone avoidance with the same forcing]{#ex-rwkl-cone-direct difficulty=2 objective="Adapt forcing with partitions to cone avoidance, and see that a single negative answer then suffices."}
Show that the forcing of this lesson also gives cone avoidance for $\mathsf{RWKL}$ directly: if $C \not\leq_T Z$, every non-empty $\Pi^0_1(Z)$ class has an infinite homogeneous set $H$ with $C \not\leq_T Z \oplus H$. Which case of the proof becomes simpler?

:::solution
Let part $\nu$ settle $e$ if $\Phi^{Z \oplus \sigma_\nu}_e(x)\converge \neq C(x)$ for some $x$, or if there is $x$ such that no string $\tau$ compatible with part $\nu$ has $\Phi^{Z \oplus \tau}_e(x)\converge = C(x)$. Define $U$ as the set of pairs $(x, v)$ such that for every $X \in \mathcal A$, some $\nu \in I$ and $\tau$ compatible with part $\nu$ relative to $X$ have $\Phi^{Z \oplus \tau}_e(x)\converge = v$; it is $\Sigma^0_1(Z)$ by the same compactness argument. If $(x, 1 - C(x)) \in U$, a part extension settles a part. If $(x, C(x)) \notin U$, the class of $X \in \mathcal A$ for which no $\tau$ compatible with a part $\nu \in I$ relative to $X$ gives $C(x)$ is non-empty, and replacing $\mathcal A$ by it settles all parts of $I$ at once; no splitting is needed, since a single negative answer suffices. Otherwise $C \leq_T Z$. The rest of the proof is unchanged. This also follows from :ref{#thm-rwkl-pa-avoidance} and :ref{#thm-pa-implies-cone}.
:::
::::

::::exercise[The color cannot be prescribed]{#ex-rwkl-color-not-prescribed difficulty=2 objective="Build a non-empty $\Pi^0_1$ class whose homogeneous sets of one color are all PA, while the other color has computable solutions."}
Fix a computable bijection $\rho \mapsto \ulcorner \rho \urcorner$ between strings and numbers, and for $f : \nat \to 2$ let $X_f = \{ 2 \ulcorner f \uh n \urcorner : n \in \nat \}$. Let $\mathcal P = \{ X_f : f \in \mathrm{DNC}_2 \}$, where $\mathrm{DNC}_2$ is relative to $\emptyset$. Show that $\mathcal P$ is a non-empty $\Pi^0_1$ class, that every infinite set homogeneous for $\mathcal P$ with color $1$ is PA, and that some computable infinite set is homogeneous for $\mathcal P$ with color $0$. What does this say about :ref{#thm-rwkl-pa-avoidance}?

:::solution
A set $X$ belongs to $\mathcal P$ if and only if: every element of $X$ is even; for every $n$, $X$ contains exactly one number $2 \ulcorner \rho \urcorner$ with $|\rho| = n$; the strings coded by any two elements of $X$ are comparable; and no string $\rho$ coded by an element of $X$ has $J(x)\converge = \rho(x)$ for some $x < |\rho|$. If so, the coded strings form an increasing sequence with one string of each length, whose union $f$ is $\mathrm{DNC}_2$, and $X = X_f$; the converse is clear. Each clause, for fixed numbers and a fixed number of steps of the computation of $J$, is decided by a finite part of $X$, uniformly; so $\mathcal P$ is $\Pi^0_1$, and it is non-empty since $\mathrm{DNC}_2$ is.

Let $H$ be infinite and homogeneous with color $1$: by :ref{#prop-homogeneous-member}, $H \subseteq X_f$ for some $f \in \mathrm{DNC}_2$. To compute $f(m)$, search for an element of $H$ coding a string of length larger than $m$; it exists, since $H$ is infinite and only finitely many numbers code shorter strings, and its bit at $m$ is $f(m)$. So $H$ computes $f$ and is PA. On the other hand, the set of odd numbers is disjoint from every $X_f$, so it is contained in $P^{-1}(0)$ for every $P \in \mathcal P$: it is a computable infinite set homogeneous with color $0$.

So the color of the homogeneous set in :ref{#thm-rwkl-pa-avoidance} cannot be chosen in advance: the theorem gives some color, and for this class only the color $0$ admits solutions that are not PA. This is why the construction keeps all the parts and chooses the branch of parts, and with it the color, at the end.
:::
::::

::::exercise[Strong cone avoidance]{#ex-rwkl-strong-cone difficulty=1 objective="Derive the strong cone avoidance of $\mathsf{RWKL}$ from that of the pigeonhole principle, by choosing a path without computing it."}
Show that $\mathsf{RWKL}$ admits strong cone avoidance: for every set $Z$, every $C \not\leq_T Z$ and every infinite binary tree $T$, not necessarily computable in $Z$, there is an infinite set $H$ homogeneous for $T$ with $C \not\leq_T Z \oplus H$. Which theorem would give strong PA avoidance in the same way?

:::solution
By König's lemma, $T$ has a path $P$. By :ref{#thm-dj-cone-avoidance} applied to the set $P$, there is an infinite set $H$ contained in $P$ or in $\overline P$ with $C \not\leq_T Z \oplus H$. Then $H \subseteq P^{-1}(1)$ or $H \subseteq P^{-1}(0)$, so $H$ is homogeneous for $T$ by :ref{#prop-homogeneous-member}. The path $P$ may be complex, but it is only used as an instance of the pigeonhole principle, whose strong avoidance property allows arbitrary instances. The same argument with the strong PA avoidance of the pigeonhole principle, proved in :ref{to="compactness-avoidance/liu-theorem"}, shows that $\mathsf{RWKL}$ admits strong PA avoidance; but that proof uses the present theorem.
:::
::::

::::exercise[More than two colors]{#ex-rwkl-ell-colors difficulty=2 objective="Run the proof of Liu's theorem for classes of partitions into $\ell$ parts, and adapt the compactness argument for homogeneity."}
Let $\ell \geq 2$, $D \leq_T Z$ with $Z$ not PA relative to $D$, and $\mathcal P \subseteq \ell^\nat$ a non-empty $\Pi^0_1(Z)$ class. Show that there are $P \in \mathcal P$, $c < \ell$ and an infinite set $H \subseteq P^{-1}(c)$ such that $Z \oplus H$ is not PA relative to $D$.

:::solution
Start from the condition $p_0 = (\ell, (\varepsilon, \dots, \varepsilon), \mathcal P)$, whose class consists of partitions into $\ell$ parts, and run the construction of the proof of :ref{#thm-rwkl-pa-avoidance} unchanged: neither :ref{#lem-partition-progress} nor the steps $2n + 2$ depend on the number of parts. The branch $(\nu_s)$ of acceptable parts and the set $H$, the union of the stems $\sigma^s_{\nu_s}$, are obtained in the same way; $H$ is infinite, and $Z \oplus H$ is not PA relative to $D$, by the same arguments.

For homogeneity, the composite map from the parts of $p_s$ to those of $p_0$ sends $\nu_s$ to a color $c < \ell$ independent of $s$, and for each $s$ the class $\mathcal C_s = \{ P \in \mathcal P : \sigma^s_{\nu_s} \subseteq P^{-1}(c) \}$ is non-empty, by the definition of extension applied to a member of $\mathcal A_s$. These classes are closed and decreasing, since the stems increase. The space $\ell^\nat$ is compact, by König's lemma for the full $\ell$-branching tree, so their intersection contains some $P$, and $H \subseteq P^{-1}(c)$.
:::
::::

::::exercise[Acceptable parts may die]{#ex-acceptable-dead-end difficulty=1 objective="See on an example that an acceptable part can lose its acceptability after an extension, and why the branch of parts is chosen by König's lemma."}
Let $X(n) = n \bmod 2$, and let $X'(0) = 0$ and $X'(n) = 1$ for $n \geq 1$. Let $p = (2, (\varepsilon, \varepsilon), \{ X, X' \})$. Show that part $0$ of $p$ is acceptable, and find a part extension $q$ of $p$ in which part $0$, which refines part $0$ of $p$, is not acceptable. Explain why the proof of :ref{#thm-rwkl-pa-avoidance} still finds an infinite branch of acceptable parts.

:::solution
A finite class of computable functions is $\Pi^0_1$, so $p$ is a condition. Part $0$ is acceptable, since $X_0$, the set of even numbers, is infinite. The string $\tau = \{ 2 \}$ is compatible with part $1$ relative to $X'$, since $2 \in X'_1$. The part extension replaces $\sigma_1$ by $\tau$ and the class by $\{ Y \in \{ X, X' \} : 2 \in Y_1 \} = \{ X' \}$, since $X(2) = 0$. In the resulting condition $q$, part $0$ is not acceptable: the only member is $X'$, and $X'_0 = \{ 0 \}$. Part $0$ of $q$ refines part $0$ of $p$, through the identity map.

So in the tree of the proof, whose nodes at level $s$ are the acceptable parts of $p_s$, a node may have no child. The tree is still infinite, since every condition has an acceptable part, and finitely branching, so König's lemma gives an infinite branch; it avoids the dead nodes, which cannot be recognized during the construction. This is also why the steps $2n + 2$ extend a part only if it is acceptable at its turn.
:::
::::
:::::
