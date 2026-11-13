---
title: Liu's theorem for the Ramsey-type weak König lemma
summary: Every non-empty Π⁰₁ class has an infinite homogeneous set that is not PA, so the Ramsey-type weak König lemma admits PA avoidance; the solution follows a branch of parts chosen at the end by König's lemma.
duration: 30
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

## Exercises

::::exercise{#exr-rwkl-subset difficulty=2}
Using :ref{#thm-rwkl-pa-avoidance} and :ref{#prop-homogeneous-member}, show that for all $D \leq_T Z$ with $Z$ not PA relative to $D$ and every non-empty $\Pi^0_1(Z)$ class $\mathcal P \subseteq \cs$ and infinite set $X \leq_T Z$, there are $P \in \mathcal P$, $i < 2$ and an infinite set $H \subseteq X \cap P^{-1}(i)$ such that $Z \oplus H$ is not PA relative to $D$.

:::solution
Let $p_X$ be the increasing enumeration of $X$, computable in $Z$, and $\mathcal Q = \{ P \circ p_X : P \in \mathcal P \}$, where $(P \circ p_X)(k) = P(p_X(k))$. It is non-empty, and it is a $\Pi^0_1(Z)$ class. Let $S$ be a $Z$-computable tree with $[S] = \mathcal P$. If $Q \notin \mathcal Q$, the strings of $S$ that agree with $Q$ at the positions $p_X(j)$ below their length form a subtree of $S$ without path, hence finite, so some level $p_X(n) + 1$ of $S$ contains no string agreeing with $Q \uh (n + 1)$ at the positions $p_X(0), \dots, p_X(n)$; conversely, this condition excludes $Q$ from $\mathcal Q$. It is $\Sigma^0_1(Z)$, so the complement of $\mathcal Q$ is $\Sigma^0_1(Z)$. By the theorem, $\mathcal Q$ has an infinite homogeneous set $K$, with $Z \oplus K$ not PA relative to $D$, and $K \subseteq (P \circ p_X)^{-1}(i)$ for some $P \in \mathcal P$. Then $H = p_X[K]$ is an infinite subset of $X \cap P^{-1}(i)$, computable in $Z \oplus K$, so $Z \oplus H$ is not PA relative to $D$.
:::
::::

::::exercise{difficulty=2}
Show that the forcing of this lesson also gives cone avoidance for $\mathsf{RWKL}$ directly: if $C \not\leq_T Z$, every non-empty $\Pi^0_1(Z)$ class has an infinite homogeneous set $H$ with $C \not\leq_T Z \oplus H$. Which case of the proof becomes simpler?

:::solution
Let part $\nu$ settle $e$ if $\Phi^{Z \oplus \sigma_\nu}_e(x)\converge \neq C(x)$ for some $x$, or if there is $x$ such that no string $\tau$ compatible with part $\nu$ has $\Phi^{Z \oplus \tau}_e(x)\converge = C(x)$. Define $U$ as the set of pairs $(x, v)$ such that for every $X \in \mathcal A$, some $\nu \in I$ and $\tau$ compatible with part $\nu$ relative to $X$ have $\Phi^{Z \oplus \tau}_e(x)\converge = v$; it is $\Sigma^0_1(Z)$ by the same compactness argument. If $(x, 1 - C(x)) \in U$, a part extension settles a part. If $(x, C(x)) \notin U$, the class of $X \in \mathcal A$ for which no $\tau$ compatible with a part $\nu \in I$ relative to $X$ gives $C(x)$ is non-empty, and replacing $\mathcal A$ by it settles all parts of $I$ at once; no splitting is needed, since a single negative answer suffices. Otherwise $C \leq_T Z$. The rest of the proof is unchanged. This also follows from :ref{#thm-rwkl-pa-avoidance} and :ref{#thm-pa-implies-cone}.
:::
::::

## Notes and references

The theorem that every non-empty $\Pi^0_1$ class has a homogeneous set that is not PA is implicit in Liu's proof (2012) that Ramsey's theorem for pairs does not imply weak König's lemma; Flood (2012) used Liu's argument to show that $\mathsf{RWKL}$ does not imply $\mathsf{WKL}_0$. The proof given here, with partitions that split along extensions, follows the chapter *Compactness avoidance* of Patey's monograph, section *Ramsey-type WKL*; the infinity of the solution is obtained here by a separate density step, at the steps $2n + 2$. The monograph notes that a shorter proof exists, using that the class $\mathrm{DNC}_2$ is $\Pi^0_1$ (Monin and Patey, 2019), but that the proof given here is the one whose combinatorics extend to the avoidance of arbitrary closed classes (:ref{to="compactness-avoidance/closed-classes"}).

- J. Liu, *RT²₂ does not imply WKL₀*, Journal of Symbolic Logic 77 (2012), 609–620.
- S. Flood, *Reverse mathematics and a Ramsey-type König's lemma*, Journal of Symbolic Logic 77 (2012), 1272–1280.
- B. Monin and L. Patey, *Pigeons do not jump high*, Advances in Mathematics 352 (2019), 1066–1095.
- L. Patey, *Lowness and avoidance*, chapter *Compactness avoidance*, section *Ramsey-type WKL*.
